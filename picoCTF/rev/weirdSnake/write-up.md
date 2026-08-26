---
title: "weirdSnake"
date: 2026-08-26
tags: ["picoCTF"]
categories: ["rev"]
draft: false
---

## Summary
This challenge provides the following description and a file named `snake`.
```
I have a friend that enjoys coding and he hasn't stopped talking about a snake recently
He left this file on my computer and dares me to uncover a secret phrase from it. Can you assist?
```

Artifacts
- ['snake'](https://github.com/ssung099/CTF-Writeups/blob/main/picoCTF/rev/weirdSnake/chall/snake): the Python Bytecode provided by the challenge authors
- ['solve.py'](https://github.com/ssung099/CTF-Writeups/blob/main/picoCTF/rev/weirdSnake/solve.py): the solve script for the challenge that retrieves the "secret phrase" from the provided `snake` file.

## Solve explanation
Inspecting the file, I notice that the provided file is just an ASCII text file instead of an executable.
```
$ file ./snake 
./snake: ASCII text
```

Looking at the file contents, I notice it contains Python bytecode, which probably holds the "secret phrase" we need to retrieve by reversing it.

Let's take a look at the first section of the bytecode:
```
  1           0 LOAD_CONST               0 (4)
              2 LOAD_CONST               1 (54)
              4 LOAD_CONST               2 (41)
              6 LOAD_CONST               3 (0)
              8 LOAD_CONST               4 (112)
             10 LOAD_CONST               5 (32)
             12 LOAD_CONST               6 (25)
             14 LOAD_CONST               7 (49)
             16 LOAD_CONST               8 (33)
             18 LOAD_CONST               9 (3)
             20 LOAD_CONST               3 (0)
             22 LOAD_CONST               3 (0)
             24 LOAD_CONST              10 (57)
             26 LOAD_CONST               5 (32)
             28 LOAD_CONST              11 (108)
             30 LOAD_CONST              12 (23)
             32 LOAD_CONST              13 (48)
             34 LOAD_CONST               0 (4)
             36 LOAD_CONST              14 (9)
             38 LOAD_CONST              15 (70)
             40 LOAD_CONST              16 (7)
             42 LOAD_CONST              17 (110)
             44 LOAD_CONST              18 (36)
             46 LOAD_CONST              19 (8)
             48 LOAD_CONST              11 (108)
             50 LOAD_CONST              16 (7)
             52 LOAD_CONST               7 (49)
             54 LOAD_CONST              20 (10)
             56 LOAD_CONST               0 (4)
             58 LOAD_CONST              21 (86)
             60 LOAD_CONST              22 (43)
             62 LOAD_CONST              23 (104)
             64 LOAD_CONST              24 (44)
             66 LOAD_CONST              25 (91)
             68 LOAD_CONST              16 (7)
             70 LOAD_CONST              26 (18)
             72 LOAD_CONST              27 (106)
             74 LOAD_CONST              28 (124)
             76 LOAD_CONST              29 (89)
             78 LOAD_CONST              30 (78)
             80 BUILD_LIST              40
             82 STORE_NAME               0 (input_list)
```

This section repeatedly calls `LOAD_CONST`, then eventually calls `BUILD_LIST` and `STORE_NAME` into the variable `input_list`. This just seems to be creating a list, `input_list`, containing all 40 of the constant values loaded via `LOAD_CONST`.

Let's take a look at the next few sections:
```
  2          84 LOAD_CONST              31 ('J')
             86 STORE_NAME               1 (key_str)

  3          88 LOAD_CONST              32 ('_')
             90 LOAD_NAME                1 (key_str)
             92 BINARY_ADD
             94 STORE_NAME               1 (key_str)

  4          96 LOAD_NAME                1 (key_str)
             98 LOAD_CONST              33 ('o')
            100 BINARY_ADD
            102 STORE_NAME               1 (key_str)

  5         104 LOAD_NAME                1 (key_str)
            106 LOAD_CONST              34 ('3')
            108 BINARY_ADD
            110 STORE_NAME               1 (key_str)

  6         112 LOAD_CONST              35 ('t')
            114 LOAD_NAME                1 (key_str)
            116 BINARY_ADD
            118 STORE_NAME               1 (key_str)
```

These sections build up a string in the variable `key_str`, one character at a time.

Section 2 loads the constant `'J'` and stores it into `key_str`, so `key_str = "J"`.

Section 3 loads the constant `'_'`, then loads `key_str` (currently `"J"`), and calls `BINARY_ADD`. The key here is operand order: whichever value is loaded second ends up on top of the stack, and `BINARY_ADD` computes `second-loaded + first-loaded`. Since `'_'` is loaded first and `key_str` second, the result is `"_" + "J"`, giving `key_str = "_J"`.

Section 4 loads `key_str` first, then the constant `'o'`, and adds them: `"_J" + "o"`, giving `key_str = "_Jo"`.

Section 5 follows the same pattern: `key_str` loaded first, then `'3'`, giving `"_Jo" + "3"` and `key_str = "_Jo3"`.

Section 6 reverses the order again: `'t'` is loaded first, then `key_str`, giving `"t" + "_Jo3"` and a final value of `key_str = "t_Jo3"`.

So by the end of section 6, `key_str` holds the string `"t_Jo3"`.

Scanning through the rest, I didn't understand every instruction, but a few sections stood out:
```
            126 LOAD_NAME                1 (key_str)
            128 GET_ITER
            130 CALL_FUNCTION            1
            132 STORE_NAME               2 (key_list)
```

The `key_str` value that we got previously is now stored in `key_list`.

```
 11     >>  134 LOAD_NAME                3 (len)
            136 LOAD_NAME                2 (key_list)
            138 CALL_FUNCTION            1
            140 LOAD_NAME                3 (len)
            142 LOAD_NAME                0 (input_list)
            144 CALL_FUNCTION            1
            146 COMPARE_OP               0 (<)
            148 POP_JUMP_IF_FALSE      162

 12         150 LOAD_NAME                2 (key_list)
            152 LOAD_METHOD              4 (extend)
            154 LOAD_NAME                2 (key_list)
            156 CALL_METHOD              1
            158 POP_TOP
            160 JUMP_ABSOLUTE          134
```

This section compares the length of `key_list` and `input_list` and extends `key_list` by `key_list`, or in other words, doubles the list while `len(key_list) < len(input_list)`.

```
            168 LOAD_NAME                5 (zip)
            170 LOAD_NAME                0 (input_list)
            172 LOAD_NAME                2 (key_list)
```

This calls `zip` on `input_list` and the now-extended `key_list`, pairing them up element by element.

```
              8 STORE_FAST               1 (a)
             10 STORE_FAST               2 (b)
             12 LOAD_FAST                1 (a)
             14 LOAD_FAST                2 (b)
             16 BINARY_XOR
```

Each pair `(a, b)` from the `zip` is unpacked and XORed together. This is the actual decode step: `[a ^ b for a, b in zip(input_list, key_list)]`.

Putting it all together, this is equivalent to `input_list` being XORed against a repeating key derived from `key_str`. Once we convert the each XORed value to characters and join them together, we should get the flag.

## Solve script
From this, I wrote a script to extract the `LOAD_CONST` values and XOR them with the recovered key:

```python
import re

def extract_consts():
    vals = []
    f = open("chall/snake", "r")
    for line in f:
        if "LOAD_CONST" in line:
            m = re.search(r'\((\d+)\)', line)
            if m:
                vals.append(int(m.group(1)))
        else:
            break
    f.close()
    return vals

if __name__ == "__main__":
    vals = extract_consts()
    key = "t_Jo3"
    key_bytes = [ord(c) for c in key]

    flag = []
    for i in range(0, len(vals)):
        flag.append(vals[i] ^ key_bytes[i % len(key_bytes)])

    print(''.join(map(chr, flag)))
```

Running this script gives us the flag:
```
picoCTF{N0t_sO_coNfus1ng_sn@ke_7f44f566}
```
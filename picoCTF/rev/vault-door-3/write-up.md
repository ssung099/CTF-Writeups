---
title: "vault-door-3"
date: 2026-08-30
tags: ["picoCTF"]
categories: ["rev"]
draft: false
---
 
## Challenge Description
This challenge provides us with a Java source file with the following description:
```
This vault uses for-loops and byte arrays.
The source code for this vault is here: VaultDoor3.java
```
 
Artifacts:
- [VaultDoor3.java](https://github.com/ssung099/CTF-Writeups/blob/main/picoCTF/rev/vault-door-3/chall/VaultDoor3.java): the chall file
- [solve.py](https://github.com/ssung099/CTF-Writeups/blob/main/picoCTF/rev/vault-door-3/chall/solve.py): the solve script

## Solve Explanation
Like the previous `Vault Door` challenge, this challenge provides us with Java source code with a `checkPassword` function that checks our input value.

```java
public boolean checkPassword(String password) {
    if (password.length() != 32) {
        return false;
    }
    char[] buffer = new char[32];
    int i;
    for (i=0; i<8; i++) {
        buffer[i] = password.charAt(i);
    }
    for (; i<16; i++) {
        buffer[i] = password.charAt(23-i);
    }
    for (; i<32; i+=2) {
        buffer[i] = password.charAt(46-i);
    }
    for (i=31; i>=17; i-=2) {
        buffer[i] = password.charAt(i);
    }
    String s = new String(buffer);
    return s.equals("jU5t_a_sna_3lpm13gf49_u_4_m9r540");
}
```

This functions seems to scramble the inputted value using four `for` loops and checks the scrambled value against the fixed value `jU5t_a_sna_3lpm13gf49_u_4_m9r540`. This means that to find the correct input value, all we need to do is unscramble this value back by reversing the steps in the `for` loops.

Looking at each of the `for` loops, they do not seem to modify the same index twice.

The first loop does not actually modify any values. It copies the first 8 char values from the input to the local buffer. 
```java
for (i=0; i<8; i++) {
    buffer[i] = password.charAt(i);
}
```

Using the fixed value in the code, we can do the same:
```python
s = "jU5t_a_sna_3lpm13gf49_u_4_m9r540"

password = ""
password += s[0:8] # for loop 1 
```

The next loop takes the next 8 char values (from index 8 to 15, inclusive) and reverses it.
```java
for (; i<16; i++) {
    buffer[i] = password.charAt(23-i);
}
```

To repeat this step in python:
```python
password += s[8:16][::-1] # for loop 2
```

Like the second loop, the third loop also reverses the char values in the substring (index 16 to 30, inclusive). The main difference is that the loop increments the index value by 2, flipping the positions of every other char values, specifically the even-indexed values.
```java
for (; i<32; i+=2) {
    buffer[i] = password.charAt(46-i);
}
```

The last loop iterates backwards by 2 from `i=31` to `i>=17`, but it does not do anything in particular. It takes every other char value, specifically the odd-indexed values, and writes it into the local buffer, similar to loop 1.
```java
for (i=31; i>=17; i-=2) {
    buffer[i] = password.charAt(i);
}
```

Combining the third and fourth loop, we can undo the operations based on the parity of the indices.
```python
for i in range(16, 32):
    if i % 2 == 0: # for loop 3
        password += s[46-i]
    else: # for loop 4
        password += s[i]
```

For every even index, I flipped the char value in the substring and for every odd index, I appended the char value as is.

Performing these four operations on the value `jU5t_a_sna_3lpm13gf49_u_4_m9r540` and wrapping it in the flag format, I was able to get the full flag and solve the challenge.
```
picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_99f530}
```
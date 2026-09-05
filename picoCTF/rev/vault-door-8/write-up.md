---
title: "vault-door-8"
date: 2026-09-05
tags: ["picoCTF"]
categories: ["rev"]
draft: false
---

## Challenge Description
This challenge provides us with a Java source file with the following description:
```
Apparently Dr. Evil's minions knew that our agency was making copies of their source code, because they intentionally sabotaged this source code in order to make it harder for our agents to analyze and crack into! The result is a quite mess, but I trust that my best special agent will find a way to solve it.
```

Artifacts:
- [VaultDoor7.java](https://github.com/ssung099/CTF-Writeups/blob/main/picoCTF/rev/vault-door-8/chall/VaultDoor8.java): the chall file
- [solve.py](https://github.com/ssung099/CTF-Writeups/blob/main/picoCTF/rev/vault-door-8/solve.py): the solve script

## Solve Explanation
Similar to the previous `Vault Door` challenges, the challenge file has a `checkPassword` function that verifies our input.

```java
public boolean checkPassword(String password) {
    char[] scrambled = scramble(password); 
    char[] expected = { 0xF4, 0xC0, 0x97, 0xF0, 0x77, 0x97, 0xC0, 0xE4, 0xF0, 0x77, 0xA4, 0xD0, 0xC5, 0x77, 0xF4, 0x86, 0xD0, 0xA5, 0x45, 0x96, 0x27, 0xB5, 0x77, 0xC1, 0xC0, 0x95, 0x94, 0x94, 0xC1, 0xD1, 0xE1, 0xF1 }; 
    return Arrays.equals(scrambled, expected); 
}
```

`checkPassword` performs a scrambling operation using the `scramble` function on the password input and checks each byte of the resulting value against some fixed hexadecimal values.

```java
public char[] scramble(String password) {
    /* Scramble a password by transposing pairs of bits. */
    char[] a = password.toCharArray(); 
    for (int b=0; b<a.length; b++) {
        char c = a[b]; 
        c = switchBits(c,1,2); 
        c = switchBits(c,0,3);
        c = switchBits(c,5,6); 
        c = switchBits(c,4,7);
        c = switchBits(c,0,1);
        c = switchBits(c,3,4); 
        c = switchBits(c,2,5); 
        c = switchBits(c,6,7); 
        a[b] = c; 
    } 
    return a;
} 
```

`scramble` first converts our password input into a char array. Then, for each `char` value in the array, it performs a sequence of operations using the function `switchBits` and stores it back into the array. `switchBits` swaps the position of the bit values specified in the parameters.

To reverse engineer the correct password, we can take the `expected` char array and reverse the scrambling steps. For each `char` value in the array, we can take the `switchBits` function from the challenge file and perform the operations in reverse order.

```java
for (int i=0; i < expected.length; i++) {
    char c = expected[i];
    c = switchBits(c, 6, 7);
    c = switchBits(c, 2, 5);
    c = switchBits(c, 3, 4);
    c = switchBits(c, 0, 1);
    c = switchBits(c, 4, 7);
    c = switchBits(c, 5, 6);
    c = switchBits(c, 0, 3);
    c = switchBits(c, 1, 2);
    expected[i] = c;
}
```

Printing out the values after the unscrambling in flag format, we can get the flag and solve the challenge.
```
picoCTF{s0m3_m0r3_b1t_sh1fTiNg_40eaa4567}
```
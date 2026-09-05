---
title: "vault-door-6"
date: 2026-09-04
tags: ["picoCTF"]
categories: ["rev"]
draft: false
---

## Challenge Description
This challenge provides us with a Java source file with the following description:
```
This vault uses an XOR encryption scheme.
```

Artifacts:
- [VaultDoor6.java](https://github.com/ssung099/CTF-Writeups/blob/main/picoCTF/rev/vault-door-6/chall/VaultDoor6.java): the chall file
- [solve.py](https://github.com/ssung099/CTF-Writeups/blob/main/picoCTF/rev/vault-door-6/chall/solve.py): the solve script

## Solve Explanation
Similar to the previous `Vault Door` challenges, the challenge file has a `checkPassword` function that verifies our input.

```java
public boolean checkPassword(String password) {
    if (password.length() != 32) {
        return false;
    }
    byte[] passBytes = password.getBytes();
    byte[] myBytes = {
        0x3b, 0x65, 0x21, 0xa , 0x38, 0x0 , 0x36, 0x1d,
        0xa , 0x3d, 0x61, 0x27, 0x11, 0x66, 0x27, 0xa ,
        0x21, 0x1d, 0x61, 0x3b, 0xa , 0x2d, 0x65, 0x27,
        0xa , 0x61, 0x37, 0x65, 0x61, 0x65, 0x65, 0x64,
    };
    for (int i=0; i<32; i++) {
        if (((passBytes[i] ^ 0x55) - myBytes[i]) != 0) {
            return false;
        }
    }
    return true;
}
```

The key check in the function is the `for` loop. This function checks that each byte of the password input XORed with `0x55` minus the corresponding byte in `myBytes` equals 0. In other words, it checks that the XORed value of each input byte equals the bytes in the function.

To figure out the correct input value, we can take this array of bytes and XOR it with `0x55`. This works since XORing with the same value twice undoes the operation and returns the original value.

```python
password = ""
for byte in myBytes:
    password += chr(byte ^ 0x55)
```

By applying XOR to each of the bytes, converting them to `char` values, and joining them into a string, we can get the correct value. Wrapping it in flag format, we can get the flag and solve the challenge.
```
picoCTF{n0t_mUcH_h4rD3r_tH4n_x0r_4b04001}
```
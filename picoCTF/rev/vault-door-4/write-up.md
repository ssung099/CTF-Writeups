---
title: "vault-door-4"
date: 2026-09-04
tags: ["picoCTF"]
categories: ["rev"]
draft: false
---
 
## Challenge Description
This challenge provides us with a Java source file with the following description:
```
This vault uses ASCII encoding for the password.
```

Artifacts:
- [VaultDoor4.java](https://github.com/ssung099/CTF-Writeups/blob/main/picoCTF/rev/vault-door-4/chall/VaultDoor4.java): the chall file
- [solve.py](https://github.com/ssung099/CTF-Writeups/blob/main/picoCTF/rev/vault-door-4/solve.py): the solve script

## Solve Explanation
Like the previous `Vault Door` challenges, this challenge provides us with Java source code with a `checkPassword` function that checks whether our input value is correct.

```java
public boolean checkPassword(String password) {
    byte[] passBytes = password.getBytes();
    byte[] myBytes = {
        106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
        0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
        0142, 0131, 0164, 063 , 0163, 0137, 067 , 065 ,
        '9' , '6' , '0' , '0' , 'a' , 'b' , 'c' , '3' ,
    };
    for (int i=0; i<32; i++) {
        if (passBytes[i] != myBytes[i]) {
            return false;
        }
    }
    return true;
}
```

This function converts the `password` value from our input to bytes and checks if each byte matches the fixed byte values in the function.

```java
byte[] myBytes = {
    106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
    0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
    0142, 0131, 0164, 063 , 0163, 0137, 067 , 065 ,
    '9' , '6' , '0' , '0' , 'a' , 'b' , 'c' , '3' ,
};
```

Looking at the values in `myBytes`, it is pretty evident that the first row is ASCII values, second row is in hexadecimal, third is in octal, and the last row is just plain char values.

For each of the values, we can convert them to their respective `char` value and append them to a string.
```python
for byte in password_bytes:
    if isinstance(byte, int):
        password_str += chr(byte)
    else:
        password_str += byte
```

Wrapping the resulting value in flag format, we can get the flag and solve the challenge.
```
picoCTF{jU5t_4_bUnCh_0f_bYt3s_759600abc3}
```
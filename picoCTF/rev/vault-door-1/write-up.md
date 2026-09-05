---
title: "vault-door-1"
date: 2026-09-04
tags: ["picoCTF"]
categories: ["rev"]
draft: false
---

## Challenge Description
This challenge provides us with a Java source file with the following description:
```
This vault uses some complicated arrays! I hope you can make sense of it, special agent.
```

Artifacts:
- [VaultDoor1.java](https://github.com/ssung099/CTF-Writeups/blob/main/picoCTF/rev/vault-door-1/chall/VaultDoor1.java): the chall file
- [solve.py](https://github.com/ssung099/CTF-Writeups/blob/main/picoCTF/rev/vault-door-1/solve.py): the solve script

## Solve explanation
The challenge provides us with Java source code that checks if our input is correct through a function `checkPassword`.
```java
public boolean checkPassword(String password) {
    return password.length() == 32 &&
           password.charAt(0)  == 'd' &&
           password.charAt(29) == '8' &&
           password.charAt(4)  == 'r' &&
           password.charAt(2)  == '5' &&
           password.charAt(23) == 'r' &&
           password.charAt(3)  == 'c' &&
           password.charAt(17) == '4' &&
           password.charAt(1)  == '3' &&
           password.charAt(7)  == 'b' &&
           password.charAt(10) == '_' &&
           password.charAt(5)  == '4' &&
           password.charAt(9)  == '3' &&
           password.charAt(11) == 't' &&
           password.charAt(15) == 'c' &&
           password.charAt(8)  == 'l' &&
           password.charAt(12) == 'H' &&
           password.charAt(20) == 'c' &&
           password.charAt(14) == '_' &&
           password.charAt(6)  == 'm' &&
           password.charAt(24) == '5' &&
           password.charAt(18) == 'r' &&
           password.charAt(13) == '3' &&
           password.charAt(19) == '4' &&
           password.charAt(21) == 'T' &&
           password.charAt(16) == 'H' &&
           password.charAt(27) == '9' &&
           password.charAt(30) == 'd' &&
           password.charAt(25) == '_' &&
           password.charAt(22) == '3' &&
           password.charAt(28) == 'e' &&
           password.charAt(26) == '2' &&
           password.charAt(31) == '8';
}
```

From the main function, we can see that `checkPassword` is called on the input with the flag header `picoCTF{` and the closing curly brace `}` stripped off.
```java
String input = userInput.substring("picoCTF{".length(), userInput.length() - 1);
if (vaultDoor.checkPassword(input)) {
    System.out.println("Access granted.");
}
```

To open the vault, we can reverse engineer the value by building a string from the conditions in `checkPassword`. I wrote a script that extracts, for each condition, the index being checked and the character it's checked against, using a regex pattern.

```python
m = re.match(r"password\.charAt\((\d+)\)\s*==\s*'(.)'", condition)
```

I match each condition line and store the `(index, char)` pair into the dictionary `chars`. Once every condition has been parsed, joining all the char values in ascending index order gives us the value, and appending the flag header `picoCTF{` and closing curly brace `}` gives us the full flag.
```
picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_29e8d8}
```
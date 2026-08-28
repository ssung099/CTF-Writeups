---
title: "Reverse"
date: 2026-08-28
tags: ["picoCTF"]
categories: ["rev"]
draft: false
---

## Summary
This challenge provides a file `ret` with the following description:
```
Try reversing the file? Can ya?
I forgot the password to this file. Please find it for me?
```

Artifacts:
- [ret](https://github.com/ssung099/CTF-Writeups/blob/main/picoCTF/rev/Reverse/chall/ret): the chall file

## Solve explanation
Running the executable, we get the following prompt:
```
$ ./ret
Enter the password to unlock this file:  
```

I first tried to use the `strings` command to look for the password or any readable text in the binary.

```
$ strings ret | less
...
[]A\A]A^A_
Enter the password to unlock this file: 
You entered: %s
Password correct, please see flag: picoCTF{3lf_r3v3r5ing_succe55ful_7851ef7d}
Access denied
:*3$"
GCC: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0
crtstuff.c
deregister_tm_clones
__do_global_dtors_aux
completed.8061
...
```

The flag was surprisingly embedded directly into the file and I was able to solve the challenge.
---
title: "packer"
date: 2026-08-27
tags: ["picoCTF"]
categories: ["rev"]
draft: false
---

## Summary
This challenge provides a file `out` with the following description:
```
Reverse this linux executable?
```

Artifacts:
- [out](https://github.com/ssung099/CTF-Writeups/blob/main/picoCTF/rev/packer/chall/out): the chall file

## Solve explanation
Running the executable, we are prompted to enter a password:
```
$ ./out
Enter the password to unlock this file: 
```

We can use the `strings` command to look for possible clues for the password in the executable.

```
$ strings out | less
...
$Info: This file is packed with the UPX executable packer http://upx.sf.net $
$Id: UPX 3.95 Copyright (C) 1996-2018 the UPX Team. All Rights Reserved. $
...
```

While there is not much useful information, we do find that the file is compressed using UPX. Let's decompress the file:
```
$ upx -d ./out
...
Unpacked 1 file.
```

Now let's use `strings` again to see if there is any new useful information. This time we can try searching for the word `password` to see if there is any relevant text.
```
$ strings ./out | grep "password"
Enter the password to unlock this file: 
```

Nothing useful, let's look for the word "flag" this time.

```
$ strings ./out | grep "flag"
Password correct, please see flag: 7069636f4354467b5539585f556e5034636b314e365f42316e34526933535f36666639363465667d
(mode_flags & PRINTF_FORTIFY) != 0
WARNING: Unsupported flag value(s) of 0x%x in DT_FLAGS_1.
version == NULL || !(flags & DL_LOOKUP_RETURN_NEWEST)
flag.c
_dl_x86_hwcap_flags
_dl_stack_flags
```

The flag seems to be encoded as hex values. Converting these hex values to their ASCII values, we can get the flag and solve the challenge:
```
picoCTF{U9X_UnP4ck1N6_B1n4Ri3S_6ff964ef}
```
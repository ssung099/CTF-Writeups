---
title: "unpackme.flag.py"
date: 2026-08-29
tags: ["picoCTF"]
categories: ["rev"]
draft: false
---

## Summary
This challenge provides us with a Python source file with the following description:
```
Can you get the flag?
Reverse engineer this Python program.
```

Artifacts:
- [unpackme.flag.py](https://github.com/ssung099/CTF-Writeups/blob/main/picoCTF/rev/unpackme.flag.py/chall/unpackme.flag.py): the chall file

## Solve explanation
Let's first inspect the source code provided to us.
```python
import base64
from cryptography.fernet import Fernet

payload = b'gAAAAABkzWGWvEp8gLI9AcIn5o-ahDUwkTvM6EwF7YYMZlE-_Gf9rcNYjxIgX4b0ltY6bcxKarib2ds6POclRwCwhsRb1LOXVt4Q3ePtMY4BmHFFZlIHLk05CjwigT7hiI9p3sH9e7Cpk1uO90xbHbuy-mfi3nkmn411aBgwxyWpJvykpkuBIG_nty6zbox3UhbB85TOis0TgM0zG4ht0-GUW4wTq2_5-wkw3kV1ZAisLJHzF-Z9oLMmwFZU0UCAcHaBTGDF5BnVLmUeCGTgzVLSNn6BmB61Yg=='

key_str = 'correctstaplecorrectstaplecorrec'
key_base64 = base64.b64encode(key_str.encode())
f = Fernet(key_base64)
plain = f.decrypt(payload)
exec(plain.decode())
```

We can see that there is a payload that is decrypted using the Fernet library, with `key_str` encoded in Base64 as the key.

To figure out what the payload does, we can comment out the `exec` line and add a `print` statement instead, then run the program.

```python
...
key_str = 'correctstaplecorrectstaplecorrec'
key_base64 = base64.b64encode(key_str.encode())
f = Fernet(key_base64)
plain = f.decrypt(payload)
# exec(plain.decode())
print(plain)
```

Running the program, we get the following output:
```bash
$ python unpackme.flag.py 
b"\npw = input('What\\'s the password? ')\n\nif pw == 'batteryhorse':\n  print('picoCTF{175_chr157m45_85f5d0ac}')\nelse:\n  print('That password is incorrect.')\n\n"
```

The flag is embedded directly in the decrypted payload, solving the challenge.
```
picoCTF{175_chr157m45_85f5d0ac}
```
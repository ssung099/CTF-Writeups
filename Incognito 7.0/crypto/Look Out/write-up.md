---
title: "Look Out"
date: 2026-04-17
tags: ["Incognito 7.0"]
categories: ["crypto"]
draft: true
---

## Summary
This challenge provides us with the following description and an `Untitled_document.pdf`.
```
Look it's plane, no it's a jet, no it's a bird!!!!!!!
```
<!-- Insert Image -->

Artifacts:
- `Untitled_document.pdf`: contains a picture of birds on a wire.
- `solve.py`: a python script that decodes the metadata binary and XORs it with a key.

## Solve Explanation
Looking at the PDF file directly, there does not seem to be anything that can help us obtain a flag.

I first inspected the metadata of the PDF file using `exiftool`.
```
$ ./exiftool.exe "./Incognito 7.0/crypto/Look Out/Untitled_document.pdf"
ExifTool Version Number         : 13.57
File Name                       : Untitled_document.pdf
Directory                       : ./Incognito 7.0/crypto/Look Out
...
Subject                         : 00100101001001100010011000111111001111110001011100011101000000110000110000010010001101000001001000011000000001110011000000001100000010110000001000000000000101100000001000011101000010110011011000000111000010100000110100110100010100100100000001001100010111010101111001011100010110110101011001011000010110000100011000010001
Title                           : Untitled document
Producer                        : Skia/PDF m148 Google Docs Renderer
Keywords                        : What, is, this?
```

The long binary value in the subject of the metadata immediately stands out.

Breaking the value into 8-bit chunks and converting to hex, we get the following: 

`25 26 26 3F 3F 17 1D 03 0C 12 34 12 18 07 30 0C 0B 02 00 16 02 1D 0B 36 07 0A 0D 34 52 40 4C 5D 5E 5C 5B 56 58 58 46 11`.

Although we seem to be on the right track, the hex value does not directly decode into a readable flag.

Next, I tried inspecting the raw file to see if there are any other hidden information. After scanning through the file, I noticed that the raw file contains some `/Alt (char\)` elements.
```
/Alt (char\(76\))
...
/Alt (char\(79\))
...
/Alt (char\(79\))
...
```

These values seem to fall into the alphabet range in the ASCII table. Using `strings.exe`, I searched the file for just the `/Alt (char\)` elements.

```
$ strings.exe '.\Incognito 7.0\crypto\Look Out\Untitled_document.pdf' | Select-String "/Alt"
/Alt (char\(76\))
/Alt (char\(79\))
/Alt (char\(79\))
/Alt (char\(75\))
/Alt (char\(83\))
/Alt (char\(76\))
/Alt (char\(73\))
/Alt (char\(75\))
/Alt (char\(69\))
/Alt (char\(65\))
/Alt (char\(75\))
/Alt (char\(69\))
/Alt (char\(89\))
/Alt (char\(84\))
/Alt (char\(79\))
/Alt (char\(77\))
/Alt (char\(69\))
```

Mapping each of the values to the ASCII table, we get the string `LOOKSLIKEAKEYTOME`.

Going back to the hex value retrieved from the PDF metadata, I tried XORing the bytes with this key.

```
$ python3 solve.py LOOKSLIKEAKEYTOME
Flag: iiitl[THISWASANNOYINGLOL]
```

We get some readable flag but the letter casing seems off. Therefore, I tried again with the lowercased key `lookslikeakeytome`.
```
$ python3 solve.py lookslikeakeytome
Flag: IIITL{this_was_annoying_lol_79823979735}
```

This gives us the correct flag and we can solve the challenge.
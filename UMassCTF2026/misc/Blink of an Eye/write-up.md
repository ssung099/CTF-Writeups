---
title: "Blink of an Eye"
date: 2026-04-13
tags: ["UMassCTF-2026"]
categories: ["osint"]["crypto"]
draft: false
---

## Summary
This challenge provides the following description and a `nums.txt` file.
```
This Ohio '67 director once watched over a hero-creating hopecore machine. One of his actors (a wine expert) was the subject of a legal dispute between a Cannon and a giant Dane. My secrets are on page 138.

nums.txt
pieces = [
6196548
,379526
,6175367
,300426
,300426
,362326
,6092585
,6234695
,4644456
,302001
...
]
```

Artifacts:
- `nums.txt`: contains an array `pieces` with integers as its elements.

## Solve Explanation:

### OSINT Aspect
From the description, the key words that I noticed were `Ohio '67 director`, `a wine expert actor`, `legal dispute between a Cannon and a giant Dane`, and `secrets ... page 138`.

I initially tried identifying directors born in Ohio in 1967, but this was too broad to be useful. Similarly, searching for a “wine expert” actor did not meaningfully narrow things down.

I then focused on the phrase “legal dispute between a Cannon and a giant Dane,” which seemed intentionally obfuscated. Interpreting “giant Dane” as a reference to a large Danish company, and considering the Lego theme of the CTF, this pointed toward Lego.

Searching for legal disputes involving Lego led to Concannon v. Lego Systems, Inc., where artist James Concannon sued Lego over the `Queer Eye - The Fab 5 Loft` set. The director of the TV series "Queer Eye" was David Collins who was born on 1967 in Ohio and one of the "Fab 5" was Antoni Poroski who is a wine expert. 

At this point, I considered two possible sources for “page 138”: the legal document and the Lego instruction manual. The legal document did not provide anything useful, but the instruction manual did have a page 138, listing all the Lego piece IDs used in the set.

Here is a screenshot of page 138:
<!-- insert picture -->

### Crypto Aspect
Since nums.txt contains an array called pieces, the values clearly correspond to Lego piece IDs from this list.
Since the flag format was UMASS{}, each piece should be representing one character. From the flag format, we would know the mapping to the first 6 pieces and the last piece.
Looking through the rest of the pieces, I noticed that the piece id `6234695` appeared frequently in `pieces`. Given the nature of CTF flags, I assumed that this would be representing the char `_`.

To figure out the rest of the mappings, you needed to assign each piece of 138 to ascii key value. Starting from the top left and moving down the columns sequentially, we assign each piece to a number starting from 0. By doing so we can verify that the first 6 pieces `6196548`, `379526` , `6175367` , `300426`,`300426` , `362326` in fact maps to `UMASS{`. By going through each piece and retrieving the respective ascii key value, we can get the flag and solve the challenge.

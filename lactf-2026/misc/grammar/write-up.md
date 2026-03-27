# grammar

## Summary
The `grammar` challenge authors provide the parse tree of the flag and the grammar that defines the structure of flag. The grammar and the parse tree can be used together to generate the full flag.

Artifacts:
- `tree.png`: the parse tree of the flag
- `grammar-notes.txt`: the grammar rules defining the structure of the flag.

## Solve Explanation
Looking at the `grammar-notes.txt`, we can see that the flag is defined in EBNF (Extended Backus-Naur Form).

The production rule of the flag is defined as `start, word, {underscore, word}, end`. In EBNF, commas (`,`) represent concatenation of terminals and nonterminals, while curly braces (`{...}`) indicate the contained terminals and/or nonterminals are repeated 0 or more times. This is equivalent to the Kleene Star (`*`) in regex expressions.

From this production rule and the provided parse tree, we can further reason about the production rule of the flag, which can be expanded as to `start, word, underscore, word, underscore, word, end`. Since we also know that `start`, `underscore`, and `end` are production rules for terminal characters, we only need to figure out the how each `word` of the flag was structured. From these information, we can partially fill in the parse tree.

[INSERT PARSE TREE]

The next step is to figure out how each word in the flag was produced. From the grammar rules, we see that the production of word is `fragment, {fragment}`. In other words, a `word` is produced by one or more repetitions of `fragment`. `fragment` is defined as `cd | vc | vd | c | d`, meaning that each fragment can be produced by any of the nonterminals `cd`, `vc`, `vd`, `c`, `d`.

Before we can figure out how each word in the flag is produced, we need to figure out which `nonterminal` is represented by which `fragment`. In the parse tree, each colored circle (besides black) represents a unique production of `fragment`. As the grammar notes states, "Circles of the same color represent the same nonterminal (excluding black circles, which can be any)".

We can figure out which color refers to which production of `fragment` based on the parse subtree for each fragment color. Looking at the yellow and red parse subtrees, we can see that these fragment only result in one terminal character. This means that the only candidates for these fragment colors are `c` and `d`. Similarly, the other color fragments (blue, green, and purple) result in two terminal characters, meaning that its candidates are `cd`, `vc`, and `vd`.

We can further reason about the possible candidates for each fragment color based on the number of nonterminals in the parse subtrees for each fragment color. Looking at the leftmost parse subtree for the blue fragment, we can see that the first terminal character is a result of five nonterminals while the second terminal character is a result of one nonterminal. Given the candidates `cd`, `vc`, and `vd`, the first terminal character must be a product of `c` or `v`. However, given that `v` can only produce up to three nonterminals, it must be the case that the first nonterminal of the blue fragment must have been produced by the rule for `c`. Therefore, it only follows that blue represents the fragment production for `cd`.

We can repeat a similar step for fragment pruple and green to eliminate candidates. Looking at the leftmost parse subtree for purple fragment, we can see that the second terminal character is a result of five nonterminal characters. Given the remaining candidates `vc` and `vd`, the second terminal character must be a product of `c` or `d`. Once again, since `d` can only produce at most four nonterminal characters, it must be that the second terminal character for purple was produced by the rule for `c` and therefore, purple represents the fragment production for `vc`. Since only `vd` remains, we also now know that green was the representation for `vd`.

For yellow and red, it is not possible to figure out which `fragment` production rule refers to which as the parse subtrees do not tell us any additional information. The highest number of nonterminals for yellow and red are both four. Given that `c` and `d` can both produce four nonterminals, we cannot reason any further and must try both possibilities.

```
Fixed Colors:
blue = 'cd'
purple = 'vc'
green = 'vd'

Combination 1:
yellow = 'c'
red = 'd'

Combination 2:
yellow = 'd'
red = 'c'
```

By using testing both combinations with the parse tree, we can obtain the correct flag and solve the challenge.
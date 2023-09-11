# MOCUS-variants

supermodel = [("TOP", "Or", ["a", "G1"]),
      ("G1", "And", ["G2", "G3"]),
      ("G2", "Or", ["b", "c"]),
      ("G3", "Or", ["d", "e"])]

Input:  a,b,c
output: 
Minimal Cut Sets for Supermodel is:
[['a'], ['b', 'd'], ['d', 'c'], ['e', 'b'], ['e', 'c']]
Minimal Cut Sets for variant is:
[['a'], ['b'], ['c']]

Input: a,b,c,d
Minimal Cut Sets for Supermodel is:
[['a'], ['d', 'b'], ['d', 'c'], ['e', 'b'], ['c', 'e']]
Minimal Cut Sets for variant is:
[['a'], ['d', 'b'], ['d', 'c']]

Input:  a,c,d,e
Minimal Cut Sets for Supermodel is:
[['a'], ['d', 'b'], ['d', 'c'], ['e', 'b'], ['c', 'e']]
Minimal Cut Sets for variant is:
[['a'], ['d', 'c'], ['e', 'c']]

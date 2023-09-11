# MOCUS-variants

supermodel = [("TOP", "Or", ["a", "G1"]),
      ("G1", "And", ["G2", "G3"]),
      ("G2", "Or", ["b", "c"]),
      ("G3", "Or", ["d", "e"])]

 Input: 
 a,b,c
 output: 
 Minimal Cut Sets for Supermodel is:
[['a'], ['b', 'd'], ['d', 'c'], ['e', 'b'], ['e', 'c']]
Minimal Cut Sets for variant is:
[['a'], ['b'], ['c']]

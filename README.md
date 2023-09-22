# Fault Tree analysis with MOCUS method for variants
This Program calculates minimal cut sets for the fault tree of a 150% model and its variants.
First, the Boolean formula for the Fault tree is given inside the code.
This program asks the user to enter the elements of a specific variant and it calculates minimal cut sets for that specific variant 



supermodel = [("TOP", "Or", ["a", "G1"]),
      ("G1", "And", ["G2", "G3"]),
      ("G2", "Or", ["b", "c"]),
      ("G3", "Or", ["d", "e"])]


Input: a,b,c,d
Minimal Cut Sets for Supermodel is:
[['a'], ['b', 'd'], ['c', 'd'], ['b', 'e'], ['c', 'e']]
Minimal Cut Sets for variant is:
[['a'], ['b', 'd'], ['c', 'd']]

Input:  a,c,d,e
Minimal Cut Sets for Supermodel is:
[['a'], ['d', 'b'], ['d', 'c'], ['b', 'e'], ['c', 'e']]
Minimal Cut Sets for variant is:
[['a'], ['c', 'd'], ['c', 'e']]

Input: a,b,d,e
Minimal Cut Sets for Supermodel is:
[['a'], ['d', 'b'], ['d', 'c'], ['b', 'e'], ['c', 'e']]
Minimal Cut Sets for variant is:
[['a'], ['d', 'b'], ['b', 'e']]

Input: b,c,d,e
Minimal Cut Sets for Supermodel is:
[['a'], ['d', 'b'], ['c', 'd'], ['e', 'b'], ['e', 'c']]
Minimal Cut Sets for variant is:
[['b', 'd'], ['e', 'b'], ['c', 'd'], ['e', 'c']]

Input: a,b,d
Minimal Cut Sets for Supermodel is:
[['a'], ['b', 'd'], ['c', 'd'], ['b', 'e'], ['c', 'e']]
Minimal Cut Sets for variant is:
[['a'], ['b', 'd']]

Input:  a,b,c
output: 
Minimal Cut Sets for Supermodel is:
[['a'], ['b', 'd'], ['d', 'c'], ['e', 'b'], ['e', 'c']]
Minimal Cut Sets for variant is:
[['a'], ['b'], ['c']]

Input: a,c,e
Minimal Cut Sets for Supermodel is:
[['a'], ['d', 'b'], ['d', 'c'], ['e', 'b'], ['e', 'c']]
Minimal Cut Sets for variant is:
[['a'], ['e', 'c']]

Input: a,b,e
Minimal Cut Sets for Supermodel is:
[['a'], ['d', 'b'], ['d', 'c'], ['e', 'b'], ['e', 'c']]
Minimal Cut Sets for variant is:
[['a'], ['e', 'b']]

Input: a,c,d
Minimal Cut Sets for Supermodel is:
[['a'], ['d', 'b'], ['d', 'c'], ['e', 'b'], ['e', 'c']]
Minimal Cut Sets for variant is:
[['a'], ['d', 'c']]

Input: a,b
Minimal Cut Sets for Supermodel is:
[['a'], ['b', 'd'], ['d', 'c'], ['e', 'b'], ['e', 'c']]
Minimal Cut Sets for variant is:
[['a'], ['b']]

Input: b,e
Minimal Cut Sets for Supermodel is:
[['a'], ['d', 'b'], ['d', 'c'], ['e', 'b'], ['e', 'c']]
Minimal Cut Sets for variant is:
[['e', 'b']]

Input: a,c
Minimal Cut Sets for Supermodel is:
[['a'], ['d', 'b'], ['c', 'd'], ['b', 'e'], ['c', 'e']]
Minimal Cut Sets for variant is:
[['a'], ['c']]

Input: a
Minimal Cut Sets for Supermodel is:
[['a'], ['d', 'b'], ['d', 'c'], ['b', 'e'], ['e', 'c']]
Minimal Cut Sets for variant is: 
[a]

Input: b
Minimal Cut Sets for Supermodel is:
[['a'], ['b', 'd'], ['d', 'c'], ['b', 'e'], ['c', 'e']]
Minimal Cut Sets for variant is: 
[b]

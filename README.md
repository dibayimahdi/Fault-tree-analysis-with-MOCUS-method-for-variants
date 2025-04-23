# ⚙️ Fault Tree Analysis with MOCUS Method for Variants

This Python program computes **minimal cut sets** for a given **150% fault tree model (supermodel)** and its **variants**, based on user-specified active components (variant variables).

It supports systematic **variant reduction** of the supermodel and applies the **MOCUS (Method Of Cut Sets)** algorithm to compute the minimal cut sets.

---

## 📄 Related Publication

This implementation is based on the research presented in the following IEEE publication:

📘 **"An Efficient Cut Set Computation Approach for Variant-Aware Fault Tree Analysis"**  
🖋️ Authors: Mahdi Dibaei, et al.  
📅 Published: 2024  
📚 Available on IEEE Xplore  
🔗 [View the Paper](https://ieeexplore.ieee.org/abstract/document/10381472)

Please refer to this paper for the theoretical background, algorithms, and case studies.

✏️ TODO:
 Add support for multi-input gates

 Improve UI with error handling and formatting

 Optionally export results to a file (e.g., CSV)

📫 Contact:
For academic use or collaboration inquiries, feel free to cite the IEEE paper or contact the authors through the IEEE Xplore page.

---

## 🧠 What This Program Does

- Defines a **supermodel fault tree** as a list of logic gates and basic events.
- Takes user input to define **active variant components**.
- Prunes the model to reflect only selected variant variables.
- Computes minimal cut sets for both the **original supermodel** and the **derived variant model** using the MOCUS method (via `cutsets.mocus()`).

---



## 🧪 Example Supermodel

```python
supermodel = [
    ("TOP", "Or", ["a", "G1"]),
    ("G1", "And", ["G2", "G3"]),
    ("G2", "Or", ["b", "c"]),
    ("G3", "Or", ["d", "e"])
]


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






# 🚀 DSA Journey — Day 02

**Date:** 10–11 October 2026  
**Programming Language:** Python 🐍  
**Practice Platforms:** GeeksforGeeks & LeetCode  
**Questions Covered:** 7 (Q8–Q14)  
**Topics:** Mathematics, Arrays, Binary Exponentiation, Two Pointers

---

## 🎯 Day 02 Overview

On Day 02 of my DSA journey, I continued practicing mathematical problems and started learning array-based problem-solving techniques.

I focused on writing efficient Python solutions, debugging errors, understanding edge cases, and learning how to optimize algorithms.

## 📚 Questions Practiced

| No. | Problem | Approach | Time Complexity | Space Complexity |
|---|---|---|---|---|
| Q8 | [LCM and GCD](https://www.geeksforgeeks.org/problems/lcm-and-gcd4516/1) | Euclidean Algorithm | O(log(min(a,b))) | O(1) |
| Q9 | [Fibonacci Number](https://leetcode.com/problems/fibonacci-number/) | Iterative Approach | O(n) | O(1) |
| Q10 | [Pow(x, n)](https://leetcode.com/problems/powx-n/) | Binary Exponentiation | O(log \|n\|) | O(1) |
| Q11 | [Largest Element in Array](https://www.geeksforgeeks.org/problems/largest-element-in-array4009/1) | Linear Traversal | O(n) | O(1) |
| Q12 | [Second Largest Element](https://www.geeksforgeeks.org/problems/second-largest3735/1) | Single-Pass Traversal | O(n) | O(1) |
| Q13 | [Check if Array Is Sorted](https://www.geeksforgeeks.org/problems/check-if-an-array-is-sorted0701/1) | Adjacent Comparison | O(n) | O(1) |
| Q14 | [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | Two Pointers | O(n) | O(1) |

## 💻 Python Files and Progress

| Question | Python Filename | Progress |
|---|---|---|
| Q8 | `Q8_LCM_of_Two_Numbers.py` | Code written and logic reviewed |
| Q9 | `Q9_Fibonacci_Number.py` | Logic learned; implementation pending |
| Q10 | `Q10_Power_of_a_Number.py` | Optimized solution studied |
| Q11 | `Q11_Largest_Element_in_Array.py` | Initial attempt; edge-case fix pending |
| Q12 | `Q12_Second_Largest_Element.py` | Code written and logic reviewed |
| Q13 | `Q13_Check_If_Array_Is_Sorted.py` | Correct solution verified |
| Q14 | `Q14_Remove_Duplicates_From_Sorted_Array.py` | Complete solution studied |

*These are the planned filenames from my practice sessions. Repository uploads and platform submissions should be verified separately.*

## 🧠 Key Learnings

### 1. LCM and GCD

- Practiced the Euclidean Algorithm.
- Learned to preserve original numbers before modifying variables.
- Used the formula:

  `LCM(a, b) = (a × b) // GCD(a, b)`

### 2. Fibonacci Number

- Understood how Fibonacci numbers are generated.
- Learned the iterative approach using two variables.
- Explored how previous values help calculate the next term.

### 3. Binary Exponentiation

- Initially explored repeated multiplication.
- Encountered a Time Limit Exceeded issue for large exponents.
- Learned how Binary Exponentiation reduces the time complexity from O(n) to O(log n).
- Understood how to handle negative exponents.

### 4. Largest Element in an Array

- Practiced finding the maximum element using linear traversal.
- Learned why initializing the maximum value to `0` fails for arrays containing only negative numbers.
- Understood the importance of choosing correct initial values.

### 5. Second Largest Element

- Practiced tracking the largest and second-largest elements.
- Learned how to find the second-largest distinct element in a single traversal.
- Improved conditional logic.

### 6. Check if Array Is Sorted

- Learned to compare adjacent elements.
- Fixed an `IndexError` caused by incorrect indexing.
- Understood why returning `True` inside the loop can produce incorrect results.
- Successfully corrected the solution to handle sorted, unsorted, and single-element arrays.

### 7. Remove Duplicates from Sorted Array

- Learned the Two Pointers technique.
- Understood in-place array modification.
- Explored Python built-in functions such as `set()` and `sorted()`.
- Compared the built-in approach with the optimized O(1)-extra-space solution.

## 🐛 Errors and Debugging

| Question | Issue | What I Learned |
|---|---|---|
| Q8 | Original values changed during GCD calculation | Preserve inputs before updating variables |
| Q10 | Time Limit Exceeded | Use Binary Exponentiation |
| Q11 | Incorrect initialization of maximum | Consider negative-number edge cases |
| Q13 | IndexError due to incorrect loop boundaries | Understand Python's zero-based indexing |
| Q13 | Returning too early inside the loop | Check the complete array before returning `True` |
| Q14 | Built-in approach uses additional memory | Use Two Pointers for O(1) extra space |

## 📊 Progress Summary

**7 questions covered during Day 02.**

- Code written and logic reviewed: Q8, Q12, Q13
- Optimized solution studied: Q10, Q14
- Logic studied; implementation pending: Q9
- Initial implementation needs correction: Q11

**Cumulative questions covered: 14**

## 🎯 Next Goals

- Complete the remaining pending implementations.
- Strengthen array traversal.
- Practice additional Two Pointers problems.
- Improve edge-case handling.
- Continue learning optimized algorithms.

---

**Day 02 Reflection:**  
Today, I learned that solving a problem is not only about writing working code. Understanding edge cases, choosing the right approach, and improving time complexity are equally important.

*Learn. Code. Debug. Optimize. Repeat.* 🚀

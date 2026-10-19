# 🚀 DSA Journey — Day 04

**Language:** Python 🐍  
**Topics:** Arrays, Mathematics, Sorting, Digit Manipulation, Functions  
**Questions Solved:** 6  
**Question Range:** Q23–Q28

---

## 📚 Problems Practiced

| No. | Problem | Concepts | Python File |
|---|---|---|---|
| Q23 | Quadratic Equation Roots | Mathematics, Discriminant | [Q23_Quadratic_Equation_Roots.py](Q23_Quadratic_Equation_Roots.py) |
| Q24 | Find Median of Array | Arrays, Sorting | [Q24_Find_Median_of_Array.py](Q24_Find_Median_of_Array.py) |
| Q25 | Find Mean of Array | Arrays, Arithmetic Mean | [Q25_Find_Mean_of_Array.py](Q25_Find_Mean_of_Array.py) |
| Q26 | Alternate Elements of Array | Arrays, Iteration | [Q26_Alternate_Elements_of_Array.py](Q26_Alternate_Elements_of_Array.py) |
| Q27 | Palindrome Array | Arrays, Digit Reversal, Functions | [Q27_Palindrome_Array.py](Q27_Palindrome_Array.py) |
| Q28 | Replace All Zeros With Five | Mathematics, Digit Manipulation | [Q28_Replace_All_Zeros_With_Five.py](Q28_Replace_All_Zeros_With_Five.py) |

---

## 🧠 Concepts Learned

### 1. Quadratic Equation Roots
- Calculated the discriminant using `D = b² - 4ac`.
- Used the quadratic formula to calculate real roots.
- Handled negative discriminants.
- Returned roots in descending order.

**Time Complexity:** O(1)  
**Space Complexity:** O(1)

### 2. Median of an Array
- Sorted the array before calculating the median.
- Handled both odd-length and even-length arrays.
- Practiced array indexing and integer division.

**Time Complexity:** O(n log n)  
**Space Complexity:** O(n) worst case for Python sorting

### 3. Mean of an Array
- Traversed an array using a `for` loop.
- Calculated the sum of all elements.
- Used floor division to calculate the integer mean.

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

### 4. Alternate Elements of an Array
- Used `range()` with a step size of 2.
- Selected elements at indices `0, 2, 4, ...`.
- Practiced creating and returning a result list.

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

### 5. Palindrome Array
- Reversed the digits of each number mathematically.
- Used a helper method to check individual numbers.
- Checked whether every array element was a palindrome.

**Time Complexity:** O(n × d), where d is the maximum number of digits  
**Space Complexity:** O(1)

### 6. Replace All Zeros With Five
- Extracted digits using the modulo operator `%`.
- Replaced zero digits with five.
- Reconstructed the number using powers of 10.
- Handled the special case `n = 0`.

**Time Complexity:** O(d), where d is the number of digits  
**Space Complexity:** O(1) for fixed-size integers

---

## 💻 Skills Practiced

- Python loops and conditional statements
- Array traversal and indexing
- Mathematical formulas
- Sorting and finding middle elements
- Writing reusable helper functions
- Digit extraction and number reconstruction
- Handling edge cases
- Understanding time and space complexity

---

## 🌟 Day 04 Achievement

Today, I independently wrote Python solutions for six DSA problems.

My main focus was improving my ability to translate problem statements into working code without immediately relying on hints or complete solutions.

I also practiced organizing my solutions with meaningful filenames, documentation, and complexity analysis.

**Progress Note:** All six solutions were submitted for code review and prepared for GitHub. Online judge acceptance has not been independently verified.

---

## 📂 Folder Structure

```text
DSA-Journey/
└── Day4/
    ├── Q23_Quadratic_Equation_Roots.py
    ├── Q24_Find_Median_of_Array.py
    ├── Q25_Find_Mean_of_Array.py
    ├── Q26_Alternate_Elements_of_Array.py
    ├── Q27_Palindrome_Array.py
    ├── Q28_Replace_All_Zeros_With_Five.py
    └── README.md
```

---

## 🎯 Goals for Day 05

- Continue solving problems independently.
- Strengthen mathematical and array-based problem-solving skills.
- Practice identifying edge cases before submission.
- Improve code readability and complexity analysis.
- Revise previously solved problems when needed.

---

### 📈 DSA Journey Progress

| Day | Questions Covered |
|---|---|
| Day 01 | Q1–Q7 |
| Day 02 | Q8–Q14 |
| Day 03 | Q15–Q21 |
| Day 04 | Q22–Q28 (Q22 studied; Q23–Q28 independently coded) |

**Total Questions Covered:** 28  
**Day 04 Independently Written Solutions:** 6

---

**GitHub Repository:** [DSA-Journey](https://github.com/Kumkum-lohiya/DSA-Journey/)

*Consistency over speed. Learn, practice, revise, and improve every day.* 💪

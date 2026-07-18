## 📁 Chapter 3 Practical Applications: Pay & Score Calculators

This file contains Python scripts solving two foundational core exercises from Chapter 3 of the *Python for Everybody* course. These scripts focus on control flow, advanced conditional logic, and strict user input validation.

### 1. Overtime Pay Calculator
* **Objective:** Automatically calculates an employee's total gross pay based on total hours worked and a standard hourly rate.
* **Logic Breakdown:** 
  * If hours worked are **40 or less**, the standard rate applies (`hours * rate`).
  * If hours exceed **40**, the script calculates the first 40 hours at the regular rate, and applies a **1.5x overtime multiplier** to all additional hours worked.
* **Error Handling:** Implements a strict `try/except` block to intercept non-numeric text inputs, preventing program crashes and prompting a clean exit message.

### 2. Academic Score Grader
* **Objective:** Converts a numerical academic score ranging between `0.0` and `1.0` into a standard letter grade.
* **Logic Breakdown:**
  * First, it performs a strict boundary check using chained conditional syntax (`1.0 >= score >= 0.0`) to ensure the score is valid.
  * It then triggers a nested multi-way decision chain (`if/elif/else`) to map out the correct grade:
    * `>= 0.9` ➔ **A**
    * `>= 0.8` ➔ **B**
    * `>= 0.7` ➔ **C**
    * `>= 0.6` ➔ **D**
    * `< 0.6`  ➔ **F**
* **Error Handling:** Protects against bad user input by validating data types first and safely prompting the user to re-enter values if they fall out of bounds.

---
*Built as part of a structured programming portfolio to demonstrate fundamental mastery of Python syntax, logic tracking, and defensive coding patterns.*

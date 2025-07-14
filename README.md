# Codtech-Task-4-A-Business-Problem
- COMPANY: CODTECH IT SOLUTIONS
- NAME: BHUKYA JANI
- INTERN ID: CT04DH2696
- DOMAIN: DATA SCIENCE
- DURATION: 4 WEEKS
- MENTOR: NEELA SANTOSH
## 🔍 Overview
This project applies **Linear Programming (LP)** using the **PuLP** library in Python to solve a real-world business optimization problem.

The scenario involves a retail business that wants to stock two products while maximizing profit under budget and space constraints. LP helps determine the optimal number of each product to stock.

---

## 📈 Problem Statement
A business wants to stock **Product A** and **Product B** to **maximize profit**. Each product has associated cost and space requirements. The business must stay within a fixed **budget of ₹200** and **warehouse space limit of 100 units**.

| Product | Profit (₹/unit) | Cost (₹/unit) | Space (units) |
|---------|------------------|----------------|----------------|
| A       | 20               | 5              | 3              |
| B       | 30               | 7              | 4              |

---

## 🧮 Mathematical Formulation

**Objective Function:**  
Maximize `Profit = 20x + 30y`

**Subject To:**  
- `5x + 7y ≤ 200` (Budget constraint)  
- `3x + 4y ≤ 100` (Space constraint)  
- `x, y ≥ 0` (Non-negative values)

Where `x` = units of Product A and `y` = units of Product B.

---

## ⚙️ Technologies Used
- Python  
- PuLP (Linear Programming Solver)

---

## ✅ Result
Using the PuLP solver, the optimal stocking strategy is:
- ✅ **Product A:** 16 units  
- ✅ **Product B:** 10 units  
- 💰 **Maximum Profit:** ₹620

---

## 🧪 How to Run

1. Make sure PuLP is installed:
   ```bash
   pip install pulp
Run the script:

bash
Copy
Edit
python TASK4.py
📁 Files Included
bash
Copy
Edit
Task-4-Optimization/
├── TASK4.py            # Python script with optimization logic
├── README.md           # Project documentation
📌 Conclusion
This task demonstrates how linear programming can be used to solve real-world decision-making problems efficiently. It showcases the power of mathematical modeling in business optimization, an essential skill for data science professionals.
#OUTPUT

from pulp import LpMaximize, LpProblem, LpVariable, value

# Define the LP problem
model = LpProblem("Inventory_Optimization", LpMaximize)

# Decision variables
x = LpVariable("Product_A", lowBound=0, cat='Integer')
y = LpVariable("Product_B", lowBound=0, cat='Integer')

# Objective function
model += 20 * x + 30 * y, "Total_Profit"

# Constraints
model += 5 * x + 7 * y <= 200, "Cost_Constraint"
model += 3 * x + 4 * y <= 100, "Space_Constraint"

# Solve the model
model.solve()

# Output
print(f"Optimal number of Product A to stock: {x.varValue}")
print(f"Optimal number of Product B to stock: {y.varValue}")
print(f"Maximum Profit: ₹{value(model.objective)}")

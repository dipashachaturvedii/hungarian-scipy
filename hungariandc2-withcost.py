import tkinter as tk
from tkinter import messagebox
import numpy as np
import scipy.optimize as opt

def hungarian_method(cost_matrix):
    # Convert the cost matrix to a profit matrix by subtracting each element from the maximum value in the matrix.
    min_value = np.min(cost_matrix)
    profit_matrix = cost_matrix - min_value

    # Use scipy's linear_sum_assignment function to find the optimal assignment.
    row_indices, col_indices = opt.linear_sum_assignment(profit_matrix)

    total_cost = np.sum(cost_matrix[row_indices, col_indices])

    return row_indices, col_indices, total_cost

def solve_problem():
    try:
        n = len(cost_entries)
        m = len(cost_entries[0])
        cost_matrix = np.array([[int(cost_entries[i][j].get()) for j in range(m)] for i in range(n)]
)
        row_indices, col_indices, total_cost = hungarian_method(cost_matrix)

        for i in range(n):
            for j in range(m):
                cost_entries[i][j].config(state=tk.NORMAL)
                cost_entries[i][j].delete(0, tk.END)

        for i, j in zip(row_indices, col_indices):
            cost_entries[i][j].insert(0, "X")
            cost_entries[i][j].config(state=tk.DISABLED)

        total_cost_label.config(text=f"Total Cost: {total_cost}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers in all cells.")

root = tk.Tk()
root.title("Unbalanced Hungarian Method")

# Create a grid of Entry widgets to input the cost matrix.
cost_entries = []
n, m = 4, 5  # Adjust the values of n and m as needed.

for i in range(n):
    row_entries = []
    for j in range(m):
        entry = tk.Entry(root, width=5)
        entry.grid(row=i, column=j)
        row_entries.append(entry)
    cost_entries.append(row_entries)

# Create a button to solve the problem.
solve_button = tk.Button(root, text="Solve", command=solve_problem)
solve_button.grid(row=n, column=m // 2)

# Label to display the total cost.
total_cost_label = tk.Label(root, text="")
total_cost_label.grid(row=n + 1, column=m // 2)

root.mainloop()

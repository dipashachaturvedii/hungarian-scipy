import tkinter as tk
from tkinter import messagebox
from scipy.optimize import linear_sum_assignment
import numpy as np

def solve_assignment_problem(cost_matrix):
    rows, cols = cost_matrix.shape
    # If there are more rows than columns, add dummy columns
    if rows > cols:
        dummy_cols = np.zeros((rows, rows - cols))
        cost_matrix = np.hstack((cost_matrix, dummy_cols))
    # If there are more columns than rows, add dummy rows
    if cols > rows:
        dummy_rows = np.zeros((cols - rows, cols))
        cost_matrix = np.vstack((cost_matrix, dummy_rows))
    
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    # Only return the assignments for the original rows and columns
    row_assignments = row_ind[:rows]
    col_assignments = col_ind[:cols]
    return row_assignments, col_assignments

def solve_problem():
    input_text = cost_matrix_entry.get("1.0", "end-1c")
    try:
        lines = input_text.split("\n")
        cost_matrix = []
        for line in lines:
            row = list(map(int, line.split()))
            cost_matrix.append(row)
        cost_matrix = np.array(cost_matrix)
        row_assignments, col_assignments = solve_assignment_problem(cost_matrix)
        result_text = f"Row Assignments: {row_assignments}\nColumn Assignments: {col_assignments}"
        result_label.config(text=result_text)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid cost matrix.")

# Create the main window
root = tk.Tk()
root.title("Unbalanced Hungarian Method Solver")

# Create input text box
cost_matrix_label = tk.Label(root, text="Enter the cost matrix:")
cost_matrix_label.pack()
cost_matrix_entry = tk.Text(root, width=40, height=10)
cost_matrix_entry.pack()

# Create a button to solve the problem
solve_button = tk.Button(root, text="Solve", command=solve_problem)
solve_button.pack()

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

# Run the Tkinter main loop
root.mainloop()

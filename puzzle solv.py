import tkinter as tk
from tkinter import messagebox

# Sudoku solver using backtracking
def is_valid(board, row, col, num):
    # Check if 'num' is not in the current row
    for i in range(3):
        if board[row][i] == num:
            return False

    # Check if 'num' is not in the current column
    for i in range(3):
        if board[i][col] == num:
            return False

    # Check if 'num' is not in the current 3x3 box
    start_row, start_col = (row // 3) * 3, (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def solve_sudoku(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                for num in range(1, 4):
                    if is_valid(board, row, col, num):
                        board[row][col] = num

                        if solve_sudoku(board):
                            return True

                        board[row][col] = 0
                return False
    return True

# Function to solve the Sudoku puzzle and update the GUI
def solve_puzzle():
    board = []
    for i in range(3):
        row = []
        for j in range(3):
            val = entries[i][j].get()
            if val == "":
                row.append(0)
            else:
                row.append(int(val))
        board.append(row)

    if solve_sudoku(board):
        for i in range(3):
            for j in range(3):
                entries[i][j].delete(0, tk.END)
                entries[i][j].insert(0, str(board[i][j]))
    else:
        messagebox.showerror("Error", "No solution exists for the given puzzle.")

# Function to clear the puzzle
def clear_puzzle():
    for i in range(3):
        for j in range(3):
            entries[i][j].delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("3x3 Sudoku Solver")
root.geometry("200x250")

# Create a 3x3 grid of Entry widgets for input
entries = []
for i in range(3):
    row = []
    for j in range(3):
        entry = tk.Entry(root, width=3, font=('Arial', 24), justify='center')
        entry.grid(row=i, column=j, padx=5, pady=5)
        row.append(entry)
    entries.append(row)

# Solve button
button_solve = tk.Button(root, text="Solve", command=solve_puzzle, width=10)
button_solve.grid(row=4, column=0, columnspan=3, pady=10)

# Clear button
button_clear = tk.Button(root, text="Clear", command=clear_puzzle, width=10)
button_clear.grid(row=5, column=0, columnspan=3, pady=10)

# Run the main loop
root.mainloop()

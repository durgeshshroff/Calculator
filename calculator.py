import tkinter as tk

def press(key):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(key))

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def clear():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("350x400")
root.resizable(False, False)

entry = tk.Entry(root, width=20, font=("Arial", 20), borderwidth=5, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == "=":
        btn = tk.Button(root, text=button, width=5, height=2, font=("Arial", 14), bg="lightblue",
                        command=calculate)
    elif button == "C":
        btn = tk.Button(root, text=button, width=5, height=2, font=("Arial", 14), bg="lightcoral",
                        command=clear)
    else:
        btn = tk.Button(root, text=button, width=5, height=2, font=("Arial", 14),
                        command=lambda b=button: press(b))

    btn.grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1

    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()

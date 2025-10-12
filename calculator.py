import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(entry.get()))
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif text == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + text)

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(0, 0)

# Entry field
entry_var = tk.StringVar()
entry = tk.Entry(root, textvar=entry_var, font="Arial 20", bd=10, relief=tk.RIDGE, justify='right')
entry.pack(fill=tk.BOTH, ipadx=8, ipady=15, pady=10, padx=10)

# Button frame
btns_frame = tk.Frame(root)
btns_frame.pack()

# Button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for row in buttons:
    row_frame = tk.Frame(btns_frame)
    row_frame.pack(expand=True, fill='both')
    for btn_text in row:
        btn = tk.Button(row_frame, text=btn_text, font="Arial 18", relief=tk.GROOVE, border=0)
        btn.pack(side='left', expand=True, fill='both', padx=5, pady=5)
        btn.bind("<Button-1>", click)

# Run the app
root.mainloop()
import tkinter as tk


# Main window
window = tk.Tk()
window.title("My Calculator")
window.geometry("320x430")
window.resizable(False, False)

# This variable stores whatever the user types
calculation = ""


def add_to_calculation(value):
    global calculation

    calculation = calculation + str(value)
    display_var.set(calculation)

    # I used this while checking button values
    # print("Current calculation:", calculation)


def clear_calculation():
    global calculation

    calculation = ""
    display_var.set("")

    # print("Calculator cleared")


def delete_last():
    global calculation

    calculation = calculation[:-1]
    display_var.set(calculation)

    # print("After deleting:", calculation)


def calculate_answer():
    global calculation

    try:
        answer = eval(calculation)

        display_var.set(str(answer))
        calculation = str(answer)

        # print("Answer is:", answer)

    except:
        display_var.set("Error")
        calculation = ""

        # This happened when I entered an incomplete calculation
        # print("Something went wrong")


display_var = tk.StringVar()

display = tk.Entry(
    window,
    textvariable=display_var,
    font=("Arial", 22),
    justify="right",
    bd=8
)
display.pack(fill="x", padx=10, pady=15, ipady=10)


button_frame = tk.Frame(window)
button_frame.pack()


# Row 1
button_7 = tk.Button(
    button_frame,
    text="7",
    width=6,
    height=2,
    command=lambda: add_to_calculation(7)
)
button_7.grid(row=0, column=0, padx=3, pady=3)

button_8 = tk.Button(
    button_frame,
    text="8",
    width=6,
    height=2,
    command=lambda: add_to_calculation(8)
)
button_8.grid(row=0, column=1, padx=3, pady=3)

button_9 = tk.Button(
    button_frame,
    text="9",
    width=6,
    height=2,
    command=lambda: add_to_calculation(9)
)
button_9.grid(row=0, column=2, padx=3, pady=3)

button_divide = tk.Button(
    button_frame,
    text="/",
    width=6,
    height=2,
    command=lambda: add_to_calculation("/")
)
button_divide.grid(row=0, column=3, padx=3, pady=3)


# Row 2
button_4 = tk.Button(
    button_frame,
    text="4",
    width=6,
    height=2,
    command=lambda: add_to_calculation(4)
)
button_4.grid(row=1, column=0, padx=3, pady=3)

button_5 = tk.Button(
    button_frame,
    text="5",
    width=6,
    height=2,
    command=lambda: add_to_calculation(5)
)
button_5.grid(row=1, column=1, padx=3, pady=3)

button_6 = tk.Button(
    button_frame,
    text="6",
    width=6,
    height=2,
    command=lambda: add_to_calculation(6)
)
button_6.grid(row=1, column=2, padx=3, pady=3)

button_multiply = tk.Button(
    button_frame,
    text="*",
    width=6,
    height=2,
    command=lambda: add_to_calculation("*")
)
button_multiply.grid(row=1, column=3, padx=3, pady=3)


# Row 3
button_1 = tk.Button(
    button_frame,
    text="1",
    width=6,
    height=2,
    command=lambda: add_to_calculation(1)
)
button_1.grid(row=2, column=0, padx=3, pady=3)

button_2 = tk.Button(
    button_frame,
    text="2",
    width=6,
    height=2,
    command=lambda: add_to_calculation(2)
)
button_2.grid(row=2, column=1, padx=3, pady=3)

button_3 = tk.Button(
    button_frame,
    text="3",
    width=6,
    height=2,
    command=lambda: add_to_calculation(3)
)
button_3.grid(row=2, column=2, padx=3, pady=3)

button_minus = tk.Button(
    button_frame,
    text="-",
    width=6,
    height=2,
    command=lambda: add_to_calculation("-")
)
button_minus.grid(row=2, column=3, padx=3, pady=3)


# Row 4
button_0 = tk.Button(
    button_frame,
    text="0",
    width=6,
    height=2,
    command=lambda: add_to_calculation(0)
)
button_0.grid(row=3, column=0, padx=3, pady=3)

button_decimal = tk.Button(
    button_frame,
    text=".",
    width=6,
    height=2,
    command=lambda: add_to_calculation(".")
)
button_decimal.grid(row=3, column=1, padx=3, pady=3)

button_equal = tk.Button(
    button_frame,
    text="=",
    width=6,
    height=2,
    command=calculate_answer
)
button_equal.grid(row=3, column=2, padx=3, pady=3)

button_plus = tk.Button(
    button_frame,
    text="+",
    width=6,
    height=2,
    command=lambda: add_to_calculation("+")
)
button_plus.grid(row=3, column=3, padx=3, pady=3)


# Row 5
button_clear = tk.Button(
    button_frame,
    text="Clear",
    width=13,
    height=2,
    command=clear_calculation
)
button_clear.grid(row=4, column=0, columnspan=2, padx=3, pady=3)

button_delete = tk.Button(
    button_frame,
    text="Delete",
    width=13,
    height=2,
    command=delete_last
)
button_delete.grid(row=4, column=2, columnspan=2, padx=3, pady=3)


window.mainloop()

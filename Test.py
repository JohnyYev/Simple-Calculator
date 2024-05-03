import tkinter as tk

def button_click(symbol):
    current_text = result_label["text"]
    if current_text == "Error":
        return
    if symbol == "=":
        try:
            result = eval(current_text)
            result_label["text"] = str(result)
        except Exception:
            result_label["text"] = "Error"
    elif symbol == "C":
        result_label["text"] = ""
    else:
        result_label["text"] += symbol

root = tk.Tk()
root.title("Simple Calculator")

result_label = tk.Label(root, text="", anchor="e", width=25, font=("Arial", 18))
result_label.grid(row=0, column=0, columnspan=4)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

for (symbol, row, col) in buttons:
    button = tk.Button(root, text=symbol, width=5, height=2, font=("Arial", 18),
                       command=lambda s=symbol: button_click(s))
    button.grid(row=row, column=col)

root.mainloop()

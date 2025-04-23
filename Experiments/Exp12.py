import tkinter as tk

root = tk.Tk()
root.title("Area Calculator")

shapes = ["Circle", "Triangle", "Rectangle"]
inputs = [("Radius",1), ("Base, Height",2), ("Length, Width",2)]
entries = {}

tk.Label(root, text="Calculate Area").pack()

for t,n in inputs:
    tk.Label(root, text=t).pack()
    entries[t] = [tk.Entry(root) for _ in range(n)]
    for e in entries[t]: e.pack()

var = tk.StringVar(value=shapes[0])
out = tk.Label(root); out.pack()

for s in shapes:
    tk.Radiobutton(root, text=s, variable=var, value=s,
                  command=lambda: out.config(text=f"Selected: {var.get()}")).pack()

tk.Button(root, text="Calculate", command=lambda: [
    out.config(text={
        "Circle": f"Area: {3.14*float(entries[inputs[0][0]][0].get())**2:.2f}",
        "Triangle": f"Area: {0.5*float(entries[inputs[1][0]][0].get())*float(entries[inputs[1][0]][1].get()):.2f}",
        "Rectangle": f"Area: {float(entries[inputs[2][0]][0].get())*float(entries[inputs[2][0]][1].get()):.2f}"
    }.get(var.get(), "Invalid input"))
]).pack()

root.mainloop()
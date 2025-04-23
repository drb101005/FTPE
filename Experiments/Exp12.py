import tkinter as tk

root = tk.Tk()
root.title("Area Calculator")

shapes = ["Circle", "Triangle", "Rectangle"]
entries = {}
labels = [
    ("Radius for Circle", 1),
    ("Base and Height for Triangle", 2),
    ("Length and Breadth for Rectangle", 2)
]

tk.Label(root, text="Calculate Area").pack()

for text, count in labels:
    tk.Label(root, text=text).pack()
    entries[text] = [tk.Entry(root) for _ in range(count)]
    for entry in entries[text]:
        entry.pack()

var = tk.StringVar(value="Circle")
label4 = tk.Label(root, text="OUTPUT")
label4.pack()

for shape in shapes:
    tk.Radiobutton(root, text=shape, variable=var, value=shape,
                  command=lambda: label4.config(text=f"Selected: {var.get()}")).pack()

def calculate():
    choice = var.get()
    try:
        if choice == "Circle":
            r = float(entries[labels[0][0]][0].get())
            label4.config(text=f"Area of Circle: {3.14*r*r:.2f}")
        elif choice == "Triangle":
            b, h = [float(x.get()) for x in entries[labels[1][0]]]
            label4.config(text=f"Area of Triangle: {0.5*b*h:.2f}")
        elif choice == "Rectangle":
            l, w = [float(x.get()) for x in entries[labels[2][0]]]
            label4.config(text=f"Area of Rectangle: {l*w:.2f}")
    except ValueError:
        label4.config(text="Invalid input")

tk.Button(root, text="Calculate", command=calculate).pack()
root.mainloop()
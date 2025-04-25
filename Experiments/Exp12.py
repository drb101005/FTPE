import tkinter as tk  # Import the Tkinter module

# Create the main application window
root = tk.Tk()
root.title("Experiment No: 12 Title: GUI")

# Create a label widget
L1 = tk.Label(root, text="Experiment No:12 Calculate Area of Circle, Triangle and Rectangle", font=("Arial", 15))
L1.pack()

# Input for Circle
label1 = tk.Label(root, text="Enter Radius for Circle", font=("Arial", 15))
label1.pack()
entry1 = tk.Entry(root, font=("Arial", 15))
entry1.pack()

# Input for Triangle
label2 = tk.Label(root, text="Enter Base and height for Triangle", font=("Arial", 15))
label2.pack()
entry21 = tk.Entry(root, font=("Arial", 15))
entry21.pack()
entry22 = tk.Entry(root, font=("Arial", 15))
entry22.pack()

# Input for Rectangle
label3 = tk.Label(root, text="Enter length and breadth for Rectangle", font=("Arial", 15))
label3.pack()
entry31 = tk.Entry(root, font=("Arial", 15))
entry31.pack()
entry32 = tk.Entry(root, font=("Arial", 15))
entry32.pack()

# Variable to hold selected shape
var = tk.StringVar(value="Circle")

# Radio Buttons to select different options
radio1 = tk.Radiobutton(root, text="Circle", variable=var, value="Circle", command=lambda: label4.config(text=f"You selected: {var.get()}"))
radio2 = tk.Radiobutton(root, text="Triangle", variable=var, value="Triangle", command=lambda: label4.config(text=f"You selected: {var.get()}"))
radio3 = tk.Radiobutton(root, text="Rectangle", variable=var, value="Rectangle", command=lambda: label4.config(text=f"You selected: {var.get()}"))

radio1.pack()
radio2.pack()
radio3.pack()

# OUTPUT label creation
label4 = tk.Label(root, text="OUTPUT", font=("Arial", 15))
label4.pack()

# Function to calculate area based on selected shape
def combine2():
    choice = var.get()
    try:
        rad = float(entry1.get())
    except ValueError:
        rad = 0
    try:
        base = float(entry21.get())
    except ValueError:
        base = 0
    try:
        ht = float(entry22.get())
    except ValueError:
        ht = 0
    try:
        lh = float(entry31.get())
    except ValueError:
        lh = 0
    try:
        Br = float(entry32.get())
    except ValueError:
        Br = 0

    if choice == "Circle":
        area1 = 3.14 * rad * rad
        label4.config(text=f"Area of Circle: {area1}")
    elif choice == "Triangle":
        area2 = 0.5 * base * ht
        label4.config(text=f"Area of Triangle: {area2}")
    elif choice == "Rectangle":
        area3 = lh * Br
        label4.config(text=f"Area of Rectangle: {area3}")
    else:
        label4.config(text="Wrong Choice")

# Submit Button
button1 = tk.Button(root, text="Calculate", font=("Arial", 20), command=combine2)
button1.pack()

# Run the application
root.mainloop()
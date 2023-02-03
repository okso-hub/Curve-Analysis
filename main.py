from tkinter import *
from functions import *
import numpy as np
from matplotlib import pyplot as plt

window = Tk()

# Entry field for function (e.g. f(x) = x^2)
Label(window, text="Enter function ").grid(row=0)
entry = Entry(window, )
entry.grid(row=0, column=1)
entry.insert(0, "f(x) = ")


# get the data from entry widget
def get_data():
   data = entry.get()
   return data

# get value of factors
def split_into_factors(func):
    global a, b, c, d, e, f
    a, b, c, d, e, f = 0, 0, 0, 0, 0, 0
    ls = func.split()
    ls.remove("f(x)")
    ls.remove("=")

    j = 0
    for i in ls:
        if "+" in i:
            continue
        if "-" in i and "x" not in i:
            try:
                ls[j+1] = f"-{ls[j+1]}"
            except:
                pass
        if "x^5" in i:
            try:
                a = int(i.split("x")[0])
            except:
                a = 1
        if "x^4" in i:
            try:
                b = int(i.split("x")[0])
            except:
                b = 1
        if "x^3" in i:
            try:
                c = int(i.split("x")[0])
            except:
                c = 1
        if "x^2" in i:
            try:
                d = int(i.split("x")[0])
            except:
                d = 1
        if "x^1" in i:
            try:
                e = int(i.split("x")[0])
            except:
                e = 1
        if "x" not in i and i != "+" and i != "-":
            f = int(i)

        j += 1

def generate():
    split_into_factors(get_data())

    derivatives = Label(window, text=f"{get_derivatives(a, b, c, d, e, f)}", anchor="w")
    derivatives.grid(row=4, column=0)

    range_of_def = Label(window, text=f"{range_of_definition()}", anchor="w")
    range_of_def.grid(row=5, column=0)

    bhv_to_inf = Label(window, text=f"{behaviour_to_infinity(a, b, c, d, e, f)}", anchor="w")
    bhv_to_inf.grid(row=6, column=0)

    y_intercept = Label(window, text=f"{axis_intercept(f)}", anchor="w")
    y_intercept.grid(row=7, column=0)

    sym = Label(window, text=f"{symmetry(a, b, c, d, e)}", anchor="w")
    sym.grid(row=8, column=0)

    zero_pts = Label(window, text=f"{zero_points(a, b, c, d, e)}", anchor="w")
    zero_pts.grid(row=9, column=0)

    extr = Label(window, text=f"{extrema(a, b, c, d, e, f)}", anchor="w")
    extr.grid(row=10, column=0)

    turning_pts = Label(window, text=f"{turning_points(a, b, c, d, e, f)}", anchor="w")
    turning_pts.grid(row=11, column=0)

    p = np.poly1d([a, b, c, d, e, f])
    print(p)
    x = np.linspace(-50, 50, num=200)
    y = p(x)
    
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.grid(alpha=.4,linestyle='--')

    plt.plot(x, y, label=f"Graph of {p}")
    plt.savefig("graph.png")




# Button for generating solutions
generate = Button(window, text="Generate solutions", command=generate)
generate.grid(row=1, column=1)

# Label widget
label = Label(window, text="", font=('Helvetica 13'))
label.grid(row=4, column=0)

window.title('Visual Curve Discussion')
window.geometry("1000x1000")
window.mainloop()

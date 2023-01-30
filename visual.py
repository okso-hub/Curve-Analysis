from tkinter import *
# from functions import *

window = Tk()

# Entry field for function (e.g. f(x) = x^2)
Label(window, text="Enter function ").grid(row=0)
entry = Entry(window).grid(row=0, column=1)

# Button for generating solutions
generate = Button(window, text="Generate solutions", command={}).grid(row=1, column=1)

# Text field for showing content
output = Label(window, text="solutions").grid(row=2, column=0)

window.title('Visual Curve Discussion')
window.geometry("1000x1000")
window.mainloop()

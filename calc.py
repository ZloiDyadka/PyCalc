from tkinter import *
from math import factorial

i=0

def get_simvol(operator):
    global i
    display.insert(i, operator)
    i+=1

def clear_all():
    display.delete(0, END)

def calculate():
    a=display.get()
    try:
        result=eval(a)
        print(a, result)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, 'error')

def fact():
    entire_string=display.get()
    try:
        result=factorial(int(entire_string))
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0, 'Error')

def undo():
    entire_string=display.get()
    if len(entire_string):
        new_string=entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0, 'Error')

root = Tk()
root.title('Calculator')

root.geometry('500x500')

display=Entry(root)
display.grid(row=1, columnspan=6, sticky=N+E+W+S)
w=7
h=2

# кнопки
Button(root, width=w, height=h, text="1", command=lambda: get_simvol(1)).grid(row=2, column=0, sticky=N + S + E + W)
Button(root, width=w, height=h, text=" 2", command=lambda: get_simvol(2)).grid(row=2, column=1, sticky=N + S + E + W)
Button(root, width=w, height=h, text=" 3", command=lambda: get_simvol(3)).grid(row=2, column=2, sticky=N + S + E + W)

Button(root, width=w, height=h, text="4", command=lambda: get_simvol(4)).grid(row=3, column=0, sticky=N + S + E + W)
Button(root, width=w, height=h, text=" 5", command=lambda: get_simvol(5)).grid(row=3, column=1, sticky=N + S + E + W)
Button(root, width=w, height=h, text=" 6", command=lambda: get_simvol(6)).grid(row=3, column=2, sticky=N + S + E + W)

Button(root, width=w, height=h, text="7", command=lambda: get_simvol(7)).grid(row=4, column=0, sticky=N + S + E + W)
Button(root, width=w, height=h, text=" 8", command=lambda: get_simvol(8)).grid(row=4, column=1, sticky=N + S + E + W)
Button(root, width=w, height=h, text=" 9", command=lambda: get_simvol(9)).grid(row=4, column=2, sticky=N + S + E + W)

# adding other buttons to the calculator
Button(root, width=w, height=h, text="AC", command=lambda: clear_all()).grid(row=5, column=0, sticky=N + S + E + W)
Button(root, width=w, height=h, text=" 0", command=lambda: get_simvol(0)).grid(row=5, column=1, sticky=N + S + E + W)
Button(root, width=w, height=h, text=" .", command=lambda: get_simvol(".")).grid(row=5, column=2, sticky=N + S + E + W)

Button(root, width=w, height=h, text="+", command=lambda: get_simvol("+")).grid(row=2, column=3, sticky=N + S + E + W)
Button(root, width=w, height=h, text="-", command=lambda: get_simvol("-")).grid(row=3, column=3, sticky=N + S + E + W)
Button(root, width=w, height=h, text="*", command=lambda: get_simvol("*")).grid(row=4, column=3, sticky=N + S + E + W)
Button(root, width=w, height=h, text="/", command=lambda: get_simvol("/")).grid(row=5, column=3, sticky=N + S + E + W)

# adding new operations
Button(root, width=w, height=h, text="pi", command=lambda: get_simvol("*3.14")).grid(row=2, column=4, sticky=N + S + E + W)
Button(root, width=w, height=h, text="%", command=lambda: get_simvol("%")).grid(row=3, column=4, sticky=N + S + E + W)
Button(root, width=w, height=h, text="(", command=lambda: get_simvol("(")).grid(row=4, column=4, sticky=N + S + E + W)
Button(root, width=w, height=h, text="exp", command=lambda: get_simvol("**")).grid(row=5, column=4, sticky=N + S + E + W)

Button(root, width=w, height=h, text="<-", command=lambda: undo()).grid(row=2, column=5, sticky=N + S + E + W)
Button(root, width=w, height=h, text="x!", command=lambda: fact()).grid(row=3, column=5, sticky=N + S + E + W)
Button(root, width=w, height=h, text=")", command=lambda: get_simvol(")")).grid(row=4, column=5, sticky=N + S + E + W)
Button(root, width=w, height=h, text="^2", command=lambda: get_simvol("**2")).grid(row=5, column=5, sticky=N + S + E + W)
Button(root, width=w, height=h, text="^2", command=lambda: get_simvol("**2")).grid(row=5, column=5, sticky=N + S + E + W)
Button(root, text="=", command=lambda: calculate()).grid(columnspan=6, sticky=N + S + E + W)

root.mainloop()


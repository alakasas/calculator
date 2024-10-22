import tkinter as tk
from tkinter import ttk


def add_to_calculation(num):
    current = display_var.get()
    display_var.set(current + str(num))

def clear_display():
    display_var.set("") 

def back_display():
     current = display_var.get()
     display_var.set(current[:-1])

def calculate_result():
    try:
        result = eval(display_var.get())
        display_var.set(result)
    except:
        display_var.set("Error")



root = tk.Tk()
root.title("Calculator")

frame = ttk.Frame(root,padding=10)
frame.grid()

display_var = tk.StringVar()
display = ttk.Entry(frame, textvariable=display_var, font=("Arial", 15), width=25)
display.grid(column=0,row=0,columnspan=4)

ttk.Button(frame,text="1",command=lambda: add_to_calculation(1)).grid(column=0,row=1)
ttk.Button(frame,text="2",command=lambda: add_to_calculation(2)).grid(column=1,row=1)
ttk.Button(frame,text="3",command=lambda: add_to_calculation(3)).grid(column=2,row=1)
ttk.Button(frame,text="4",command=lambda: add_to_calculation(4)).grid(column=0,row=2)
ttk.Button(frame,text="5",command=lambda: add_to_calculation(5)).grid(column=1,row=2)
ttk.Button(frame,text="6",command=lambda: add_to_calculation(6)).grid(column=2,row=2)
ttk.Button(frame,text="7",command=lambda: add_to_calculation(7)).grid(column=0,row=3)
ttk.Button(frame,text="8",command=lambda: add_to_calculation(8)).grid(column=1,row=3)
ttk.Button(frame,text="9",command=lambda: add_to_calculation(9)).grid(column=2,row=3)
ttk.Button(frame,text="0",command=lambda: add_to_calculation(0)).grid(column=1,row=4)
ttk.Button(frame,text="+",command=lambda: add_to_calculation("+")).grid(column=3,row=1)
ttk.Button(frame,text="-",command=lambda: add_to_calculation("-")).grid(column=3,row=2)
ttk.Button(frame,text="x",command=lambda: add_to_calculation("*")).grid(column=3,row=3)
ttk.Button(frame,text="/",command=lambda: add_to_calculation("/")).grid(column=3,row=4)
ttk.Button(frame,text="(",command=lambda: add_to_calculation("(")).grid(column=0,row=5)
ttk.Button(frame,text=")",command=lambda: add_to_calculation(")")).grid(column=1,row=5)
ttk.Button(frame,text="=",command=calculate_result).grid(column=0,row=4)
ttk.Button(frame,text="C",command=clear_display).grid(column=2,row=4)
ttk.Button(frame,text="DEL",command=back_display).grid(column=2,row=5)

root.mainloop()



# Python program to trace
# variable in tkinter


from tkinter import *


root = Tk()

my_var = StringVar()

# defining the callback function (observer)
def my_callback(var, index, mode,variable):
	print ("Traced variable {}".format(variable.get()))

# registering the observer
my_var.trace_add('write', lambda var,index,mode,my_var:my_callback(my_var))

Label(root, textvariable = my_var).pack(padx = 5, pady = 5)

Entry(root, textvariable = my_var).pack(padx = 5, pady = 5)

root.mainloop()

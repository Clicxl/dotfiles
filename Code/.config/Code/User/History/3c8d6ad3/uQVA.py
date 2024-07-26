# Python program to change position
# of cursor in Entry widget

# Import the library tkinter
from tkinter import *

# Create a GUI app
app = Tk()

# Create a function to move cursor one character
# left


def shift_cursor1(event=None):
	position = entry_label.index(INSERT)

	# Changing position of cursor one character left
	entry_label.icursor(position - 1)

# Create a function to move the cursor one character
# right


def shift_cursor2(event=None):
	position = entry_label.index(INSERT)

	# Changing position of cursor one character right
	entry_label.icursor(position + 1)


# Create and display the button to shift cursor left
button1 = Button(app, text="Shift cursor left", command=shift_cursor1)
button1.grid(row=1, column=1, padx=10, pady=10)

# Create and display the button to shift the cursor right
button2 = Button(app, text="Shift cursor right", command=shift_cursor2)
button2.grid(row=1, column=0, padx=10, pady=10)

# Create and display the textbox
entry_label = Entry(app)
entry_label.grid(row=0, column=0, padx=10, pady=10)

# Set the focus in the textbox
entry_label.focus()

# Make the infinite loop for displaying the app
app.mainloop()

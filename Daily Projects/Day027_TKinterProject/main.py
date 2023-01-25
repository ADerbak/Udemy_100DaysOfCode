from  tkinter import *

window = Tk()

window.title('My First GUI Program!')
window.minsize(width=500, height=300)



# Label
my_label = Label(text="I am a label", font = ('Ariel',24,'bold'),)
my_label.grid(column=1,row=1)


# create a clickable button
my_button = Button()

def button_clicked():
    my_label.config(text=input.get())

my_button.config(text = 'Click Me', command=button_clicked)
my_button.grid(column=2,row=2)


# create a clickable button
my_button2 = Button()

def button_clicked():
    my_label.config(text='Button2!')

my_button.config(text = 'Click Me, too', command=button_clicked)
my_button.grid(column=3,row=1)


# Create a text entry
def return_entry(en):
    content = input.get()
    print(content)

input = Entry(window, width=10)

input.grid(column=3,row=3)
# name = ''
# input.config(textvariable= name)
# print(input.get())
# Connect the entry with the return button
input.bind('<Return>', return_entry)

window.mainloop()


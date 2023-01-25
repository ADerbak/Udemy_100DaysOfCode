from  tkinter import *

window = Tk()

window.title('Miles to KM converter!')
window.minsize(width=300, height=200)


# Create a text entry
def return_entry(en):
    content = input.get()
    print(content)

input = Entry(window, width=10)

input.grid(column=2,row=1)
# name = ''
# input.config(textvariable= name)
# print(input.get())
# Connect the entry with the return button
input.bind('<Return>', return_entry)

# Label
is_equal_label = Label(text="is equal to", font = ('Ariel',24,'bold'))
is_equal_label.grid(column=1,row=2)

km_amount_label = Label(text="0", font = ('Ariel',24,'bold'),)
km_amount_label.grid(column=2,row=2)

miles_label = Label(text="Miles", font = ('Ariel',24,'bold'),)
miles_label.grid(column=3,row=1)

km_label = Label(text="Km",font = ('Ariel',24,'bold'),)
km_label.grid(column=3,row=2)


# create a clickable button
my_button = Button()

def button_clicked():
    km_amount_label.config(text=int(input.get()*1.6))

my_button.config(text = 'Calculate', command=button_clicked)
my_button.grid(column=2,row=3)





window.mainloop()


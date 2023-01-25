from  tkinter import *

window = Tk()

window.title('Miles to KM converter!')
window.config(padx = 20, pady=20)

# Entry
input = Entry(window, width=10)
input.grid(column=2,row=1)

# Labels
is_equal_label = Label(text="is equal to", font = ('Ariel'))
is_equal_label.grid(column=1,row=2)

km_amount_label = Label(text="0", font = ('Ariel'),)
km_amount_label.grid(column=2,row=2)

miles_label = Label(text="Miles", font = ('Ariel'),)
miles_label.grid(column=3,row=1)

km_label = Label(text="Km",font = ('Ariel'),)
km_label.grid(column=3,row=2)


# create a clickable button
my_button = Button()

def button_clicked():
    km_amount_label.config(text=str(int(input.get())*1.6))

my_button.config(text = 'Calculate', command=button_clicked)
my_button.grid(column=2,row=3)

window.mainloop()


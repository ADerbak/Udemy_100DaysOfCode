from tkinter import *
import PIL.Image
import PIL.ImageTk

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    print('Ok')

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    print('Saved')
    f = open('password_list.txt','a')
    f.write(website_text.get() + " | " + email_text.get() + " | " + password_text.get())
    website_text.delete(0, END)
    email_text.delete(0, END)
    email_text.insert(0,'andrewderbak@gmail.com')
    password_text.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
# window.maxsize(width=500, height=200)
window.config(padx=50, pady=50, bg='white')

canvas = Canvas(width=200, height=200, highlightthickness=0)
# Fix for reading in image.
# image = PIL.Image.open('logo.png')
# logo = PIL.ImageTk.PhotoImage(image)
logo = PhotoImage(file = "unlock_animaiton-97042947.gif")

canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Create labels
website_label = Label(text='Website:')
website_label.grid(row=1, column=0)

email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)

password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

# Create Text
website_text = Entry(width=35)
website_text.grid(row=1, column=1, columnspan=2)
website_text.focus()

email_text = Entry(width=35)
email_text.grid(row=2, column=1, columnspan=2)
email_text.insert(0,'andrewderbak@gmail.com') #Set cursor to end

password_text = Entry(width=21)
password_text.grid(row=3, column=1)

# Create Buttons

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text='Add', width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()

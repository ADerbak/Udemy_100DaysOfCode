from tkinter import *
import PIL.Image
import PIL.ImageTk

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    print('Ok')

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    print('Saved')


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
# window.maxsize(width=500, height=200)
window.config(padx=20, pady=20, bg='white')

canvas = Canvas(width=200, height=200, highlightthickness=0)
# Fix for reading in image.
image = PIL.Image.open('logo.png')
logo = PIL.ImageTk.PhotoImage(image)

canvas.create_image(50, 50, image=logo)
canvas.grid(row=0, column=1)

# Create labels
website_label = Label(text='Website:')
website_label.grid(row=1, column=0)

email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)

password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

# Create Text
website_text = Text(width=35, height=10)
website_text.grid(row=1, column=1, columnspan=2)

email_text = Text(width=35, height=10)
email_text.grid(row=2, column=1, columnspan=2)

password_text = Text(width=21, height=10)
password_text.grid(row=3, column=1)

# Create Buttons

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text='Add', command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()

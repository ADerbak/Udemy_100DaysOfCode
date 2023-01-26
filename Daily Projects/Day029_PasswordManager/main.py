from tkinter import *
import PIL.Image
import PIL.ImageTk
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
# window.minsize(400, 400)
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
# Fix for reading in image.
image = PIL.Image.open('logo.png')
logo = PIL.ImageTk.PhotoImage(image)

canvas.create_image(100, 100, image=logo)
canvas.pack()




mainloop()
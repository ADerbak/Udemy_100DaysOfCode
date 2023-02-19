from tkinter import *
from tkinter import messagebox
import random
import json
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

df = pd.read_csv('./data/french_words.csv')
df = df.to_dict(orient="records")
# french_word = df['French'][random.randint(0,len(df))]
# word = df[random.randint(0,len(df))]['French']
current_card = random.choice(df)
language = "French"

# ------------------- Yes/No Functions ----------------- #

def next_card():
    # word = df[random.randint(0,len(df))]['French']
    current_card = random.choice(df)
    # window.update()
    canvas.itemconfig(card_title, text= language)
    canvas.itemconfigure(card_word, text=current_card[language])



# ------------------- New Word Functions ----------------- #





# ------------------- Canvas ----------------- #

window = Tk()
window.title('Flashy')
window.minsize(width=900, height=700)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
# Fix for reading in image.
# image = PIL.Image.open('logo.png')
# logo = PIL.ImageTk.PhotoImage(image)
card_front = PhotoImage(file='./images/card_front.png')
canvas.create_image(400,275 , image=card_front)
card_title = canvas.create_text((400,150), text="" ,  font= ("Ariel",40,'italic'), justify='center') #"italic"))#, __coords=(400,150))
card_word = canvas.create_text((400,263),text="" ,  font= ("Ariel",60, 'bold'), justify='center') #60, "italic"))#, __coords=(400,263))

canvas.grid(row=0, column=0, columnspan=2 )

# canvas.grid(row=0, column=0, columnspan=2, rowspan=3)



# ------------------- Text/Labels ----------------- #

# language_label = Label(text="French" , highlightthickness=0, font= ("Ariel",40,"italic"))
# language_label.place(x=400, y=150)


# word_label = Label(text="trouve", highlightthickness=0, font= ("Ariel",60,"bold"))
# word_label.place(x=400, y=263)


# ------------------- Buttons ----------------- #

cross_image = PhotoImage(file = './images/wrong.png')
cross_button = Button(image=cross_image
                      , bg=BACKGROUND_COLOR
                      , highlightthickness=0
                      , pady=50
                      , bd=0
                      , command=next_card)
# cross_button.image = cross_image
cross_button.grid(row=1, column=0)
# cross_button.place(x=100, y=500)

check_image = PhotoImage(file = './images/right.png')
check_button = Button( image=check_image
                      , bg=BACKGROUND_COLOR
                      , highlightthickness=0
                      , pady=50
                      , bd=0
                      , command= next_card)
# check_button.image = check_image
check_button.grid(row=1, column=1)
# cross_button.place(x=700, y=500)

next_card()

mainloop()
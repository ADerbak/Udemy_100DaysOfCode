from tkinter import *
from tkinter import messagebox
import random
import json
import pandas as pd
import time

BACKGROUND_COLOR = "#B1DDC6"

try:
    to_learn = pd.read_csv('words_to_learn.csv')
except FileNotFoundError:
    to_learn = pd.read_csv('./data/french_words.csv')
finally:
    df = to_learn.to_dict(orient="records")


current_card = {}
language = "French"

# ------------------- Yes/No Functions ----------------- #

def next_card():
    global current_card, timer
    window.after_cancel(timer)
    # word = df[random.randint(0,len(df))]['French']
    current_card = random.choice(df)
    # window.update()
    canvas.itemconfig(card_image, image= card_front)
    canvas.itemconfig(card_title, text= language,fill="black")
    canvas.itemconfig(card_word, text=current_card[language], fill="black")
    canvas.itemconfig(card_image, image= card_front)
    timer = window.after(3000, func=back_of_card)
    # check_button.after_cancel(timer)
    # window.after_cancel(timer)
    

    
    
def back_of_card():
    # window.after(3000)    

    canvas.itemconfig(card_image, image= card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    



# ------------------- New Word Functions ----------------- #

def remove_card():
    global df, current_card
    # print(current_card)
    df.remove(current_card)
    words_to_learn = pd.DataFrame(df)
    words_to_learn.to_csv('words_to_learn.csv', index=False)



# ------------------- Canvas ----------------- #

window = Tk()
window.title('Flashy')
window.minsize(width=900, height=700)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, func=back_of_card)
canvas = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
# Fix for reading in image.
# image = PIL.Image.open('logo.png')
# logo = PIL.ImageTk.PhotoImage(image)
card_front = PhotoImage(file='./images/card_front.png')
card_back = PhotoImage('./images/card_back.png')
card_image = canvas.create_image(400,275, image = card_front)
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
                      , command= lambda: [remove_card(),next_card()])
# check_button.image = check_image
check_button.grid(row=1, column=1)
# cross_button.place(x=700, y=500)

next_card()

mainloop()
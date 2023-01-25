from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx = 100, pady = 50, bg=YELLOW )


# Create Label
label = Label(text = 'Timer', fg=GREEN, bg=YELLOW, font = (FONT_NAME, 35,'bold'))
label.pack()


checkmark = '√'
counter = 0
checkmark_label = Label(text=checkmark*counter, fg=GREEN,bg=YELLOW, font=(FONT_NAME,18))
checkmark_label.place(x=80, y=275)

# Create Canvas
canvas = Canvas(width=200, height=224, bg = YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png') 
canvas.create_image(100, 112, image = tomato_img)  # image needs to a photoimage type

canvas.create_text(100,130, text='00:00', fill='white', font=(FONT_NAME,35,'bold'))
canvas.pack()


# Create buttons

def start_click():
    global counter
    counter += 1
    print(counter)
    checkmark_label.config(text=checkmark*counter)
    
def finish_click():
    global counter
    counter = 0
    print(counter)
    checkmark_label.config(text=checkmark*counter)
    

start_button = Button(text='Start',bg=YELLOW, font=(FONT_NAME), command=start_click)
start_button.place(x=-60, y=260)

finish_button = Button(text='Finish',bg=YELLOW, font=(FONT_NAME), command=finish_click)
finish_button.place(x=175, y= 260)





mainloop()
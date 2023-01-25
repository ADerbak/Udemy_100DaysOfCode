from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 5
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 4
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_click():
    global timer
    window.after_cancel(timer)
    
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text="")
    label.config(text = 'Timer', fg=GREEN, bg=YELLOW, font = (FONT_NAME, 35,'bold'))
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_click():
    # update timer
    global reps
    reps += 1
    if reps % 2 == 1:
        count_down(WORK_MIN)
        label.config(text = 'Work', fg=GREEN, bg=YELLOW, font = (FONT_NAME, 35,'bold'))
        
        
    elif reps == 8:
        count_down(LONG_BREAK_MIN)
        reps = 0
        label.config(text = 'Long Break', fg=RED, bg=YELLOW, font = (FONT_NAME, 35,'bold'))
        
    else:
        label.config(text = 'Break', fg=PINK, bg=YELLOW, font = (FONT_NAME, 35,'bold'))
        count_down(SHORT_BREAK_MIN)
        counter = int(reps / 2)
        checkmark_label.config(text=checkmark*counter)
        
    
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    
    time = str(int(count/60)).zfill(2) +":"+str(count%60).zfill(2)
    
    if count > -1:
        global timer
        canvas.itemconfig(timer_text, text=time)
        timer = window.after(1000, count_down, count - 1)
    else:
        start_click()
        

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx = 100, pady = 50, bg=YELLOW )


# Create Label
label = Label(text = 'Timer', fg=GREEN, bg=YELLOW, font = (FONT_NAME, 35,'bold'))
label.pack()


checkmark = '√'
checkmark_label = Label(text=checkmark*reps, fg=GREEN,bg=YELLOW, font=(FONT_NAME,18))
checkmark_label.place(x=80, y=275)

# Create Canvas
canvas = Canvas(width=200, height=224, bg = YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png') 
canvas.create_image(100, 112, image = tomato_img)  # image needs to a photoimage type

timer_text = canvas.create_text(100,130, text='00:00', fill='white', font=(FONT_NAME,35,'bold'))
canvas.pack()



# Create buttons
start_button = Button(text='Start',bg=YELLOW, font=(FONT_NAME), command=start_click, highlightthickness=0)
start_button.place(x=-60, y=260)

reset_button = Button(text='Reset',bg=YELLOW, font=(FONT_NAME), command=reset_click, highlightthickness=0)
reset_button.place(x=175, y= 260)





mainloop()
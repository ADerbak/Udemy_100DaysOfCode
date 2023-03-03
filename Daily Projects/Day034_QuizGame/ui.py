from tkinter import Tk, Label, Button, Canvas, PhotoImage
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"



class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = 0
        
        # ------------------- Score ----------------- #
        
        self.score_label = Label(text="Score: 0"
                                 ,fg="white"
                                 , bg=THEME_COLOR
                                 ,highlightbackground=None)
        self.score_label.grid(row=0, column=1)
        
        
        # ------------------- Canvas ----------------- #
        
        self.canvas = Canvas(width=300
                             , height=250
                             , highlightthickness=0
                             , bg="white")
        self.question_text = self.canvas.create_text( (150,125)
                                                 ,text="Some Question Text"
                                                 , fill=THEME_COLOR 
                                                 ,  font= ("Ariel",20,'italic')
                                                 , justify='center'
                                                 , width=280)

        self.canvas.grid(row=1, column=0, columnspan=2, pady=50 )
        
        
        # ------------------- Buttons ----------------- #
        cross_image = PhotoImage(file = './images/false.png')
        self.cross_button = Button(image=cross_image
                            , highlightthickness=0
                            , pady=50
                            , bd=0)
        self.cross_button.grid(row=2, column=1)

        check_image = PhotoImage(file = './images/true.png')
        self.check_button = Button( image=check_image
                            , highlightthickness=0
                            , pady=50
                            , bd=0)
                            
        self.check_button.grid(row=2, column=0)
        
        self.get_next_question()
        
    
        self.window.mainloop()
        
        
        
    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
        
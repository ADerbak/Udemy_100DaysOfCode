from tkinter import *

THEME_COLOR = "#375362"



class QuizInterface:
    
    def __init__(self):
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
                                                 , justify='center')

        self.canvas.grid(row=1, column=0, columnspan=2, pady=50 )
        
        
        # ------------------- Buttons ----------------- #
        cross_image = PhotoImage(file = './images/false.png')
        self.cross_button = Button(image=self.cross_image
                            , highlightthickness=0
                            , pady=50
                            , bd=0)
        self.cross_button.grid(row=2, column=1)

        check_image = PhotoImage(file = './images/true.png')
        self.check_button = Button( image=self.check_image
                            , highlightthickness=0
                            , pady=50
                            , bd=0)
                            
        self.check_button.grid(row=2, column=0)
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
        self.window.mainloop()
from tkinter import *

THEME_COLOR = "#375362"



class QuizInterface:
    
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR)
        self.score = 0
        
        # ------------------- Score ----------------- #
        
        self.text_box = Text(self.window
                             , font= ("Ariel",12)
                             , highlightcolor=THEME_COLOR
                             , height = 12
                             , width=30
                             , background=THEME_COLOR
                             ,highlightbackground=None)
        self.text_box.grid(row=0, column=1)
        self.text_box.insert('end',f"Score: {self.score}")
        
        
        # ------------------- Canvas ----------------- #
        
        self.canvas = Canvas(width=600
                             , height=526
                             , highlightthickness=0
                             , bg=THEME_COLOR)
        self.card_word = self.canvas.create_text((400,263)
                                                 ,text="" 
                                                 ,  font= ("Ariel",60, 'bold')
                                                 , justify='center')

        self.canvas.grid(row=1, column=0, columnspan=2 )
        
        # ------------------- Buttons ----------------- #
        self.cross_image = PhotoImage(file = './images/false.png')
        self.cross_button = Button(image=self.cross_image
                            , highlightthickness=0
                            , pady=50
                            , bd=0)
        self.cross_button.grid(row=2, column=1)

        self.check_image = PhotoImage(file = './images/true.png')
        self.check_button = Button( image=self.check_image
                            , highlightthickness=0
                            , pady=50
                            , bd=0)
                            
        self.check_button.grid(row=2, column=0)
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
        self.window.mainloop()
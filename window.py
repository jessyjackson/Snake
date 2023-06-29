from tkinter import *
from snake import Snake
from food import Food
GAME_WIDTH = 900
GAME_HEIGHT = 800
BACKGROUND_COLOR = "#1E5945"
SNAKE_COLOR = "blue"
FOOD_COLOR = "red"

Score = 0


def nextSet():
    return 0
def Gameover():
    return 0
def checkCollision():
    return 0




#create window
window = Tk()
window.title("snake")
window.resizable(False,False)
window.geometry("+100+100")
#label score
label = Label(window,text="score: {}".format(Score), font=24)
label.pack()
#game window
canva = Canvas(window,height=GAME_HEIGHT,width=GAME_WIDTH,bg=BACKGROUND_COLOR)
canva.pack()

#window loop
window.mainloop()

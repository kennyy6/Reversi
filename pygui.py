import reversi
from tkinter import *
import os

root = Tk()
screen = Canvas(root, width=800, height=700, background="#222",highlightthickness=0)
screen.pack()

#player1 = Label(text = "my label", fg ="blue",bg = "red",width = 0,height = 0).pack()
# for i in range(7):
#     lineShift = 50 + 50 * (i + 1)
#
#     # Horizontal line
# #    screen.create_oval(50+,0,100,100,fill ="#222")
#     screen.create_line(50, lineShift, 450, lineShift, fill="#111")

#     # Vertical line
#     screen.create_line(lineShift, 50, lineShift, 450, fill="#111")
class gui:
    def __init__(self):

    #Horizontal Line
        screen.create_line(200, 150, 600, 150, fill="red")
        screen.create_line(200, 200, 600, 200, fill="red")
        screen.create_line(200, 250, 600, 250, fill="red")
        screen.create_line(200, 300, 600, 300, fill="red")
        screen.create_line(200, 350, 600, 350, fill="red")
        screen.create_line(200, 400, 600, 400, fill="red")
        screen.create_line(200, 450, 600, 450, fill="red")
        screen.create_line(200, 500, 600, 500, fill="red")
        screen.create_line(200, 550, 600, 550, fill="red")


            #Vertical Line
        screen.create_line(200, 150, 200, 550, fill="red")
        screen.create_line(250, 150, 250, 550, fill="red")
        screen.create_line(300, 150, 300, 550, fill="red")
        screen.create_line(350, 150, 350, 550, fill="red")
        screen.create_line(400, 150, 400, 550, fill="red")
        screen.create_line(450, 150, 450, 550, fill="red")
        screen.create_line(500, 150, 500, 550, fill="red")
        screen.create_line(550, 150, 550, 550, fill="red")
        screen.create_line(600, 150, 600, 550, fill="red")





        # Allocate the Intialize
    def create_circle(self,x, y, r, canvasName,player): #center coordinates, radius
        if player == 1:
            colour = "green"
        elif player == 2:
            colour = "red"
        else: # for hints
            colour = "white"

        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return canvasName.create_oval(x0, y0, x1, y1, fill = colour)

    # for i in range(8):
    #     for j in range(8):
    #         create_circle(225+(i*50),175+(j*50),24,screen)




def left_click(event):
    global reversiBoard
    posx=event.x
    posy = event.y

    rounded_x = (int((posx - 200) / 50))
    rounded_y = (int((posy - 150) / 50))
    value_in_list = (rounded_x,rounded_y)

    if value_in_list in reversi.valid_moves(reversiBoard,1):
        print("you can do this cunt")
    print("left Click" ,posx,posy)

if __name__ == "__main__":

    gui = gui()
    gui.create_circle(225 + (3 * 50), 175 + (3 * 50), 24, screen, 1)
    gui.create_circle(225 + (4 * 50), 175 + (4 * 50), 24, screen, 1)

    gui.create_circle(225 + (3 * 50), 175 + (4 * 50), 24, screen, 2)
    gui.create_circle(225 + (4 * 50), 175 + (3 * 50), 24, screen, 2)

    reversiBoard = reversi.new_board()
    for i in reversi.valid_moves(reversiBoard,1):
        gui.create_circle(225+(i[0]*50),175 + (i[1] * 50),12,screen,3)
    print("hi")
    print(reversi.valid_moves(reversiBoard, 1))

    screen.bind("<Button-1>",left_click)
    root.mainloop()




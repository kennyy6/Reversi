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
        #self.board = reversi.new_board()
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
        hint = 0
        if player == 1:
            colour = "green"
        elif player == 2:
            colour = "red"
        else: # for hints
            colour = "white"
            hint = 1

        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        if hint == 1:
            return canvasName.create_oval(x0, y0, x1, y1, fill=colour, tags ="hint")
        return canvasName.create_oval(x0, y0, x1, y1, fill = colour)

    # for i in range(8):
    #     for j in range(8):
    #         create_circle(225+(i*50),175+(j*50),24,screen)




def left_click(event):
    global reversiBoard , player
    posx=event.x
    posy = event.y

    rounded_x = (int((posx - 200) / 50))
    rounded_y = (int((posy - 150) / 50))
    value_in_tuple = (rounded_x,rounded_y)

    # if player == 1 and there not more turns then let the other player play its turn
    if value_in_tuple in reversi.valid_moves(reversiBoard,1) and player == 1:
       # print("you can do this cunt")
        gui.create_circle(225 + (rounded_x * 50), 175 + (rounded_y * 50), 24, screen, 1)
        x1 = reversi.next_state(reversiBoard,1,value_in_tuple)
        reversiBoard = x1[0] # gets the next state of the board
        player = x1[1]
        reverse_stones = x1[2]
        inbetweenStones(reverse_stones,player)
        #print(reverse_stones)
        createNewplayers_hint(reversiBoard,player)
        score(reversiBoard)
    elif reversi.valid_moves(reversiBoard,1) == [] :
        player =2
        createNewplayers_hint(reversiBoard, player)

    if value_in_tuple in reversi.valid_moves(reversiBoard,2) and player == 2:
        gui.create_circle(225 + (rounded_x * 50), 175 + (rounded_y * 50), 24, screen, 2)
        x2 = reversi.next_state(reversiBoard,2,value_in_tuple)
        reversiBoard = x2[0] # gets the next state of the board
        player = x2[1]
        reverse_stones = x2[2]
        inbetweenStones(reverse_stones,player)
        #print(reverse_stones)
        createNewplayers_hint(reversiBoard,player)
        score(reversiBoard)
    elif  reversi.valid_moves(reversiBoard,2) == [] :
        player = 1
        createNewplayers_hint(reversiBoard, player)

    print(reversi.valid_moves(reversiBoard,1))
    print(reversi.valid_moves(reversiBoard, 2))

    if reversi.valid_moves(reversiBoard,1) == [] and reversi.valid_moves(reversiBoard,2) == []:
        endgame()
        counter = 0







def endgame():
    scoreBoard =score(reversiBoard)
    if scoreBoard[0] > scoreBoard[1]:
        print("Player 1 Wins", str(scoreBoard[0]))
        msg = "Player 1 Wins " + str(scoreBoard[0])
    else:
        print("player 2 Wins")
        msg = "Player 2 Wins "+  str(scoreBoard[1])

    popup = Tk()
    popup.wm_title("!")
    label = Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="quit", command = screen.quit)
    B1.pack()

    popup.mainloop()



def inbetweenStones(list,currentPlayer):
    # switch the players around cause the other python files switches it
    if currentPlayer == 1:
        currentPlayer = 2
    else:
        currentPlayer = 1

    for i in list:
        gui.create_circle(225 + (i[0] * 50), 175 + (i[1] * 50), 24, screen, currentPlayer)
    #delete all new hints
    screen.delete("hint")
    screen.update()

    # make all the list into the

def createNewplayers_hint(board,player):
    for i in reversi.valid_moves(board,player):
        gui.create_circle(225 + (i[0] * 50), 175 + (i[1] * 50), 12, screen, 3)


def score(board):
    """
returns as output a pair of integers (s1, s2) where s1 represents
the number of stones of Player 1 in the given board configuration and s2 represents the number of stones of
Player 2.

s1 represents black
s2 represents White

    """
    s1 = 0
    s2 = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                s1 += 1
            elif board[i][j] == 2:
                s2 += 1
    return display_score((s1,s2))

def display_score(tupleVal):
    playerOneScore = tupleVal[0]
    playertwoScore = tupleVal[1]

    screen.delete("playerval")
    screen.create_text(200, 75, fill="lightgreen", font="Times 20 italic bold",
                            text=str(playerOneScore), tag ="playerval")
    screen.create_text(600, 75, fill="red", font="Times 20 italic bold",
                            text=str(playertwoScore), tag ="playerval")

    return tupleVal
    #playeroneLabel = Label(screen,text =str(playerOneScore),)


if __name__ == "__main__":


    gui = gui()
    gui.create_circle(225 + (3 * 50), 175 + (3 * 50), 24, screen, 2)
    gui.create_circle(225 + (4 * 50), 175 + (4 * 50), 24, screen, 2)

    gui.create_circle(225 + (3 * 50), 175 + (4 * 50), 24, screen, 1)
    gui.create_circle(225 + (4 * 50), 175 + (3 * 50), 24, screen, 1)



    # make player = 1
    player = 1

    reversiBoard = reversi.new_board()
    for i in reversi.valid_moves(reversiBoard,1):
        gui.create_circle(225+(i[0]*50),175 + (i[1] * 50),12,screen,3)
    print("hi")
    print(reversi.valid_moves(reversiBoard, 1))

    screen.bind("<Button-1>",left_click)

    # playeroneLabel = Label(screen, text=str(10),bd = 1)
    # playeroneLabel.pack()
    screen.create_text(200, 75, fill="lightgreen", font="Times 20 italic bold",
                            text="0", tag ="playerval")
    screen.create_text(600, 75, fill="red", font="Times 20 italic bold",
                            text="0", tag ="playerval")


    root.mainloop()




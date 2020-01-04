"""
@ Kenny Y
"""



def new_board():
    """
    The function new board() takes no parameters and returns a fresh board
    configuration representing the Reversi starting position.
    """
    empty_outer_board = []
    empty_inner_board = []
    board_length = 8
    for i in range(board_length):
        empty_inner_board.append(0)

    empty_outer_board.append(empty_inner_board)
    empty_outer_board = empty_outer_board * board_length
    # print(new_board)

    for i in range(board_length):
        empty_outer_board[i] = [0] * 8
    # Stating Values
    empty_outer_board[3][3] = 2
    empty_outer_board[3][4] = 1
    empty_outer_board[4][3] = 1
    empty_outer_board[4][4] = 2



    # for x in range(len(empty_outer_board)):
    #         print(x+1, empty_outer_board[x])
    # print("   A  B  C  D  E  F  G  H")
    #
    #

    return (empty_outer_board)

# return empty_outer_board


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

    print("Player one/black has", s1, "pieces on the board", "Player two/White has", s2, "pieces on the board") # To get rid of talking marks
    return " "


def print_board(board):
    """
has no return value but prints the given board configuration
in human-readable form to the console (in particular, all rows of the board must be printed in separate lines
of the console and labelled by their names 1, 2, . . . and all columns must be properly aligned and labelled by
their names a, b,

    """

    for x in range(len(board)):
        print(x + 1, (board[x]))
    print("   A| B| C| D| E| F| G| H")

    return ""


# For function position if they dont add string but say b2
a, b, c, d, e, f, g, h = "a", "b", "c", "d", "e", "f", "g", "h"

aa, bb, cc, dd, ee, ff, gg, hh = 1, 2, 3, 4, 5, 6, 7, 8,


def position(string):
    """
    inputs: cooridnates
    purpose: If given column index then row index flip them around and make them within range if not = error
    output: (r,c)
    """
    if len(string)> 2:
        return None
    if len(string) == 1:
        return None

    string = string.lower()
    firstindex = string[0]
    secondindex = string[1]
    if firstindex in (
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
    "x", "y", "z") and secondindex in (
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
    "x", "y", "z"):
        return None
    if firstindex in (
    "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z") or secondindex in (
    "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"):
        return None

    if firstindex == "a":
        firstindex = aa
        temp_variable = firstindex
        firstindex = secondindex
        secondindex = temp_variable
    elif firstindex == "b" or firstindex == "B":
        firstindex = bb
        temp_variable = firstindex
        firstindex = secondindex
        secondindex = temp_variable
    elif firstindex == "c" or firstindex == "C":
        firstindex = cc
        temp_variable = firstindex
        firstindex = secondindex
        secondindex = temp_variable
    elif firstindex == "d" or firstindex == "D":
        firstindex = dd
        temp_variable = firstindex
        firstindex = secondindex
        secondindex = temp_variable
    elif firstindex == "e" or firstindex == "E":
        firstindex = ee
        temp_variable = firstindex
        firstindex = secondindex
        secondindex = temp_variable
    elif firstindex == "f" or firstindex == "F":
        firstindex = ff
        temp_variable = firstindex
        firstindex = secondindex
        secondindex = temp_variable
    elif firstindex == "g" or firstindex == "G":
        firstindex = gg
        temp_variable = firstindex
        firstindex = secondindex
        secondindex = temp_variable
    elif firstindex == "h" or firstindex == "H":
        firstindex = hh
        temp_variable = firstindex
        firstindex = secondindex
        secondindex = temp_variable

    firstindex = int(firstindex)  # Using range which starts from zero
    firstindex = firstindex - 1
    secondindex = int(secondindex)
    secondindex = secondindex - 1

    if firstindex >= 8 or secondindex >= 8 or firstindex <= -1 or secondindex <= -1:
        return None

    return (firstindex, secondindex)

def valid_table_range(pos_x, pos_y):
    return pos_x >= 0 and pos_y >=0 and pos_x <= 7 and pos_y <= 7

# (dr, dc) x and y direction respectively

def enclosing(board, player, pos, direction):
    if player == 1:
        otherplayer = 2
    if player == 2:
        otherplayer = 1
    position_x = pos[0]
    position_y = pos[1]

    #### all possible directions:
    North = (-1, 0)
    NorthEast = (-1, 1)
    East = (0, 1)
    SouthEast = (1, 1)
    South = (1, 0)
    SouthWest = (1, -1)
    West = (0, -1)
    NorthWest = (-1, -1)

    otherplayer_count_North = 0  # Check in the wild loop if it has seen at least one
    otherplayer_count_NorthEast = 0
    otherplayer_count_East = 0
    otherplayer_count_SouthEast = 0
    otherplayer_count_South = 0
    otherplayer_count_SouthWest = 0
    otherplayer_count_West = 0
    otherplayer_count_NorthWest = 0

                                      # Had to use two valid move checks as valid_move-> while loop -> valid_move

    if direction == North:
        North_y_position = North[0]
        North_x_position = North[1]
        if valid_table_range(position_x + North_y_position, position_y)== True:      # Checks to see within range
            while board[position_x + North_y_position][position_y] == otherplayer:  # and otherplayer_count <= 0: # BECAREFUL with operators as -- = + affecting the coordiantes
                     # Cant play when the same colour on the same side
                if board[position_x + North_y_position][position_y] == otherplayer:
                    otherplayer_count_North += 1                     # conformation that they are inbetween stone
                    if valid_table_range(position_x + North_y_position -1, position_y) == False: # Checks to see if i program does another while loop will it be out of range
                        return False

                North_y_position -= 1

        reverse_position_x = position_x + North_y_position
        # print(reverse_position_x)
        if board[reverse_position_x][position_y] == player and otherplayer_count_North >= 1:
            output = True
        else:
            output = False

    if direction == NorthEast:
        North_east_y_position = NorthEast[0]
        North_east_x_position = NorthEast[1]
        if valid_table_range(position_x + North_east_y_position, position_y + North_east_x_position) == True:
            while board[position_x +North_east_y_position][position_y+North_east_x_position] == otherplayer:  # and otherplayer_count <= 0: # BECAREFUL with operators as -- = + affecting the coordiantes
            #print(board[position_x + North_y_position][position_y])
                if board[position_x + North_east_y_position][position_y+North_east_x_position] == otherplayer:
                    if valid_table_range(position_x + North_east_y_position -1, position_y + North_east_x_position +1) == False:
                        return False
                otherplayer_count_NorthEast += 1
                North_east_y_position -= 1
                North_east_x_position += 1
        reverse_position_x = position_x +North_east_y_position
        reverse_position_y = position_y +North_east_x_position
        #print(reverse_position_x, reverse_position_y)
        if valid_table_range(position_x + North_east_y_position, position_y + North_east_x_position)== True:
            if board[reverse_position_x][reverse_position_y] == player and otherplayer_count_NorthEast >= 1:
                output = True
            else:
                output = False
        else:
            output = False

    if direction == East:
        East_y_position = East[0]
        East_x_position = East[1]
        if valid_table_range(position_x + East_y_position, position_y + East_x_position)== True:
            while board[position_x + East_y_position][position_y + East_x_position] == otherplayer:  # and otherplayer_count <= 0: # BECAREFUL with operators as -- = + affecting the coordiantes
                # print(board[position_x + North_y_position][position_y])
                if board[position_x][position_y + East_x_position] == otherplayer:
                    otherplayer_count_East += 1
                    if valid_table_range(position_x + East_y_position, position_y + East_x_position+1) == False:
                        return False
                East_x_position += 1
        reverse_position_y = position_y + East_x_position
        reverse_position_x = position_x

        #print(reverse_position_x, reverse_position_y)
        if valid_table_range(position_x + East_y_position, position_y + East_x_position)== True:
            if board[reverse_position_x][reverse_position_y] == player and otherplayer_count_East >= 1:
                output = True
            else:
                output = False
        else:
            output = False

    if direction == SouthEast:
        South_east_y_position = SouthEast[0]
        South_east_x_position = SouthEast[1]
        if valid_table_range(position_x + South_east_y_position, position_y + South_east_x_position) == True:
            while board[position_x + South_east_y_position][position_y + South_east_x_position] == otherplayer:  # and otherplayer_count <= 0: # BECAREFUL with operators as -- = + affecting the coordiantes
                # print(board[position_x + North_y_position][position_y])
                if board[position_x + South_east_y_position][position_y + South_east_x_position] == otherplayer:
                    otherplayer_count_SouthEast += 1
                    if valid_table_range(position_x + South_east_y_position+1, position_y + South_east_x_position+1) == False:
                        return False
                South_east_y_position += 1
                South_east_x_position += 1
        reverse_position_x = position_x + South_east_y_position
        reverse_position_y = position_y + South_east_x_position
        #print(reverse_position_x, reverse_position_y)


        if valid_table_range(position_x + South_east_y_position, position_y + South_east_x_position)== True:
            if board[reverse_position_x][reverse_position_y] == player and otherplayer_count_SouthEast >= 1:
                output = True
            else:
                output = False
        else:
            output = False



    if direction == South:
        South_y_position = South[0]
        South_x_position = South[1]
        if valid_table_range(position_x + South_y_position, position_y + South_x_position) == True:
            while board[position_x + South_y_position][position_y + South_x_position] == otherplayer:   # BECAREFUL with operators as -- = + affecting the coordiantes
                # print(board[position_x + North_y_position][position_y])
                if board[position_x + South_y_position][position_y + South_x_position] == otherplayer:
                    otherplayer_count_South += 1
                    if valid_table_range(position_x + South_y_position+1, position_y + South_x_position) == False:
                        return False
                South_y_position += 1
        reverse_position_x = position_x + South_y_position
        reverse_position_y = position_y + South_x_position
        #print(reverse_position_x, reverse_position_y)
        if valid_table_range(position_x + South_y_position, position_y + South_x_position) == True:
            if board[reverse_position_x][reverse_position_y] == player and otherplayer_count_South >= 1:
                output = True
            else:
                output = False
        else:
            output = False
    if direction == SouthWest:
        South_West_y_position = SouthWest[0]
        South_West_x_position = SouthWest[1]
        if valid_table_range(position_x + South_West_y_position, position_y + South_West_x_position)== True:
            while board[position_x + South_West_y_position][position_y + South_West_x_position] == otherplayer:  # and otherplayer_count <= 0: # BECAREFUL with operators as -- = + affecting the coordiantes
                # print(board[position_x + North_y_position][position_y])
                if board[position_x + South_West_y_position][position_y + South_West_x_position] == otherplayer:
                    otherplayer_count_SouthWest += 1
                    if valid_table_range(position_x + South_West_y_position +1, position_y + South_West_x_position -1) == False:
                        return False
                South_West_y_position += 1
                South_West_x_position -= 1
        reverse_position_x = position_x + South_West_y_position
        reverse_position_y = position_y + South_West_x_position
        #print(reverse_position_x, reverse_position_y)
        if valid_table_range(position_x + South_West_y_position, position_y + South_West_x_position) == True:
            if board[reverse_position_x][reverse_position_y] == player and otherplayer_count_SouthWest >= 1:
                output = True
            else:
                output = False
        else:
            output = False

    if direction == West:
        West_y_position = West[0]
        West_x_position = West[1]
        if valid_table_range(position_x + West_y_position, position_y + West_x_position)== True:
            while board[position_x + West_y_position][position_y + West_x_position] == otherplayer:  # and otherplayer_count <= 0: # BECAREFUL with operators as -- = + affecting the coordiantes
                # print(board[position_x + North_y_position][position_y])
                if board[position_x][position_y + West_x_position] == otherplayer:
                    if valid_table_range(position_x + West_y_position, position_y + West_x_position -1) == False:
                        return  False
                    otherplayer_count_West += 1
                West_x_position -= 1
        reverse_position_y = position_y + West_x_position
        reverse_position_x = position_x

        #print(reverse_position_x, reverse_position_y)
        if valid_table_range(position_x + West_y_position, position_y + West_x_position) == True:
            if board[reverse_position_x][reverse_position_y] == player and otherplayer_count_West >= 1:
                output = True
            else:
                output = False
        else:
            output = False

    if direction == NorthWest:
        North_West_y_position = NorthWest[0]
        North_west_x_position = NorthWest[1]
        if valid_table_range(position_x + North_West_y_position, position_y + North_west_x_position) == True:
            while board[position_x + North_West_y_position][position_y + North_west_x_position] == otherplayer:  # and otherplayer_count <= 0: # BECAREFUL with operators as -- = + affecting the coordiantes
                # print(board[position_x + North_y_position][position_y])
                if board[position_x + North_West_y_position][position_y + North_west_x_position] == otherplayer:
                    if valid_table_range(position_x + North_West_y_position -1,position_y + North_west_x_position-1 ) == False:
                        return False
                    otherplayer_count_NorthWest += 1
                North_West_y_position -= 1
                North_west_x_position -= 1
        reverse_position_x = position_x + North_West_y_position
        reverse_position_y = position_y + North_west_x_position
        #print(reverse_position_x, reverse_position_y)
        if valid_table_range(position_x + North_West_y_position, position_y + North_west_x_position) == True:
            if board[reverse_position_x][reverse_position_y] == player and otherplayer_count_NorthWest >= 1:
                output = True
            else:
                output = False
        else:
            output = False

    return output



def valid_moves(board, player):
    player_list_coordiantes_position = []
    valid_corrdinates_list = []

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                player_list_coordiantes_position.append((i, j))                # Finds all the player name location

    for list_length in (player_list_coordiantes_position):
        if enclosing(board, player, list_length, (-1, 0)) == True:
            #print("hi")
            valid_corrdinates_list.append(list_length)
        if enclosing(board, player, list_length, (-1, 1)) == True:
            #print("hi")
            valid_corrdinates_list.append(list_length)
        if enclosing(board, player, list_length, (0, 1)) == True:
            #print("hi")
            valid_corrdinates_list.append(list_length)

        if enclosing(board, player, list_length, (1, 1)) == True:
             # print("hi")
            valid_corrdinates_list.append(list_length)

        if enclosing(board, player, list_length, (1, 0)) == True:
            #print("hi")
            valid_corrdinates_list.append(list_length)
        if enclosing(board, player, list_length, (1, -1)) == True:
            #print("hi")
            valid_corrdinates_list.append(list_length)
        if enclosing(board, player, list_length, (0, -1)) == True:
            #print("hi")
            valid_corrdinates_list.append(list_length)
        if enclosing(board, player, list_length, (-1, -1)) == True:
            valid_corrdinates_list.append(list_length)


    return valid_corrdinates_list


def next_state(board, player, pos):
    """
    input:
    output: result of dropping something in the list of next_board and the next player
    appends all the index that are true
    """
    if player == 1:
        next_player = 2
    if player == 2:
        next_player = 1
    x = []

    x += effect_swap_variable(board, player, pos, (-1, 0))
    x += effect_swap_variable(board, player, pos, (-1, 1))
    x += effect_swap_variable(board, player, pos, (0, 1))
    x += effect_swap_variable(board, player, pos, (1, 1))
    x += effect_swap_variable(board, player, pos, (1, 0))
    x += effect_swap_variable(board, player, pos, (1, -1))
    x += effect_swap_variable(board, player, pos, (0, -1))
    x += effect_swap_variable(board, player, pos, (-1, -1))

    # Stone Added
    board[pos[0]][pos[1]] = player
    #Replace the stones inbetween
    for replace_index in x:
        board[replace_index[0]][replace_index[1]] = player




    return (board, next_player)


### similar to enclosing but rather than going forward go backwards to original

def effect_swap_variable(board, player, pos, direction):
    """

    appends all the index that are inbetween the stones that has been placed

    """
    if player == 1:
        next_player = 2
    if player == 2:
        next_player = 1
    position_x = pos[0]
    position_y = pos[1]
    indices_to_swap_list = [] # Only notable change

    #### all possible directions:
    North = (-1, 0)
    NorthEast = (-1, 1)
    East = (0, 1)
    SouthEast = (1, 1)
    South = (1, 0)
    SouthWest = (1, -1)
    West = (0, -1)
    NorthWest = (-1, -1)

    otherplayer_count_North = 0  # Check in the wild loop if it has seen at least one
    otherplayer_count_NorthEast = 0
    otherplayer_count_East = 0
    otherplayer_count_SouthEast = 0
    otherplayer_count_South = 0
    otherplayer_count_SouthWest = 0
    otherplayer_count_West = 0
    otherplayer_count_NorthWest = 0



    if direction == North:
        North_y_position = North[0]
        North_x_position = North[1]
        if valid_table_range(position_x + North_y_position, position_y)== True: #### CHECKS VALID POSITION
            while board[position_x + North_y_position][position_y] == next_player:  # and otherplayer_count <= 0: # BECAREFUL with operators as -- = + affecting the coordiantes
                # print(board[position_x + North_y_position][position_y])             # Cant play when the same colour on the same side
                if board[position_x + North_y_position][position_y] == next_player: #### CHECK IF THAT DIRECTION HAS OPOSSITE TILE
                    indices_to_swap_list.append([position_x +North_y_position, position_y]) #APPENDS IT SO IT CAN CHANGE TO OYHER TILE
                    otherplayer_count_North += 1 #### EnSURE THATS THERE ARE ONE  INBETWEEN THE STONE
                    if valid_table_range(position_x + North_y_position-1, position_y) == False: ##### CHECKS IF ADDING IT MAKES IT OUT OF RANGE
                        if board[position_x + North_y_position][position_y] == player and otherplayer_count_North >= 1: ####APPENDS THE EDGES IF ITS A THE SAME TILE AND THERE ARE OTHER PLAYER TILES
                            return indices_to_swap_list

                        return [] ### OTHERWISE IF ITS THE OPPOSITE PLAYER THAN YOU CANT
                    North_y_position -= 1

        reverse_position_x = position_x + North_y_position
        # print(reverse_position_x)
        if valid_table_range(position_x + North_y_position, position_y) == True:
            if board[reverse_position_x][position_y] == player and otherplayer_count_North >= 1:
                output = True
            else:
                output = False
                indices_to_swap_list = []
        else:
            output = False
            indices_to_swap_list = []

    if direction == NorthEast:
        North_east_y_position = NorthEast[0]
        North_east_x_position = NorthEast[1]
        if valid_table_range(position_x + North_east_y_position, position_y + North_east_x_position) == True:
            while board[position_x +North_east_y_position][position_y+North_east_x_position] == next_player:  # and otherplayer_count <= 0: # BECAREFUL with operators as -- = + affecting the coordiantes
            #print(board[position_x + North_y_position][position_y])
                if board[position_x + North_east_y_position][position_y+North_east_x_position] == next_player:
                    indices_to_swap_list.append([position_x + North_east_y_position, position_y+North_east_x_position])
                    otherplayer_count_NorthEast += 1
                    if valid_table_range(position_x + North_east_y_position-1,position_y + North_east_x_position+1) == False:
                        if board[position_x + North_east_y_position][position_y + North_east_x_position] == player and otherplayer_count_NorthEast >= 1:
                            return indices_to_swap_list
                        return []
                North_east_y_position -= 1
                North_east_x_position += 1
        reverse_position_x = position_x +North_east_y_position
        reverse_position_y = position_y +North_east_x_position
        #print(reverse_position_x, reverse_position_y)
        if valid_table_range(position_x + North_east_y_position, position_y + North_east_x_position)== True:
            if board[reverse_position_x][reverse_position_y] == player and otherplayer_count_NorthEast >= 1:
                output = True
            else:
                output = False
                indices_to_swap_list = []
        else:
            output = False
            indices_to_swap_list = []

    if direction == East:
        East_y_position = East[0]
        East_x_position = East[1]
        if valid_table_range(position_x + East_y_position, position_y + East_x_position)== True:
            while board[position_x + East_y_position][position_y + East_x_position] == next_player:  # and otherplayer_count <= 0: # BECAREFUL with operators as -- = + affecting the coordiantes
                # print(board[position_x + North_y_position][position_y])
                if board[position_x][position_y + East_x_position] == next_player:
                    indices_to_swap_list.append([position_x + East_y_position, position_y + East_x_position])
                    otherplayer_count_East += 1
                    if valid_table_range(position_x + East_y_position, position_y + East_x_position+1) == False:
                        if board[position_x + East_y_position][position_y + East_x_position] == player and otherplayer_count_East >= 1:
                            return indices_to_swap_list
                        return []
                East_x_position += 1
        reverse_position_y = position_y + East_x_position
        reverse_position_x = position_x

        #print(reverse_position_x, reverse_position_y)
        if valid_table_range(position_x + East_y_position, position_y + East_x_position)== True:
            if board[reverse_position_x][reverse_position_y] == player and otherplayer_count_East >= 1:
                output = True
            else:
                output = False
                indices_to_swap_list = []
        else:
            output = False
            indices_to_swap_list = []

    if direction == SouthEast:
        South_east_y_position = SouthEast[0]
        South_east_x_position = SouthEast[1]
        if valid_table_range(position_x + South_east_y_position, position_y + South_east_x_position) == True:
            while board[position_x + South_east_y_position][position_y + South_east_x_position] == next_player:  # and otherplayer_count <= 0: # BECAREFUL with operators as -- = + affecting the coordiantes
                # print(board[position_x + North_y_position][position_y])
                if board[position_x + South_east_y_position][position_y + South_east_x_position] == next_player:
                    indices_to_swap_list.append([position_x + South_east_y_position, position_y + South_east_x_position])
                    otherplayer_count_SouthEast += 1
                    if valid_table_range(position_x + South_east_y_position +1,position_y + South_east_x_position+1) == False:
                        if board[position_x + South_east_y_position][position_y + South_east_x_position] == player and otherplayer_count_SouthEast >= 1:
                            return indices_to_swap_list
                        return []
                South_east_y_position += 1
                South_east_x_position += 1
        reverse_position_x = position_x + South_east_y_position
        reverse_position_y = position_y + South_east_x_position
        #print(reverse_position_x, reverse_position_y)


        if valid_table_range(position_x + South_east_y_position, position_y + South_east_x_position):
            if board[reverse_position_x][reverse_position_y] == player and otherplayer_count_SouthEast >= 1:
                output = True
            else:
                output = False
                indices_to_swap_list = []
        else:
            output = False
            indices_to_swap_list = []



    if direction == South:
        South_y_position = South[0]
        South_x_position = South[1]
        if valid_table_range(position_x + South_y_position, position_y + South_x_position) == True:
            while board[position_x + South_y_position][position_y + South_x_position] == next_player:  # and otherplayer_count <= 0: # BECAREFUL with operators as -- = + affecting the coordiantes
                # print(board[position_x + North_y_position][position_y])
                if board[position_x + South_y_position][position_y + South_x_position] == next_player:
                    indices_to_swap_list.append([position_x + South_y_position, position_y + South_x_position])
                    otherplayer_count_South += 1
                    if valid_table_range(position_x + South_y_position+1, position_y + South_x_position) == False:
                        if board[position_x + South_y_position][position_y + South_x_position] == player and otherplayer_count_South >= 1:
                            return indices_to_swap_list
                        return []
                South_y_position += 1
        reverse_position_x = position_x + South_y_position
        reverse_position_y = position_y + South_x_position
        #print(reverse_position_x, reverse_position_y)
        if valid_table_range(position_x + South_y_position, position_y + South_x_position) == True:
            if board[reverse_position_x][reverse_position_y] == player and otherplayer_count_South >= 1:
                output = True
            else:
                output = False
                indices_to_swap_list = []
        else:
            output = False
            indices_to_swap_list = []
    if direction == SouthWest:
        South_West_y_position = SouthWest[0]
        South_West_x_position = SouthWest[1]
        if valid_table_range(position_x + South_West_y_position, position_y + South_West_x_position)== True:
            while board[position_x + South_West_y_position][position_y + South_West_x_position] == next_player:  # and otherplayer_count <= 0: # BECAREFUL with operators as -- = + affecting the coordiantes
                # print(board[position_x + North_y_position][position_y])
                if board[position_x + South_West_y_position][position_y + South_West_x_position] == next_player:
                    indices_to_swap_list.append([position_x + South_West_y_position, position_y + South_West_x_position])
                    otherplayer_count_SouthWest += 1
                    if valid_table_range(position_x + South_West_y_position+1,position_y + South_West_x_position-1) == False:
                        if board[position_x + South_West_y_position][position_y + South_West_x_position] == player and otherplayer_count_SouthWest >= 1:
                            return indices_to_swap_list
                        return []
                South_West_y_position += 1
                South_West_x_position -= 1
        reverse_position_x = position_x + South_West_y_position
        reverse_position_y = position_y + South_West_x_position
        #print(reverse_position_x, reverse_position_y)
        if valid_table_range(position_x + South_West_y_position, position_y + South_West_x_position) == True:
            if board[reverse_position_x][reverse_position_y] == player and otherplayer_count_SouthWest >= 1:
                output = True
            else:
                output = False
                indices_to_swap_list = []
        else:
            output = False
            indices_to_swap_list = []

    if direction == West:
        West_y_position = West[0]
        West_x_position = West[1]
        if valid_table_range(position_x + West_y_position, position_y + West_x_position)== True:
            while board[position_x + West_y_position][position_y + West_x_position] == next_player:  # and otherplayer_count <= 0: # BECAREFUL with operators as -- = + affecting the coordiantes
                # print(board[position_x + North_y_position][position_y])
                if board[position_x][position_y + West_x_position] == next_player:
                    indices_to_swap_list.append([position_x + West_y_position, position_y + West_x_position])
                    otherplayer_count_West += 1
                    if valid_table_range(position_x + West_y_position, position_y + West_x_position-1) == False:
                        if board[position_x + West_y_position][ position_y + West_x_position]== player and otherplayer_count_West >= 1:
                            return indices_to_swap_list
                        return []
                West_x_position -= 1

        reverse_position_y = position_y + West_x_position
        reverse_position_x = position_x

        #print(reverse_position_x, reverse_position_y)
        if valid_table_range(position_x + West_y_position, position_y + West_x_position) == True:
            if board[reverse_position_x][reverse_position_y] == player and otherplayer_count_West >= 1:
                output = True
            else:
                output = False
                indices_to_swap_list = []
        else:
            output = False
            indices_to_swap_list = []

    if direction == NorthWest:
        North_West_y_position = NorthWest[0]
        North_west_x_position = NorthWest[1]
        if valid_table_range(position_x + North_West_y_position, position_y + North_west_x_position) == True:
            while board[position_x + North_West_y_position][position_y + North_west_x_position] == next_player:  # and otherplayer_count <= 0: # BECAREFUL with operators as -- = + affecting the coordiantes
                # print(board[position_x + North_y_position][position_y])
                if board[position_x + North_West_y_position][position_y + North_west_x_position] == next_player:
                    indices_to_swap_list.append([position_x + North_West_y_position, position_y + North_west_x_position])
                    otherplayer_count_NorthWest += 1
                    if valid_table_range(position_x + North_West_y_position-1,position_y + North_west_x_position-1) == False:
                        if board[position_x + North_West_y_position][position_y + North_west_x_position] == player and otherplayer_count_NorthWest >= 1:
                            return indices_to_swap_list
                        return []
                North_West_y_position -= 1
                North_west_x_position -= 1
        reverse_position_x = position_x + North_West_y_position
        reverse_position_y = position_y + North_west_x_position
        #print(reverse_position_x, reverse_position_y)
        if valid_table_range(position_x + North_West_y_position, position_y + North_west_x_position) == True:
            if board[reverse_position_x][reverse_position_y] == player and otherplayer_count_NorthWest >= 1:
                output = True
            else:
                output = False
                indices_to_swap_list = []
        else:
            output = False
            indices_to_swap_list = []

    return indices_to_swap_list


def run_two_players():
    print("Welcome to REVERSI |TWO PLAYER !!!!| If you want to quit type 'q'")
    input_text = " "
    fresh_board = new_board()
    while input_text != "q":
        print(print_board(fresh_board))
        if valid_moves(fresh_board, 1) != []:   # Checks if its valid
            player = 1
            print("Player One your up!")
            player_one_move = input("Whats your move:")

            if player_one_move == "q":
                break
            if player_one_move == "Q":
                break
            acctual_coordiantes_one = position(player_one_move)
            if acctual_coordiantes_one in valid_moves(fresh_board, player):
                x1 = next_state(fresh_board, player, acctual_coordiantes_one)
                fresh_board = x1[0]
                print(print_board(fresh_board))
                player = x1[1]
            elif acctual_coordiantes_one not in valid_moves(fresh_board, player):
                print("Mate you got it wrong enter another one")
                player_one_move = input("Another move:")
                if player_one_move == "q":
                    break
                if player_one_move == "Q":
                    break
                acctual_coordiantes_one = position(player_one_move)
                if acctual_coordiantes_one in valid_moves(fresh_board, player):
                    x1 = next_state(fresh_board, player, acctual_coordiantes_one)
                    fresh_board = x1[0]
                    print(print_board(fresh_board))
                    player = x1[1]
                else:
                    player =2
            else:
                print("Invalid Move")
                print(print_board(fresh_board))
                player = 2

            # Stops if no valid move
        #if valid_moves(fresh_board, 1) == []:
            #if valid_moves(fresh_board, 2) == []:
             #   print(score(fresh_board))
             #   input_text = 'q'

        if valid_moves(fresh_board, 2) != []:
            print("Player two your up")
            player_two_move = input("Whats your move:")
            if player_two_move == "q":
                break
            if player_two_move == "Q":
                break
            acctual_coordiantes_two = position(player_two_move)
            if acctual_coordiantes_two in valid_moves(fresh_board, player):
                x2 = next_state(fresh_board, player, acctual_coordiantes_two)
                fresh_board = x2[0]
                #print(print_board(fresh_board))
                player = x2[1]
            elif acctual_coordiantes_two not in valid_moves(fresh_board, player):
                print("Mate Invalid move try again")
                player_two_move = input("Whats your move:")
                if player_two_move == "q":
                    break
                if player_two_move == "Q":
                    break
                acctual_coordiantes_two = position(player_two_move)
                if acctual_coordiantes_two in valid_moves(fresh_board, player):
                    x2 = next_state(fresh_board, player, acctual_coordiantes_two)
                    fresh_board = x2[0]
                    # print(print_board(fresh_board))
                    player = x2[1]
                else:
                    player = 1
            else:
                print("Invalid Move")
                # print(print_board(fresh_board))
                player = 1
        # Stops if no valid move
        if valid_moves(fresh_board, 1) == []:
           if valid_moves(fresh_board, 2) == []:
               print(score(fresh_board))
               break
    return("Thanks for playing")









def run_single_player():
    print("Welcome to REVERSI |SINGLE PLAYER !!!!| If you want to quit type 'q'")
    input_text = ""
    fresh_board = new_board()
    while input_text != "q":
        print(print_board(fresh_board))
        if valid_moves(fresh_board, 1) != []:
            player = 1
            print("Player One your up!")
            player_one_move = input("Whats your move:")

            if player_one_move == "q":
                break
            if player_one_move == "Q":
                break
            acctual_coordiantes_one = position(player_one_move)
            if acctual_coordiantes_one in valid_moves(fresh_board, player):
                x1 = next_state(fresh_board, player, acctual_coordiantes_one)
                fresh_board = x1[0]
                print(print_board(fresh_board))
                player = x1[1]
            elif acctual_coordiantes_one not in valid_moves(fresh_board, player):
                print("Mate you got it wrong enter another one")
                player_one_move = input("Another move:")
                if player_one_move == "q":
                    break
                if player_one_move == "Q":
                    break
                acctual_coordiantes_one = position(player_one_move)
                if acctual_coordiantes_one in valid_moves(fresh_board, player):
                    x1 = next_state(fresh_board, player, acctual_coordiantes_one)
                    fresh_board = x1[0]
                    print(print_board(fresh_board))
                    player = x1[1]
                else:
                    player = 2
            else:
                print("Invalid Move")
                print(print_board(fresh_board))


        if valid_moves(fresh_board, 2) != []:
            highest_value_cords = valid_moves(fresh_board, player)[0]   # Base value to compare
            for i in valid_moves(fresh_board, player):
                if len(max_values(fresh_board, player, highest_value_cords)) <= len(max_values(fresh_board, player, i)):
                    highest_value_cords = i
            x2 = next_state(fresh_board, player, highest_value_cords)
            fresh_board = x2[0]
            # print(print_board(fresh_board))
            player = x2[1]
        if valid_moves(fresh_board, 1) == []:
           if valid_moves(fresh_board, 2) == []:
               print(score(fresh_board))
               break

    return "Thanks for playing :)"









# f5, d6




def max_values(board, player, pos):
    """
    input: Similar to next_state but it doesnt append the inbetween stones
    output: gives me the list of coordinates to append
    """
    if player == 1:
        next_player = 2
    if player == 2:
        next_player = 1
    x = []

    x += effect_swap_variable(board, player, pos, (-1, 0))
    x += effect_swap_variable(board, player, pos, (-1, 1))
    x += effect_swap_variable(board, player, pos, (0, 1))
    x += effect_swap_variable(board, player, pos, (1, 1))
    x += effect_swap_variable(board, player, pos, (1, 0))
    x += effect_swap_variable(board, player, pos, (1, -1))
    x += effect_swap_variable(board, player, pos, (0, -1))
    x += effect_swap_variable(board, player, pos, (-1, -1))




    return x






#print(run_single_player())
#print(run_two_players())
#print(run_single_player())
#print(enclosing(new_board(), 2, (7,4), (1, 0)) )
#enclosing(board, 2, list_length, (1, 0)) == True
#print(print_board(new_board()))
#print(score(new_board()))
#print(position("e8"))
#print(valid_table_range(7+1,3))
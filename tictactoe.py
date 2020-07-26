cells = {(1, 1): " ", (1, 2): " ", (1, 3): " ",
         (2, 1): " ", (2, 2): " ", (2, 3): " ",
         (3, 1): " ", (3, 2): " ", (3, 3): " "}


def draw_board():
    print("---------")
    for i in range(1, 4):
        print("|", cells[1, 4 - i], cells[2, 4 - i], cells[3, 4 - i], "|")
    print("---------")


def check_game_state():
    if is_x_wins():
        return "X wins"
    elif is_o_wins():
        return "O wins"
    elif [e for e in cells.values()].count(" ") == 9:
        return "Empty"
    elif [e for e in cells.values()].count(" ") == 0:
        return "Draw"
    else:
        return "Play"


def is_x_wins():

    for i in range(1, 4):
        if (cells[1, i] + cells[2, i] + cells[3, i] == "XXX" or
                cells[i, 1] + cells[i, 2] + cells[i, 3] == "XXX"):
            return True

    if (cells[1, 1] + cells[2, 2] + cells[3, 3] == "XXX" or
            cells[1, 3] + cells[2, 2] + cells[3, 1] == "XXX"):
        return True

    return False


def is_o_wins():

    for i in range(1, 4):
        if (cells[1, i] + cells[2, i] + cells[3, i] == "OOO" or
                cells[i, 1] + cells[i, 2] + cells[i, 3] == "OOO"):
            return True

    if (cells[1, 1] + cells[2, 2] + cells[3, 3] == "OOO" or
            cells[1, 3] + cells[2, 2] + cells[3, 1] == "OOO"):
        return True

    return False


def make_move(symbol):

    while True:
        user_input = input("Enter the coordinates: ").split()
        if len(user_input) != 2:
            print("You should enter exactly two numbers!")
        else:
            x, y = user_input[0], user_input[1]
            if x.isdigit() and y.isdigit():
                if (1 <= int(x) <= 3) and (1 <= int(y) <= 3):
                    if cells[int(x), int(y)] == " ":
                        cells[int(x), int(y)] = symbol
                        return
                    else:
                        print("This cell is occupied! Choose another one!")
                else:
                    print("Coordinates should be from 1 to 3!")
            else:
                print("You should enter numbers!")


def change_gamer(symbol):
    return "O" if symbol == "X" else "X"


draw_board()
end_states = {"X wins", "O wins", "Draw"}
sym = "X"
while check_game_state() not in end_states:
    make_move(sym)
    draw_board()
    sym = change_gamer(sym)

print(check_game_state())

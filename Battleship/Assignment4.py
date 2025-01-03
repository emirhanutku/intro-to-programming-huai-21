import sys
all_outputs = open("Battleship.out", "w")
def saving_outputs_to_file(x):
    print(x)
    all_outputs.write(x+"\n")
player1_ships = sys.argv[1]
player2_ships = sys.argv[2]
player1_moves = sys.argv[3]
player2_moves = sys.argv[4]
io_error_list = []
players_name = []
try:
    player1_ships_input = open(player1_ships, "r")
except IOError as txt1:
    io_error_list.append(txt1)
try:
    player2_ships_input = open(player2_ships, "r")

except IOError as txt2:
    io_error_list.append(txt2)
try:
    player1_moves_input = open(player1_moves, "r")
except IOError as in1:
    io_error_list.append(in1)
try:
    player2_moves_input = open(player2_moves, "r")
except IOError as in2:
    io_error_list.append(in2)
if len(io_error_list) != 0:
    for i in io_error_list:
        index_of_quotes = str(i).index("'")
        players_name.append(str(i)[index_of_quotes + 1:-1])
    saving_outputs_to_file("IOError: input file(s) {} is/are not reachable.".format(", ".join(players_name)))
    quit()

optional1 = open("OptionalPlayer1.txt", "r")
optional2 = open("OptionalPlayer2.txt", "r")


def required_inputs():
    global moves1, moves2, all_ships1, all_ships2, ships1, ships2
    all_ships1 = []
    all_ships2 = []
    moves2 = player2_moves_input.readline().rstrip(";").split(";")
    moves1 = player1_moves_input.readline().rstrip(";").split(";")
    for i in range(len(open(player1_ships, "r").readlines())):
        ships1 = player1_ships_input.readline().rstrip("\n").split(";")
        ships2 = player2_ships_input.readline().rstrip("\n").split(";")
        all_ships1.append(ships1)
        all_ships2.append(ships2)


required_inputs()
Player1s_Board = {}
Player2s_Board = {}
Main_Table1 = {}
Main_Table2 = {}
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
alphabet=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


def grids():
    for i in range(10):
        Player1s_Board[i + 1] = {}
        Player2s_Board[i + 1] = {}
        Main_Table1[i + 1] = {}
        Main_Table2[i + 1] = {}
        for k in range(len(letters)):
            Player1s_Board[i + 1][letters[k]] = {}
            Player2s_Board[i + 1][letters[k]] = {}
            Main_Table1[i + 1][letters[k]] = {}
            Main_Table2[i + 1][letters[k]] = {}
            Main_Table1[i + 1][letters[k]] = "-"
            Main_Table2[i + 1][letters[k]] = "-"
            Player1s_Board[i + 1][letters[k]] = all_ships1[i][k]
            Player2s_Board[i + 1][letters[k]] = all_ships2[i][k]

grids()
ships1 = {}
ships2 = {}

def ships():
    global ships1, ships2
    for n in ("Carrier", "Destroyer", "Submarine"):
        ships1[n] = {}
        ships2[n] = {}
    for i in range(10):
        for l in ("Carrier", "Destroyer", "Submarine"):
            ships1[l][i + 1] = {}
            ships2[l][i + 1] = {}
        for k in range(len(letters)):
            if Player1s_Board[i + 1][letters[k]] == "C":
                ships1["Carrier"][i + 1][letters[k]] = "C"
            elif Player1s_Board[i + 1][letters[k]] == "D":
                ships1["Destroyer"][i + 1][letters[k]] = "D"
            elif Player1s_Board[i + 1][letters[k]] == "S":
                ships1["Submarine"][i + 1][letters[k]] = "S"
            if Player2s_Board[i + 1][letters[k]] == "C":
                ships2["Carrier"][i + 1][letters[k]] = "C"
            elif Player2s_Board[i + 1][letters[k]] == "D":
                ships2["Destroyer"][i + 1][letters[k]] = "D"
            elif Player2s_Board[i + 1][letters[k]] == "S":
                ships2["Submarine"][i + 1][letters[k]] = "S"

    def optional_txt_func(optTxt, ships):
        opt_file = open(optTxt, "r")
        while True:
            line = opt_file.readline()
            if line == "":
                break
            else:

                ship_name, data = line.split(":")
                position, direction = data.split(";")[:-1]
                row, column = position.split(",")
                row = int(row)
                ship_lenghth = {"B": 4, "P": 2}
                ships[ship_name] = {}
                if direction == "right":
                    column_index = letters.index(column)
                    interval = letters[column_index:ship_lenghth[ship_name[0]] + column_index]
                    ships[ship_name][row] = {}
                    for column_counter in interval:
                        ships[ship_name][row][column_counter] = ship_name[0]
                elif direction == "down":
                    interval = range(row, ship_lenghth[ship_name[0]] + row)
                    for row_counter in interval:
                        ships[ship_name][row_counter] = {column: ship_name[0]}
        return ships

    ships1 = optional_txt_func("OptionalPlayer1.txt", ships1)
    ships2 = optional_txt_func("OptionalPlayer2.txt", ships2)


ships()


def write_table():
    for o in ("Carrier", "Battleship", "Destroyer", "Submarine", "Patrol Boat"):
        if o=="Carrier":
            print(o, end="\t\t")
            all_outputs.write(o+"\t\t")
        else:
            print(o, end="\t")
            all_outputs.write(o + "\t")
        if o == "Battleship":
            a = 0
            b = 0
            if any(list(ships1["B1"][l].values())[m] != "" for l in list(ships1["B1"].keys()) for m in
                   range(len(list(ships1["B1"][l].values())))):
                a = a + 1
            else:
                b = b + 1
            if any(list(ships1["B2"][l].values())[m] != "" for l in list(ships1["B2"].keys()) for m in
                   range(len(list(ships1["B2"][l].values())))):
                a = a + 1
            else:
                b = b + 1
            if a==0:
                print((b * "X ").strip(" "), end="")
                all_outputs.write((b * "X ").rstrip(" ") + "")
            else:
                print(b * "X ", end="")
                all_outputs.write(b * "X " + "")
            print((a * "- ").strip(""), end="\t\t\t\t")
            all_outputs.write((a * "- ").rstrip(" ") + "\t\t\t\t")
        elif o == "Patrol Boat":
            c = 0
            d = 0
            if any(list(ships1["P1"][l].values())[m] != "" for l in list(ships1["P1"].keys()) for m in
                   range(len(list(ships1["P1"][l].values())))):
                c = c + 1
            else:
                d = d + 1
            if any(list(ships1["P2"][l].values())[m] != "" for l in list(ships1["P2"].keys()) for m in
                   range(len(list(ships1["P2"][l].values())))):
                c = c + 1
            else:
                d = d + 1
            if any(list(ships1["P3"][l].values())[m] != "" for l in list(ships1["P3"].keys()) for m in
                   range(len(list(ships1["P3"][l].values())))):
                c = c + 1
            else:
                d = d + 1
            if any(list(ships1["P4"][l].values())[m] != "" for l in list(ships1["P4"].keys()) for m in
                   range(len(list(ships1["P4"][l].values())))):
                c = c + 1
            else:
                d = d + 1
            if c==0:
                print((d * "X ").rstrip(" "), end="")
                all_outputs.write((d * "X ").rstrip(" ")+"")
            else:
                print(d * "X ", end="")
                all_outputs.write(d * "X " + "")
            print((c * "- ").rstrip(" "), end="\t\t\t")
            all_outputs.write((c * "- ").rstrip(" ")+"\t\t\t")

        else:
            if any(list(ships1[o][l].values())[m] != "" for l in list(ships1[o].keys()) for m in
                   range(len(list(ships1[o][l].values())))):
                print("-", end="\t\t\t\t")
                all_outputs.write("-"+"\t\t\t\t")
            else:
                print("X", end="\t\t\t\t")
                all_outputs.write("X"+"\t\t\t\t")
        if o=="Carrier":
            print(o, end="\t\t")
            all_outputs.write(o+"\t\t")
        else:
            print(o, end="\t")
            all_outputs.write(o + "\t")
        if o == "Battleship":
            k = 0
            l = 0
            if any(list(ships2["B1"][l].values())[m] != "" for l in list(ships2["B1"].keys()) for m in
                   range(len(list(ships2["B1"][l].values())))):
                k = k + 1
            else:
                l = l + 1
            if any(list(ships2["B2"][l].values())[m] != "" for l in list(ships2["B2"].keys()) for m in
                   range(len(list(ships2["B2"][l].values())))):
                k = k + 1
            else:
                l = l + 1
            if k==0:
                print((l * "X ").rstrip(" "), end="")
                all_outputs.write((l * "X ").rstrip(" ")+"")
            else:
                print(l * "X ", end="")
                all_outputs.write(l * "X " + "")

            saving_outputs_to_file((k * "- ").rstrip(" "))
        elif o == "Patrol Boat":
            m = 0
            n = 0
            if any(list(ships2["P1"][l].values())[m] != "" for l in list(ships2["P1"].keys()) for m in
                   range(len(list(ships2["P1"][l].values())))):
                m = m + 1
            else:
                n = n + 1
            if any(list(ships2["P2"][l].values())[m] != "" for l in list(ships2["P2"].keys()) for m in
                   range(len(list(ships2["P2"][l].values())))):
                m = m + 1
            else:
                n = n + 1
            if any(list(ships2["P3"][l].values())[m] != "" for l in list(ships2["P3"].keys()) for m in
                   range(len(list(ships2["P3"][l].values())))):
                m = m + 1
            else:
                n = n + 1
            if any(list(ships2["P4"][l].values())[m] != "" for l in list(ships2["P4"].keys()) for m in
                   range(len(list(ships2["P4"][l].values())))):
                m = m + 1
            else:
                n = n + 1
            if m!=0:
                print(n * "X ", end="")
                all_outputs.write(n * "X "+"")
            else:
                print((n * "X ").rstrip(" "), end="")
                all_outputs.write((n * "X ").rstrip(" ") + "")


            saving_outputs_to_file((m * "- ").rstrip(" "))
        else:
            if any(list(ships2[o][l].values())[m] != "" for l in list(ships2[o].keys()) for m in
                   range(len(list(ships2[o][l].values())))):
                saving_outputs_to_file("-")
            else:
                saving_outputs_to_file("X")


def write_tables():
    for i in range(10):
        if list(Main_Table1.keys())[i] > 9:

            print(list(Main_Table1.keys())[i], end="")
            all_outputs.write(str(list(Main_Table1.keys())[i])+"")
            for k in range(len(letters)):
                if k == 9:
                    print(list(Main_Table1[i + 1].values())[k], end="")
                    all_outputs.write(list(Main_Table1[i + 1].values())[k] + "")
                else:
                    print(list(Main_Table1[i + 1].values())[k], end=" ")
                    all_outputs.write(list(Main_Table1[i + 1].values())[k] + " ")

            print("\t\t",list(Main_Table2.keys())[i], end="")
            all_outputs.write("\t\t"+str(list(Main_Table2.keys())[i])+"")
            for k in range(len(letters)):
                if k==9:
                    print(list(Main_Table2[i + 1].values())[k], end="")
                    all_outputs.write(list(Main_Table2[i + 1].values())[k]+"")
                else:
                    print(list(Main_Table2[i + 1].values())[k], end=" ")
                    all_outputs.write(list(Main_Table2[i + 1].values())[k] + " ")
            saving_outputs_to_file("")
            saving_outputs_to_file("")
            write_table()



        else:
            print(list(Main_Table1.keys())[i], end=" ")
            all_outputs.write(str(list(Main_Table1.keys())[i])+" ")
            for k in range(len(letters)):
                if k==9:
                    print(list(Main_Table1[i + 1].values())[k], end="")
                    all_outputs.write(list(Main_Table1[i + 1].values())[k]+"")
                else:
                    print(list(Main_Table1[i + 1].values())[k], end=" ")
                    all_outputs.write(list(Main_Table1[i + 1].values())[k] + " ")


            print("\t\t", list(Main_Table2.keys())[i], end=" ")
            all_outputs.write("\t\t"+str(list(Main_Table2.keys())[i])+" ")
            for k in range(len(letters)):
                if k==9:
                    print(list(Main_Table2[i + 1].values())[k], end="")
                    all_outputs.write(list(Main_Table2[i + 1].values())[k]+"")
                else:
                    print(list(Main_Table2[i + 1].values())[k], end=" ")
                    all_outputs.write(list(Main_Table2[i + 1].values())[k] + " ")
        saving_outputs_to_file("")


def control_of_moves(Table, moves, ships, board, j):
    Table[int(moves[j].split(",")[0])][moves[j].split(",")[1]] = "X"
    if board[int(moves[j].split(",")[0])][moves[j].split(",")[1]] == "B":
        if int(moves[j].split(",")[0]) in list(ships["B1"].keys()) and (moves[j].split(",")[1]) in list(
                ships["B1"][int(moves[j].split(",")[0])].keys()):
            ships["B1"][int(moves[j].split(",")[0])][moves[j].split(",")[1]] = ""
        else:
            ships["B2"][int(moves[j].split(",")[0])][moves[j].split(",")[1]] = ""
    elif board[int(moves[j].split(",")[0])][moves[j].split(",")[1]] == "P":
        if int(moves[j].split(",")[0]) in list(ships["P1"].keys()) and (moves[j].split(",")[1]) in list(
                ships["P1"][int(moves[j].split(",")[0])].keys()):
            ships["P1"][int(moves[j].split(",")[0])][moves[j].split(",")[1]] = ""
        elif int(moves[j].split(",")[0]) in list(ships["P2"].keys()) and (moves[j].split(","))[1] in list(
                ships["P2"][int(moves[j].split(",")[0])].keys()):
            ships["P2"][int(moves[j].split(",")[0])][moves[j].split(",")[1]] = ""
        elif int(moves[j].split(",")[0]) in list(ships["P3"].keys()) and (moves[j].split(","))[1] in list(
                ships["P3"][int(moves[j].split(",")[0])].keys()):
            ships["P3"][int(moves[j].split(",")[0])][moves[j].split(",")[1]] = ""
        else:
            ships["P4"][int(moves[j].split(",")[0])][moves[j].split(",")[1]] = ""
    elif board[int(moves[j].split(",")[0])][moves[j].split(",")[1]] == "C":
        ships["Carrier"][int(moves[j].split(",")[0])][moves[j].split(",")[1]] = ""
    elif board[int(moves[j].split(",")[0])][moves[j].split(",")[1]] == "D":
        ships["Destroyer"][int(moves[j].split(",")[0])][moves[j].split(",")[1]] = ""
    else:
        ships["Submarine"][int(moves[j].split(",")[0])][moves[j].split(",")[1]] = ""


def error_func(position):
    def index_error(position):
        try:
            if position == "":
                saving_outputs_to_file("IndexError:Please enter row and column\n")
                error_of_index = True
            elif "," not in position and position != "":
                try:
                    number = int(position[0:-1])
                    letter = position[-1]
                    try:
                        letter = int(letter)
                        raise AssertionError("IndexError:Please enter column\n")
                    except:
                        saving_outputs_to_file("IndexError:Please enter row\n")
                        error_of_index= True
                except ValueError:
                    if position[-1] in letters:
                        saving_outputs_to_file("IndexError:Please enter row\n")
                        error_of_index=True
                    else:
                        saving_outputs_to_file("IndexError:Please enter column\n")
                        error_of_index = True
                except AssertionError as msg:
                    saving_outputs_to_file(msg)
                    error_of_index = True

            else:
                row = position.split(",")[0]
                column = position.split(",")[1]
                if row == "" and column == "":
                    saving_outputs_to_file("IndexError:Please enter row and column\n")
                    error_of_index = True
                elif row == "":
                    saving_outputs_to_file("IndexError:Please enter row\n")
                    error_of_index = True
                elif column == "":
                    saving_outputs_to_file("IndexError:Please enter column\n")
                    error_of_index = True
                else:
                    error_of_index = False
            return error_of_index
        except:
            saving_outputs_to_file("kaBOOM: run for your life!\n")
            error_of_index=True
            return error_of_index

    def value_error(positon):
        try:
            row=positon.split(",")[0]
            column=positon.split(",")[1]
            if len(positon.split(","))>2:
                saving_outputs_to_file("ValueError:Please enter a correct move\n")
                error_of_value=True
            elif row in alphabet and column not in alphabet:
                saving_outputs_to_file("ValueError:Row must be number and column must be letter\n")
                error_of_value=True
            elif column not in alphabet:
                saving_outputs_to_file("ValueError:Column must be letter\n")
                error_of_value = True
            elif row in alphabet:
                saving_outputs_to_file("ValueError:Row must be number\n")
                error_of_value = True
            else:
                error_of_value=False
            return error_of_value
        except:
            saving_outputs_to_file("kaBOOM: run for your life!\n")
            error_of_value=True
            return error_of_value

    def assertion_error(positon):
        try:
            row = positon.split(",")[0]
            column = positon.split(",")[1]
            if int(row)>10 and column not in letters:
                saving_outputs_to_file("AssertionError:Row must be less than ten and Column must be between A and J\n")
                error_of_assertion=True
            elif int(row)>10:
                saving_outputs_to_file("AssertionError:Row must be less than ten\n")
                error_of_assertion = True
            elif column not in letters:
                saving_outputs_to_file("AssertionError:Column must be between A and J\n")
                error_of_assertion = True
            else:
                error_of_assertion=False
            return error_of_assertion
        except:
            saving_outputs_to_file("kaBOOM: run for your life!\n")
            error_of_assertion=True
            return error_of_assertion




    if index_error(position):
        return True
    elif value_error(position):
        return True
    elif assertion_error(position):
        return True
    else:
        return False

def moves(a, j):
    saving_outputs_to_file(a+ "\n")
    saving_outputs_to_file("Round : {}\t\t\t\t\tGrid Size: 10x10\n".format(j + 1))
    saving_outputs_to_file("Player1’s Hidden Board\t\tPlayer2’s Hidden Board")
    saving_outputs_to_file("  "+ " ".join(letters)+ "\t\t"+ " "+" "+ " ".join(letters))
    write_tables()

def game():
    saving_outputs_to_file("Battle of Ships Game\n")

    def game_for_player(current_player_moves=moves1, next_player_moves=moves2, currentCounter=0, nextCounter=0):


        def result1(counter):
            count2 = 0
            for i in range(10):
                for k in letters:
                    if Main_Table2[i + 1][k] == "X":
                        count2 = count2 + 1
            count1=0
            for i in range(10):
                for k in letters:
                    if Main_Table1[i + 1][k] == "X":
                        count1 = count1 + 1

            if count2 == 27 and count1 == 27:
                saving_outputs_to_file("Player1 Wins! , Player2 Wins! , It is a Draw'" + "\n\n" + "Final Information" + "\n")
                saving_outputs_to_file("Player1’s Board\t\t\t\tPlayer2’s Board")
                saving_outputs_to_file("  "+ " ".join(letters)+ "\t\t"+ "  "+ " ".join(letters))
                write_tables()
                quit()
            elif count2 == 27:
                saving_outputs_to_file("Player1 Wins!" + "\n\n" + "Final Information" + "\n")
                saving_outputs_to_file("Player1’s Board\t\t\t\tPlayer2’s Board")
                saving_outputs_to_file("  "+ " ".join(letters)+ "\t\t"+ "  "+ " ".join(letters))
                write_tables()
                quit()

        def result2():
            count1=0
            for i in range(10):
                for k in letters:
                    if Main_Table1[i + 1][k] == "X":
                        count1 = count1 + 1
            if count1 == 27:
                saving_outputs_to_file("Player2 Wins!" + "\n\n" + "Final Information" + "\n")
                saving_outputs_to_file("Player1’s Board\t\t\t\tPlayer2’s Board")
                saving_outputs_to_file("  "+ " ".join(letters)+ "\t\t"+ "  "+ " ".join(letters))
                write_tables()
                quit()

        if current_player_moves == moves1:
            com_arguments = {"Table": Main_Table2, "moves": moves1, "ships": ships2, "board": Player2s_Board,
                             "j": currentCounter}
            moves_arguments = {"a": "Player1's Move", "j": nextCounter}
            currentBoard = Player2s_Board
            currentMainTable = Main_Table2
            resultfunc = result2
        else:
            com_arguments = {"Table": Main_Table1, "moves": moves2, "ships": ships1, "board": Player1s_Board,
                             "j": currentCounter}
            moves_arguments = {"a": "Player2's Move", "j": currentCounter}
            currentBoard = Player1s_Board
            currentMainTable = Main_Table1
            resultfunc = result1

        global control_of_moves, moves
        while True:
            if currentCounter == len(current_player_moves):
                result1(currentCounter)
                result2()

                quit()
            if error_func(current_player_moves[currentCounter]) != True:
                if currentMainTable[int(current_player_moves[currentCounter].split(",")[0])][current_player_moves[currentCounter].split(",")[1]] == "O":
                    saving_outputs_to_file("AssertionError: Invalid Operation\n")
                    current_player_moves.pop(currentCounter)
                    game_for_player(current_player_moves, next_player_moves, currentCounter, nextCounter)
                if currentMainTable[int(current_player_moves[currentCounter].split(",")[0])][current_player_moves[currentCounter].split(",")[1]] == "X":
                    saving_outputs_to_file("AssertionError: Invalid Operation\n")
                    current_player_moves.pop(currentCounter)
                    game_for_player(current_player_moves, next_player_moves, currentCounter, nextCounter)
                moves(**moves_arguments)
                if currentBoard[int(current_player_moves[currentCounter].split(",")[0])][current_player_moves[currentCounter].split(",")[1]] == "":
                    saving_outputs_to_file("Enter your move: {}\n".format(current_player_moves[currentCounter]))
                    currentMainTable[int(current_player_moves[currentCounter].split(",")[0])][current_player_moves[currentCounter].split(",")[1]] = "O"
                else:
                    saving_outputs_to_file("Enter your move: {}\n".format(current_player_moves[currentCounter]))
                    control_of_moves(**com_arguments)

                currentCounter += 1


                game_for_player(next_player_moves, current_player_moves, nextCounter, currentCounter)
            else:
                current_player_moves.pop(currentCounter)
                game_for_player(current_player_moves, next_player_moves, currentCounter, nextCounter)

    game_for_player()


game()











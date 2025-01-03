#Emirhan Utku 2210765029
import sys
input_file=sys.argv[1]
all_inputs=open(input_file,"r")
def inputs_from_txtfile ():
    global inputs,function,contents
    contents= all_inputs.readline().rstrip("\n").split(" ") #We have created a list of each row one by one.
    function = contents[0]
    inputs= contents[1:]
all_outputs = open("output.txt", "w")
def saving_outputs_to_file(x):
    print(x)
    all_outputs.write(x+"\n")
Dict = {}
letters=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
def create_category():
    number_rows_and_clumns = contents[2].split("x")
    if int(number_rows_and_clumns[0])>26:
        saving_outputs_to_file("The number of rows of any category is limited to 26")
    else:
        if contents[1]  in Dict:
            saving_outputs_to_file("Warning: Cannot create the category for the second time. The stadium has already {}." .format(contents[1]))
            return
        else:
            Dict[contents[1]] = {}
            for i in range(int(number_rows_and_clumns[0])):
                rows=letters[i]
                for k in range(int(number_rows_and_clumns[1])):
                    clumns= str(k)
                    Dict[contents[1]][rows+clumns]="X"
            saving_outputs_to_file("The category \'{}\' having {} seats has been created" .format(contents[1],int(number_rows_and_clumns[0])*int(number_rows_and_clumns[1])))
def sell_ticket():
    seat_numbers=(contents[4:])
    for k in range (len(seat_numbers)):
        if "-" in seat_numbers[k]:
            middle_line_index= seat_numbers[k].index("-")
            first_seat= seat_numbers[k][1:middle_line_index]
            last_seat=seat_numbers[k][middle_line_index+1:]
            for v in range(int(first_seat), int(last_seat) + 1):
                continue
            a=list(Dict[contents[3]].keys())
            if letters.index(a[-1][0]) < letters.index(seat_numbers[k][0]) and (v) > int(a[-1][1:]):
                saving_outputs_to_file("Error: The category \'{}\' has less row and column than the specified index {}!".format(contents[3],seat_numbers[k]))
            elif letters.index(a[-1][0]) < letters.index(seat_numbers[k][0]):
                saving_outputs_to_file("Error: The category \'{}\' has less row  than the specified index {}!".format(contents[3],seat_numbers[k]))
            elif v > int(a[-1][1:]):
                saving_outputs_to_file("Error: The category \'{}\' has less column  than the specified index {}!".format(contents[3],seat_numbers[k]))
            else:
                if any(Dict[contents[3]][seat_numbers[k][0] + str(v)] !="X" for v in range(int(first_seat), int(last_seat) + 1)):
                    saving_outputs_to_file("Warning: The seats {} cannot be sold to {} due some of them have already been sold".format(seat_numbers[k],contents[1]))
                else:
                    for j in range(int(first_seat),int(last_seat)+1):
                        if contents[2][0]=="f":
                            Dict[contents[3]][seat_numbers[k][0] + str(j)] = "F"
                        elif contents[2][0:2]=="st":
                            Dict[contents[3]][seat_numbers[k][0] + str(j)] = "S"
                        else:
                            Dict[contents[3]][seat_numbers[k][0] + str(j)] = "T"
                    saving_outputs_to_file("Success: {} has bought {} at {}".format(contents[1],seat_numbers[k],contents[3]))
        else:
            a = list(Dict[contents[3]].keys())
            if letters.index(a[-1][0])<letters.index(seat_numbers[k][0]) and int(seat_numbers[k][1:])> int(a[-1][1:]):
                saving_outputs_to_file("Error: The category \'{}\' has less row and column than the specified index {}!".format(contents[3], seat_numbers[k]))
            elif letters.index(a[-1][0])<letters.index(seat_numbers[k][0]):
                saving_outputs_to_file("Error: The category \'{}\' has less row  than the specified index {}!".format(contents[3],seat_numbers[k]))
            elif int(seat_numbers[k][1:])> int(a[-1][1:]):
                saving_outputs_to_file("Error: The category \'{}\' has less column  than the specified index {}!".format(contents[3],seat_numbers[k]))
            else:
                if Dict[contents[3]][seat_numbers[k]] !="X":
                    saving_outputs_to_file("Warning: The seat {} cannot be sold to {} since it was already sold".format(seat_numbers[k],contents[1]))
                    return
                else:
                    if contents[2][0]=="f":
                        Dict[contents[3]][seat_numbers[k]] = "F"
                    elif contents[2][0:2]=="st":
                        Dict[contents[3]][seat_numbers[k]] = "S"
                    else:
                        Dict[contents[3]][seat_numbers[k]] = "T"
                    saving_outputs_to_file("Success: {} has bought {} at {}" .format(contents[1],seat_numbers[k],contents[3]))
def cancel_ticket():
    seat_numbers = (contents[2:])
    for k in range(len(seat_numbers)):
        a = list(Dict[contents[1]].keys()) #the keys of the desired category
        if letters.index(a[-1][0]) < letters.index(seat_numbers[k][0]) and int(seat_numbers[k][1:]) > int(a[-1][1:]):
            saving_outputs_to_file("Error: The category \'{}\' has less row and column than the specified index {}!".format(contents[1],seat_numbers[k]))
        elif letters.index(a[-1][0]) < letters.index(seat_numbers[k][0]):
            saving_outputs_to_file("Error: The category \'{}\' has less row  than the specified index {}!".format(contents[1],seat_numbers[k]))
        elif int(seat_numbers[k][1:]) > int(a[-1][1:]):
            saving_outputs_to_file("Error: The category \'{}\' has less column  than the specified index {}!".format(contents[1], seat_numbers[k]))
        else:
                if Dict[contents[1]][seat_numbers[k]] != "X":
                    Dict[contents[1]][seat_numbers[k]] = "X"
                    saving_outputs_to_file("Success: The seat {} at \'{}\' has been canceled and now ready to sell again".format(seat_numbers[k],contents[1]))
                else:
                    saving_outputs_to_file("Error: The seat {} at \'{}\' has already been free! Nothing to cancel".format(seat_numbers[k],contents[1]))
def balance():
    d={ "S":0 , "F":0 , "T":0}
    for v in Dict[contents[1]].values():
        if v !="X":
            if d[v]==0: d[v]=1
            else: d[v]+=1
        else:
            continue
    saving_outputs_to_file("category report of \'{}\'\n--------------------------------".format(contents[1]))
    for i in range(len(list(d.keys()))):
        if list(d.keys())[i]=="S":
            money_earned_from_totalstudents= int(list(d.values())[i])*10
            print("Sum of students=",list(d.values())[i],end = ', ')
            all_outputs.write("Sum of students="+ str(list(d.values())[i]) + ", ")
        elif list(d.keys())[i] == "F":
            money_earned_from_totalfullpay = int(list(d.values())[i]) * 20
            print("Sum of full pay=", list(d.values())[i],end = ', ')
            all_outputs.write("Sum of full pay=" + str(list(d.values())[i]) + ", ")
        else:
            money_earned_from_total_season = int(list(d.values())[i]) * 250
            print("Sum of season ticket", list(d.values())[i],end = ', ')
            all_outputs.write("Sum of season ticket=" + str(list(d.values())[i]) + ", ")
    saving_outputs_to_file("and Revenues = {} Dollars".format(money_earned_from_totalstudents+money_earned_from_totalfullpay+money_earned_from_total_season))
def show_category():
    a = list(Dict[contents[1]].keys()) #the keys of the desired category
    c= list(Dict[contents[1]].values()) #the values of the desired category
    b=letters.index(a[-1][0]) # index of row
    d=a[-1][1:] #index of column
    saving_outputs_to_file("Printing category layout of {}".format(contents[1]))
    saving_outputs_to_file("")
    for k in range(b+1):
        print(letters[int(b) - k],end=" ")
        all_outputs.write(letters[int(b) - k]+ " ")
        for i in range(int(d)+1):
            print(Dict[contents[1]][letters[int(b)-k]+str(i)],end="  ")
            all_outputs.write(Dict[contents[1]][letters[int(b)-k]+str(i)]+"  ")
        saving_outputs_to_file("")
    print("  ",end="")
    all_outputs.write("  ")
    for h in range(int(d)+1):
        if h<9:
            print(h,end="  ")
            all_outputs.write(str(h)+ "  ")
        else:
            print(h, end=" ")
            all_outputs.write(str(h)+" ")
    saving_outputs_to_file("")
length_of_input_txt=len(open(input_file, "r").readlines())
for i in range(length_of_input_txt):
    inputs_from_txtfile()
    if function=="CREATECATEGORY":
        create_category()
    if function=="SELLTICKET":
        sell_ticket()
    if function=="CANCELTICKET":
        cancel_ticket()
    if function=="BALANCE":
        balance()
    if function=="SHOWCATEGORY":
        show_category()
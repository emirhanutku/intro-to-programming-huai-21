
#Emirhan Utku 2210765029
all_inputs=open('doctors_aid_inputs.txt', "r")


all_outputs = ""

def inputs_from_txtfile ():
    global inputs,function
    contents = all_inputs.readline().rstrip("\n").split(", ") #We have created a list of each row one by one.
    if contents[0]=="list":   #I added this because it takes the function part as a space in single word commands
        function="list"
    else:
        function = contents[0].split()[0]
        inputs=[contents[0].split()[1]]
        inputs_without_name= contents [1:]
        inputs.extend(inputs_without_name)

def saving_outputs_to_file():
    global all_outputs
    all_outputs = open("doctors_aid_outputs.txt", "w")

data_list = []
def create():
    if inputs not in data_list:
        data_list.append(inputs)
        all_outputs.write("Patient {} is recorded.\n".format(inputs[0]))

    else:
        all_outputs.write("Patient {} cannot be recorded due to duplication.\n" .format(inputs[0]))

def remove():
    x = []      #i did it to find the element inside the list inside the list

    for y in data_list:
        x.extend(y)

    if inputs[0]  in x:
        index_of_inputs = int((x.index(inputs[0]))/6)    #I divided it into 6 because the names repeat every 6 times in the list.
        data_list.pop(index_of_inputs)
        all_outputs.write("Patient {} is removed.\n".format(inputs[0]))
        return data_list

    else:
        all_outputs.write("Patient {}  cannot be removed due to absence.\n".format(inputs[0]))
        return data_list

def list():
    for each_input in data_list:
        each_input[1] = float(each_input[1]) * 100
        each_input[5] = str(int(float(each_input[5]) * 100)) + "%"


    all_outputs.write("Patient\tDiagnosis\tDisease\t\t\tDisease\t\tTreatment\t\tTreatment\n")
    all_outputs.write("Name\tAccuracy\tName\t\t\tIncidence\tName\t\t\tRisk\n")
    all_outputs.write("-------------------------------------------------------------------------\n")

    for a in data_list:
        if a[0] =="Hayriye":
            all_outputs.write(a[0]+"\t"+str("%.2f" %a[1])+"%"+"\t\t"+a[2]+"\t"+a[3]+"\t"+a[4]+"\t\t\t"+a[5]+"\n")
        elif a[0]=="Deniz":
            all_outputs.write(a[0]+"\t"+str("%.2f" %a[1])+"%"+"\t\t"+a[2]+"\t\t"+a[3]+"\t"+a[4]+"\t"+a[5]+"\n")

        elif a[0] == "AteÅŸ":
            all_outputs.write(a[0] + "\t" + str("%.2f" %a[1])+"%" + "\t\t" + a[2] + "\t" + a[3] + "\t" + a[4] + "\t" + a[5]+"\n")
        elif a[0] == "Toprak":
            all_outputs.write(a[0] + "\t" + str("%.2f" %a[1])+"%"+ "\t\t" + a[2] + "\t" + a[3] + "\t" + a[4] + "\t" + a[5]+"\n")
        elif a[0] == "Hypatia":
            all_outputs.write(a[0] + "\t" + str("%.2f" %a[1])+"%" + "\t\t" + a[2] + "\t" + a[3] + "\t" + a[4] + "\t" + a[5]+"\n")
        elif a[0] == "Su":
            all_outputs.write(a[0] + "\t\t" + str("%.2f" %a[1]) +"%"+ "\t\t" + a[2] + "\t" + a[3] + "\t" + a[4] + "\t" + a[5]+"\n")
        else:
            all_outputs.write(a[0] + "\t" + str("%.2f" %a[1])+"%" + "\t\t" + a[2] + "\t" + a[3] + "\t" + a[4] + "" + a[5]+"\n")

    for each_input in data_list:

        each_input[1]= each_input[1] /100
        each_input[5] = float(each_input[5][:-1]) /100


def probability():
    all_lists_inonelist = []

    for y in data_list:
        all_lists_inonelist.extend(y)

    if inputs[0] in all_lists_inonelist:
        index_of_name = int((all_lists_inonelist.index(inputs[0])) / 6)

    if inputs[0] in all_lists_inonelist:
        Disease_Incidence=[]
        for i in data_list[index_of_name][3]:
            Disease_Incidence.append(i)
        index_of_slash=Disease_Incidence.index("/") #We found the index of the slash because before and after the slash is important
        k = 1.0 - float(data_list[index_of_name][1])
        l = float(data_list[index_of_name][3][index_of_slash + 1:]) - float(
            data_list[index_of_name][3][0:index_of_slash])
        m = (k * l)
        denominator = m + float(data_list[index_of_name][3][0:index_of_slash])
        result = float(data_list[index_of_name][3][0:index_of_slash]) * float(data_list[index_of_name][1]) / denominator
        result= round(result*100,2)

    if inputs[0] in all_lists_inonelist:
        if int(result)==float(result):
            all_outputs.write("Patient {} has a probability of {} of having {}.\n".format(inputs[0],str(int(result)) + "%", (str(data_list[index_of_name][2])).lower()))
        else:
            all_outputs.write("Patient {} has a probability of {} of having {}.\n".format(inputs[0],str(result) + "%",(str(data_list[index_of_name][2])).lower()))
    else:
        all_outputs.write("Probability for {} cannot be calculated due to absence.\n".format(inputs[0]))

def recommendation():
    all_lists_inonelist = []

    for y in data_list:
        all_lists_inonelist.extend(y)

    if inputs[0] in all_lists_inonelist:
        index_of_name = int((all_lists_inonelist.index(inputs[0])) / 6)

    if inputs[0] in all_lists_inonelist:
        a = []
        for i in data_list[index_of_name][3]:
            a.append(i)
        index_of_slash = a.index("/")
        k = 1.0 - float(data_list[index_of_name][1])
        l = float(data_list[index_of_name][3][index_of_slash + 1:]) - float(
            data_list[index_of_name][3][0:index_of_slash])
        m = (k * l)
        denominator = m + float(data_list[index_of_name][3][0:index_of_slash])
        result = float(data_list[index_of_name][3][0:index_of_slash]) * float(data_list[index_of_name][1]) / denominator


    if inputs[0] in all_lists_inonelist:
        if result> float(data_list[index_of_name][5]):
            all_outputs.write("System suggests {} to have the treatment.\n".format(inputs[0]))
        else:
            all_outputs.write("System suggests {} NOT to have the treatment.\n".format(inputs[0]))
    else:
        all_outputs.write("Recommendation for {} cannot be calculated due to absence.\n".format(inputs[0]))


saving_outputs_to_file()
length_of_input_txt=len(open('doctors_aid_inputs.txt', "r").readlines())
for i in range(length_of_input_txt):
    inputs_from_txtfile()

    if function=="create":
        create()
    if function=="remove":
        remove()
    if function=="list":
        list()
    if function=="probability":
        probability()
    if function=="recommendation":
        recommendation()
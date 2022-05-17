#groupwork2

print ("Hey, give me six numbers!") #Abfrage nach Zahlen, reine Textabfrage
no_1 = int(input()) # Sechs Zahlen werden nacheinander abgefragt und über input als variablen abgelegt
no_2 = int(input())
no_3 = int(input())
no_4 = int(input())
no_5 = int(input())
no_6 = int(input())
print ("What operation do you want me to run?") # Textabfrage, welche Operation durchgeführt werden soll
op = int(input (" Press 1 for addition, press 2 for subtraction, press 3 for multiplication, press 4 for division:"))
if op == 1:
# Ergebnisse der Abfrage werden in op abgelegt
    input_01 = int(input(f"Which numbers do you choose? {no_1} + {no_2} = ? Press 1, {no_3} + {no_4} = ? Press 2, {no_5} + {no_6} = ? Press 3"))
    if input_01 == 1:
        print (f"{no_1} + {no_2} = {(no_1)+(no_2)}")
    if input_01 == 2:
        print (f"{no_3} + {no_4} = {(no_3)+(no_4)}")
    if input_01 == 3:
        print (f"{no_5} + {no_6} = {(no_5)+(no_6)}")
    if input_01 > 3:
        print ("This is none of the available choices! Please start again.")

elif op == 2:
    input_02 = int(input(f"Which numbers do you choose? {no_1} - {no_2} = ? Press 1, {no_3} - {no_4} = ? Press 2, {no_5} - {no_6} = ? Press 3"))
    if input_02 == 1:
        print (f"{no_1} - {no_2} = {(no_1)-(no_2)}")
    if input_02 == 2:
        print (f"{no_3} - {no_4} = {(no_3)-(no_4)}")
    if input_02 == 3:
        print (f"{no_5} - {no_6} = {(no_5)-(no_6)}")
    if input_02 > 3:
        print ("This is none of the available choices! Please start again.")

elif op == 3:
    input_03 = int(input(f"Which numbers do you choose? {no_1} * {no_2} = ? Press 1, {no_3} * {no_4} = ? Press 2, {no_5} * {no_6} = ? Press 3"))
    if input_03 == 1:
        print (f"{no_1} * {no_2} = {(no_1)*(no_2)}")
    if input_03 == 2:
        print (f"{no_3} * {no_4} = {(no_3)*(no_4)}")
    if input_03 == 3:
        print (f"{no_5} * {no_6} = {(no_5)*(no_6)}")
    if input_03 > 3:
        print ("This is none of the available choices! Please start again.")

elif op == 4:
    input_04 = int(input(f"Which numbers do you choose? {no_1} / {no_2} = ? Press 1, {no_3} / {no_4} = ? Press 2, {no_5} / {no_6} = ? Press 3"))
    if input_04 == 1:
        print (f"{no_1} / {no_2} = {(no_1)/(no_2)}")
    if input_04 == 2:
        print (f"{no_2} / {no_3} = {(no_2)/(no_3)}")
    if input_04 == 3:
        print (f"{no_5} / {no_6} = {(no_5)/(no_6)}")
    if input_04 > 3:
        print ("This is none of the available choices! Please start again.")

else:
    print("This is none of the available choices! Please start again.")

#groupwork2

print ("Hey, give me six numbers!")
no_1 = int(input())
no_2 = int(input())
no_3 = int(input())
no_4 = int(input())
no_5 = int(input())
no_6 = int(input())
print ("What operation do you want me to run?")
op = int(input (" Press 1 for addition, press 2 for subtraction, press 3 for multiplication, press 4 for division:"))
if op == 1:
    print (f"{no_1} + {no_2} = {(no_1)+(no_2)}")
    print (f"{no_3} + {no_4} = {(no_3)+(no_4)}")
    print (f"{no_5} + {no_6} = {(no_5)+(no_6)}")

elif op == 2:
    print (f"{no_1} - {no_2} = {(no_1)-(no_2)}")
    print (f"{no_3} - {no_4} = {(no_3)-(no_4)}")
    print (f"{no_5} - {no_6} = {(no_5)-(no_6)}")

elif op == 3:
    print (f"{no_1} * {no_2} = {(no_1)*(no_2)}")
    print (f"{no_3} * {no_4} = {(no_3)*(no_4)}")
    print (f"{no_5} * {no_6} = {(no_5)*(no_6)}")

elif op == 4:
    print (f"{no_1} / {no_2} = {(no_1)/(no_2)}")
    print (f"{no_2} / {no_3} = {(no_2)/(no_3)}")
    print (f"{no_5} / {no_6} = {(no_5)/(no_6)}")

else:
    print("This is none of the available choices! Please start again.")

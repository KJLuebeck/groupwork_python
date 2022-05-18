#Group exercise 03 - Manipulating lists
#create three different list with userchoice:
userchoice_1 = int(input("What type of list do you want to create?\nType 1 for giving only the length.\nType 2 for giving starting and endpoint of the list.\nType 3 for giving of starting-,endpoint and step size."))

if userchoice_1 == 1:
    no_1 = int(input("Give me the length of the list."))
    list_1 = list(range(no_1))
    length_1 = len(list_1)
    print (f"This ist list 1:{list_1} with a lenght of {length_1}")
    userchoice_2 = int(input("What do you want to do with the list?\n Add (1)\nRemove(2)\nReverse(3)\nSearch for index of entry(4)\nSearch for specific entry(5)"))
    if userchoice_2 == 1:
        element_1 = int(input("Give me the element you want to add to the list."))
        list_1.append(element_1)
        print (f"This is the new list 1:{list_1}")

    if userchoice_2 == 2:
        element_1 = int(input("Give me the element you want to remove from the list."))
        list_1.remove(element_1)
        print (f"This is the new list 1:{list_1}")

    if userchoice_2 == 3:
        list_1.reverse()
        print (f"List 1 has bin reversed:{(list_1)}")

    if userchoice_2 == 4:
        element_1 = int(input("Give me the element you want to be searched for."))
        if list_1.index(element_1) == element_1:
            print (f"The element is in the list at index {list_1.index(element_1)}.")
        else:
            print ("The element is not in the list.")

    if userchoice_2 == 5:
        element_1 = int(input("Give me the element you want to be searched for."))
        if element_1 in list_1:
            print ("The element is in the list.")
        else:
            print ("The element is not in the list.")

elif userchoice_1 == 2:
    no_2 = int(input("Give me the starting and the endpoint of the list.)\n"))
    no_3 = int(input())
    list_2 = list(range(no_2,no_3))
    length_2 = len(list_2)
    print (f"This ist list 2:{list_2} with a lenght of {length_2}.")

    userchoice_2 = int(input("What do you want to do with the list?\n Add (1)\nRemove(2)\nReverse(3)\nSearch for index of entry(4)\nSearch for specific entry(5)"))
    if userchoice_2 == 1:
        element_1 = int(input("Give me the element you want to add to the list."))
        list_2.append(element_1)
        print (f"This is the new list 2:{list_2}")

    if userchoice_2 == 2:
        element_1 = int(input("Give me the element you want to remove from the list."))
        list_2.remove(element_1)
        print (f"This is the new list 2:{list_2}")

    if userchoice_2 == 3:
        list_2.reverse()
        print (f"List 2 has bin reversed:{(list_2)}")

    if userchoice_2 == 4:
        element_1 = int(input("Give me the element you want to be searched for."))
        if list_2.index(element_1) == element_1:
            print (f"The element is in the list at index {list_2.index(element_1)}.")
        else:
            print ("The element is not in the list.")

    if userchoice_2 == 5:
        element_1 = int(input("Give me the element you want to be searched for."))
        
    if element_1 in list_2:
        print ("The element is in the list.")
    else:
        print ("The element is not in the list.")

elif userchoice_1 == 3:
    no_4 = int(input("Give me the starting, the endpoint and the step size of the list.)\n"))
    no_5 = int(input())
    no_6 = int(input())
    list_3 = list(range(no_4,no_5,no_6))
    length_3 = len(list_3)
    print (f"This ist list 3:{list_3} with a lenght of {length_3}")

    userchoice_2 = int(input("What do you want to do with the list?\n Add (1)\nRemove(2)\nReverse(3)\nSearch for index of entry(4)\nSearch for specific entry(5)"))
    if userchoice_2 == 1:
        element_1 = int(input("Give me the element you want to add to the list."))
        list_3.append(element_1)
        print (f"This is the new list 3:{list_3}")

    if userchoice_2 == 2:
        element_1 = int(input("Give me the element you want to remove from the list."))
        list_3.remove(element_1)
        print (f"This is the new list 3:{list_3}")

    if userchoice_2 == 3:
        list_3.reverse()
        print (f"List 3 has bin reversed:{(list_3)}")

    if userchoice_2 == 4:
        element_1 = int(input("Give me the element you want to be searched for."))
        if list_3.index(element_1) == element_1:
            print (f"The element is in the list at index {list_3.index(element_1)}.")
        else:
            print ("The element is not in the list.")

    if userchoice_2 == 5:
        element_1 = int(input("Give me the element you want to be searched for."))
        if element_1 in list_3:
            print ("The element is in the list.")
        else:
            print ("The element is not in the list.")

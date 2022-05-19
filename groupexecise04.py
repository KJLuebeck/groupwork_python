#group exercise 04
#

list_1=["Bernd", "Brigitte"]
list_2=["Dieter", "Gertrud"]
list_3=["Bernd", "Werauchimmer"]
list_4=["Fred", "Unbekannt"]
list_5=["Frau", "Herr"]
proteindictionary = {}
proteindictionary["Ferritin"] = {"Name":"Ferritin","Länge":"174/182 Aminosäuren (L/H)","Funktion":"Eisenspeicher","Location":"Leber, Milz, Knochenmark","Jahr der Entdeckung": 1950, "Publikationen":list_1}
proteindictionary["Bakterioferritin"] = {"Name":"Bakterioferritin","Länge":"lang","Funktion":"Eisenspeicher/unklar","Location":"Bakterien","Jahr der Entdeckung": 1980, "Publikationen":list_2}
proteindictionary["Myoglobin"] = {"Name":"Myoglobin","Länge":"153 Aminosäuren","Funktion":"Sauerstofftransport","Location":"Muskel","Jahr der Entdeckung": 1990, "Publikationen":list_3}
proteindictionary["Kollagen"] = {"Name":"Kollagen","Länge":"200-1000 Aminosäuren","Funktion":"Strukturprotein","Location":"Bindegewebe","Jahr der Entdeckung": 1955, "Publikationen":list_4}
proteindictionary["Hämoglobin"] = {"Name":"Hämoglobin","Länge":"141/146 Aminosäuren","Funktion":"Sauerstofftransport","Location":"Blut","Jahr der Entdeckung": 1950, "Publikationen":list_5}
print (proteindictionary)

no_1 = int(input("Do you want to add an entry (press 1), delete an entry (press 2) change an entry (press 3) or display an entry (press 4)?\n"))

#add entry
if no_1 == 1:
    print ("Please give me some information about the protein you like to add.")
    key = input("Whats the name of the protein?")
    länge = input("Welche Länge hat dein Protein?")
    funktion = input ("Welche Funktion hat dein Protein?")
    location = input ("Wo befindet sich das Protein(Location)?")
    year = int(input("Wann wurde dein Protein entdeckt?"))
    print ("Name von zwei Publikationen/Autoren")
    name_1 = input()
    name_2 = input()
    list_1 = [name_1,name_2]
    proteindictionary[key] = {"Name":key,"Länge":länge,"Funktion":funktion,"Location":location,"Jahr der Entdeckung":year,"Publikationen" :list_1}
    print (proteindictionary)

#delete entry
if no_1 == 2:
    name_1 = input("Give me the name of the entry you want to delete:\n")
    del proteindictionary[name_1]
    print (proteindictionary)

#change entry
if no_1 == 3:
    name_1 = input("Give me the name of the entry you want to change:\n")
    print ("Which part do you want to change?")
    no_2 = int(input("1: Name 2: Länge 3: Funktion 4: Location 5: Year 6: Publikationen"))
    if no_2 == 1:
        name_2 = input("Give me the new name for your protein\n")
        proteindictionary[name_1]["Name"] = name_1
        print(proteindictionary)
    if no_2 == 2:
        länge_2 = input("Give me the new length for your protein\n")
        proteindictionary[name_1]["Länge"] = länge_2
        print(proteindictionary)
    if no_2 == 3:
        funktion_2 = input("Give me the new function for your protein\n")
        proteindictionary[name_1]["Funktion"] = funktion_2
        print(proteindictionary)
    if no_2 == 4:
        location_2 = input("Give me the new location for your protein\n")
        proteindictionary[name_1]["Location"] = location_2
        print(proteindictionary)
    if no_2 == 5:
        year_2 =int(input("Give me the new year\n"))
        proteindictionary[name_1]["Jahr der Entdeckung"] = year_2
        print(proteindictionary)
    if no_2 == 6:
        name_3 = input("Sag zwei neue Publikationen\n")
        name_4 = input()
        list_1 = [name_3,name_4]
        proteindictionary[name_1]["Publikationen"] = list_1
        print(proteindictionary)
# proteindictionary[name_1].update({"Funktion":funktion2}) alternative Schreibweise
# display an entry
if no_1 == 4:
    display = input("Which entry should be displayed for you?")
    print(proteindictionary[display])

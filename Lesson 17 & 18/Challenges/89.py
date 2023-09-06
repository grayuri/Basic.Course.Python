students = [[],[],[],[]]

counter = 0
finishRegister = False

while not finishRegister:
    students[0].append(counter)
    counter += 1

    name = input("What's the name of the student: ")
    students[1].append(name)

    notes = []
    quantityOfNotes = 2
    totalOfNotes = 0
    
    for i in range(0, quantityOfNotes):
        note = float(input(f"Note {i + 1}: "))
        totalOfNotes += note
        notes.append(note)
    students[2].append(notes)

    media = totalOfNotes / quantityOfNotes
    students[3].append(media)

    choice = input("Do you want begin? [Y]es or [N]ot: ").lower()
    
    if choice == "n":
        finishRegister = True
    else: 
        finishRegister = False

finishProgram = False

while not finishProgram:
    idHeader = "ID"
    nameHeader = "Name"
    mediaHeader = "Media"

    studentsId = students[0]
    studentsName = students[1]
    studentsNotes = students[2]
    studentsMedia = students[3]

    print(f"{idHeader:<5}", end="")
    print(f"{nameHeader:<10}", end="")
    print(f"{mediaHeader:^5}")
    print("="*20)

    for i in range(0, len(students[0])):
        print(f"{studentsId[i]:<5}", end="")
        print(f"{studentsName[i]:<10}", end="")
        print(f"{studentsMedia[i]:^5}")

    whatWantToSee = int(input("The notes of wich student do you want to see? "))

    print(f"Notes of {studentsName[whatWantToSee]}: {studentsNotes[whatWantToSee]}")

    choice = input("Do you want begin? [Y]es or [N]ot: ").lower()
    
    if choice == "n":
        finishProgram = True
    else: 
        finishProgram = False
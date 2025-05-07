from student import Student

def getStudents():
    students = {}
    file = open("1300 - MP6 Data.txt", "r")
    for line in file:
        items = line.strip().split()
        if len(items) >= 3:
            stuID = items.pop(0)
            firstName = items.pop(0)
            lastName = items.pop(0)
            s = Student(stuID)
            s.setName(firstName, lastName)
            for score in items:
                s.addTest(int(score))
            students[stuID] = s
    file.close()
    return students

def printStudents(roster):
    print("Students in roster:\n")
    for student in roster.values():
        print(student)
        print()

def updateName(roster, stuID):
    firstName = input("First Name: ")
    lastName = input("Last Name: ")
    roster[stuID].setName(firstName, lastName)

def updateTests(roster, stuID):
    score = input("Enter a Test Score (<enter> to stop): ")
    while score != "":
        roster[stuID].addTest(int(score))
        score = input("Enter a Test Score (<enter> to stop): ")

roster = getStudents()
printStudents(roster)

print("You may update any student info, or add a student.\n")

stuID = input("Enter Student ID (<enter> to stop): ")

while stuID != "":
    if stuID in roster:
        print(roster[stuID])
        print("\n(1) Change the Name")
        print("(2) Add a Test")
        choice = input("\nWhat would you like to do? ")
        if choice == "1":
            updateName(roster, stuID)
        elif choice == "2":
            updateTests(roster, stuID)
        else:
            print("Invalid choice.")
        print("\n" + str(roster[stuID]))
    else:
        print("This student does not exist. You may enter the info now.")
        firstName = input("First Name: ")
        lastName = input("Last Name: ")
        newStudent = Student(stuID)
        newStudent.setName(firstName, lastName)
        score = input("Enter a Test Score (<enter> to stop): ")
        while score != "":
            newStudent.addTest(int(score))  
            score = input("Enter a Test Score (<enter> to stop): ")
        roster[stuID] = newStudent
        print("\nNew Student Added:")
        print(newStudent)
        print()
    
    stuID = input("Enter Student ID (<enter> to stop): ")

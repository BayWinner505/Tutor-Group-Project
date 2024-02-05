import csv
import time
import sys
username = input("Enter username: ")
password = input("Enter password: ")
if password != "Password1." or username != "MrM123":
  print("Access Denied")
  sys.exit()
else:
    print("Access Granted")
    time.sleep(.5)
    fieldnames = ['unique ID number', 'surname', 'forename', 'date of birth', 'home address', 'home phone number', 'gender', 'tutor group']
    print("Welcome to Administration!\nPlease choose an option from the list below.\nEnter the number that corresponds with the command you would like to choose.")
    time.sleep(.5)
    print("1. Enter student details\n2. Retrieve student details\n3. Create student report\n4. Logout\n5.Delete student data")
    time.sleep(.5)
    option = input("Enter option: ")
    if option == "1":
        filename = 'students.csv'
        while True:
            data = {
                'unique ID number': input("Enter ID number: "),
                'surname': input("Enter surname: "),
                'forename': input("Enter forename: "),
                'date of birth': input("Enter date of birth: "),
                'home address': input("Enter home address: "),
                'home phone number': input("Enter home phone number: "),
                'gender': input("Enter gender: "),
                'tutor group': input("Enter tutor group: ")
            }
            with open(filename, 'a', newline='') as csvfile:
                fieldnames = ['unique ID number', 'surname', 'forename', 'date of birth', 'home address', 'home phone number', 'gender', 'tutor group']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow(data)
            if input("Do you want to add another student? (yes/no): ") != "yes":
                break

    elif option == "2":
        id_number = input("Enter unique ID number: ")
        with open("students.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["unique ID number"] == id_number:
                    print("Student Details:")
                    for key, value in row.items():
                        print(f"{key}: {value}")
                    break
            else:
                print("Student not found")

    elif option == "3":
        with open("students.csv", "r") as file:
            reader = csv.DictReader(file)
            print("Student Report:")
            for row in reader:
              print(reader.fieldnames)

    elif option == "4":
        print("Logged out")
    elif option == "5":
      id_number = input("Enter unique ID number of the student to be deleted: ")
      with open("students.csv", "r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
      with open("students.csv", "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        for row in rows:
          if row["unique ID number"] != id_number:
            writer.writerow(row)
            print("Student data deleted if found")

    else:
        print("Invalid Option")
  
  
  
  
  

import re
import csv

def email_validator():
    emails = []
    while True:
        USER = input("Enter You email adress :\n")
        pattren = r"^[a-zA-Z0-9-.~+_]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        # ^ --> start 

        # [a-zA-Z0-9-.~+_]---->Matches one or more occurrences of letters, numbers, underscores, periods, plus signs, 
        # or hyphens (this matches the part before @

        # @ --> matches the symbole @
        # [a-zA-Z0-9-] ----> matches after @
        # \. --->  Matches the dot (.) separating the domain and top-level domain.

        # [a-zA-Z0-9-.]+ ---->  Matches the top-level domain (like .com, .org, etc.).
        # $ indicate that its  end

        if re.match(pattren,USER):
            response = input("Do you want to add it-yes-quit-view \n")
            if response=="YES".strip().lower():
                emails.append(USER)
                print("Added sucessfully !")

                # Save email to txt file
                with open("emails.txt", "a") as file:
                    file.write(USER + "\n")

            elif response == "view":
                print("Here is the list of emails:")
                
                # Read emails from the txt file
                try:
                    with open("emails.txt", "r") as file:
                        emails = file.readlines()
                    for idx, email in enumerate(emails, 1):
                        print(f"{idx}. {email.strip()}")
                except FileNotFoundError:
                    print("No emails have been added yet.")

            elif response==response=="QUIT".strip().lower():
                break
            
        else:
            print("Please enter email in valid pattren ")

email_validator()

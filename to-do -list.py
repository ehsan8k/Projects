
def toDoList():
    list2 = []
    
    while True:
        user_Input = input("Enter command (add/remove/view/quit): ").strip().lower()
        
        if user_Input == 'add':
            item = input("Enter item to add: ")
            list2.append(item)
            print(f"'{item}' added to the list.")
        
        elif user_Input == 'remove':
            list2.clear()
            print("List cleared.")
        
        elif user_Input == 'view':
            if not list2:
                print("The list is empty.")
            else:
                print("Current list:")
                for item in list2:
                    print(item)
#
        
        elif user_Input == 'quit':
            print("Thanks for using the to-do list!")
            break
        
        else:
            print("Invalid command. Please try again.")

toDoList()

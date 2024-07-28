from p import nameFinder


ollist=[]
def namefinder():
    global ollist
    alphabetes ={
    'a1' : ['a','b','c','d'],
    'b2' : ['e','f','g','h'],
    'c3':['i', 'j', 'k', 'l'],
    'e4' :['m', 'n', 'o', 'p'],
    'f5':['q', 'r', 's', 't'],
    'g6':['u', 'v', 'w', 'x'],
    'h7':['', 'y', 'z', '']
    }
    for key , value in alphabetes.items():
        print(value)
    alphabetes1 ={
    'a' : ['a','e','m','q','u'],
    'b' : ['b','f','j','n','r','v','y'],
    'c':['c', 'g', 'k', 'o','s','w','z'],
    'e' :['d', 'h', 'l', 'p','t','x'],
    }
    UserInput = input('Please select coloum by etc(a or b)').lower()
    # Initialize a list to collect selected letters
    selected_letters = [[] for _ in range(len(alphabetes))]

    # Prompt user for column input
    for _ in range(4):  # Assuming we want to collect 4 column inputs
            try:
                user_input = int(input('Enter your column (1-4): '))
                if user_input < 1 or user_input > 4:
                    print("Please enter a valid number between 1 and 4.")
                    continue
            
            # Append the corresponding letters for the chosen column
                for row in alphabetes:
                    if user_input - 1 < len(row):
                        selected_letters[alphabetes1.index(row)].append(row[user_input - 1])
        
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    # Update the global list with the selected_letters structure
    ollist[:] = selected_letters

    # Print the collected letters in list format
    print("Collected letters:")
    for i in range(len(alphabetes1)):
        print(selected_letters[i])
        # Call the function
nameFinder()

# Print the final collected list
print("Final list of collected letters:")
print(ollist)

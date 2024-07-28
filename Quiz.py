def QuizGame():
    score = 0
    
    while True:
        print('Who created the whole universe?')
        print(" 1- Allah\n 2- Bhagwan\n 3- Krishna\n")
        user = input('Enter your choice (e.g., 1) or type "quit" to exit: ')
        
        if user == "1":
            print("TRUE")
            score += 1  # Increase score if the answer is correct
        else:
            print("FALSE")
        
        print('Who is the first man in the world?')
        print(" 1- Adam\n 2- Krishna\n 3- Semon\n")
        user = input('Enter your choice (e.g., 1) or type "quit" to exit: ')
        
        if user == '1':
            print('TRUE')
            score += 1  # Increase score if the answer is correct
        else:
            print('FALSE')
        
        # Check if the user wants to quit
        user_choice = input('Enter "quit" to exit or any key to continue: ')
        if user_choice.lower() == 'quit':
            print(f'Thank you for playing! Your final score is: {score}')
            break
        
        # Display current score
        print(f'Your current score: {score}\n')

QuizGame()

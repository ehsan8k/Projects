def SimpleCalculator():
    while True:
        UserInput1=int(input(" Enter the num 1 : "))
        UserInput2=int(input(" Enter the num 2 : "))
        list=['add','multiply','subtrate','divide']
        for i in list:
            print(i)
        arthimatic=input(" please select one of the following command : ").strip().lower()
        if arthimatic == 'add':
            add = UserInput1+UserInput2
            print( 'The addition of '+ str(UserInput1) + ' and ' +' '+ str(UserInput2) + ' is ' +' '+ str(add))
        elif arthimatic == 'multiply':
            multiply = UserInput1*UserInput2
            print('The Multiplication of '+ str(UserInput1) + ' and '+' ' + str(UserInput2) + ' is '+' ' + str(multiply))
        elif arthimatic == 'subtrate':
            subtrate = UserInput1-UserInput2
            print('The subtraction of '+ str(UserInput1) + ' and '+' ' + str(UserInput2) + ' is '+' ' + str(subtrate))        
        elif arthimatic == 'divide':
            divide = UserInput1 / UserInput2
            if UserInput2 !=2:
                divide = UserInput1/UserInput2
                print('The division  of '+ str(UserInput1) + ' and '+ ' ' + str(UserInput2) + 'is' +' '+ str(divide))  
            else:
                print('Division error')
        elif arthimatic == 'quit':
            print("Thanks")
            break
        else:
            print('Try again please')
SimpleCalculator()
         
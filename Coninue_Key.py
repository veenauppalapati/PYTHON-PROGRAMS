#INITIALIZE THE VARIABLES
#------------------------
Continue_Key = 'Y'
Num_1 = 0
Num_2 = 0
Sum = 0

#ITERATE THROUGH THE STEPS UNTIL THE USER DOES NOT CHOOSE Y
#----------------------------------------------------------
while ( Continue_Key == 'Y' ):
    
    # PROMPT THE USER TO ENTER TWO NUMBERS AND STORE THEM INTO VARIABLES
    Num_1 = int(input("Please enter your first number: "))
    Num_2 = int(input("Please enter your Second number: "))
    print()
    
    # CALCULATE:  ADD THE TWO NUMBERS AND DISPLAY THE SUM
    Sum = Num_1 + Num_2
    print(Num_1, '+', Num_2, '=', Sum)
    print()
    
    # PROMPT THE USER IF THEY WANT TO CONTINUE THE PROGRAM
    Continue_Key = input("Please press y to continue if you would like to continue the program: ")
    
    # CAPITALIZE THE KEY THE USER PRESSED
    Continue_Key = Continue_Key.capitalize()
    print("You pressed:", Continue_Key)
    
    print()
    print("-" * 100)
    print()

#----------------------------------------------------------
    
#DISPLAY THE END MESSAGE
#-----------------------
print("Your program has ended.  T H A N K  Y O U !! ")   
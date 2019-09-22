#INITIALIZE THE VARIABLES
#------------------------
User_Number = 0
Total = 0
#ITERATE THROUGH 10 TIMES
#------------------------
for i in range(0, 10):
    #INPUT
    #------
    #PROMPT USER FOR A NUMBER AND STORE IT INTO THE USER_NUMBER VARIABLE
    User_Number = int(input("Enter a number: "))
    #CALCULATION: ADD THE USER NUMBER TO TOTAL THE NUMBERS ENTERED 
    Total += User_Number
    #OUTPUT
    #------
    #DISPLAY THE TOTAL VALUE
    print(Total)
   
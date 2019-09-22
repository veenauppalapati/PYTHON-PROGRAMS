#INITIALIZE THE VARIABLES
product = 0;
User_Number = 0;

#LOOP UNTIL THE PRODUCT IS LESS THAN 100
while ( product < 100 ):  
    #PROMPT THE USER TO ENTER A NUMBER
    User_Number = int(input("Please enter a number: "))
    #MULTIPLY THE NUMBER ENTERED BY THE USER WITH 10
    #ASSIGN IT TO THE VARIABLE PRODUCT
    product = User_Number * 10

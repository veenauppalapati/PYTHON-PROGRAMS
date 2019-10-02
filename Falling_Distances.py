# F A L L I N G    D I S T A N C E S
# ----------------------------------

# DIVIDER FORMAT
#---------------
Console_Divider = format('-' * 120)
Center_The_Table = format(' ' * 36)
Table_Row_Divider = format('-' * 19)
Heading_Dash = '-' * 50
Title_Divider = '-' * 75



#-------------------------------------
Results_In_Array = []


#==================================================================================================================  

#----------------------------------------------------------------
# This function will structure the program flow
#----------------------------------------------------------------

#  P R O G R A M    F L O W
#  -------------------------
def main():    
    display_title()
    display_welcome_message()

    #call the function in a loop that passes the values 1 throught 10 as arguments and displays the return value
    for Time in range(1, 11):   
        Results_In_Array.append([Time, falling_distance(Time)])

    #Display the final output
    beautify_output(Results_In_Array)

    display_goodbye_message()

#==================================================================================================================


            # F U N C T I O N    D E C L A R A T I O N S

            #--------------------------------------------


#----------------------------------------------------------------
# This function will format and display the program title
#----------------------------------------------------------------
def display_title():
    Program_Title = 'FALLING DISTANCES'
    Program_Title = " ".join(Program_Title)

    #PROGRAM TITLE
    print('{:^100}'.format(Title_Divider))
    print('{:^100}'.format(Program_Title))
    print('{:^100}'.format(Title_Divider))
    
#==================================================================================================================

#----------------------------------------------------------------
# This function will display the welcome message to the user
#----------------------------------------------------------------
def display_welcome_message():
    print("HELLO \n This program will display the results for the distance in meters for the time values within the range 1 to 10")

#----------------------------------------------------------------
# This function will display the goodbye message to the user
#----------------------------------------------------------------
def display_goodbye_message():
    print()
    print('{:^100}'.format(Heading_Dash))
    print('{:^100}'.format("Thanks for choosing our program! G O O D B Y E !"))
    print('{:^100}'.format(Heading_Dash))

#==================================================================================================================
    
#---------------------------------------------------------------------------------------------------------
# This function will calculate the distance that the object has fallen during a particular time interval
# FUNCTION INPUT = time in seconds
# FUNCTION OUTPUT = distance in meters
#--------------------------------------------------------------------------------------------------------

# B U S I N E S S   L O G I C
# ---------------------------

def falling_distance(_Time):
    #GIVEN
    #------
    _ACCELERATION_OF_GRAVITY = 9.8
    Distance = 0
    Time = 0
    
    Distance = (1/2) * (_ACCELERATION_OF_GRAVITY * (_Time**2))
    return Distance

#==================================================================================================================  

#----------------------------------------------------------------
# This function will format the results in the array into a table
#----------------------------------------------------------------

def beautify_output(x_Results_In_Array):
    
    #---------------
    # TABLE HEADING
    #---------------
    print('{:^100}'.format(Heading_Dash))
    print('{:^90}'.format('{:>10}{:>7}{:>8}{:>8}'.format("TIME", '|', ' ', 'DESCRIPTION' )))
    print('{:^100}'.format(Heading_Dash))
    #----------------------------------------
    # TABLE BODY / DYNAMIC DATA FROM THE LOOP
    #----------------------------------------
    for i in range(len(x_Results_In_Array)):
        print('{:^90}'.format('{:>8}{:<1}{:>8}{:>8}{:>8}{:<1}'.format((Results_In_Array[i][0]), 's', '|', ' ', format(x_Results_In_Array[i][1],'.2f'), ' m')))
    #----------------------------------------
    # TABLE FOOTER DIVIDER
    #----------------------------------------
    print('{:^100}'.format(Heading_Dash))
    
#==================================================================================================================    

#--------------------
# MAIN FUNCTION CALL
#--------------------
main()

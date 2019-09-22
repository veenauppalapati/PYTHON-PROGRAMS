# Ocean's level is currently rising about 1.6 millimeters per year
# Create an application that displays the number of millimeters that the ocean will have risen each year for the next 25 years

#-----------------------
# INITIATE THE VARIABLES
#-----------------------

# PROGRAM TITLE
#--------------
Program_Title = "oceans Levels"
Program_Title = Program_Title.upper() #Convert the title to uppercase
Program_Title = ' '.join(Program_Title) # Add a space between each letter

# FONT WEIGHT
#------------
BOLD = '\033[1m'
RESET = "\033[0;0m"

# DIVIDER FORMAT
#---------------
Console_Divider = format('-' * 120)
Center_The_Table = format(' ' * 36)
Table_Row_Divider = format('-' * 26)

# PROGRAM VARIABLES
#------------------
years = 1
risen = 0
Current_Year = 2019
Column1 = 'YEAR'
Column2 = 'RAISE LEVEL'

#=====================================================================================================

print()
print()
print(Console_Divider)
print()
print()

#-----------------------
#DISPLAY WELCOME MESSAGE
#-----------------------
print('{:^100}'.format(Table_Row_Divider))
print(BOLD + '{:^100}'.format(Program_Title) + RESET)
print('{:^100}'.format(Table_Row_Divider))
print("WELCOME\nThis program will display the number of millimeters that the ocean will have risen each year for the next 25 years")
print()
print()

#=====================================================================================================

#--------------------
#DISPLAY TABLE HEADER
#--------------------
print(Center_The_Table, " ", Table_Row_Divider, sep = "") #Table Row divider

#------------
#COLUMN NAMES
#------------
print(Center_The_Table,
      "| ",
      Column1,
      format(" " * 2),
      "|",
      Column2.rjust(8, ' '),
      format('|', '4'))

print(Center_The_Table, " ", Table_Row_Divider, sep = "")#Table Row divider

#=====================================================================================================

#---------------
#ITERATE TILL 25
#---------------
while years <= 25:
    #-----------------------------------------------
    # POPULATE THE TABLE BY ADDING 1.6 mm EACH YEAR
    #-----------------------------------------------
    risen += 1.6 #CALCULATION: ADDING 1.6 mm
    #------------
    # DISPLAY
    #------------
    print(Center_The_Table,
          " |  ",
          Current_Year,
          format(" " * 3),
          "|",
          format(" "* 4),
          format(risen, '05.2f'), "mm ",
          format(" " * 2),
          "|",
          sep = "")
  
    
    Current_Year+=1
    years+= 1
    
#-----------    
# LOOP ENDS
#-----------
#=====================================================================================================

print(Center_The_Table, " ", Table_Row_Divider, sep = "")#Table Row divider for footer

#=====================================================================================================

print()
print()
print(Console_Divider)
print()

#-----------------------
#DISPLAY GOODBYE MESSAGE
#-----------------------
print("Thank you for using our ----", Program_Title, "---- program\nGOODBYE!!!")

print()
print(Console_Divider)
print()
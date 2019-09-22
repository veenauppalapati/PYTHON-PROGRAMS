#INITIALIZE THE VARIABLES
Numerator = 1
Denominator = 30
Total = 0.0

while ( Numerator <= 30 ):
    #CALCULATION:  ACCUMULATE THE TOTAL VALUE OF THE INCREMENTING NUMERATOR AND DECREMENTING DENOMINATOR
    Total += (Numerator / Denominator)
    print('Total:', format(Total, '.2f'))
    
    #INCREMENT AND DECREMENT THE VALUES
    Numerator += 1
    Denominator -= 1
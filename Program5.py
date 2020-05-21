#***************************************************************
#
#  Developer:         Renee White
#
#  Program #:         Program 5
#
#  File Name:         Program5.py
#
#  Course:            COSC 1336 Programming Fundamentals I 
#
#  Due Date:          09-29-19
#
#  Instructor:        Fred Kumi 
#
#  Chapter:           Chapter #s 1-3
#
#  Description:
#     This program is used to determine discounts on software packages.
#
#***************************************************************

#***************************************************************
#
#  Function:     main
# 
#  Description:  The main function of the program
#
#  Parameters:   None
#
#  Returns:      Nothing 
#
#**************************************************************
def main():
    
    developerInfo()

    units = int(input('Enter the number of units purchased: '))

    if units >= 100:
        BasePrice = units * 99.00
        PercentOff = 0.5
        Discount = BasePrice * PercentOff
        FinalPrice = BasePrice - Discount
        print('Number of units purchased is: ', units)
        print('Discount applied is: 50%')
        print('Total savings due to the discount is $',
          format(Discount, ',.2f'),
          sep='')
        print('The total cost of the purchase is: $',
          format(FinalPrice, ',.2f'),
          sep='')
    elif units >= 70:
        BasePrice = units * 99.00
        PercentOff = 0.40
        Discount = BasePrice * PercentOff
        FinalPrice = BasePrice - Discount
        print('Number of units purchased is: ', units)
        print('Discount applied is: 40%')
        print('Total savings due to the discount is $',
          format(Discount, ',.2f'),
          sep='')
        print('The total cost of the purchase is: $',
          format(FinalPrice, ',.2f'),
          sep='')
    elif units >= 50:
        BasePrice = units * 99.00
        PercentOff = 0.35
        Discount = BasePrice * PercentOff
        FinalPrice = BasePrice - Discount
        print('Number of units purchased is: ', units)
        print('Discount applied is: 35%')
        print('Total savings due to the discount is $',
          format(Discount, ',.2f'),
          sep='')
        print('The total cost of the purchase is: $',
          format(FinalPrice, ',.2f'),
          sep='')
    elif units >= 20:
        BasePrice = units * 99.00
        PercentOff = 0.30
        Discount = BasePrice * PercentOff
        FinalPrice = BasePrice - Discount
        print('Number of units purchased is: ', units)
        print('Discount applied is: 30%')
        print('Total savings due to the discount is $',
          format(Discount, ',.2f'),
          sep='')
        print('The total cost of the purchase is: $',
          format(FinalPrice, ',.2f'),
          sep='')
    elif units >= 10:
        BasePrice = units * 99.00
        PercentOff = 0.20
        Discount = BasePrice * PercentOff
        FinalPrice = BasePrice - Discount
        print('Number of units purchased is: ', units)
        print('Discount applied is: 20%')
        print('Total savings due to the discount is $',
          format(Discount, ',.2f'),
          sep='')
        print('The total cost of the purchase is: $',
          format(FinalPrice, ',.2f'),
          sep='') 
    else:
        BasePrice = units * 99.00
        PercentOff = 0.00
        Discount = 0.00
        FinalPrice = BasePrice
        print('Number of units purchased is: ', units)
        print('Discount applied is: 0%')
        print('Total savings due to the discount is $',
          format(Discount, ',.2f'),
          sep='')
        print('The total cost of the purchase is: $',
          format(FinalPrice, ',.2f'),
          sep='')
        
   
    
    # End of the main function 
    
#***************************************************************
#
#  Function:     developerInfo
# 
#  Description:  Prints Programmer's information
#
#  Parameters:   None
#
#  Returns:      Nothing 
#
#**************************************************************
def developerInfo():
    print('Name:     Renee White')
    print('Course:   Programming Fundamentals I')
    print('Program:  Five')
    print()
    # End of the developerInfo function

# Call the main function
main()

# End of Program 1

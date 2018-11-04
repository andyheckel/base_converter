#!/usr/bin/python3

#code for converting a decimal value to a specified base (up to 36)
def decimal_to_base():
#sets variable number to an empty string. While number contains characters other than numbers, prompts user to enter a decimal to convert.
    number=""
    while(not(number.isnumeric())):
        number = input("What is the decimal to convert? ")
#prompts user for a base to convert to. NOTE: if the user enters a number above 36, it WILL break the program in its current state.
    base=""
    while(not(base.isnumeric())):
        base = input("What base would you like to convert to? Please choose a number between 1 and 36. ")

#converts number(returned from input as string) to tempnumb, an integer. Converts base to an integer.
    tempnumb = int(number)
    tempbase = int(base)
#creates a variable output and sets it to an empty string
    output = ""
#establishes the symbols necessary for higher bases. bases 0-10 will use normal digits, but the letters of the alphabet (a-z) are borrowed as placeholders when using higher bases.
    values = "0123456789abcdefghijklmnopqrstuvwxyz"


#Performs mod division (by the specified base) on tempnumb. The result(the remainder) is converted to a string and concatenated to output. A normal division operation is also performed and tempnumb is set to this new value. These operations continue until tempnumb is no longer greater than zero. The variable values is referenced to assign appropriate symbols when the base is higher than 10.
    while(tempnumb > 0):
        output = str(values[tempnumb % tempbase]) + output
        tempnumb = int(tempnumb / tempbase)
#prints output (a string representing the new based value of number) to console
    print (output)

def base_to_decimal():
#prompt user for a value to convert
    number = input("What number would you like to convert? ").lower()
    #tempnum = int(number)
#prompt user for the base of the value
    base = input("And what base is this number currently in? ")
    tempbase = int(base)
#create values to represent higher bases
    values = "0123456789abcdefghijklmnopqrstuvwxyz"

#Do the math. Sets output_num to an initial value of zero. Obtains the number of digits in the number from the length of the string number. This is set as the counter places. The counter num_place, used to parse each digit of the number, is created and set to zero.  While places is greater than zero, the program iterates through each digit of the provided number. It first obtains the correct value for each digit by consulting the index of values. It then multiplies this value by the appropriate power of tempbase (represented by places). This value is added to output_num and the loop continues, moving on to the next digit place (by incrementing num_place) and the next lower power (by decrementing places). The loop finishes when it has iterated through every digit (and exponential function) and output is printed to console.
    output_num = 0
    places = int(len(number))
    num_place = 0

    while(places > 0):
        digit = int(values.index(number[num_place]))
        iteration = int(digit) * (tempbase ** (places-1))
        output_num += iteration
        num_place += 1
        places -= 1
#output to console
    print(output_num)

#basic flow control allowing the user to choose the direction of conversion. Choosing 1 calls the decimal_to_base() function and choosing 2 calls base_to_decimal().
def newgame():
    user_choice = ""
    while (user_choice != "1") and (user_choice != "2"):
        user_choice = input("Hello! Please choose an option: 1 (convert decimal to base) 2 (Convert base to decimal) : ")

    if (user_choice == "1"):
        decimal_to_base()
    elif (user_choice == "2"):
        base_to_decimal()
#start the conversion function
newgame()


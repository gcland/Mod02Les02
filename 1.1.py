number = input("Enter a number: ")
number = int(number) #input was previously a str and needed to be converted to integer variable.

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.") #cannot have text after 'else' statement. 'Else' must be defined by if and elif statements above.
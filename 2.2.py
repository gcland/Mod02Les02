print("Enter three numbers, the system will determine the smallest number of the three inputs!")
number_1 = input("Enter the first number: ")
number_1 = int(number_1)

number_2 = input("Enter the second number: ")
number_2 = int(number_2)

number_3 = input("Enter the third number: ")
number_3 = int(number_3)

if number_1 < number_2 and number_1 < number_3:
    print("The first number is the smallest: ")
    print(number_1)

elif number_2 < number_1 and number_2 < number_3:
    print("The second number is the smallest: ")
    print(number_2)

else:
   print("The third number is the smallest: ")
   print(number_3)
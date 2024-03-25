print("Enter three numbers, the system will determine if any of the three inputs are equal!")
number_1 = input("Enter the first number: ")
number_1 = int(number_1)

number_2 = input("Enter the second number: ")
number_2 = int(number_2)

number_3 = input("Enter the third number: ")
number_3 = int(number_3)

if number_1 == number_2 and number_1 == number_3:
    print("All numbers are equal:", number_1,"=", number_2,"=",number_3,".")

elif number_1 == number_2:
    print("Numbers one and two are equal:" +str(number_1),"= " +str(number_2),".")

elif number_1 == number_3:
    print("Numbers one and three are equal:", number_1,"=",number_3,".")

elif number_2 == number_3:
    print("Numbers two and three are equal:", number_2,"=",number_3,".")

else:
    print("None of the numbers are equal.", number_1,"!=", number_2,"!=",number_3,".")

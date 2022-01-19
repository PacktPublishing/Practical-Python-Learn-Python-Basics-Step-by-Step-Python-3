def add_2_numbers(a, b):
    return a + b

number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))

print(str(number1) + " + " + str(number2)
      + " = " + str(add_2_numbers(number1, number2)))

from operation import sum_two_numbers, subtract_two_numbers, multiply_two_numbers, divide_two_numbers

option = 0
while option != 5:
    try:
        number1 = float(input("Please, enter two numbers.\nFirst number: "))
        number2 = float(input("Second number: "))
        option = int(input("1 - Sum\n2 - Subtract\n3 - Multiply\n4 - Divide\n5 - Exit\nNow, choose one option: "))
        if option == 1:
            print(sum_two_numbers(number1, number2))
        elif option == 2:
            print(subtract_two_numbers(number1, number2))
        elif option == 3:
            print(multiply_two_numbers(number1, number2))
        elif option == 4:
            print(divide_two_numbers(number1, number2))
        elif option == 5:
            exit(0)
    except (Exception, ZeroDivisionError) as e:
        print(e)


# print(subtract_two_numbers(3, 4))
# print(multiply_two_numbers(3, 4))
# print(divide_two_numbers(3, 0))

import math


# ---------- Functions ----------

def Addition(number1, number2):
    return number1 + number2


def Subtraction(number1, number2):
    return number1 - number2


def Multiplication(number1, number2):
    return number1 * number2


def Division(number1, number2):
    return number1 / number2


def Modulus(number1, number2):
    return number1 % number2


def Power(number, power):
    return number ** power


def SquareRoot(number):
    return math.sqrt(number)


def Percentage(number, percentage):
    return (number * percentage) / 100


# ---------- Calculator ----------

print("======================================")
print("      Welcome to Scientific Calculator")
print("======================================")


while True:

    print("\n---------- MENU ----------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Square Root")
    print("8. Percentage")
    print("9. Exit")
    print("--------------------------")

    # ---------- Choice Validation ----------

    try:
        choose = int(input("Enter your choice : "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue


    # ---------- Operations ----------

    match choose:

        case 1:
            number1 = float(input("Enter number 1 : "))
            number2 = float(input("Enter number 2 : "))

            print(f"Result : {Addition(number1, number2)}")


        case 2:
            number1 = float(input("Enter number 1 : "))
            number2 = float(input("Enter number 2 : "))

            print(f"Result : {Subtraction(number1, number2)}")


        case 3:
            number1 = float(input("Enter number 1 : "))
            number2 = float(input("Enter number 2 : "))

            print(f"Result : {Multiplication(number1, number2)}")


        case 4:
            number1 = float(input("Enter number 1 : "))
            number2 = float(input("Enter number 2 : "))

            if number2 == 0:
                print("Error: Cannot divide by zero.")
            else:
                print(f"Result : {Division(number1, number2)}")


        case 5:
            number1 = float(input("Enter number 1 : "))
            number2 = float(input("Enter number 2 : "))

            if number2 == 0:
                print("Error: Cannot perform modulus by zero.")
            else:
                print(f"Result : {Modulus(number1, number2)}")


        case 6:
            number = float(input("Enter number : "))
            power = float(input("Enter power : "))

            print(f"Result : {Power(number, power)}")


        case 7:
            number = float(input("Enter number : "))

            if number < 0:
                print("Error: Cannot find square root of a negative number.")
            else:
                print(f"Result : {SquareRoot(number)}")


        case 8:
            number = float(input("Enter number : "))
            percentage = float(input("Enter percentage : "))

            print(f"Result : {Percentage(number, percentage)}")


        case 9:
            print("Thank you for using the calculator.")
            break


        case _:
            print("Invalid choice. Please choose between 1 and 9.")

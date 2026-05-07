#IMPORTING MATH MODULE
import math as m

#MENU TO CHOOSE BASIC, SCIENTIFIC OR EXIT
def menu():
    print("Welcome to the Calculator!\n")
    print("Please select an option:\n")
    print("1. Basic Calculator")
    print("2. Scientific Calculator")
    print("3. Exit\n")

    choice = int(input("Enter your choice (1/2/3): "))
    return choice

#BASIC CALCULATOR FUNCTION
def basic_calculator():
    print("Basic Calculator\n")
    num1 = float(input("Enter the first number: "))
    operator = input("Enter the operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = round((num1 / num2),10)
        else:
            print("Error: Division by zero is not allowed.\n")
            return
    else:
        print("Invalid operator. Please try again.\n")
        return

    print("The result is: ",result,"\n")

#SCIENTIFIC CALCULATOR FUNCTION
def scientific_calculator():
    print("Scientific Calculator\n")
    print("Please select an option:\n")
    print("1. Factorial")
    print("2. Combination")
    print("3. Permutation")
    print("4. Square Root")
    print("5. Cube Root")
    print("6. Power")
    print("7. Log Function")
    print("8. Exponent")
    print("9. Sin")
    print("10. Cosine")
    print("11. Tan")
    print("12. asin")
    print("13. acos")
    print("14. atan\n")

    operator = int(input("Enter your choice (1/2/3/.....): "))

    if operator == 1 :
        n = int(input("Enter Positive Integer: "))
        result = m.factorial(n)
    elif operator == 2 :
        n = int(input("Enter Integer N: "))
        k = int(input("Enter Integer K: "))
        result = m.comb(n,k)
    elif operator == 3 :
         n = int(input("Enter Integer N: "))
         k = int(input("Enter Integer K: "))
         result = m.perm(n,k)
    elif operator == 4 :
        n = float(input("Enter Positive Number: "))
        if n >= 0 :
            result = round((m.sqrt(n)),10)
        else :
            print("Invalid Input\n")
            return
        
    elif operator == 5 :
        n = float(input("Enter Number: "))
        result = round((m.cbrt(n)),10)
    elif operator == 6 :
        base = float(input("Enter Base Number: "))
        power = float(input("Enter Power Number: "))
        result = round((m.pow(base,power)),10)
    elif operator == 7 :
        arg = int(input("Enter Number: "))
        base = int(input("Enter Base Number: "))
        if arg > 0 and base > 0 and base != 1 :
            result = round((m.log(arg,base)),10)
        else :
            print("Invalid Input\n")
            return
        
    elif operator == 8 :
        x = float(input("Enter Power Number: "))
        result = round((m.exp(x)),10)
    elif operator == 9 :
        x = float(input("Enter Angle in Degrees: "))
        rad = m.radians(x)
        result = round(m.sin(rad),10)
    elif operator == 10 :
        x = float(input("Enter Angle in Degrees: "))
        rad = m.radians(x)
        result = round(m.cos(rad),10)
    elif operator == 11 :
        x = float(input("Enter Angle in Degrees: "))
        rad = m.radians(x)
        result = round(m.tan(rad),10)
    elif operator == 12 :
        x = float(input("Enter Value: "))
        if x < -1 or x > 1 :
            print("Error: value must be between -1 and 1\n")
            return   
        result = round((m.degrees(m.asin(x))),10)
    elif operator == 13 :
        x = float(input("Enter Value: "))
        if x < -1 or x > 1 :
            print("Error: value must be between -1 and 1\n")
            return
        result = round((m.degrees(m.acos(x))),10)
    elif operator == 14 :
        x = float(input("Enter Value: "))
        result = round((m.degrees(m.atan(x))),10)
    
    else:
        print("Invalid operator. Please try again.\n")
        return

    print("The result is: ",result,"\n")




#CALLING OF MENU FUNCTION
while True :
    op = menu()
    if op == 1 :
       basic_calculator()
    elif op == 2 :
       scientific_calculator()
    elif op == 3 :
       print("Bye!")
       break
    else :
        print("Invalid Operator Value\n")




    

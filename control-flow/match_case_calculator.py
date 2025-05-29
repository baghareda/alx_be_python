num1 =float(input("Enter the first number:"))
num2 =float(input("Enter the second number:"))
opr =input("Choose the operation (+, -, *, /):")
match opr:
 case   "*":
    print("The result is: ", num1 * num2)
 case   "+":
    print("The result is: ", num1 + num2)
 case   "-":
    print("The result is: ", num1 - num2)
 case   "/":
    print("The result is: ", num1 / num2)
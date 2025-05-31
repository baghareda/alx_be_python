number = int(input("Enter a number to see its multiplication table: "))

if number >= 0 and number <= 10:
    for m in range(1, 11):
        print (f"{number} * {m} = {number * m}")
else:
        print ("enter a valid number")
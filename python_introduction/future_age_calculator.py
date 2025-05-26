user_input = input("How old are you?\n")

is_number = True
for char in user_input:
    if char < '0' or char > '9':
        is_number = False
        break

if is_number:
    age = int(user_input)
    print("In 2050, you will be", age + 27, "years old.")
else:
    print("That's not a valid age.")


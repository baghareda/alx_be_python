number = int(input("Enter the size of the pattern:"))
if number > 0:

    row = 0
    while row < number :
        colon = 0
        while colon < number:
            print("*",end="")
            colon +=1
        print()
        row +=1

else :
    print("hadchi ma khedamch")
        
        
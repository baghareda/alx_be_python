Task = input("describe yout task: ")
Priority = input("choose the task priority(high,medium,low): ")

reminder = f"reminder: {Task} is a {Priority} priority task"
match Priority:

    case "high":
        print("High-priority task ")
    case "medium":
        print("medium-priority task ")
    case "low":
        print("low-priority task ")
    case _:
        print("non of the above")
        exit()

Time_Bound = input("is the task is time-bound (yes or no): ")

if Time_Bound == "yes":
    reminder += (" requires immediate attention today!")
elif Time_Bound == "no":
    reminder += (" Consider completing it when you have free time.")
else :
    print("yes or no only")
    exit()

print (reminder)
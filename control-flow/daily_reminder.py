task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")

reminder = f"reminder: {task} is a {priority} priority task"
match priority:

    case "high":
        print("High-priority task ")
    case "medium":
        print("medium-priority task ")
    case "low":
        print("low-priority task ")
    case _:
        print("non of the above")
        exit()

time_bound = input("Is it time-bound? (yes/no): ")

if time_bound == "yes":
    reminder += (" requires immediate attention today!")
elif time_bound == "no":
    reminder += (" Consider completing it when you have free time.")
else :
    print("yes or no only")
    exit()

print (reminder)
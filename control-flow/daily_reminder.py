task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")

match priority:
    case "high":
        print("High-priority task")
    case "medium":
        print("medium-priority task")
    case "low":
        print("low-priority task")
    case _:
        print("none of the above")
        exit()

time_bound = input("Is it time-bound? (yes/no): ")

if time_bound == "yes":
    print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
elif time_bound == "no":
    print(f"Reminder: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
else:
    print("yes or no only")
    exit()

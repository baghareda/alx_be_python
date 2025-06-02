task = input("describe yout task: ")
priority = input("choose the task priority(high,medium,low): ")


match priority:

    case "high":
        print("High-priority task")
    case "medium":
        print("medium-priority task")
    case "low":
        print("low-priority task")
    case _:
        print("non of the above")
        exit()

time_bound = input("is the task is time-bound (yes or no): ")

if time_bound == "yes":
    reminder += ("requires immediate attention today!")
elif time_bound == "no":
    reminder += ("Consider completing it when you have free time.")
else :
    print("yes or no only")
    exit()

reminder = f"reminder: {task} is a {priority} priority task"
print (reminder)
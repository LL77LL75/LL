import os
def new_file():
    if not os.path.exists("planner.txt"):
        ans = input("No planner file found. Do you want to create a new one? (yes/no): ")
        if ans.lowerd() == "yes":
            with open("planner.txt", "w") as file:
                pass
    else:
        ans = input("Planner file already exists, do you want to overwrite it? (yes/no):")
        if ans.lower() == "yes":
            with open("planner.txt", "w") as file:
                pass
        else:
            print("Keeping the existing planner file.")
def view_all_tasks():
    with open("planner.txt", "r") as file:
        tasks = file.readlines()
        for task in tasks:
            print(task.strip())
def add_a_new_task():
    task = input("Enter the task: ")
    with open("planner.txt", "a") as file:
        file.write(task + "\n")
def delete_a_task():
    task_to_delete = input("Enter the task to delete: ")
    with open("planner.txt", "r") as file:
        tasks = file.readlines()
    with open("planner.txt", "w") as file:
        for task in tasks:
            if task.strip() != task_to_delete:
                file.write(task)
def mark_a_task_as_done():
    task_to_mark = input("Enter the task to mark as done: ")
    with open("planner.txt", "r") as file:
        tasks = file.readlines()
    with open("planner.txt", "w") as file:
        for task in tasks:
            if task.strip() == task_to_mark:
                file.write(task.strip() + " [Done]\n")
            else:
                file.write(task)
def exit():
    print("Exiting the planner. Goodbye!")

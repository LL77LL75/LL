#kim-jong-un.com
import os
def new_file():
    if not os.path.exists("planner.txt"):
        ans = input("No planner file found. Do you want to create a new one? (yes/no): ")
        if ans.lower() == "yes":
            with open("planner.txt", "w") as file:
                file.write("my task list\n")
            print("Planner file has been created.")
    else:
        ans = input("Planner file already exists, do you want to overwrite it? (yes/no):")
        if ans.lower() == "yes":
            with open("planner.txt", "w") as file:
                file.write("my task list\n")
            print("Planner file has been overwritten.")
        else:
            print("Planner file will not be overwritten.")
def view_all_tasks():
    with open("planner.txt", "r") as file:
        tasks = file.readlines()
        for i in range(len(tasks)):
            if i == 0:
                print(f"{tasks[i].strip()}")
            else:
                print(f"{i}. {tasks[i].strip()}")
def add_a_new_task():
    task = input("Enter the task: ")
    with open("planner.txt", "a") as file:
        file.write(task + "\n")
def delete_a_task():
    with open("planner.txt", "r") as file:
        tasks = file.readlines()
        for i in tasks:
            print(i)
        task_to_delete = input("which task do you want to delete? ")
    with open("planner.txt", "w") as file:
        for task in tasks:
            if task.strip() != task_to_delete or task == "my task list":
                file.write(task)
            else:
                print(f"{task} was deleted")
def mark_a_task_as_done():
    with open("planner.txt", "r") as file:
        tasks = file.readlines()
        for i in tasks:
            print(i)    
    task_to_mark = input("Enter the task to mark as done: ")
    with open("planner.txt", "w") as file:
        for task in tasks:
            if task.strip() == task_to_mark:
                file.write(task.strip() + " - done\n")
            else:
                file.write(task)
def exit():
    print("Exiting the planner. Goodbye!")
def main():
    new_file()
    while True:
        print("--Task Planner Menu--")
        print("1. View all tasks")
        print("2. Add a new task")
        print("3. Delete a task")
        print("4. Mark a task as done")
        print("5. new task file")
        print("6. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            view_all_tasks()
        elif choice == "2":
            add_a_new_task()
        elif choice == "3":
            delete_a_task()
        elif choice == "4":
            mark_a_task_as_done()
        elif choice == "5":
            new_file()
        elif choice == "6":
            exit()
            break
        else:
            print("Invalid choice. Please try again.")
main()
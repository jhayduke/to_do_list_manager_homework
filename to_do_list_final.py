tasks = [] 

def add_task(task):
    task = input("Enter the task you want to add: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

def view_all_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("Your tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def mark_task_completed(task_number):
    if 0 < task_number <= len(tasks):
        task = tasks[task_number - 1]
        print(f"Task '{task}' marked as completed!")
    else:
        print("Invalid task number.")

def delete_task(task_number):
    view_all_tasks()
    try:
        task_number = int(input("Enter the task number you want to delete: "))
        if 0 < task_number <= len(tasks):
            task = tasks.pop(task_number - 1)
            print(f"Task '{task}' deleted successfully!")
        else:
            print(f"task number #{task_number} does not exist.")
    except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":


    print("Lets get you organized! ;)")
    
    while True:
        print("\n")
        print("====================================")
        print("Choose an option 1-5: ")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Mark a task as completed")
        print("4. Delete a task")
        print("5. Quit")
        print("====================================")

        choice = input("Enter your choice (1-5): ")  
        if (choice == 1):
            add_task = input("Enter the task you want to add: ")
        elif (choice == 2):
            view_all_tasks = input("Here are all your tasks: ")
        elif (choice == 3):
            mark_completed = input("Enter the task you want to mark as completed: ") 
        elif (choice == 4):
            delete_task = input("Enter the task you want to delete: ")
        elif (choice == 5):
            print("Goodbye! May the Force be with you!")           
            break


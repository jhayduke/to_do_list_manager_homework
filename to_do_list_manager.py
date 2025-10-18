tasks =[]

def add_task(task):
    task = input("Enter the task you want to add: ")
    tasks.append({"task": task, "completed": False})
    print(f'Task "{task}" groovily added!')

def view_all_tasks():
    if not tasks:
        print("Your to-do list is empty. You're a failure. This is why mommy left. Time to do something with your life!")
    else:
        print("Here are all your tasks:")
        for idx, task in enumerate(tasks, start=1):
            status = "✓" if task["completed"] else "✗"
            print(f"{idx}. [{status}] {task['task']}")


def mark_completed(task_number):

if __name__ == "__main__":
    print("Lets get you organized! ;)")
    while True:
        print("Please select one of the following options:D")
        print("====================================)
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Mark a task as completed")
        print("4. Delete a task")
        print("5. Quit")
        print("====================================)

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
        else:
            print("Invalid choice. Please try again.")
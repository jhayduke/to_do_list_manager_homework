
class Task:

    
    def __init__(self, name):
        self.name = name
        self.completed = False
    
    def mark_complete(self):
        self.completed = True
    
    def __str__(self):
        status = "Complete" if self.completed else "Incomplete"
        return f"{self.name} - {status}"


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head is None
    
    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
            current = self.head
        while current.next is not None:
            current = current.next
        
            current.next = new_node
    
    def get_at_position(self, position):
        if position < 1 or self.is_empty():
            return None
        
        current = self.head
        current_position = 1
        
        while current is not None and current_position < position:
            current = current.next
            current_position += 1
        
        return current
    
    def remove_at_position(self, position):
        if position < 1 or self.is_empty():
            return False
        if position == 1:
            self.head = self.head.next
            return True
        previous = self.head
        current_position = 1
        
        while previous.next is not None and current_position < position - 1:
            previous = previous.next
            current_position += 1
        if previous.next is None:
            return False
        
        previous.next = previous.next.next
        return True
    
    def get_all_tasks(self):
        tasks = []
        current = self.head
        
        while current is not None:
            tasks.append(current.data)
            current = current.next
        
        return tasks
    
    def count(self):
        count = 0
        current = self.head
        
        while current is not None:
            count += 1
            current = current.next
        
        return count


class ToDoList:
    def __init__(self, list_name="My Tasks"):
        self.list_name = list_name
        self.tasks = LinkedList()     
    
    def add_task(self, task_name):
        new_task = Task(task_name)
        
        self.tasks.append(new_task)
        
        print(f"✅ '{task_name}' added")
    
    def complete_task(self, position):
        node = self.tasks.get_at_position(position)
        
        if node is None:
            print(f"No task found at position {position}")
            return False
        
        node.data.mark_complete()
        print(f"Task {position} marked as completed!")
        return True
    
    def remove_task(self, position):
        success = self.tasks.remove_at_position(position)
        
        if success:
            print(f"Task {position} removed!")
        else:
            print(f"No task found at position {position}")
        
        return success
    
    def view_all_tasks(self):
        if self.tasks.is_empty():
            print(f"\n{self.list_name}")
            print("=" * len(self.list_name))
            print("Nothing here to see. Please add a task!\n")
            return
        
        print(f"\n{self.list_name}")
        print("=" * len(self.list_name))

        all_tasks = self.tasks.get_all_tasks()

        for position, task in enumerate(all_tasks, start=1):
            print(f"{position}. {task}")
        
        print() 



def display_menu():
    print("\n" + "=" * 50)
    print(" Take Accountability and get organized! ")
    print("=" * 50)
    print("1. Add a task")
    print("2. Complete a task")
    print("3. Remove a task")
    print("4. View all tasks")
    print("5. Exit")
    print("=" * 50)


def main():
``
    print("Lets get your life in order, slacker!\n")
    
    list_name = input("Enter a name for your to-do list (or press Enter for 'My Tasks'): ")
    if not list_name:
        list_name = "My Tasks"
    
    todo = ToDoList(list_name)
    
    while True:
        display_menu()
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            task_name = input("Enter task description: ")
            if task_name:
                todo.add_task(task_name)
            else:
                print("Please add task!")
        
        elif choice == '2':
            todo.view_all_tasks()
            try:
                position = int(input("Enter task number to mark complete: "))
                todo.complete_task(position)
            except ValueError:
                print("Error 404: task not found!")
        
        elif choice == '3':
            todo.view_all_tasks()
            try:
                position = int(input("Enter task number to remove: "))
                todo.remove_task(position)
            except ValueError:
                print("Please enter a valid number!")
        
        elif choice == '4':
            todo.view_all_tasks()
        
        elif choice == '5':
            print("\nNow go do something with your life!")
            print("May the Force be with you\n")
            break
        
        else:
            print("Nope! Please choose 1-5.")



def example_usage():

    print("\n" + "="*60)
    print("EXAMPLE USAGE DEMONSTRATION")
    print("="*60)
    
    todo = ToDoList("My Daily Tasks")
    

    print("\n--- Adding tasks ---")
    todo.add_task("Buy groceries")
    todo.add_task("Finish homework")
    todo.add_task("Sacrifice a goat")
    todo.add_task("Do HW for Allan")
    

    print("\n--- Viewing all tasks ---")
    todo.view_all_tasks()
    

    print("\n--- Completing task 2 ---")
    todo.complete_task(2)

    print("\n--- Viewing tasks after completion ---")
    todo.view_all_tasks()
    
    print("\n--- Removing task 1 ---")
    todo.remove_task(1)
    
    print("\n--- Final task list ---")
    todo.view_all_tasks()
    
    print("\n--- Testing error handling ---")
    todo.complete_task(10)  
    todo.remove_task(0)    


if __name__ == "__main__":
    main()
    

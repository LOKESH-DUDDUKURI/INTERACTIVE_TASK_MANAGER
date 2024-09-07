# Initialize an empty list to store tasks
task_list = []

# Function to create a new task
def create_task():
    task_name = input("Please enter the task title: ")
    task_details = input("Please enter the task description: ")
    task_list.append({"name": task_name, "details": task_details})
    print("Task has been successfully added!")

# Function to display all tasks
def display_tasks():
    if task_list:
        print("Current Tasks:")
        for index, task in enumerate(task_list, start=1):
            print(f"{index}. Title: {task['name']}, Description: {task['details']}")
    else:
        print("No tasks are currently available.")

# Function to modify a task
def modify_task():
    display_tasks()
    if task_list:
        task_num = int(input("Enter the number of the task you want to modify: ")) - 1
        if 0 <= task_num < len(task_list):
            updated_name = input("Enter new title (or press Enter to keep current): ")
            updated_details = input("Enter new description (or press Enter to keep current): ")
            if updated_name:
                task_list[task_num]['name'] = updated_name
            if updated_details:
                task_list[task_num]['details'] = updated_details
            print("Task has been updated successfully!")
        else:
            print("The task number provided is invalid.")
    else:
        print("No tasks are currently available.")

# Function to remove a task
def remove_task():
    display_tasks()
    if task_list:
        task_num = int(input("Enter the number of the task you wish to remove: ")) - 1
        if 0 <= task_num < len(task_list):
            removed_task = task_list.pop(task_num)
            print(f"Task '{removed_task['name']}' has been deleted successfully!")
        else:
            print("The task number provided is invalid.")
    else:
        print("No tasks are currently available.")

# Main program loop
while True:
    print("\nTask Management System")
    print("1. Create Task")
    print("2. Display Tasks")
    print("3. Modify Task")
    print("4. Remove Task")
    print("5. Exit")
    
    user_choice = input("Please select an option (1-5): ")
    
    if user_choice == "1":
        create_task()
    elif user_choice == "2":
        display_tasks()
    elif user_choice == "3":
        modify_task()
    elif user_choice == "4":
        remove_task()
    elif user_choice == "5":
        print("Exiting the Task Management System. Farewell!")
        break
    else:
        print("Invalid selection. Please choose a valid option (1-5).")

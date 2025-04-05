import json
import os
import datetime
from plyer import notification

# File to store tasks
TASKS_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a task
def add_task():
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD) or leave blank: ")
    priority = input("Set priority (Low, Medium, High): ").capitalize()
    
    if due_date:
        try:
            due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d").strftime("%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Task not added.")
            return
    
    task = {"description": description, "due_date": due_date, "priority": priority, "status": "Pending"}
    tasks.append(task)
    save_tasks(tasks)
    print("âœ… Task added successfully!")

# View tasks
def view_tasks(filter_type=None):
    if not tasks:
        print("ðŸ“­ No tasks available.")
        return
    
    print("\nðŸ“‹ Your Tasks:")
    for i, task in enumerate(tasks, 1):
        status_color = "\033[92m" if task["status"] == "Completed" else "\033[91m"
        print(f"{i}. {task['description']} | Due: {task['due_date']} | Priority: {task['priority']} | {status_color}{task['status']}\033[0m")
    print()

# Mark task as completed
def complete_task():
    view_tasks()
    try:
        task_index = int(input("Enter task number to mark as completed: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index]["status"] = "Completed"
            save_tasks(tasks)
            print("âœ… Task marked as completed!")
        else:
            print("âŒ Invalid task number.")
    except ValueError:
        print("âŒ Please enter a valid number.")

# Edit task
def edit_task():
    view_tasks()
    try:
        task_index = int(input("Enter task number to edit: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index]["description"] = input("New description: ")
            tasks[task_index]["due_date"] = input("New due date (YYYY-MM-DD) or leave blank: ")
            tasks[task_index]["priority"] = input("New priority (Low, Medium, High): ").capitalize()
            save_tasks(tasks)
            print("âœ… Task updated successfully!")
        else:
            print("âŒ Invalid task number.")
    except ValueError:
        print("âŒ Please enter a valid number.")

# Delete task
def delete_task():
    view_tasks()
    try:
        task_index = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            del tasks[task_index]
            save_tasks(tasks)
            print("âœ… Task deleted successfully!")
        else:
            print("âŒ Invalid task number.")
    except ValueError:
        print("âŒ Please enter a valid number.")

# View tasks sorted by due date
def view_sorted_tasks():
    sorted_tasks = sorted([task for task in tasks if task["due_date"]], key=lambda x: x["due_date"])
    print("\nðŸ“‹ Tasks Sorted by Due Date:")
    for i, task in enumerate(sorted_tasks, 1):
        print(f"{i}. {task['description']} | Due: {task['due_date']} | Priority: {task['priority']} | Status: {task['status']}")

# Send notifications for due tasks
def send_reminders():
    today = datetime.date.today()
    for task in tasks:
        if task["due_date"]:
            due_date = datetime.datetime.strptime(task["due_date"], "%Y-%m-%d").date()
            if today <= due_date <= today + datetime.timedelta(days=3) and task["status"] == "Pending":
                notification.notify(
                    title="â³ Task Reminder!",
                    message=f"Task '{task['description']}' is due on {task['due_date']}!",
                    timeout=10
                )

# Main menu
def main():
    global tasks
    tasks = load_tasks()
    send_reminders()
    
    while True:
        print("\nðŸ“ To-Do List Manager")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. View Completed Tasks")
        print("4. Mark Task as Completed")
        print("5. Edit Task")
        print("6. Delete Task")
        print("7. View Tasks (Sorted by Due Date)")
        print("8. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks("Completed")
        elif choice == "4":
            complete_task()
        elif choice == "5":
            edit_task()
        elif choice == "6":
            delete_task()
        elif choice == "7":
            view_sorted_tasks()
        elif choice == "8":
            print("ðŸ‘‹ Exiting... Have a productive day!")
            break
        else:
            print("âŒ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
# Simple To-Do List Manager

This Python script provides a basic command-line interface for managing your to-do list. It allows you to add, view, mark as complete, edit, delete, and sort your tasks. It also includes a feature to send desktop notifications for tasks due within the next three days.

## Features

* **Add Tasks:** Easily add new tasks with a description, optional due date, and priority level (Low, Medium, High).
* **View All Tasks:** Display all tasks with their description, due date, priority, and status (Pending or Completed).
* **View Completed Tasks:** Filter and view only the tasks that have been marked as completed.
* **Mark Task as Completed:** Change the status of an existing task to "Completed".
* **Edit Task:** Modify the description, due date, or priority of an existing task.
* **Delete Task:** Remove a task from your to-do list.
* **View Tasks (Sorted by Due Date):** Display all tasks with a due date, sorted chronologically.
* **Desktop Notifications:** Receive desktop notifications for tasks that are due within the next three days and are still marked as "Pending".
* **Data Persistence:** Tasks are saved in a `tasks.json` file, so your to-do list persists between sessions.

## Prerequisites

* **Python 3.x:** This script requires Python 3 to be installed on your system.
* **plyer library:** The `plyer` library is used for sending desktop notifications. You can install it using pip:
    ```bash
    pip install plyer
    ```
    **Note:** Desktop notifications may require additional configuration depending on your operating system. Refer to the `plyer` documentation for details.

## How to Use

1.  **Save the code:** Save the provided Python code as a `.py` file (e.g., `todo.py`).
2.  **Run the script:** Open your terminal or command prompt, navigate to the directory where you saved the file, and run the script using:
    ```bash
    python todo.py
    ```
3.  **Follow the menu:** The script will display a menu with different options. Enter the number corresponding to the action you want to perform and follow the prompts.

## Data Storage

The to-do list data is stored in a JSON file named `tasks.json` in the same directory where you run the script. This file will be created automatically when you add your first task. You should not manually edit this file unless you understand the JSON format.

## Contributing

This is a simple personal project. However, if you have suggestions for improvements or find any issues, feel free to open an issue on a related platform if this was shared as part of a repository.

## License

This project is open-source and available under a permissive license (e.g., MIT License). Feel free to use, modify, and distribute it as you wish. (Add the specific license details if applicable).

## Acknowledgements

* The `plyer` library for providing cross-platform desktop notification functionality.
* The Python standard library for its excellent built-in modules like `json`, `os`, and `datetime`.

---

Enjoy managing your tasks! 🚀

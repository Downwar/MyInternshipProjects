class Task:
    def __init__(self, description, due_date, priority):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date, priority):
        new_task = Task(description, due_date, priority)
        self.tasks.append(new_task)
        print("Task added successfully!")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for index, task in enumerate(self.tasks):
                print(f"Task {index + 1}: {task.description} - Due: {task.due_date} - Priority: {task.priority} - Completed: {task.completed}")

    def mark_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].completed = True
            print("Task marked as completed.")
        else:
            print("Invalid task index.")

    def update_task(self, task_index, new_description, new_due_date, new_priority):
        if 0 <= task_index < len(self.tasks):
            task = self.tasks[task_index]
            task.description = new_description
            task.due_date = new_due_date
            task.priority = new_priority
            print("Task updated successfully.")
        else:
            print("Invalid task index.")

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
            print("Task removed from the list.")
        else:
            print("Invalid task index.")

todo_list = ToDoList()

while True:
    print("\n===== To-Do List Menu =====")
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Mark Task as Completed")
    print("4. Update Task")
    print("5. Remove Task")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        description = input("Enter task description: ")
        due_date = input("Enter due date: ")
        priority = input("Enter priority: ")
        todo_list.add_task(description, due_date, priority)

    elif choice == "2":
        todo_list.display_tasks()

    elif choice == "3":
        index = int(input("Enter the task index to mark as completed: ")) - 1
        todo_list.mark_completed(index)

    elif choice == "4":
        index = int(input("Enter the task index to update: ")) - 1
        description = input("Enter new description: ")
        due_date = input("Enter new due date: ")
        priority = input("Enter new priority: ")
        todo_list.update_task(index, description, due_date, priority)

    elif choice == "5":
        index = int(input("Enter the task index to remove: ")) - 1
        todo_list.remove_task(index)

    elif choice == "6":
        break

    else:
        print("Invalid choice. Please enter a valid option.")

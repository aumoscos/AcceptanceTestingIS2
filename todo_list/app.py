class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"name": task, "status": "Pending"})

    def get_tasks(self):
        return [(task["name"], task["status"]) for task in self.tasks]

    def mark_task_completed(self, task_name):
        for task in self.tasks:
            if task["name"] == task_name:
                task["status"] = "Completed"
                break

    def clear_tasks(self):
        self.tasks = []

    def delete_task(self, task_name):
        self.tasks = [task for task in self.tasks if task["name"] != task_name]

    def mark_all_completed(self):
        for task in self.tasks:
            task["status"] = "Completed"


def main():
    todo_list = TodoList()

    while True:
        print("\nTodo List Menu:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Completed")
        print("4. Clear Entire Todo List")
        print("5. Delete a Task")
        print("6. Mark All Tasks as Completed")
        print("7. Quit")

        choice = input("Enter your choice (1/2/3/4/5/6/7): ")

        if choice == "1":
            task_name = input("Enter task name: ")
            todo_list.add_task(task_name)
            print(f"Task '{task_name}' added.")
        elif choice == "2":
            tasks = todo_list.get_tasks()
            if tasks:
                print("\nTasks:")
                for task_name, status in tasks:
                    status_mark = 'X' if status == 'Completed' else ''
                    print(f"- {task_name} [{status_mark}]")
            else:
                print("No tasks in the list.")
        elif choice == "3":
            task_name = input("Enter task name to mark as completed: ")
            todo_list.mark_task_completed(task_name)
            print(f"Task '{task_name}' marked as completed.")
        elif choice == "4":
            todo_list.clear_tasks()
            print("Todo list cleared.")
        elif choice == "5":
            task_name = input("Enter task name to delete: ")
            todo_list.delete_task(task_name)
            print(f"Task '{task_name}' deleted.")
        elif choice == "6":
            todo_list.mark_all_completed()
            print("All tasks marked as completed.")
        elif choice == "7":
            print("Exiting Todo List. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, 6, or 7.")


if __name__ == "__main__":
    main()

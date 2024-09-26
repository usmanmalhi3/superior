class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f'Task added: "{task}"')

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f'Task removed: "{removed_task["task"]}"')
        else:
            print("Invalid task index.")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            print(f'Task completed: "{self.tasks[index]["task"]}"')
        else:
            print("Invalid task index.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
            return
        for index, task in enumerate(self.tasks):
            status = "✓" if task["completed"] else "✗"
            print(f'{index + 1}. [{status}] {task["task"]}')

def main():
    todo_list = ToDoList()
    
    while True:
        print("\n*** To-Do List Menu ***")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Complete Task")
        print("4. View Tasks")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
            index = int(input("Enter the task number to remove: ")) - 1
            todo_list.remove_task(index)
        elif choice == '3':
            todo_list.view_tasks()
            index = int(input("Enter the task number to complete: ")) - 1
            todo_list.complete_task(index)
        elif choice == '4':
            todo_list.view_tasks()
        elif choice == '5':
            print("Exiting the To-Do List. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

main()

'''

Project Requirements

User Interface (UI):
Create a command-line interface (CLI) for the To-Do List Application.
Display a welcoming message and a menu with the following options:
Welcome to the To-Do List App!

Menu:
1. Add a task
2. View tasks
3. Mark a task as complete
4. Delete a task
5. Quit
To-Do List Features:
Implement the following features for the To-Do List:
Adding a task with a title (by default “Incomplete”).
Viewing the list of tasks with their titles and statuses (e.g., "Incomplete" or "Complete").
Marking a task as complete.
Deleting a task.
Quitting the application.
User Interaction:
Allow users to interact with the application by selecting menu options using input().
Implement input validation to handle unexpected user input gracefully.
Error Handling:
Implement error handling using try, except, else, and finally blocks to handle potential issues.
Code Organization:
Organize your code into functions to promote modularity and readability.
Use meaningful function names with appropriate comments and docstrings for clarity.
Testing and Debugging:
Thoroughly test your application to identify and fix any bugs.
Consider edge cases, such as empty task lists or incorrect user input.
Documentation:
Include a README file that explains how to run the application and provides a brief overview of its features.
Optional Features (Bonus):
If you feel adventurous, you can add extra features like task priorities, due dates, or color-coding tasks based on their status.

'''
# All in one task 


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title="Incomplete"):
        self.tasks.append({"title": title, "status": "Incomplete"})

    def view_tasks(self):
        if self.tasks:
            print("Tasks:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task['title']} - {task['status']}")
        else:
            print("No tasks.")

    def mark_task_complete(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1]["status"] = "Complete"
            print("Task marked as complete.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            del self.tasks[task_number - 1]
            print("Task deleted.")
        else:
            print("Invalid task number.")

def display_menu():
    print("Welcome to the To-Do List App!")
    print("Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")

def get_user_input(prompt):
    while True:
        try:
            user_input = input(prompt)
            return user_input
        except KeyboardInterrupt:
            print("\nExiting...")
            exit()
        except:
            print("Invalid input. Please try again.")

def main():
    todo_list = TodoList()

    while True:
        display_menu()
        choice = get_user_input("Enter your choice: ")

        if choice == "1":
            task_title = get_user_input("Enter task title (optional, default is 'Incomplete'): ")
            todo_list.add_task(task_title)
            print("Task added successfully!")
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_number = int(get_user_input("Enter task number to mark as complete: "))
            todo_list.mark_task_complete(task_number)
        elif choice == "4":
            task_number = int(get_user_input("Enter task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == "5":
            print("Thank you for using the To-Do List App!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
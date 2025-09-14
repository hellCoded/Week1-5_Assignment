import json
import os

class TodoApp:
    def __init__(self, filename="todos.json"):
        self.filename = filename
        self.todos = self.load_todos()

    def load_todos(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                return json.load(f)
        return []

    def save_todos(self):
        with open(self.filename, "w") as f:
            json.dump(self.todos, f, indent=4)

    def add_todo(self):
        todo = input("Enter a new todo: ").strip()
        if todo:
            self.todos.append({"task": todo, "done": False})
            self.save_todos()
            print(f'Todo "{todo}" added.')
        else:
            print("⚠️ Empty task not added.")

    def view_todos(self):
        if not self.todos:
            print("No todos found.")
        else:
            print("\nYour todos:")
            for idx, todo in enumerate(self.todos, start=1):
                status = "✅" if todo["done"] else "❌"
                print(f"{idx}. {todo['task']} [{status}]")

    def delete_todo(self):
        self.view_todos()
        if self.todos:
            try:
                idx = int(input("Enter the number of the todo to delete: ")) - 1
                if 0 <= idx < len(self.todos):
                    removed = self.todos.pop(idx)
                    self.save_todos()
                    print(f'Todo "{removed["task"]}" deleted.')
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a valid number.")

    def complete_todo(self):
        self.view_todos()
        if self.todos:
            try:
                idx = int(input("Enter the number of the todo to mark as complete: ")) - 1
                if 0 <= idx < len(self.todos):
                    self.todos[idx]["done"] = True
                    self.save_todos()
                    print(f'Todo "{self.todos[idx]["task"]}" marked as complete ✅")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a valid number.")

    def run(self):
        actions = {
            "1": self.add_todo,
            "2": self.view_todos,
            "3": self.delete_todo,
            "4": self.complete_todo,
        }

        while True:
            print("\nTodo List Menu:")
            print("1. Add Todo")
            print("2. View Todos")
            print("3. Delete Todo")
            print("4. Complete Todo")
            print("5. Exit")

            choice = input("Choose an option (1-5): ").strip()

            if choice in actions:
                actions[choice]()
            elif choice == "5":
                print("Exiting the todo list application.")
                break
            else:
                print("Invalid choice. Please choose a number between 1 and 5.")

if __name__ == "__main__":
    app = TodoApp()
    app.run()

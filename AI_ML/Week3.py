todos= []


def add_todo():
    todo = input("Enter a new todo: ")
    todos.append(todo)
    print(f'Todo "{todo}" added.')
    
def view_todos():
    if not todos:
        print("No todos found.")
    else:
        print("Your todos:")
        for idx, todo in enumerate(todos, start=1):
            print(f"{idx}. {todo}")
    
def delete_todo():
    view_todos()
    if todos:
        try:
            idx = int(input("Enter the number of the todo to delete: ")) - 1
            if 0 <= idx < len(todos):
                removed = todos.pop(idx)
                print(f'Todo "{removed}" deleted.')
            else:
                print("Invalid number.")
        except ValueError:
            print("Please enter a valid number.")
def complete_todo():
    view_todos()
    if todos:
        try:
            idx = int(input("Enter the number of the todo to mark as complete: ")) - 1
            if 0 <= idx < len(todos):
                print(f'Todo "{todos[idx]}" marked as complete.')
                todos.pop(idx)
            else:
                print("Invalid number.")
        except ValueError:
            print("Please enter a valid number.")   
def main():
    while True:
        print("\nTodo List Menu:")
        print("1. Add Todo")
        print("2. View Todos")
        print("3. Delete Todo")
        print("4. Complete Todo")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            add_todo()
        elif choice == '2':
            view_todos()
        elif choice == '3':
            delete_todo()
        elif choice == '4':
            complete_todo()
        elif choice == '5':
            print("Exiting the todo list application.")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 5.")
if __name__ == "__main__":
    main()
    
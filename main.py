import functions
import time

now = time.strftime("%d. %-m. %Y, %H:%M:%S")
print("The time is below:")
print(f"It is {now}")

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos)

        print(f'"{todo}" was added to todos.')

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        # new_todos = [item.strip('\n') for item in todos] # list comprehensions

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}. {item.capitalize()}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            old_todo = todos[number]
            old_todo = old_todo.strip("\n")
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            functions.write_todos(todos)

            print(
                f'Todo "{old_todo.capitalize()}" was changed to "{new_todo.capitalize()}"'
            )
        except ValueError:
            print("Your command is not valid.")
            continue
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            functions.write_todos(todos)

            message = f'Todo "{todo_to_remove.capitalize()}" was removed from the list.'
            print(message)
        except IndexError:
            print("There is no item wth that number!")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid!")

print("Bye!")

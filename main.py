# This function displays the main menu, from where the user chooses his actions.
def main_menu():
    print()
    print("===== To-Do List Menu ===== \n"
          "1. Add a new task \n"
          "2. Mark a task as completed \n"
          "3. View all tasks\n"
          "4. Quit")


# This function adds a new task to the list of tasks, giving it a starting value of False, until it is completed.
def add_new_task():
    new_task = [input("Enter your new task: "), False]
    all_tasks.append(new_task)


# This function marks a task as completed, changing the starting value of a task to True, which determines if the task
# is completed or not. That changes the way the task is visualized in the task lists(either with [] or [X]).
def mark_task_as_completed():
    print("===== Tasks =====")
    for index, task in enumerate(all_tasks):
        if task[1]:
            print(f"{index}. [X] {task[0]}")
        else:
            print(f"{index}. [] {task[0]}")

    completed_task = input("Enter the index of the task to mark as completed: ")
    if int(completed_task) > len(all_tasks):
        print("Task index does not exist!")
    else:
        for task in all_tasks:
            if int(completed_task) == all_tasks.index(task) and task[1] is False:
                task[1] = True
                print("Task marked as completed!")
            elif int(completed_task) == all_tasks.index(task) and task[1]:
                print("Task already completed!")


# This function visualizes all tasks with their proper status and index.
def view_all_tasks():
    print(f"These are your tasks:\n"
          f"===== Tasks =====")
    for task in all_tasks:
        if task[1]:
            print(f"{all_tasks.index(task)}. [X] {task[0]}")
        else:
            print(f"{all_tasks.index(task)}. [] {task[0]}")


all_tasks = []
while True:
    main_menu()
    user_choice = int(input("Enter your choice (1-4): "))
    if user_choice == 1:
        add_new_task()
    elif user_choice == 2:
        mark_task_as_completed()
    elif user_choice == 3:
        view_all_tasks()
    elif user_choice == 4:
        print("Thank you for using the app!")
        break
    else:
        print("Please select a valid number!")

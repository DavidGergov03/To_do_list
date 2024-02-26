def main_menu():
    """Displays the main menu, from where the user chooses his actions."""
    print()
    print("===== To-Do List Menu =====\n"
          "1. Add a new task\n"
          "2. Mark a task as completed\n"
          "3. View all tasks\n"
          "4. Quit")


def add_new_task():
    """Adds a new task to the list of tasks, starting value of False, until completed."""
    new_task = [input("Enter your new task: "), False]
    all_tasks.append(new_task)


def mark_task_as_completed():
    """Marks a task as completed, changes the starting value to True.
    True, task is completed [X].
    False, task is not completed [].
    """

    print("===== Tasks =====")
    for index, task in enumerate(all_tasks):
        if task[1]:
            print(f"{index}. [X] {task[0]}")
        else:
            print(f"{index}. [ ] {task[0]}")

    completed_task = input("Enter the index of the task to mark as completed: ")
    if int(completed_task) > len(all_tasks) or int(completed_task) < 0:
        print("Task index does not exist!")
        return
    retrieved_task = all_tasks[int(completed_task)]
    if not retrieved_task[1]:
        retrieved_task[1] = True
        print("Task marked as completed!")
        return
    print("Task already completed!")


def view_all_tasks():
    """Visualizes all tasks with their proper status and index."""
    print("These are your tasks:\n"
          "===== Tasks =====")
    for index, task in enumerate(all_tasks):
        if task[1]:
            print(f"{index}. [X] {task[0]}")
            continue
        print(f"{index}. [ ] {task[0]}")


all_tasks = []

actions = {
    1: add_new_task,
    2: mark_task_as_completed,
    3: view_all_tasks,
    4: lambda: print("Thank you for using the app!")
}
user_choice = 0
while user_choice != 4:
    main_menu()
    user_choice = int(input("Enter your choice (1-4): "))
    match user_choice:
        case 1 | 2 | 3 | 4:
            actions[user_choice]()
        case _:
            print("Please select a valid number!")

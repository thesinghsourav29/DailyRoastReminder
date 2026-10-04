tasks = []


# =========================
# ADD TASK
# =========================

def add_task():

    task_name = input("Enter task: ")
    task_time = input("Enter time: ")

    task = {
        "name": task_name,
        "time": task_time,
        "completed": False
    }

    tasks.append(task)

    print("✅ Task added!")


# =========================
# VIEW TASKS
# =========================

def view_tasks():

    if len(tasks) == 0:
        print("📭 No tasks available.")
        return

    print("\nYour tasks:")

    for i in range(len(tasks)):

        if tasks[i]["completed"] == True:
            status = "✅ Completed"
        else:
            status = "⏳ Pending"

        print(
            i + 1,
            ".",
            tasks[i]["name"],
            "-",
            tasks[i]["time"],
            "-",
            status
        )


# =========================
# EDIT TASK
# =========================

def edit_task():

    view_tasks()

    if len(tasks) == 0:
        return

    edit_number = int(
        input("\nWhich task do you want to edit? ")
    )

    print("\n0. Cancel")

    if edit_number == 0:
        print("❌ Edit cancelled.")
        return

    new_name = input("Enter the new task name: ")

    tasks[edit_number - 1]["name"] = new_name

    print("✅ Task updated!")


# =========================
# DELETE TASK
# =========================

def delete_task():

    view_tasks()

    if len(tasks) == 0:
        return

    print("\n0. Cancel")

    delete_number = int(
        input("\nWhich task do you want to delete? ")
    )

    if delete_number == 0:
        print("❌ Delete cancelled.")
        return

    deleted_task = tasks.pop(delete_number - 1)

    print("🗑️ Deleted:", deleted_task["name"])


# =========================
# COMPLETE TASK
# =========================

def complete_task():

    view_tasks()

    if len(tasks) == 0:
        return

    print("\n0. Cancel")

    complete_number = int(
        input("\nWhich task did you complete? ")
    )

    if complete_number == 0:
        print("❌ Completion cancelled.")
        return

    tasks[complete_number - 1]["completed"] = True

    print("✅ Task completed!")


# =========================
# MAIN MENU
# =========================

while True:

    print("\n========================================")
    print("       🔥 DAILY ROAST REMINDER 🔥")
    print("========================================")

    print("\n1. ➕ Add Task")
    print("2. 👀 View Tasks")
    print("3. ✏️ Edit Task")
    print("4. 🗑️ Delete Task")
    print("5. ✅ Complete Task")
    print("6. 🚪 Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        edit_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        complete_task()

    elif choice == "6":
        print("\n👋 Goodbye!")
        break

    else:
        print("❌ Invalid option. Please choose 1-6.")
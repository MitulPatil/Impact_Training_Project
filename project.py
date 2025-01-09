class TaskManager:
    def __init__(self):
        self.pending_tasks = []  # Queue for pending tasks
        self.completed_tasks = []  # Stack for completed tasks

    # Add a task to the queue
    def add_task(self, task):
        self.pending_tasks.append(task)
        print(f"Task '{task}' added to pending tasks.")

    # View all pending tasks
    def view_pending_tasks(self):
        if not self.pending_tasks:
            print("No pending tasks!")
        else:
            print("\nPending Tasks:")
            for idx, task in enumerate(self.pending_tasks, 1):
                print(f"{idx}. {task}")

    # Mark a task as completed
    def complete_task(self):
        if not self.pending_tasks:
            print("No tasks to complete!")
        else:
            task = self.pending_tasks.pop(0)  # Dequeue
            self.completed_tasks.append(task)  # Push to stack
            print(f"Task '{task}' marked as completed.")

    # View all completed tasks
    def view_completed_tasks(self):
        if not self.completed_tasks:
            print("No completed tasks!")
        else:
            print("\nCompleted Tasks:")
            for idx, task in enumerate(reversed(self.completed_tasks), 1):
                print(f"{idx}. {task}")

    # Undo the last completed task
    def undo_completed_task(self):
        if not self.completed_tasks:
            print("No completed tasks to undo!")
        else:
            task = self.completed_tasks.pop()  # Pop from stack
            self.pending_tasks.insert(0, task)  # Enqueue at the front
            print(f"Task '{task}' moved back to pending tasks.")

# Main program
def main():
    manager = TaskManager()

    while True:
        print("\n=== Task Manager ===")
        print("1. Add Task")
        print("2. View Pending Tasks")
        print("3. Complete Task")
        print("4. View Completed Tasks")
        print("5. Undo Completed Task")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            task = input("Enter the task: ")
            manager.add_task(task)
        elif choice == "2":
            manager.view_pending_tasks()
        elif choice == "3":
            manager.complete_task()
        elif choice == "4":
            manager.view_completed_tasks()
        elif choice == "5":
            manager.undo_completed_task()
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
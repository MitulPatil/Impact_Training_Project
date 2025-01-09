# Task Manager Using Stack and Queue

## Problem Statement
Managing tasks efficiently is crucial in personal and professional life. Users often face challenges in keeping track of pending tasks, marking tasks as completed, and undoing mistakenly completed tasks. A simple yet effective system is needed to organize and manage tasks in a structured way.

## Description of the Project
The *Task Manager Using Stack and Queue* is a Python-based application designed to help users efficiently manage their tasks. The project utilizes two fundamental data structures:

1. *Queue*: To manage pending tasks in a FIFO (First In, First Out) order.
2. *Stack*: To handle completed tasks in a LIFO (Last In, First Out) order.

This structure allows users to:
- Add new tasks.
- View pending and completed tasks.
- Mark tasks as completed.
- Undo the last completed task.

The program offers a menu-based interface, making it user-friendly and easy to navigate.

## Solution
### Key Features
1. *Add Task*: Allows users to add new tasks to the pending queue.
2. *View Pending Tasks*: Displays all tasks in the pending queue.
3. *Complete Task*: Marks the first task in the pending queue as completed and moves it to the completed stack.
4. *View Completed Tasks*: Lists all tasks in the completed stack, showing the most recently completed tasks first.
5. *Undo Completed Task*: Moves the most recently completed task back to the pending queue.
6. *Exit*: Terminates the application.

### Data Structures Used
- *Queue*: Efficiently manages tasks in the order they are added.
- *Stack*: Provides an easy way to track and undo completed tasks.

### Implementation
The application is implemented in Python, using list data structures to mimic the behavior of a queue and a stack. The program provides a menu-driven interface for user interaction.

## Conclusion
The *Task Manager Using Stack and Queue* is an intuitive application demonstrating the practical use of data structures in managing tasks. By leveraging the strengths of stacks and queues, the application offers an organized and efficient way to track tasks. It is ideal for beginners to understand the fundamentals of these data structures and their real-world applications.

# Todo-App

A simple Python CLI Todo App built entirely on Android using Pydroid 3.

## Features
- Add new tasks with title and date
- View all tasks with completion status
- Mark tasks as complete
- JSON for data storage
- datetime module

## How to Run
```
python main.py
```

## Sample Output
```
1. Add Task
2. View Tasks
3. Complete Task
4. Exit
Choose: 1
Enter task title: Learn Python
Task added: Learn Python

Choose: 1
Enter task title: Build Todo App
Task added: Build Todo App

Choose: 2
--- MY TODO LIST ---
1. [ ] Learn Python - 2026-05-13
2. [ ] Build Todo App - 2026-05-13

Choose: 3
Enter task ID to complete: 1
Completed: Learn Python

Choose: 2
--- MY TODO LIST ---
1. [✓] Learn Python - 2026-05-13
2. [ ] Build Todo App - 2026-05-13

Choose: 4
Todo App working successfully!
```

## Tech Stack
- Python 3
- JSON for storage
- datetime module
- Pydroid 3 on Android

## Author
Wisdom Akpan - Built for Draft.dev portfolio.

## License
MIT License - See LICENSE file 
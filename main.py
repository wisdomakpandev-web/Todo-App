# ======================================
# Project: Todo-App - Python CLI Task Manager
# Author: Wisdom Akpan
# Based in: Akwa Ibom State, Nigeria
# Built on: Android with Pydroid 3
# License: MIT
# GitHub: github.com/wisdomakpandev-web
# ======================================

import json
import os
from datetime import datetime

class TodoApp:
    def __init__(self):
        self.tasks = []
        self.file = "tasks.json"
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file):
            with open(self.file, "r") as f:
                self.tasks = json.load(f)

    def save_tasks(self):
        with open(self.file, "w") as f:
            json.dump(self.tasks, f, indent=2)

    def add_task(self, task):
        date = datetime.now().strftime("%Y-%m-%d")
        self.tasks.append({"task": task, "done": False, "date": date})
        self.save_tasks()
        print(f"✓ Added: {task}")

    def show_tasks(self):
        print("\n--- MY TODO LIST ---")
        if not self.tasks:
            print("No tasks yet!")
        for i, t in enumerate(self.tasks, 1):
            status = "✓" if t["done"] else " "
            print(f"{i}. [{status}] {t['task']} - {t['date']}")

    def complete_task(self, num):
        if 1 <= num <= len(self.tasks):
            self.tasks[num-1]["done"] = True
            self.save_tasks()
            print(f"✓ Completed task {num}")
        else:
            print("Invalid task number")

# Demo
app = TodoApp()
app.add_task("Learn Python")
app.add_task("Build Todo App")
app.add_task("Apply for Draft.dev")
app.show_tasks()
app.complete_task(1)
app.show_tasks()
print("\nTodo App working successfully!")

# Copyright (c) 2026 Wisdom Akpan
# Based in Akwa Ibom State, Nigeria
# Licensed under MIT License
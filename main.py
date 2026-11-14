# Simple Todo App - Python CLI Project
# Built on Android with Pydroid 3

class TodoApp:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})
        print(f"✓ Added: {task}")

    def show_tasks(self):
        print("\n--- MY TODO LIST ---")
        if not self.tasks:
            print("No tasks yet!")
        for i, t in enumerate(self.tasks, 1):
            status = "✓" if t["done"] else " "
            print(f"{i}. [{status}] {t['task']}")

    def complete_task(self, num):
        if 1 <= num <= len(self.tasks):
            self.tasks[num-1]["done"] = True
            print(f"✓ Completed task {num}")
        else:
            print("Invalid task number")

# Demo - this will run and you can screenshot
app = TodoApp()
app.add_task("Learn Python")
app.add_task("Build Todo App")
app.add_task("Apply for Draft.dev")
app.show_tasks()
app.complete_task(1)
app.show_tasks()
print("\nTodo App working successfully!")
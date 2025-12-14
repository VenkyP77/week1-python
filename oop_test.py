class Task:
    # 1. Constructor (__init__)
    def __init__(self, title, priority):
        self.title = title  # Instance variable (unique to this task)
        self.priority = priority
        self.completed = False

    # 2. Method (Function inside a class)
    def complete(self):
        self.completed = True
        print(f"Task '{self.title}' marked as done! ✅")

    # 3. String Representation (for printing)
    def __str__(self):
        status = "Done" if self.completed else "Pending"
        return f"[{self.priority}] {self.title} - {status}"


# Usage
task1 = Task("Learn Python OOP", "High")
task2 = Task("Buy Groceries", "Low")

task1.complete()

print(task1)
print(task2)

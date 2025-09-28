"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""

def has_duplicates(product_ids):
    ID = set()
    for id in product_ids:
        if id in ID:
            return True
        ID.add(id)
    return False

print(has_duplicates([10, 20, 30, 20, 40]))
print(has_duplicates([1, 2, 3, 4, 5]))

# Justification:
# I used sets because they give O(1) average time lookups and insertions. It checks the ID's given to detect duplicates and inserts them into the set telling if a duplicate is found.

"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""

class TaskQueue:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_oldest_task(self):
        if self.tasks:
            return self.tasks.pop(0)
        return None

task_queue = TaskQueue()

task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")

print(task_queue.remove_oldest_task())
print(task_queue.remove_oldest_task())
print(task_queue.remove_oldest_task())

# Justification:
# I used a list in this case because it mantains the order of insertion as they are added. It appends tasks to the end and removes tasks from the front. 

"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""

class UniqueTracker:
    def __init__(self):
        self.unique_values = set()

    def add(self, value):
        self.unique_values.add(value)

    def get_unique_count(self):
        return len(self.unique_values)

tracker = UniqueTracker()

tracker.add(10)
tracker.add(20)
tracker.add(10)

print(tracker.get_unique_count())

# Justification:
# For this problem I used a set, as it handles the duplicate values automatically. It adds the value of the set and returns the number of unique values.
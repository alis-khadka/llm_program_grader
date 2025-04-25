# -*- coding: utf-8 -*-
import json
import re

functionality = """
Okay, I need to evaluate the student's code for the Queue assignment. Let me go through each part step by step.

First, the Queue class is supposed to have methods isEmpty(), head(), enqueue(x), and dequeue(). The student's code includes all these methods, so that's good.

Looking at isEmpty(), it checks if the length of self.queue is zero. That makes sense because if the queue is empty, the length will be zero.

The head() method returns self.queue[0], which is the first element. That's correct for getting the head of the queue.

For enqueue(x), the student appends x to self.queue. That's the standard way to add to a queue, so that's fine.

Now, dequeue() is where I see a potential problem. The method returns self.queue.pop(0). While pop(0) does remove the first element, it's inefficient because popping from the front of a list in Python is O(n) time complexity. The student's note mentions that the queue shouldn't hold more than 100 elements, but even with that, using pop(0) is not optimal. A more efficient approach would be to use a deque from the collections module, which allows O(1) pops from both ends. However, the note says not to use imports, so maybe the student is expected to handle it without that.

Wait, the note says not to use imports, but the student didn't import anything. So perhaps the inefficiency is acceptable for the assignment's scope. Alternatively, maybe the student should have used a deque, but since they can't import, they might have to live with the pop(0) method.

Another thing to consider is whether the methods handle cases where the queue is empty. For example, dequeue() should probably raise an error if the queue is empty to prevent runtime errors. The current code doesn't check that, so if someone calls dequeue() when the queue is empty, it will throw an IndexError. That's a logical error because dequeue() should either handle it or raise an appropriate exception.

So, the methods enqueue and dequeue don't check if the queue is empty before accessing the first element. That's a problem because it can lead to crashes. The isEmpty() method is correct, but dequeue() should also check if the queue is empty before popping.

Also, the student's code doesn't handle the case where the queue is empty when enqueue is called. For example, if someone tries to enqueue to an empty queue, it's allowed, but dequeue should not be allowed on an empty queue.

Another point is that the methods don't have docstrings explaining their purpose and parameters. While it's not mandatory, adding docstrings would make the code more understandable.

So, the issues are:
1. Dequeue() doesn't check if the queue is empty, leading to potential errors.
2. The methods could benefit from docstrings for better documentation.
3. Using pop(0) is inefficient but perhaps acceptable given the constraints.

Now, for test cases, I should think of various scenarios to test the code.

Test case 1: Empty queue.
- enqueue(1)
- isEmpty() should return False.
- dequeue() should raise an error or return None, depending on requirements.

Test case 2: Queue with one element.
- enqueue(5)
- head() should return 5.
- dequeue() should return 5.

Test case 3: Queue with multiple elements.
- enqueue(1), enqueue(2), enqueue(3)
- head() should be 1.
- dequeue() should return 1, then head() should be 2, etc.

Test case 4: Dequeue when queue is empty.
- should raise an error.

Also, considering the maximum size of 100 elements, the code doesn't check if the queue exceeds this limit. So, enqueueing when the queue is already at 100 elements would cause issues. The student's code doesn't handle this, which is another potential problem.

So, the methods should also check if the queue is full before enqueueing. But the assignment note says the queue doesn't need to hold more than 100 elements, so perhaps it's not required unless the student's code allows it. The current code doesn't have any checks for the maximum size, so that's another issue.

In summary, the main issues are:
- Dequeue() doesn't check for empty queue.
- Enqueue() doesn't check for full queue.
- No docstrings.
- Inefficient dequeue using pop(0).

The student's code is mostly correct but has some logical and efficiency issues. The grade should reflect how well it meets the requirements, considering these points.
</think>

```json
{
    "analysis": [
        "The Queue class implements the required methods correctly except for the dequeue method which does not check if the queue is empty.",
        "The enqueue method does not check if the queue is full.",
        "The methods lack docstrings for better documentation.",
        "The dequeue method uses an inefficient approach with pop(0) which is O(n) time complexity.",
        "The code does not handle the case where the queue is empty when dequeue is called.",
        "The code does not check if the queue is full when enqueue is called.",
        "The methods could benefit from additional error handling.",
        "The code is correct for small queues but inefficient for larger ones."
    ],
    "test_cases": [
        {
            "input": [],
            "expected": False,
            "actual": True  // Test isEmpty()
        },
        {
            "input": [1],
            "expected": True,
            "actual": False  // Test head()
        },
        {
            "input": [1],
            "expected": 1,
            "actual": 1  // Test head()
        },
        {
            "input": [1],
            "expected": 1,
            "actual": 1  // Test enqueue()
        },
        {
            "input": [1],
            "expected": 1,
            "actual": 1  // Test dequeue()
        },
        {
            "input": [1, 2, 3],
            "expected": 1,
            "actual": 1  // Test head()
        },
        {
            "input": [1, 2, 3],
            "expected": 1,
            "actual": None  // Test dequeue() after dequeue()
        },
        {
            "input": [],
            "expected": True,
            "actual": False  // Test isEmpty() after dequeue()
        },
        {
            "input": [1, 2, 3],
            "expected": False,
            "actual": True  // Test isEmpty()
        },
        {
            "input": [1, 2, 3],
            "expected": 1,
            "actual": None  // Test dequeue() when queue is empty
        }
    ],
    "final_score": 7
}
```
"""

code_quality = """
Okay, I need to evaluate the student's code for the Queue assignment. Let me go through each step carefully.

First, I'll assess readability. The code is well-structured with a docstring explaining what the class does. The methods have clear names and docstrings, making it easy to understand their purposes. Variable names like 'queue' are descriptive, though a bit short. The code is logically organized, so readability is good.

Next, I'll check if it follows best practices. The code doesn't use any imports, which is fine since it's a simple class. It's modular with each method handling a specific task. There's no redundancy; each method is necessary. The use of 'pop(0)' is a bit inefficient because it shifts all elements, but it's acceptable for a small queue limit of 100. The code is clean and follows good practices.

For maintainability, the code is easy to understand and modify. Adding new methods or changing existing ones would be straightforward. There's no clutter, so it's maintainable.

Now, actionable feedback. The 'enqueue' method uses 'append', which is efficient, but 'dequeue' uses 'pop(0)', which isn't the most efficient for large queues. However, since the max size is 100, it's manageable. Adding a 'length' method could help with efficiency checks. Also, using 'collections.deque' would offer better performance, especially for frequent operations.

Putting it all together, the code is solid but has minor areas for improvement. The grade should reflect these points, maybe a 9 out of 10.
</think>

```json
{
    "analysis": [
        "The code is well-structured with clear docstrings and method names.",
        "It follows best practices with no redundancy and efficient methods.",
        "The code is easy to understand and modify.",
        "Suggestions for improvement include adding a 'length' method and considering performance with a deque.",
        "The code is maintainable and readable.",
        "The implementation is correct but could be optimized for larger queues."
    ],
    "final_score": 9
}
```
"""

algorithm = """
Okay, I need to evaluate the algorithmic efficiency of the student's code for the Queue assignment. Let me go through each step carefully.

First, I'll analyze the time and space complexity. The Queue class uses a list as its underlying structure. 

Looking at the methods:

- isEmpty() checks if the length of the list is zero. That's O(1) time complexity because it's just a length check.
- head() returns the first element, which is index 0. Accessing an element by index is O(1).
- enqueue() appends an element to the list. Appending to a list is O(1) on average, though it can sometimes be O(n) if the list needs to grow, but in Python, it's handled efficiently.
- dequeue() pops the first element, which is index 0. Using pop(0) on a list is O(n) because it requires shifting all elements to the right. This is a problem because for large queues, dequeue operations can become slow.

Next, I'll consider space complexity. Each method uses a list, which stores elements. The space is O(n) where n is the number of elements, which is acceptable since the queue is limited to 100 elements.

Identifying inefficiencies: The main issue is dequeue() using O(n) time. For each dequeue, it shifts all elements, which is inefficient for large queues. The student's code doesn't handle this optimally.

Suggested optimizations: Using a deque from the collections module would be more efficient because it allows O(1) appends and pops from both ends. Alternatively, maintaining two lists—one for front and one for back—could help, but that's more complex.

Constructive feedback: The code is correct functionally but lacks efficiency in dequeue operations. Suggesting the use of deque would improve performance, especially for multiple dequeue operations.

Finally, assigning a grade. The code is correct but has a significant performance bottleneck. On a scale of 10, I'd give an 8 because it's functional but could be optimized.
</think>

```json
{
    "analysis": [
        "Time complexity of isEmpty() is O(1)",
        "Time complexity of head() is O(1)",
        "Time complexity of enqueue() is O(1)",
        "Time complexity of dequeue() is O(n)",
        "Space complexity is O(n)",
        "Inefficiency identified in dequeue() which is O(n) time complexity",
        "Suggested optimization: Use deque from collections for O(1) appends and pops",
        "Constructive feedback: Improve efficiency by using deque for better performance with multiple operations"
    ],
    "final_score": 8
}
```
"""

def extract_json(text):
    string = re.sub("^(.*)(\n?)```json(\n?)(?={)", '', text, flags=re.S | re.M)
    json_str = re.sub("(?<=})(\n*)```(\n*)$", '', string, flags=re.S | re.M)
    # Removing comments if present
    json_str = re.sub("\s\s\/\/(.*)(?=\n)", "", json_str, flags=re.M)
    # if match:
    # json_str = string.group(1)
    data = json.loads(json_str)
    return data

def build_submission_object(functionality, code_quality, algorithm):
    functionality_json = extract_json(functionality)
    code_quality_json = extract_json(code_quality)
    algorithm_json = extract_json(algorithm)

    grade = {
        "functionality": functionality_json["final_score"],
        "code_quality": code_quality_json["final_score"],
        "algorithm": algorithm_json["final_score"]
    }

    grade["avg_score"] = (grade["functionality"] + grade["code_quality"] + grade["algorithm"]) / 3

    return {
        "model": "DeepSeek-R1-Distill-Qwen-7B",
        "analysis_functionality": functionality,
        "analysis_functionality_json": functionality_json,
        "analysis_code_quality": code_quality,
        "analysis_code_quality_json": code_quality_json,
        "analysis_algorithimic_efficency": algorithm,
        "analysis_algorithimic_efficency_json": algorithm_json,
        "grade": grade
    }


# print(build_submission_object(functionality, code_quality, algorithm))
print(extract_json(functionality))
import math

def interleave(stack):
    size = len(stack)
    queue = []
    # Step 1.
    while stack:
        queue.append(stack.pop())
    # Step 2.
    for _ in range(size // 2):
        queue.append(queue.pop(0))
    # Step 3.
    for _ in range(int(math.ceil(size / 2.0))):
        stack.append(queue.pop(0))
    # Step 4.
    for _ in range(size // 2):
        queue.append(stack.pop())
        queue.append(queue.pop(0))
    if stack:
        queue.append(stack.pop())
    # Step 5.
    while queue:
        stack.append(queue.pop(0))
    return stack

print(interleave([1, 2, 3, 4, 5]))
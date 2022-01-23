def slidingWindowMinimum(arr, n):
    if not arr:
        return None
    queue = []
    for i in range(0, n):
        while len(queue) > 0 and queue[len(queue) - 1] > arr[i]:
            del queue[-1]
        queue.append(arr[i])
    for i
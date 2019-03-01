def nearestSmallestElements(arr):
    if not arr:
        return None
    queue = [arr[0]]
    for i in range(1, len(arr)):
        while len(queue) > 0 and queue[len(queue) - 1] > arr[i]:
            del queue[-1]
        queue.append(arr[i])
    return queue


arr = [1, 3, 4, 2, 5, 3, 4, 2]
print(nearestSmallestElements(arr))

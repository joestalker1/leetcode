import json

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def arrayToTreeNode(inputValues):
    root = TreeNode(inputValues[0])
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item is not None:
            leftNumber = item
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item is not None:
            rightNumber = item
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

#list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#API
def arrayToListNode(numbers):

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def listNodeToArray(nodes):
    if not nodes:
        return []
    p = nodes
    arr = []
    while p:
        arr.append(p.val)
        p = p.next
    return arr

def stringToIntegerList(input):
    return json.loads(input)

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


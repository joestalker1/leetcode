from sortedcontainers import SortedList

lst= SortedList()
lst.add(1)
lst.add(1)
lst.add(2)
lst.add(2)
print(lst[-1])
print(lst[0])
lst.remove(1)
lst.remove(2)
print(lst[-1])
print(lst[0])

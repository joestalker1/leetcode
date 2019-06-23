n = int(input())
s = input()
arr = s.split()
brackets = []
for i in range(len(arr)):
    a = int(arr[i])
    brackets.append(a)

nesting_depth = 0
pos1 = 0
max_len = 0
pos2 = 0


def match_brackets(brackets):
    global nesting_depth, pos1, max_len, pos2
    stack = []
    i = 0
    while i < len(brackets):
        if brackets[i] == 1:
            stack.append(i)
            if nesting_depth < len(stack):
                nesting_depth = len(stack)
                pos1 = i
        else:
            j = stack.pop()
            if (i - j + 1) > max_len:
                max_len = i - j + 1
                pos2 = j
        i += 1

match_brackets(brackets)
print('{} {} {} {}'.format(nesting_depth, pos1+1, max_len, pos2+1))

        

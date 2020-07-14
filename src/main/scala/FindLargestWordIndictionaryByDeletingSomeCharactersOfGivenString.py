def is_subsequence(S, W):
    # W is a subsequence
    j = 0
    for i in range(len(S)):
        if j < len(W) and S[i] == W[j]:
            j += 1
        if j == len(W):
            return True
    return False

def findLargestWord(dict, word):
    dict.sort(key=lambda x:len(x), reverse=True)

    for w in dict:
        if is_subsequence(word, w):
            return w
    return None

print(findLargestWord(["pintu", "geeksfor", "geeksgeeks", "forgeek"], "geeksforgeeks"))
print(findLargestWord(["ale", "apple", "monkey", "plea"], "abpcplea"))

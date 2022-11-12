from typing import *

def completeString(n: int, a: List[str])-> str:
    a.sort(key=lambda x:(len(x), x))
    seen_words = set()
    min_res = None
    for word in a:
        present = True
        for i in range(len(word)-1):
            prefix = word[0:i + 1]
            if prefix not in seen_words:
                present = False
                break
        seen_words.add(word)
        if present:
            if not min_res:
                min_res = word
            elif len(min_res) == len(word) and word < min_res or len(min_res) < len(word):
                min_res = word
    return min_res


print(completeString(6,['n', 'ni', 'nin', 'ninj', 'ninja', 'ninga']))

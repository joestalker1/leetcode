from collections import defaultdict

class FreqStack:

    def __init__(self):
        self.max_freq = 0
        self.item_to_freq = defaultdict(int)
        self.freq_to_item = defaultdict(list)

    def push(self, val: int) -> None:
        self.item_to_freq[val] += 1
        freq = self.item_to_freq[val]
        self.max_freq = max(freq, self.max_freq)
        self.freq_to_item[freq].append(val)

    def pop(self) -> int:
        val = self.freq_to_item[self.max_freq].pop()
        self.item_to_freq[val] = self.max_freq - 1
        if len(self.freq_to_item[self.max_freq]) == 0:
            del self.freq_to_item[self.max_freq]
            self.max_freq -= 1
        return val
#"push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
#[[], [5], [7], [5], [7], [4], [5], [], [], [], []]
freqStack = FreqStack()
freqStack.push(5)
freqStack.push(7)
freqStack.push(5)
freqStack.push(7)
freqStack.push(4)
freqStack.push(5)
print(freqStack.pop())#5
print(freqStack.pop())#7
print(freqStack.pop())#5
print(freqStack.pop())#4
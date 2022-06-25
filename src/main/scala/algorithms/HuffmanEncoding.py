from collections import Counter,defaultdict
from heapq import heappop,heappush,heapify
from functools import total_ordering

@total_ordering
class HuffNode:
    def __init__(self, freq, symbol, left=None, right=None):
        # frequency of symbol
        self.freq = freq

        # symbol name (character)
        self.symbol = symbol

        # node left of current node
        self.left = left

        # node right of current node
        self.right = right

        # tree direction (0/1)
        self.huff = ''

    def __lt__(self, other):
        return self.freq < other.freq

def huffman_encode(node, buf, res):
    new_buf = buf + node.huff
    if node.left:
        huffman_encode(node.left, new_buf, res)
    if node.right:
        huffman_encode(node.right, new_buf,res)
    if not node.left and not node.right:
        res[node.symbol] = new_buf[::]

def solve(s):
    freq = Counter(s)
    q = []
    for ch in freq:
        n = HuffNode(freq[ch], ch)
        heappush(q,n)
    while len(q) > 1:
        left = heappop(q)
        right = heappop(q)
        left.huff = '0'
        right.huff = '1'
        node = HuffNode(left.freq + right.freq, left.symbol+right.symbol,left,right)
        heappush(q, node)
    root = q[0]
    res = defaultdict(lambda :'')
    huffman_encode(root, '', res)
    print(res)

solve('aaaaabcd')







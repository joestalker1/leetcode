def read4(buf):
    return 0


class Solution:
    def __init__(self):
        self.buf = [0] * 4

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        r = n // 4
        j = 0
        for k in range(r):
            read = read4(self.buf)
            for k in range(read):
                buf[j + k] = self.buf[k]
            j += read
        r = n % 4
        if r > 0:
            read = read4(self.buf)
            for k in range(min(r, read)):
                buf[j + k] = self.buf[k]
            j += read
        return j


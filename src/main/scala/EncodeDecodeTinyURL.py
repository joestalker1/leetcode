class Codec:
    def __init__(self):
        self.key = [0] * 6
        self.encodedToUrl = {}

    def next(self):
        arr = [0] * len(self.key)
        for i in range(len(self.key)):
            arr[i] = self.key[i] + 65
        for i in range(len(self.key)):
            if arr[i] < 63:
                arr[i] += 1
        return ''.join(map(chr, arr))

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        if not longUrl:
            return ''
        key = self.next()
        self.encodedToUrl[key] = longUrl
        return 'http://tinyurl.com/{}'.format(key)

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        if not shortUrl:
            return None
        parts = shortUrl.split('/')
        encoded = parts[len(parts) - 1]
        if encoded in self.encodedToUrl:
            return self.encodedToUrl[encoded]
        return None


codec = Codec()
print(codec.encode('https://leetcode.com/problems/design-tinyurl'))
print(codec.decode(codec.encode('https://leetcode.com/problems/design-tinyurl')))



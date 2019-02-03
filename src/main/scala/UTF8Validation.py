class Solution:

    def is_header(self, a):
        return a & 0xe0 == 0xC0 or a & 0xF0 == 0xE0 or a & 0xF8 == 0xF0

    def char_size(self, a):
        if a & 0xe0 == 0xC0:
            return 2
        if a & 0xF0 == 0xE0:
            return 3
        if a & 0xF8 == 0xF0:
            return 4
        return 0

    def is_valid_part(self, a):
        return a & 0xc0 == 0x80

    def is_one_byte_char(self, a):
        return a & 0x80 == 0

    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        if not data or len(data) == 0:
            return False
        i = 0
        while i < len(data):
            b = data[i]
            if self.is_header(b):
                sz = self.char_size(b)
                for j in range(i + 1, i + sz):
                    if j == len(data):
                        return False
                    if not self.is_valid_part(data[j]):
                        print(b)
                        return False
                i += sz
            elif self.is_one_byte_char(b):
                i += 1
            else:
                return False
        return True


sol = Solution()
# true
print(sol.validUtf8(
    [194, 155, 231, 184, 185, 246, 176, 131, 161, 222, 174, 227, 162, 134, 241, 154, 168, 185, 218, 178, 229, 187, 139,
     246, 178, 187, 139, 204, 146, 225, 148, 179, 245, 139, 172, 134, 193, 156, 233, 131, 154, 240, 166, 188, 190, 216,
     150, 230, 145, 144, 240, 167, 140, 163, 221, 190, 238, 168, 139, 241, 154, 159, 164, 199, 170, 224, 173, 140, 244,
     182, 143, 134, 206, 181, 227, 172, 141, 241, 146, 159, 170, 202, 134, 230, 142, 163, 244, 172, 140, 191]
    ))

# false
# print(sol.validUtf8([39,89,227,83,132,95,10,0]))
# print(sol.validUtf8([197, 130, 1]))
# print(sol.validUtf8([235, 140, 4]))

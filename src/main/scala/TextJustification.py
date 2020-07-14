class Solution:
    def format_text(self, maxWidth, words, sentence, cur_len):
        if len(sentence) == 1:
            word = words[sentence[0]]
            return ''.join([word] + ([' '] * (maxWidth - len(word))))
        new_sentence = []
        is_last = sentence[-1] == (len(words) - 1)
        total_spaces = maxWidth - cur_len
        num_space = total_spaces // (len(sentence) - 1)
        space = ' ' if is_last else (' ' * num_space)
        rem = 0 if is_last else total_spaces % (len(sentence) - 1)
        for j in range(len(sentence)):
            if j > 0:
                new_sentence.append(space)
                if rem > 0:
                    new_sentence.append(' ')
                    rem -= 1
            new_sentence.append(words[sentence[j]])
        right_spaces = maxWidth - sum([len(w) for w in new_sentence])
        return ''.join(new_sentence + ([' '] * right_spaces))

    def fullJustify(self, words, maxWidth):
        res = []
        sentence = []
        cur_len = 0
        for i in range(len(words)):
            spaces = len(sentence)
            if cur_len + spaces + len(words[i]) <= maxWidth:
                cur_len += len(words[i])
                sentence.append(i)
            else:
                res.append(self.format_text(maxWidth, words, sentence, cur_len))
                sentence = [i]
                cur_len = len(words[i])
        if sentence:
            res.append(self.format_text(maxWidth, words, sentence, cur_len))
        return res


sol = Solution()
# print(sol.fullJustify(
#     ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art",
#      "is", "everything", "else", "we", "do"], 20))
print(sol.fullJustify(["What", "must", "be", "acknowledgment", "shall", "be"], 16))
#print(sol.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))

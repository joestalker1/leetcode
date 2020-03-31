class Solution:
    def search_first_min_word(self, products, word):
        s = 0
        e = len(products) - 1
        while s <= e:
            m = s + (e - s)// 2
            min_len = min(len(word), len(products[m]))
            prefix = products[m][:len(word)]
            if prefix == word:
                #return index of starting word
                l = m - 1
                while l >= 0 and len(products[l]) >= len(word) and products[l][:len(word)] == word:
                    l -= 1
                l += 1
                return l
            if prefix < word:
                s = m + 1
            else:
                e = m - 1
        return -1

    def suggestedProducts(self, products, searchWord):
        if not products or not searchWord:
            return []
        products.sort()
        res = []
        for i in range(len(searchWord)):
            sub = searchWord[:i+1]
            j = self.search_first_min_word(products, sub)
            if j == -1:
                res.append([])
            else:
                words = []
                while j < len(products):
                    if len(words) < 3 and len(products[j]) >= len(sub) and products[j][:len(sub)] == sub:
                        words.append(products[j])
                        j += 1
                    else:
                        break
                res.append(words)
        return res


sol = Solution()
print(sol.suggestedProducts(["code","codephone","coddle","coddles","codes"],"coddle"))

print(sol.suggestedProducts(products = ["havana"], searchWord = "tatiana"))
print(sol.suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], "mouse"))
print(sol.suggestedProducts(products = ["havana"], searchWord = "havana"))
# ["mobile","moneypot","monitor"],
# ["mobile","moneypot","monitor"],
# ["mouse","mousepad"],
# ["mouse","mousepad"],
# ["mouse","mousepad"]




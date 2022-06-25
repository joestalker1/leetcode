class Solution:
    def lower_bound(self, products, word,s,e):
        i = s
        j = e
        while i < j:
            m = i + (j - i)// 2
            if products[m] >= word:
                j = m
            else:
                i = m + 1
        return i

    def suggestedProducts(self, products, searchWord):
        if not products or not searchWord:
            return []
        products.sort()
        res = []
        s = 0
        for i in range(len(searchWord)):
            sub = searchWord[:i+1]
            ns = self.lower_bound(products, sub, s, len(products)-1)
            sug = []
            for i in range(ns, min(len(products),ns+3)):
                if len(products[i]) < len(sub) or products[i][:len(sub)] != sub:
                    break
                sug.append(products[i])
            res.append(sug)
            s = ns
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




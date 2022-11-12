class Solution:
    def placeWordInCrossword(self, board, word: str) -> bool:
        if not board or not word:
            return False
        words = [word,word[::-1]]
        for row in board,zip(*board):
            for places in row:
                places = ''.join(places).split('#')
                for word in words:
                    for place in places:
                        if len(word) == len(place):
                            if all(word[i] == place[i] or place[i] == ' ' for i in range(len(word))):
                                return True
        return False


sol = Solution()
print(sol.placeWordInCrossword([["#"," ","#"],["#"," ","#"],["#"," ","c"]],"ca"))#True
print(sol.placeWordInCrossword([[" ","#","a"],[" ","#", "c"],[" ","#","a"]],"ac"))#False
print(sol.placeWordInCrossword([["#"," ","#"],[" "," ","#"],["#","c"," "]],"abc"))#True
print(sol.placeWordInCrossword([[" "],[" "],[" "],["#"],[" "],[" "]], "ab"))#True

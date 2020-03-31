class Solution:
    def enocode(self, s):
        res = []
        last = s[0]
        count = 1
        for c in s[1:]:
            if last != c:
                res.append([last, count])
                count = 1
                last = c
            else:
                count += 1
        res.append([c, count])
        return res

    def expressiveWords(self, S, words):
        chars1 = self.enocode(S)
        count = 0
        for word in words:
            chars2 = self.enocode(word)
            if len(chars1) != len(chars2):
                continue
            next_word = False
            i = 0
            j = 0
            while i < len(word) and j < len(chars1):
                if chars1[j][0] != chars2[i][0] or chars2[i][1] < chars1[j][1] < 3 or chars1[j][1] < chars2[i][1]:
                    next_word = True
                    break
                i += 1
                j += 1
            if next_word:
                continue
            count += 1
        return count


sol = Solution()
print(sol.expressiveWords("dddiiiinnssssssoooo", ["dinnssoo","ddinso","ddiinnso","ddiinnssoo","ddiinso","dinsoo","ddiinsso","dinssoo","dinso"]))#3

print(sol.expressiveWords("yyrrrrrjaappoooyybbbebbbbriiiiiyyynnnvvwtwwwwwooeeexxxxxkkkkkaaaaauuuu",
                          ["yrrjjappooybbebriiyynvvwtwwoeexkauu", "yrjjappooybbebrriyynnvwwttwoeexkaauu",
                           "yyrrjapoybbebriiynnvvwwtwoeexkaauu", "yyrjappooyybebbrriyynnvwttwwooeexxkkau",
                           "yrjaapooybbebrriyynnvvwwttwooexkaau", "yyrjjapooyybeebbrriiyynvwwttwoexxkau",
                           "yrrjaappoyybbeebbriynnvwwtwooexxkauu", "yrrjjaapooybebriynnvvwwttwwooexkaau",
                           "yyrrjjappooyybebriiyynvvwttwoeexxkkaau", "yrrjaappooybbebrriynvwwtwooeexkau",
                           "yyrjjaapooyybebrriiynvvwttwwooeexxkkaau", "yyrrjappooyybbebriyynnvwwttwwoeexkkauu",
                           "yyrrjjaapoyybbeebriiyynnvwwtwwooexkkaau", "yrjjaappooybbeebriiyynnvwwtwwoexkau",
                           "yrrjjappoyybbeebbrriiyynnvwttwwooexxkkaauu", "yyrrjjapooyybbebbrriyynvwtwoexxkkaauu",
                           "yyrrjappoybebrriynvwwttwooeexkkauu", "yrrjaappooybbeebriiyynnvvwwttwoexxkauu",
                           "yrrjapoybebbrriyynvvwwttwwoexkaau", "yyrrjjapoybbeebbrriynnvwwtwwooexkaauu",
                           "yyrrjjapooyybbeebbriyynnvwtwwoexkaau", "yrjjaapooyybebriynnvwwttwooeexxkkaauu",
                           "yyrjjaapooybbebbriiynvvwttwwoexxkkauu", "yrjjaapooyybeebbriiyynvvwwttwoeexxkau",
                           "yrjjappooyybbebbrriiynvvwtwooeexxkkau", "yyrrjjapoyybbebbrriiyynvwwtwwoexxkkaau",
                           "yrjjapooyybbeebriyynnvvwwtwoeexkkau", "yrjapooyybebriiynnvvwwtwwooeexkauu",
                           "yyrjaapoyybbebbrriynnvwtwwoeexkauu", "yrrjjappoybeebrriiynvvwwtwwoeexxkkaau",
                           "yrrjjapoybbeebrriiyynnvwwttwwoexxkaau", "yyrrjaapoybeebrriiyynvwttwwooeexkauu",
                           "yyrjapoybbeebbrriyynnvvwwttwwooeexkaauu", "yyrjappooybebrriiynvwtwwoeexxkaauu",
                           "yrrjjappooybebrriynnvvwttwooexkau", "yrjjaapoybbeebbriiynnvvwttwooexkauu",
                           "yyrrjapooyybbeebriiyynnvvwtwwoeexxkaauu", "yyrjjaappooybeebbrriiyynnvvwwtwwoeexkkau",
                           "yrrjappoyybbeebrriiynvvwwtwwoeexxkauu", "yrjapooyybeebriiyynvvwttwwooeexxkaauu",
                           "yrjjappooyybbebbriiynnvwwtwooeexxkauu", "yyrrjjappooybbeebbriyynnvwtwwooexxkkau",
                           "yyrrjjaapooybebriiyynvwwtwooeexxkkaauu", "yrjjappooyybbeebbriiyynvwwtwwoeexkkau",
                           "yrrjjappooybbebrriiynvvwwtwwoexxkkaau", "yrjjapooybebbriyynnvvwwttwwooeexxkkaau",
                           "yyrjjapoyybebbrriynvvwwttwoexkauu", "yyrjappoyybebriiynnvvwttwwoexxkaauu",
                           "yyrjaapoybbeebriyynvvwwttwoeexkau", "yrjjaappooyybbebbriiynnvvwtwooexxkau",
                           "yyrjjaappooyybbebrriiyynvvwttwooexkau", "yrjjappoybbeebriyynnvvwwttwwooexxkkaau",
                           "yyrrjaapooybbebbriiyynnvwwtwwooexxkkaauu", "yrrjaapooybbeebrriynnvvwwtwoeexxkkauu",
                           "yrjjaappooyybeebbrriyynnvvwttwwoexxkkauu", "yrrjapooyybebriyynnvwwttwooeexkau",
                           "yyrjjaapooyybeebrriiynnvvwwttwoeexxkkau", "yrjappooybebriyynnvvwttwwooeexkau",
                           "yrrjjaappoyybebbrriiyynvwwtwooexxkauu", "yrjjappooybeebriynnvwwtwoeexkaauu",
                           "yrjaappoybbebbriiynnvwwttwooexxkaau", "yyrrjappooyybeebbriiyynvwwttwwoexxkau",
                           "yyrjappoyybbeebrriynvwtwoeexkaau", "yrrjjaapooybbeebbriyynvwwtwooeexkkaau",
                           "yrjapoybebbrriiynvwttwwoeexxkaau", "yrjapooybebbrriiynnvwwtwwoexxkaau",
                           "yrrjjaappoybeebbriiyynvwwtwooexxkkaauu", "yrjappooybeebrriynvwwtwooeexkaauu",
                           "yrrjaapooybeebbriiynvvwtwwoexxkkaauu", "yyrrjaappooyybebbrriiyynvwwtwwooexxkkau",
                           "yyrjaappoybbeebriynnvvwwtwwooeexkaauu", "yyrjaappooyybbebbriynvvwwttwwooexkauu",
                           "yrjappooybeebbrriiynnvwttwwooexkkau", "yrrjjappooyybebbriiyynnvvwttwwoexkkau",
                           "yrrjjaapooybeebbriynnvvwwtwooexkaau", "yyrjjappoybeebbrriiynnvwtwwoexkaauu",
                           "yyrjjaapoybbebbrriiyynnvvwtwwoexkaau", "yyrrjjaappoyybbebbriyynvwwtwwooeexkkaau",
                           "yrrjjaappooybbebriiyynvvwttwwooexxkau", "yyrjjaapoyybebriiynnvwtwwooeexkauu",
                           "yrrjjappoyybeebbriiyynnvwttwoexkkau", "yrjjappoyybbebbrriynnvvwttwwooeexkkaauu",
                           "yyrjappooybeebrriiynnvwwttwwooexxkkaauu", "yrrjaappoybbeebrriyynnvvwwtwwooeexxkaauu",
                           "yyrjaappooybeebbriiynvwttwoexxkkauu", "yyrrjjapooyybbeebbrriyynvwttwwooeexxkkau",
                           "yrrjapoybbebbrriiynvwtwwoeexxkaau", "yyrrjapoybbeebbriiyynnvvwttwooexkkauu",
                           "yyrjaapooyybebbrriiyynnvvwwtwooeexkkauu", "yyrrjjaappoybbeebrriyynnvwwtwwoexkkaauu",
                           "yyrjappooybbeebrriiyynvwwttwwoexkkau", "yyrjaapooyybebbriiyynnvvwwtwoeexkkaau",
                           "yyrrjjappoyybbeebbriiyynvwtwooexxkaauu", "yrrjjaapoyybbeebriynvvwtwwoexxkaau",
                           "yyrrjjapoybbebbrriyynnvwwtwoeexxkkaau", "yyrrjapooyybebrriiyynvwttwwooeexxkkauu",
                           "yrjappooyybebriiynnvwwtwoeexkkaauu", "yrjjaapooyybeebriiynvwtwooexkauu",
                           "yyrrjjapoybeebbrriiynnvwttwwoexkaau", "yyrrjaappoyybebbrriiyynvwwtwooeexkaau"]))
print(sol.expressiveWords("abcd", ["abc"]))

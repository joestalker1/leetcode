class Solution:
    def expressiveWords(self, S, words):
        def make_group(s):
            groups = []
            for ch in s:
                if not groups or groups[-1][0] != ch:
                    groups.append([ch,1])
                else:
                    groups[-1][1] += 1
            return groups

        target_group = make_group(S)
        res = 0
        for word in words:
            word_group = make_group(word)
            if len(word_group) != len(target_group):
                continue
            stretchy = True
            for i in range(len(target_group)):
                ch1,c1 = target_group[i]
                ch2,c2 = word_group[i]
                if ch1 != ch2 or (c1 < 3 and c1 != c2) or c2 > c1:
                    stretchy = False
                if not stretchy:
                    break
            if stretchy:
                res += 1
        return res


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

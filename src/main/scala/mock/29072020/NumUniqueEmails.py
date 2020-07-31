from collections import defaultdict

class Solution:
    def numUniqueEmails(self, emails):
        if not emails:
            return 0
        use_email = defaultdict(lambda :0)
        for email in emails:
            parts = email.split("@")
            local_name = parts[0]
            local_name = local_name.replace('\\.', '')
            i = local_name.index('+')
            if i >= 0:
                local_name = local_name[0:i]
            use_email[local_name+'@'+parts[1]] += 1
        return len(use_email.keys())


sol = Solution()
print(sol.numUniqueEmails())





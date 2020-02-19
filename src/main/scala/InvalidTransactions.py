class Solution:
    def invalidTransactions(self, transactions):
        if not transactions:
            return []
        res = set()
        names = []
        times = []
        amounts = []
        cities = []
        for trans in transactions:
            name,time,amount,city = trans.split(',')
            names.append(name)
            times.append(int(time))
            amounts.append(int(amount))
            cities.append(city)
        for i,name in enumerate(names):
            if amounts[i] > 1000:
                res.add(i)
        for i in range(len(names)):
            for j in range(len(names)):
                if i == j:
                    continue
                if names[i] == names[j] and cities[i] != cities[j] and times[j] - times[i] <= 60:
                    res.add(i)
        return [transactions[i] for i in list(res)]


sol = Solution()
print(sol.invalidTransactions(["alice,20,800,mtv","alice,50,100,beijing"]))

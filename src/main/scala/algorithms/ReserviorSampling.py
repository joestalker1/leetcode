import random


class ReseviorSample:
    def __init__(self, k,n):
        self.reserv = [0] * k
        self.n = n

    def sample(self,arr):
        for i in range(len(self.reserv)):
            self.reserv[i] = arr[i]
        for i in range(len(self.reserv), len(arr)):
            j = random.randint(i)
            if j < len(self.reserv):
                self.reserv[j] = arr[i]



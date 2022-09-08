class CountPowers:
    def __init__(self, n):
        self.n = n

    def __find(self):
        power = 1
        while power * 2 <= self.n:
            power *= 2
        return power

    def count(self):
        counter = 0
        while self.n != 0:
            self.n -= self.__find()
            counter += 1
        return counter


c1 = CountPowers(18)
print(c1.count())

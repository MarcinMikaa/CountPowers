# Zadaniem programu jest znalezienie ile w sumie różnych potęg dwójek trzeba do siebie dodać,
# żeby otrzymać szukaną liczbę.

class CountPowers:
    def __init__(self, n):
        self.n = n

    # Znajdujemy i zwracamy największą potęgę liczby 2, która jest mniejsza od przekazanej liczby.
    def __find(self):
        power = 1
        while power * 2 <= self.n:
            power *= 2
        return power

    # Sprawdzamy czy szukana liczba jest różna od zera, jeśli tak, to odejmujemy od niej liczbę zwróconą
    # przez wywołaną funkcję __find(), a następnie zwiększamy counter o jeden. Jeżeli szukana liczba jest równa 0
    # to zwracamy counter, który przechowuje ilość potęg 2, które trzeba do siebie dodać aby uzyskać szukaną liczbę.
    def count(self):
        counter = 0
        while self.n != 0:
            self.n -= self.__find()
            counter += 1
        return counter


c1 = CountPowers(15)
print(c1.count())

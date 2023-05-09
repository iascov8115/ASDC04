from classes.helper import Helper
from classes.vector import Vector


class DefiningVector(Vector):
    def __init__(self, vector, n, index_intervals, by_column=False):
        super().__init__(vector, n, index_intervals, by_column)
        self.length = len(self.vector)
        self.d = self.count_d()
        self.sigma = sum([self.index_intervals[i][0] * self.d[i] for i in range(n)])

    def get_element(self, indices, mul=Helper.mul, sum=Helper.sum):
        index = sum(0, -self.sigma)
        for i in range(self.n):
            index = sum(index, mul(indices[i], self.d[i]))
        return self.vector[index]

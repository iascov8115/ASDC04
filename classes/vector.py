from classes.helper import Helper


class Vector:
    def __init__(self, vector, n, index_intervals, by_column=False):
        self.vector = vector
        self.n = n
        self.index_intervals = index_intervals
        self.by_column = by_column

    @classmethod
    def display_by_rows(cls, matrix):
        if len(matrix) == 0:
            return []
        if isinstance(matrix[0], list):
            result = []
            for row in matrix:
                result.extend(cls.display_by_rows(row))
            return result
        else:
            return matrix

    @classmethod
    def display_by_columns(cls, matrix):
        if len(matrix) == 0:
            return []
        if isinstance(matrix[0], list):
            transposed = list(zip(*matrix))
            result = []
            for col in transposed:
                result.extend(cls.display_by_columns(col))
            return result
        else:
            return matrix

    def count_d(self, mul=Helper.mul, sum=Helper.sum):
        d = [0] * self.n
        if self.by_column:
            d[0] = 1
            for i in range(self.n - 1):
                d[i + 1] = mul(sum(sum(self.index_intervals[i][1], -self.index_intervals[i][0]), 1), d[i])
        else:
            d[-1] = 1
            for i in range(self.n - 1, 0, -1):
                d[i - 1] = mul(sum(sum(self.index_intervals[i][1], -self.index_intervals[i][0]), 1), d[i])
        return d

    def get_element(self, indices, mul=Helper.mul, sum=Helper.sum):
        index = 0
        d = self.count_d(mul, sum)
        for i in range(self.n):
            index = sum(index, mul(sum(indices[i], -self.index_intervals[i][0]), d[i]))
        return self.vector[index]

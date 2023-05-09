from classes.helper import Helper


class IliffeVector:
    def __init__(self, vectors):
        self.vectors = vectors

    @classmethod
    def display_by_rows(cls, matrix, dimension, index_intervals):
        return cls._create_subvector(matrix, index_intervals, dimension)

    @classmethod
    def display_by_columns(cls, matrix, dimension, index_intervals):
        transposed_matrix = [list(row) for row in zip(*matrix)]
        return cls._create_subvector(transposed_matrix, index_intervals, dimension)

    @classmethod
    def _create_subvector(cls, matrix, index_intervals, dimension):
        if len(index_intervals) == 1:
            return matrix[index_intervals[0][0]:index_intervals[0][1] + 1]
        else:
            return [cls._create_subvector(matrix[i], index_intervals[1:], dimension - 1) for i in
                    range(index_intervals[0][0], index_intervals[0][1] + 1)]

    def get_element(self, indices, sum=Helper.sum):
        value = self.vectors
        i = 0
        while True:
            if i > len(indices) - 1:
                break
            value = value[indices[i]]
            i = sum(i, 1)
        return value

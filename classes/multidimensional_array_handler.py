from classes.defining_vector import DefiningVector
from classes.helper import Helper
from classes.iliffe_vector import IliffeVector
from classes.vector import Vector


class MultidimensionalArrayHandler:
    def __init__(self, matrix, dimension, index_intervals, by_columns=False):
        self.matrix = matrix
        self.dimension = dimension
        self.index_intervals = index_intervals
        if by_columns:
            vector = Vector.display_by_columns(matrix)
            iliffe_vectors = IliffeVector.display_by_columns(matrix, dimension, index_intervals)
        else:
            vector = Vector.display_by_rows(matrix)
            iliffe_vectors = IliffeVector.display_by_rows(matrix, dimension, index_intervals)

        self.vector = Vector(vector, dimension, index_intervals, by_columns)
        self.defining_vector = DefiningVector(vector, dimension, index_intervals, by_columns)
        self.iliffe_vectors = IliffeVector(iliffe_vectors)

    def direct_access(self, indices, mul=Helper.mul, sum=Helper.sum):
        return self.vector.get_element(indices, mul, sum)

    def access_by_ilifee_vectors(self, indices, sum=Helper.sum):
        return self.iliffe_vectors.get_element(indices, sum)

    def access_by_defining_vector(self, indices, mul=Helper.mul, sum=Helper.sum):
        return self.defining_vector.get_element(indices, mul, sum)

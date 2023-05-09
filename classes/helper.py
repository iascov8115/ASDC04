class Helper:
    def __init__(self):
        self.multiplications = 0
        self.additions = 0

    def mul_with_count(self, a, b):
        self.multiplications += 1
        return a * b

    def sum_with_count(self, a, b):
        self.additions += 1
        return a + b

    @staticmethod
    def mul(a, b):
        return a * b

    @staticmethod
    def sum(a, b):
        return a + b

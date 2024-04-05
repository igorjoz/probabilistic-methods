class LinearGenerator:
    def __init__(self, a, c, M, seed):
        self.a = a
        self.c = c
        self.M = M
        self.previous = seed % self.M

    def next(self):
        self.previous = (self.a * self.previous + self.c) % self.M
        return self.previous / self.M

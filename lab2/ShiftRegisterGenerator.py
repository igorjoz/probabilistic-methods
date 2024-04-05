class ShiftRegisterGenerator:
    def __init__(self, seed):
        self.previous = seed

    def next(self):
        new = self.previous[0] ^ self.previous[1]
        self.previous = self.previous[1:] + [new]
        return new

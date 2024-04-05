import matplotlib.pyplot as plt
import time

from LinearGenerator import LinearGenerator
from ShiftRegisterGenerator import ShiftRegisterGenerator

if __name__ == '__main__':
    a = 69069
    c = 1
    M = 2 ** 32
    N = 10000
    print("1.")
    linear_generator = LinearGenerator(a, c, M, int(time.time()))
    gen = []

    for i in range(N):
        num = linear_generator.next()
        gen.append(num)
        print(num, end=', ')

    print("Mean: ", sum(gen) / N)

    plt.hist(gen, bins=50, edgecolor='black')  # Increase number of bins
    plt.title("Linear Generator")
    plt.xlabel("Generated Numbers")
    plt.ylabel("Frequency")
    plt.grid(True)  # Add gridlines
    plt.show()

    print("2.")
    shift_register_generator = ShiftRegisterGenerator(list(map(int, bin(int(time.time()))[2:])))
    gen = []

    for i in range(N):
        num = shift_register_generator.next()
        gen.append(num)
        print(num, end=', ')

    print("Mean: ", sum(gen) / N)

    plt.title("Shift Register Generator")
    plt.xlabel("Generated Numbers")
    plt.ylabel("Frequency")
    plt.hist(gen, bins=50, edgecolor='black')  # Increase number of bins
    plt.grid(True)  # Add gridlines
    plt.show()

from solvers import newtons_error_series
from example_functions import f_1, f_1_prime
import matplotlib.pyplot as plt


def plot_errors(errors):
    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    ax.set_yscale('log')
    ax.plot(errors)
    plt.show()


def main():
    errors = newtons_error_series(
        f_1, f_1_prime, 3.8, max_iterations=10000, tolerance=0.00001)
    plot_errors(errors)


if __name__ == '__main__':
    main()

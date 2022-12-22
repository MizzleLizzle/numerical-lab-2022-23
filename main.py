from solvers import newtons_error_series, secant_error_series, bisection_error_series, fixed_point_error_series, fixed_point
from example_functions import f_1, f_1_prime, g_1_b, g_1_a, g_2_a, g_2_b
import matplotlib.pyplot as plt
from sys import float_info


def plot_errors(f, f_prime, g, tolerance):
    fig, ax = plt.subplots()

    newtons_errors = newtons_error_series(f, f_prime, 1, 10000, tolerance)
    secant_errors = secant_error_series(f, 0, 1, 10000, tolerance)
    bisection_errors = bisection_error_series(f, 0, 1, 10000, tolerance)
    try:
        fixed_point_errors = fixed_point_error_series(g, 1, 10000, tolerance)
        ax.plot(range(len(fixed_point_errors)),
                fixed_point_errors, label='Fixpunkt '+g.__name__)
    except:
        pass

    ax.plot(range(len(newtons_errors)), newtons_errors, label='Newton\'s')
    ax.plot(range(len(secant_errors)), secant_errors, label='Sekant')
    ax.plot(range(len(bisection_errors)), bisection_errors, label='Bisektion')

    ax.set(xlabel='Iterationen', ylabel='Fehler',
           title='Fehlervergleich '+f.__name__)

    ax.legend()
    ax.set_yscale('symlog')

    plt.show()


def main():
    plot_errors(f_1, f_1_prime, g_1_b, 0.0001)


if __name__ == '__main__':
    main()

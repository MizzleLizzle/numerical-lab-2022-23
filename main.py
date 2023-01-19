from solvers import newtons_error_series, secant_error_series, bisection_error_series, fixed_point_error_series, bisection
from example_functions import functions, f_2, f_1, f_1_prime, g_1_b
import matplotlib.pyplot as plt
from plotting import plot_newton_iterations_by_starting_point, plot_fixed_point_iterations_by_starting_point, plot_errors


def main():
    stats = []
    for index, function in enumerate(functions):
        f, f_prime, g = function["f"], function["f_prime"], function["g"]
        stats.append(plot_errors(f, f_prime, g, 0.00001, index))
    newton_mean, secant_mean, bisection_mean, fixed_point_mean = 0, 0, 0, 0
    for stat in stats:
        newton_mean += stat["newton"]
        secant_mean += stat["secant"]
        bisection_mean += stat["bisection"]
        fixed_point_mean += stat.get("fixed_point", 0)
    newton_mean /= len(stats)
    secant_mean /= len(stats)
    bisection_mean /= len(stats)
    fixed_point_mean /= len([stat for stat in stats if stat.get("fixed_point", None)])
    print(
        f"mean newton: {newton_mean}, mean secant: {secant_mean}, mean bisection: {bisection_mean}, mean fixed point: {fixed_point_mean}")

    """plot_fixed_point_iterations_by_starting_point(f_1, g_1_b, 10000, 0.0001)"""


if __name__ == '__main__':
    main()

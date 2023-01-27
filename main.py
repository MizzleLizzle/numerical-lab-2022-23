from example_functions import functions
from plotting import *
import os


def main():
    try:
        if not os.path.exists("./plots"):
            os.makedirs("./plots")
    except OSError:
        print ('Error: Could not create directory for plots')

    stats = []
    for index, function in enumerate(functions):
        f, f_prime, g, root = function["f"], function["f_prime"], function["g"], function["root"]
        stats.append(plot_errors(f, f_prime, g, 0.00001, root, index))
    
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
    print(f"mean newton: {newton_mean}, mean secant: {secant_mean}, mean bisection: {bisection_mean}, mean fixed point: {fixed_point_mean}")

    function = functions[0]
    f, f_prime, g, root = function["f"], function["f_prime"], function["g"], function["root"]
    plot_fixed_point_iterations_starting_point(f, g, 10000, 0.00001, root)
    plot_newton_iterations_by_starting_point(f, f_prime, 10000, 0.00001, root)
    plot_secant_iterations_by_starting_points_distance(f, 10000, 0.00001, root)
    plot_secant_iterations_by_midpoint_of_starting_points(f, 10000, 0.00001, root)
    plot_bisection_iterations_by_intervall_size(f, 10000, 0.00001, root)
    plot_bisection_iterations_by_relative_root_position(f, 10000, 0.00001, root)


if __name__ == '__main__':
    main()

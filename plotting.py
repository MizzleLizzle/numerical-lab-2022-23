from solvers import newtons_error_series, secant_error_series, bisection_error_series, fixed_point_error_series
import matplotlib.pyplot as plt
from typing import Callable


def plot_errors(f: Callable[[float], float], f_prime: Callable[[float], float], g: Callable[[float], float], tolerance: float, root: float, index: int = None):
    plt.figure()
    _, ax = plt.subplots()

    x_startingpoint = root - 0.5
    a_startingpoint, b_startingpoint = root-0.2, root+0.3
    newtons_errors = newtons_error_series(
        f, f_prime, x_startingpoint, 10000, tolerance, root)
    secant_errors = secant_error_series(
        f, a_startingpoint, b_startingpoint, 10000, tolerance, root)
    bisection_errors = bisection_error_series(
        f, a_startingpoint, b_startingpoint, 10000, tolerance, root)
    try:
        fixed_point_errors = fixed_point_error_series(
            f, g, x_startingpoint, 10000, tolerance, root)
        ax.plot(range(len(fixed_point_errors)),
                fixed_point_errors, label='Fixpunkt')
    except:
        fixed_point_errors = None

    ax.plot(range(len(newtons_errors)), newtons_errors, label='Newton\'s')
    ax.plot(range(len(secant_errors)), secant_errors, label='Sekant')
    ax.plot(range(len(bisection_errors)), bisection_errors, label='Bisektion')

    ax.set(xlabel='Iterationen', ylabel='Fehler')

    ax.legend()
    ax.set_yscale('symlog')

    ylabels = ['%.3f' % (label._y) for label in ax.get_yticklabels()]
    ax.set_yticklabels(ylabels)

    filename = "plots/error_series_plot.pdf" if not index else f"plots/error_series_plot({index}).pdf"

    plt.savefig(
        filename,
        dpi='figure',
        format="pdf",
        pad_inches=0.1,
        bbox_inches="tight"
    )

    stats = {
        "newton": len(newtons_errors),
        "secant": len(secant_errors),
        "bisection": len(bisection_errors),
    }
    if fixed_point_errors:
        stats["fixed_point"] = len(fixed_point_errors)

    return stats


def plot_newton_iterations_by_starting_point(f:  Callable[[float], float], f_prime: Callable[[float], float], max_iteratons: int, tolerance: float, root: float):
    starting_points = [y*1/20 for y in range(21)]
    iterations = []
    for x in starting_points:
        iterations.append(len(newtons_error_series(
            f, f_prime, x, max_iteratons, tolerance, root)))
    plt.figure()
    plt.bar(starting_points, iterations, width=0.03)
    plt.xlabel("Starting Point")
    plt.ylabel("Iterations")
    plt.axvline(x=root, color='r', label='root')
    plt.legend(bbox_to_anchor=(1.0, 1), loc='upper left')
    plt.savefig(
        "plots/newton_iterations_by_starting_point.pdf",
        dpi='figure',
        format="pdf",
        pad_inches=0.1,
        bbox_inches="tight"
    )


def plot_fixed_point_iterations_starting_point(f: Callable[[float], float], g: Callable[[float], float], max_iteratons: int, tolerance: float, root: float):
    starting_points = [y*1/20 for y in range(21)]
    iterations = []
    for x in starting_points:
        iterations.append(len(fixed_point_error_series(
            f, g, x, max_iteratons, tolerance, root)))
    plt.figure()
    plt.bar(starting_points, iterations, width=0.03)
    plt.xlabel("Starting Point")
    plt.ylabel("Iterations")
    plt.axvline(x=root, color='r', label='root')
    plt.legend(bbox_to_anchor=(1.0, 1), loc='upper left')
    plt.savefig(
        "plots/fixed_point_iterations_by_starting_point.pdf",
        dpi='figure',
        format="pdf",
        pad_inches=0.1,
        bbox_inches="tight"
    )


def plot_secant_iterations_by_starting_points_distance(f: Callable[[float], float], max_iterations: int, tolerance: float, root: float):
    starting_points = [(0.5-y*1/40, 0.5+y*1/40, y*1/20)for y in range(1, 21)]
    iterations = []
    for x in starting_points:
        iterations.append(len(secant_error_series(
            f, x[0], x[1], max_iterations, tolerance, root)))
    starting_points = [x[2] for x in starting_points]
    plt.figure()
    plt.bar(starting_points, iterations, width=0.04)
    plt.xlabel("Starting Points Distance")
    plt.ylabel("Iterations")
    plt.savefig(
        "plots/secant_iterations_by_starting_points_distance.pdf",
        dpi='figure',
        format="pdf",
        pad_inches=0.1,
        bbox_inches="tight"
    )


def plot_secant_iterations_by_midpoint_of_starting_points(f: Callable[[float], float], max_iterations: int, tolerance: float, root: float):
    starting_points = [(y*1/20, (y+1)*1/20, y*1/20+1/40)for y in range(0, 21)]
    iterations = []
    for x in starting_points:
        iterations.append(len(secant_error_series(
            f, x[0], x[1], max_iterations, tolerance, root)))
    starting_points = [x[2] for x in starting_points]
    plt.figure()
    plt.bar(starting_points, iterations, width=0.03)
    plt.xlabel("Starting Points Midpoint")
    plt.ylabel("Iterations")
    plt.axvline(x=root, color='r', label='root')
    plt.legend(bbox_to_anchor=(1.0, 1), loc='upper left')
    plt.savefig(
        "plots/secant_iterations_by_midpoint_of_starting_points.pdf",
        dpi='figure',
        format="pdf",
        pad_inches=0.1,
        bbox_inches="tight"
    )

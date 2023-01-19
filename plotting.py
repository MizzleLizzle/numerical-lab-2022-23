from solvers import newtons_error_series, secant_error_series, bisection_error_series, fixed_point_error_series
import matplotlib.pyplot as plt

def plot_errors(f, f_prime, g, tolerance, index=None):
    _, ax = plt.subplots()


    newtons_errors = newtons_error_series(f, f_prime, 1, 10000, tolerance)
    secant_errors = secant_error_series(f, 0, 1, 10000, tolerance)
    bisection_errors = bisection_error_series(f, 0, 1, 10000, tolerance)
    try:
        fixed_point_errors = fixed_point_error_series(
            f, g, 1, 10000, tolerance)
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

    filename = "plot.pdf" if not index else f"plot{index}.pdf"

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


def plot_newton_iterations_by_starting_point(f, f_prime, max_iteratons, tolerance):
    starting_points = [y*1/20 for y in range(21)]
    iterations = []
    for x in starting_points:
        iterations.append(len(newtons_error_series(f, f_prime, x, max_iteratons, tolerance)))
    plt.bar(starting_points, iterations, width=0.03)
    plt.show()


def plot_fixed_point_iterations_by_starting_point(f, g, max_iteratons, tolerance):
    starting_points = [y*1/20 for y in range(21)]
    iterations = []
    for x in starting_points:
        iterations.append(len(fixed_point_error_series(f, g, x, max_iteratons, tolerance)))
    plt.bar(starting_points, iterations, width=0.03)
    plt.show()

def plot_secant_iterations_by_starting_point(f, max_iterations, tolerance):
    pass

from solvers import newtons_error_series, secant_error_series, bisection_error_series, fixed_point_error_series, bisection
from example_functions import functions, f_2
import matplotlib.pyplot as plt


def plot_errors(f, f_prime, g, tolerance, index=None):
    fig, ax = plt.subplots()

    newtons_errors = newtons_error_series(f, f_prime, 1, 10000, tolerance)
    secant_errors = secant_error_series(f, 0, 1, 10000, tolerance)
    bisection_errors = bisection_error_series(f, 0, 2, 10000, tolerance)
    try:
        fixed_point_errors = fixed_point_error_series(
            f, g, 1, 10000, tolerance)
        ax.plot(range(len(fixed_point_errors)),
                fixed_point_errors, label='Fixpunkt '+g.__name__)
    except:
        fixed_point_errors = None

    ax.plot(range(len(newtons_errors)), newtons_errors, label='Newton\'s')
    ax.plot(range(len(secant_errors)), secant_errors, label='Sekant')
    ax.plot(range(len(bisection_errors)), bisection_errors, label='Bisektion')

    ax.set(xlabel='Iterationen', ylabel='Fehler',
           title='Fehlervergleich '+f.__name__)

    ax.legend()
    ax.set_yscale('symlog')

    ylabels = ['%.3f' % (label._y) for label in ax.get_yticklabels()]
    ax.set_yticklabels(ylabels)

    filename = "plot.png" if not index else f"plot{index}.png"

    plt.savefig(
        filename,
        dpi='figure',
        format="png",
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


def main():
    stats = []
    for index, function in enumerate(functions):
        f, f_prime, g = function["f"], function["f_prime"], function["g"]
        stats.append(plot_errors(f, f_prime, g, 0.0001, index))
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


if __name__ == '__main__':
    main()

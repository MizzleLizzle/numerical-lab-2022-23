from math import exp, tan, cos, log, atan


def f_1(x): return x+exp(x)-2
def f_1_prime(x): return 1+exp(x)
def f_2(x): return 2*x-tan(x)
def f_2_prime(x): return 2-1/cos(x)**2
def g_1_a(x): return 2-exp(x)
def g_1_b(x): return log(2-x)
def g_2_a(x): return 0.5*tan(x)
def g_2_b(x): return atan(2*x)


def gen_f_3(a):
    f_3 = lambda x: -a*x**2+2*a
    f_3.__name__ = f"f_3_{a}"
    return f_3


def gen_f_3_prime(a):
    return lambda x: -2*a*x


def gen_g_3(a):
    g_3 = lambda x: -a*x**2+2*a+x
    g_3.__name__ = f"g_3_{a}"
    return g_3


functions = [
    {
        "f": f_1,
        "f_prime": f_1_prime,
        "g": g_1_b,
    },
    {
        "f": f_2,
        "f_prime": f_2_prime,
        "g": g_2_b,
    },
] + [{"f": gen_f_3(a), "f_prime": gen_f_3_prime(a),  "g": gen_g_3(a)} for a in (2, 1, 1/4)]

from math import exp
from typing import Callable


class NoRootFoundException(Exception):
    pass


def newtons(f: Callable[[float], float], f_prime: Callable[[float], float], x: float, max_iterations: int, tolerance: float) -> float:
    for _ in range(max_iterations):
        x = x - f(x)/f_prime(x)
        if abs(f(x)) < tolerance:
            return x
    raise NoRootFoundException


def secant(f: Callable[[float], float], x_0: float, x_1: float, max_iterations: int, tolerance: float) -> float:
    for _ in range(max_iterations):
        swap = x_1
        x_1 = x_1 - (f(x_1)*(x_1-x_0))/(f(x_1)-f(x_0))
        if abs(f(x_1)) < tolerance:
            return x_1
        x_0 = swap
    raise NoRootFoundException


def bisection(f: Callable[[float], float], a: float, b: float, max_iterations: int, tolerance: float) -> float:
    def sign(y: float) -> int:
        if y >= 0:
            return 1
        return -1

    for _ in range(max_iterations):
        x = (a+b)/2
        if abs(f(x)) < tolerance:
            return x
        if sign(f(x)) == sign(f(a)):
            a = x
        else:
            b = x
    raise NoRootFoundException


def fixed_point(f: Callable[[float], float], x: float, max_iterations: int, tolerance: float) -> float:
    for _ in range(max_iterations):
        x = f(x)
        if abs(f(x)) < tolerance:
            return x
    raise NoRootFoundException

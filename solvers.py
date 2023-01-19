from typing import Callable


class NoRootFoundException(Exception):
    pass


def newtons(f: Callable[[float], float], f_prime: Callable[[float], float], x: float, max_iterations: int, tolerance: float) -> float:
    for _ in range(max_iterations):
        x = x - f(x)/f_prime(x)
        if abs(f(x)) < tolerance:
            return x
    raise NoRootFoundException


def newtons_error_series(f: Callable[[float], float], f_prime: Callable[[float], float], x: float, max_iterations: int, tolerance: float, root: float) -> list[float]:
    errors = [x]
    for _ in range(max_iterations):
        x = x - f(x)/f_prime(x)
        errors.append(x)
        if abs(f(x)) < tolerance:
            return [abs(root-y) for y in errors]
    raise NoRootFoundException


def secant(f: Callable[[float], float], x_0: float, x_1: float, max_iterations: int, tolerance: float) -> float:
    for _ in range(max_iterations):
        swap = x_1
        x_1 = x_1 - (f(x_1)*(x_1-x_0))/(f(x_1)-f(x_0))
        if abs(f(x_1)) < tolerance:
            return x_1
        x_0 = swap
    raise NoRootFoundException


def secant_error_series(f: Callable[[float], float], x_0: float, x_1: float, max_iterations: int, tolerance: float, root: float) -> list[float]:
    errors = [x_1]
    for _ in range(max_iterations):
        swap = x_1
        x_1 = x_1 - (f(x_1)*(x_1-x_0))/(f(x_1)-f(x_0))
        errors.append(x_1)
        if abs(f(x_1)) < tolerance:
            return [abs(root-y) for y in errors]
        x_0 = swap
    raise NoRootFoundException


def bisection(f: Callable[[float], float], a: float, b: float, max_iterations: int, tolerance: float) -> float:
    def sign(y: float) -> int:
        return y / abs(y) if y != 0 else 0

    for _ in range(max_iterations):
        x = (a+b)/2
        if abs(f(x)) < tolerance:
            return x
        if sign(f(x)) == sign(f(a)):
            a = x
        else:
            b = x
    raise NoRootFoundException


def bisection_error_series(f: Callable[[float], float], a: float, b: float, max_iterations: int, tolerance: float, root: float) -> list[float]:
    def sign(y: float) -> int:
        return y / abs(y) if y != 0 else 0

    errors = [b]
    for _ in range(max_iterations):
        x = (a+b)/2
        errors.append(x)
        if abs(f(x)) < tolerance:
            return [abs(root-y) for y in errors]
        if sign(f(x)) == sign(f(a)):
            a = x
        else:
            b = x
    raise NoRootFoundException


def fixed_point(f: Callable[[float], float], g: Callable[[float], float], x: float, max_iterations: int, tolerance: float) -> float:
    for _ in range(max_iterations):
        x = g(x)
        if abs(f(x)) < tolerance:
            return x
    raise NoRootFoundException


def fixed_point_error_series(f: Callable[[float], float], g: Callable[[float], float], x: float, max_iterations: int, tolerance: float, root: float) -> list[float]:
    errors = [x]
    for _ in range(max_iterations):
        x = g(x)
        errors.append(x)
        if abs(f(x)) < tolerance:
            return [abs(root-y) for y in errors]
    raise NoRootFoundException

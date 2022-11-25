from math import abs

def sign(x: float) -> int:
    return 0 if x == 0 else x/abs(x)
from solvers import newtons_error_series
from example_functions import f_1, f_1_prime

def main():
    print(newtons_error_series(f_1, f_1_prime, 0.8, max_iterations=10000, tolerance=0.001))



if __name__ == '__main__':
    main()

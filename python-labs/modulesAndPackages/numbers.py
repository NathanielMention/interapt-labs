import math


def square_root_of(a_num):
    '''
    Compute and return the square root of a_num
    :param a_num: Number we want sqrt of (must be >= 0)
    :return: sqrt of a_num
    '''
    return math.sqrt(a_num)


def cosine_of(a_num):
    '''
    Compute and return the cosine of a_num
    :param a_num: Number we want cos of (in radians)
    :return: cosine of a_num
    '''
    return math.cos(a_num)


def factorial_of(a_num):
    '''
    Compute and return the factorial of a_num
    :param a_num: Number we want factorial of (a positive integer)
    :return: factorial of a_num
    '''
    return math.factorial(a_num)


def main():
    a_num = 12
    print(f'Original number: {a_num}')
    print(f'Cosine: {cosine_of(a_num)}')
    print(f'Square root: {square_root_of(a_num)}')
    print(f'Factorial: {factorial_of(a_num)}')


if __name__ == "__main__":
    main()

##############################################################################
# FILE: math_print.py
# WRITER: Nadav Har-Tuv , nadav366 , 205457534
# EXERCISE: intro2cs1 ex1 20118-2019
# DESCRIPTION: A program that prints results for several math operations.
##############################################################################
import math


def golden_ratio():
    """ This function prints the gold ratio """
    print((1+math.sqrt(5))/2)
    return


def six_cubed():
    """ This function prints the result of six in the power of three """
    print(math.pow(6, 3))
    return


def hypotenuse():
    """ This function prints the hypotenuse length in the given triangle """
    print(math.sqrt(math.pow(3, 2)+math.pow(5, 2)))
    return


def pi():
    """ This function prints the constant number pi """
    print(math.pi)
    return


def e():
    """ This function prints the constant number e """
    print(math.e)
    return


def triangular_area():
    """ This function prints the area of ​​the right-angled triangles,
    and the calves, which have a length of 1-10 """
    print(
        math.pow(1, 2)/2,
        math.pow(2, 2)/2,
        math.pow(3, 2)/2,
        math.pow(4, 2)/2,
        math.pow(5, 2)/2,
        math.pow(6, 2)/2,
        math.pow(7, 2)/2,
        math.pow(8, 2)/2,
        math.pow(9, 2)/2,
        math.pow(10, 2)/2)
    return


if __name__ == "__main__":
    """ main function """
    golden_ratio()
    six_cubed()
    hypotenuse()
    pi()
    e()
    triangular_area()


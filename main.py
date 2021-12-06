from math import inf
from numpy import poly1d
import os
from sympy import symbols, limit


a = float(input("Factor of x^5 = "))
b = float(input("Factor of x^4 = "))
c = float(input("Factor of x^3 = "))
d = float(input("Factor of x^2 = "))
e = float(input("Factor of x^1 = "))
f = float(input("Factor of x^0 = "))

func = poly1d(a, b, c, d, e, f)

clear = lambda: os.system('clear') if os.name == 'posix' else os.system('cls')


def find_derivatives():
    newA = (a * 5)
    newB = (b * 4)
    newC = (c * 3)
    newD = (d * 2)
    newE = (e * 1)
    firstDerivative = poly1d([newA, newB, newC, newD, newE])

    newnewA = (newA * 4)
    newnewB = (newB * 3)
    newnewC = (newC * 2)
    newnewD = (newD * 1)
    secondDerivative = poly1d([newnewA, newnewB, newnewC, newnewD])

    verynewA = (newnewA * 3)
    verynewB = (newnewB * 2)
    verynewC = (newnewC * 1)
    thirdDerivative = poly1d([verynewA, verynewB, newnewC])

    print('{:s}'.format('\u0332'.join('Original function')))
    print(func, "\n")
    print('{:s}'.format('\u0332'.join('First derivative')))
    print(firstDerivative, "\n")
    print('{:s}'.format('\u0332'.join('Second derivative')))
    print(secondDerivative, "\n")
    print('{:s}'.format('\u0332'.join('Third derivative')))
    print(thirdDerivative, "\n")


def range_of_definition():
    print('{:s}'.format('\u0332'.join('Range of definition')))
    print("D = R (Real numbers)\n")


def behaviour_to_infinity():
    print('{:s}'.format('\u0332'.join('Behaviour to infinity')))

    x = symbols('x')
    beginning = limit(((a)*(x)**5 + (b)*(x)**4 + (c)*(x)**3 + (d)*(x)**2 + (e)*(x)**1 + (f)*(x)**0), x, (-inf))
    ending = limit(((a)*(x)**5 + (b)*(x)**4 + (c)*(x)**3 + (d)*(x)**2 + (e)*(x)**1 + (f)*(x)**0), x, (inf))

    print(f"The graph moves from {beginning} to {ending}.")


def axis_intercept():
    print('{:s}'.format('\u0332'.join('y-Achsenabschnitt')))
    print(f"The axis intercept is at Py( 0 | {f}\n")


def symmetry():
    pass


def zero_points():
    pass


def extrema():
    pass


def turning_point():
    pass


def main():
    clear()
    range_of_definition()
    behaviour_to_infinity()
    axis_intercept()
    symmetry()
    zero_points()
    extrema()
    turning_point()


if __name__ == '__main__':
    main()

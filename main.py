from math import inf
from numpy import poly1d
import os
from sympy import symbols, limit

clear = lambda: os.system('clear') if os.name == 'posix' else os.system('cls')

clear()

a = str(input("Factor of x^5 = "))
b = str(input("Factor of x^4 = "))
c = str(input("Factor of x^3 = "))
d = str(input("Factor of x^2 = "))
e = str(input("Factor of x^1 = "))
f = str(input("Factor of x^0 = "))

try:
     a = float(a)
except:
     a = float(a[0]) / float(a[2])

try:
     b = float(b)
except:
     b = float(b[0]) / float(b[2])

try:
     c = float(c)
except:
     c = float(c[0]) / float(c[2])

try:
     d = float(d)
except:
     d = float(d[0]) / float(d[2])

try:
     e = float(e)
except:
     e = float(e[0]) / float(e[2])

try:
     f = float(f)
except:
     f = float(f[0]) / float(f[2])

func = poly1d([a, b, c, d, e, f])


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

print('\n{:s}'.format('\u0332'.join('Original function')))
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

    print(f"The graph moves from {beginning} to {ending}.\n")


def axis_intercept():
    print('{:s}'.format('\u0332'.join('Axis intercept')))
    print(f"The axis intercept is at Py( 0 | {f})\n")


def symmetry():
    print('{:s}'.format('\u0332'.join('Symmetry')))

    try:
         if ((b or d) != 0) and ((a or c or e) != 0):
              print("The graph is neither axially symmetric to the y-axis nor point-symmetric to the origin, since not all exponents of the variable x are even or odd.\n")

         elif ((b or d) != 0) and ((a and c and d) == 0):
                   print("The graph is axially symmetric to the y axis, since all exponents of the variable x are even.\n")
         
         elif ((b and d) == 0) and ((a or c or d) != 0):
                   print("The graph is point symmetric to the origin, since all exponents of the variable x are odd.\n")
         else:
              print("No Symmetrie.\n")
    except:
         print("Error")


def zero_points():
    print('{:s}'.format('\u0332'.join('Zeropoints')))
    solutions = func.r

    if a != 0:
         zp1, zp2, zp3, zp4, zp5 = solutions[0], solutions[1], solutions[2], solutions[3], solutions[4]
         print("zp1:", zp1)
         print("zp2:", zp2)
         print("zp3:", zp3)
         print("zp4:", zp4)
         print("zp5:", zp5, "\n")
    elif (a == 0) and (b != 0):
         zp1, zp2, zp3, zp4 = solutions[0], solutions[1], solutions[2], solutions[3]
         print("zp1:", zp1)
         print("zp2:", zp2)
         print("zp3:", zp3)
         print("zp4:", zp4, "\n")
    elif (a == 0) and (b == 0) and (c != 0):
         zp1, zp2, zp3 = solutions[0], solutions[1], solutions[2]
         print("zp1:", zp1)
         print("zp2:", zp2)
         print("zp3:", zp3, "\n")
    elif (a == 0) and (b == 0) and (c == 0) and (d != 0):
         zp1, zp2 = solutions[0], solutions[1]
         print("zp1:", zp1)
         print("zp2:", zp2)
    elif (a == 0) and (b == 0) and (c == 0) and (d == 0) and (e != 0):
         zp1 = solutions[0]
         print("zp1:", zp1, "\n")

    elif (a == 0) and (b == 0) and (c == 0) and (d == 0) and (e == 0):
         print("No zeropoints.\n")


def extrema():
    print('{:s}'.format('\u0332'.join('Extrema')))
    
    solutions = firstDerivative.r

    if a != 0:
         zp1, zp2, zp3, zp4 = solutions[0], solutions[1], solutions[2], solutions[3]

         firstExtrema = (a)*(zp1)**5 + (b)*(zp1)**4 + (c)*(zp1)**3 + (d)*(zp1)**2 + (e)*(zp1)**1 + (f)*(zp1)**0
         secondExtrema = (a)*(zp2)**5 + (b)*(zp2)**4 + (c)*(zp2)**3 + (d)*(zp2)**2 + (e)*(zp2)**1 + (f)*(zp2)**0
         thirdExtrema = (a)*(zp3)**5 + (b)*(zp3)**4 + (c)*(zp3)**3 + (d)*(zp3)**2 + (e)*(zp3)**1 + (f)*(zp3)**0
         fourthExtrema = (a)*(zp4)**5 + (b)*(zp4)**4 + (c)*(zp4)**3 + (d)*(zp4)**2 + (e)*(zp4)**1 + (f)*(zp4)**0

         print("E1:", [zp1, firstExtrema])
         print("E2:", [zp2, secondExtrema])
         print("E3:", [zp3, thirdExtrema])
         print("E4:", [zp4, fourthExtrema], "\n")

    elif (a == 0) and (b != 0):
         zp1, zp2, zp3 = solutions[0], solutions[1], solutions[2]

         firstExtrema = (a)*(zp1)**5 + (b)*(zp1)**4 + (c)*(zp1)**3 + (d)*(zp1)**2 + (e)*(zp1)**1 + (f)*(zp1)**0
         secondExtrema = (a)*(zp2)**5 + (b)*(zp2)**4 + (c)*(zp2)**3 + (d)*(zp2)**2 + (e)*(zp2)**1 + (f)*(zp2)**0
         thirdExtrema = (a)*(zp3)**5 + (b)*(zp3)**4 + (c)*(zp3)**3 + (d)*(zp3)**2 + (e)*(zp3)**1 + (f)*(zp3)**0

         print("E1:", [zp1, firstExtrema])
         print("E2:", [zp2, secondExtrema])
         print("E3:", [zp3, thirdExtrema], "\n")

    elif (a == 0) and (b == 0) and (c != 0):
         zp1, zp2 = solutions[0], solutions[1]

         firstExtrema = (a)*(zp1)**5 + (b)*(zp1)**4 + (c)*(zp1)**3 + (d)*(zp1)**2 + (e)*(zp1)**1 + (f)*(zp1)**0
         secondExtrema = (a)*(zp2)**5 + (b)*(zp2)**4 + (c)*(zp2)**3 + (d)*(zp2)**2 + (e)*(zp2)**1 + (f)*(zp2)**0

         print("E1:", [zp1, firstExtrema])
         print("E2:", [zp2, secondExtrema], "\n")

    elif (a == 0) and (b == 0) and (c == 0) and (d != 0):
         zp1 = solutions[0]

         firstExtrema = (a)*(zp1)**5 + (b)*(zp1)**4 + (c)*(zp1)**3 + (d)*(zp1)**2 + (e)*(zp1)**1 + (f)*(zp1)**0

         print("E1:", [zp1, firstExtrema], "\n")

    elif (a == 0) and (b == 0) and (c == 0) and (d == 0):
         print("No extrema.\n")


def turning_point():
    print('{:s}'.format('\u0332'.join('Turning points')))

    solutions = secondDerivative.r

    if (a != 0):
         zp1, zp2, zp3 = solutions[0], solutions[1], solutions[2]

         wp1 = (a)*(zp1)**5 + (b)*(zp1)**4 + (c)*(zp1)**3 + (d)*(zp1)**2 + (e)*(zp1)**1 + (f)*(zp1)**0
         wp2 = (a)*(zp2)**5 + (b)*(zp2)**4 + (c)*(zp2)**3 + (d)*(zp2)**2 + (e)*(zp2)**1 + (f)*(zp2)**0
         wp3 = (a)*(zp3)**5 + (b)*(zp3)**4 + (c)*(zp3)**3 + (d)*(zp3)**2 + (e)*(zp3)**1 + (f)*(zp3)**0

         print("TP1:", [zp1, wp1])
         print("TP2:", [zp2, wp2])
         print("TP3:", [zp3, wp3], "\n")
    elif (a == 0) and (b != 0):
         zp1, zp2 = solutions[0], solutions[1]

         wp1 = (a)*(zp1)**5 + (b)*(zp1)**4 + (c)*(zp1)**3 + (d)*(zp1)**2 + (e)*(zp1)**1 + (f)*(zp1)**0
         wp2 = (a)*(zp2)**5 + (b)*(zp2)**4 + (c)*(zp2)**3 + (d)*(zp2)**2 + (e)*(zp2)**1 + (f)*(zp2)**0

         print("TP1:", [zp1, wp1])
         print("TP2:", [zp2, wp2], "\n")
    elif (a == 0) and (b == 0) and (c != 0):
         zp1 = solutions[0]

         wp1 = (a)*(zp1)**5 + (b)*(zp1)**4 + (c)*(zp1)**3 + (d)*(zp1)**2 + (e)*(zp1)**1 + (f)*(zp1)**0

         print("TP1:", [zp1, wp1], "\n")
    elif (a == 0) and (b == 0) and (c == 0):
         print("No turning points.\n")


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

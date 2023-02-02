from math import inf
from numpy import poly1d
import os
from sympy import symbols, limit

clear = lambda: os.system('clear') if os.name == 'posix' else os.system('cls')

def get_derivatives(a, b, c, d, e, f):
     global func, first_derivative, second_derivative, third_derivative
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
     first_derivative = poly1d([newA, newB, newC, newD, newE])

     newnewA = (newA * 4)
     newnewB = (newB * 3)
     newnewC = (newC * 2)
     newnewD = (newD * 1)
     second_derivative = poly1d([newnewA, newnewB, newnewC, newnewD])

     verynewA = (newnewA * 3)
     verynewB = (newnewB * 2)
     verynewC = (newnewC * 1)
     third_derivative = poly1d([verynewA, verynewB, verynewC])

     print('\n{:s}'.format('\u0332'.join('Original function')))
     print(func, "\n")
     print('{:s}'.format('\u0332'.join('First derivative')))
     print(first_derivative, "\n")
     print('{:s}'.format('\u0332'.join('Second derivative')))
     print(second_derivative, "\n")
     print('{:s}'.format('\u0332'.join('Third derivative')))
     print(third_derivative, "\n")

     result = f"{func} \n\n{first_derivative} \n\n{second_derivative} \n\n{third_derivative} \n"

     return result


def range_of_definition():
    print('{:s}'.format('\u0332'.join('Range of definition')))
    print("D = R (Real numbers)\n")
    return "D = R (Real numbers)"


def behaviour_to_infinity(a, b, c, d, e, f):
    print('{:s}'.format('\u0332'.join('Behaviour to infinity')))

    x = symbols('x')
    beginning = limit(((a)*(x)**5 + (b)*(x)**4 + (c)*(x)**3 + (d)*(x)**2 + (e)*(x)**1 + (f)*(x)**0), x, (-inf))
    ending = limit(((a)*(x)**5 + (b)*(x)**4 + (c)*(x)**3 + (d)*(x)**2 + (e)*(x)**1 + (f)*(x)**0), x, (inf))

    print(f"The graph moves from {beginning} to {ending}.\n")
    return f"The graph moves from {beginning} to {ending}."


def axis_intercept(f):
    print('{:s}'.format('\u0332'.join('Axis intercept')))
    print(f"The axis intercept is at Py( 0 | {f} )\n")
    return f"The axis intercept is at Py( 0 | {f} )"


def symmetry(a, b, c, d, e):
    print('{:s}'.format('\u0332'.join('Symmetry')))

    try:
         if ((b or d) != 0) and ((a or c or e) != 0):
               print("The graph is neither axially symmetric to the y-axis nor point-symmetric to the origin, since not all exponents of the variable x are even or odd.\n")
               return "The graph is neither axially symmetric to the y-axis nor point-symmetric to the origin, since not all exponents of the variable x are even or odd."

         elif ((b or d) != 0) and ((a and c and d) == 0):
               print("The graph is axially symmetric to the y axis, since all exponents of the variable x are even.\n")
               return "The graph is axially symmetric to the y axis, since all exponents of the variable x are even."
         
         elif ((b and d) == 0) and ((a or c or d) != 0):
               print("The graph is point symmetric to the origin, since all exponents of the variable x are odd.\n")
               return "The graph is point symmetric to the origin, since all exponents of the variable x are odd."
         else:
               print("No symmetry.\n")
               return "No symmetry."
    except:
         print("Error")
         return "Error"


def zero_points(a, b, c, d, e):
    print('{:s}'.format('\u0332'.join('Zeropoints')))
    solutions = func.r

    if a != 0:
         zp1, zp2, zp3, zp4, zp5 = solutions[0], solutions[1], solutions[2], solutions[3], solutions[4]
         print("zp1:", zp1)
         print("zp2:", zp2)
         print("zp3:", zp3)
         print("zp4:", zp4)
         print("zp5:", zp5, "\n")
         return f"zp1: {zp1} \nzp2: {zp2} \nzp3: {zp3} \nzp4: {zp4} \nzp5: {zp5}"
    elif (a == 0) and (b != 0):
         zp1, zp2, zp3, zp4 = solutions[0], solutions[1], solutions[2], solutions[3]
         print("zp1:", zp1)
         print("zp2:", zp2)
         print("zp3:", zp3)
         print("zp4:", zp4, "\n")
         return f"zp1: {zp1} \nzp2: {zp2} \nzp3: {zp3} \nzp4: {zp4}"
    elif (a == 0) and (b == 0) and (c != 0):
         zp1, zp2, zp3 = solutions[0], solutions[1], solutions[2]
         print("zp1:", zp1)
         print("zp2:", zp2)
         print("zp3:", zp3, "\n")
         return f"zp1: {zp1} \nzp2: {zp2} \nzp3: {zp3}"
    elif (a == 0) and (b == 0) and (c == 0) and (d != 0):
         zp1, zp2 = solutions[0], solutions[1]
         print("zp1:", zp1)
         print("zp2:", zp2)
         return f"zp1: {zp1} \nzp2: {zp2}"
    elif (a == 0) and (b == 0) and (c == 0) and (d == 0) and (e != 0):
         zp1 = solutions[0]
         return f"zp1: {zp1}"

    elif (a == 0) and (b == 0) and (c == 0) and (d == 0) and (e == 0):
         print("No zeropoints.\n")
         return "No zeropoints."


def extrema(a, b, c, d, e, f):
    print('{:s}'.format('\u0332'.join('Extrema')))
    
    solutions = first_derivative.r

    if a != 0:
         zp1, zp2, zp3, zp4 = solutions[0], solutions[1], solutions[2], solutions[3]

         first_extrema = (a)*(zp1)**5 + (b)*(zp1)**4 + (c)*(zp1)**3 + (d)*(zp1)**2 + (e)*(zp1)**1 + (f)*(zp1)**0
         second_extrema = (a)*(zp2)**5 + (b)*(zp2)**4 + (c)*(zp2)**3 + (d)*(zp2)**2 + (e)*(zp2)**1 + (f)*(zp2)**0
         third_extrema = (a)*(zp3)**5 + (b)*(zp3)**4 + (c)*(zp3)**3 + (d)*(zp3)**2 + (e)*(zp3)**1 + (f)*(zp3)**0
         fourth_extrema = (a)*(zp4)**5 + (b)*(zp4)**4 + (c)*(zp4)**3 + (d)*(zp4)**2 + (e)*(zp4)**1 + (f)*(zp4)**0

         print("E1:", [zp1, first_extrema])
         print("E2:", [zp2, second_extrema])
         print("E3:", [zp3, third_extrema])
         print("E4:", [zp4, fourth_extrema], "\n")
         return f"E1: {[zp1, first_extrema]} \nE2: {[zp1, second_extrema]} \nE3: {[zp3, third_extrema]} \nE4: {[zp4, fourth_extrema]}"

    elif (a == 0) and (b != 0):
         zp1, zp2, zp3 = solutions[0], solutions[1], solutions[2]

         first_extrema = (a)*(zp1)**5 + (b)*(zp1)**4 + (c)*(zp1)**3 + (d)*(zp1)**2 + (e)*(zp1)**1 + (f)*(zp1)**0
         second_extrema = (a)*(zp2)**5 + (b)*(zp2)**4 + (c)*(zp2)**3 + (d)*(zp2)**2 + (e)*(zp2)**1 + (f)*(zp2)**0
         third_extrema = (a)*(zp3)**5 + (b)*(zp3)**4 + (c)*(zp3)**3 + (d)*(zp3)**2 + (e)*(zp3)**1 + (f)*(zp3)**0

         print("E1:", [zp1, first_extrema])
         print("E2:", [zp2, second_extrema])
         print("E3:", [zp3, third_extrema], "\n")
         return f"E1: {[zp1, first_extrema]} \nE2: {[zp1, second_extrema]} \nE3: {[zp3, third_extrema]}"

    elif (a == 0) and (b == 0) and (c != 0):
         zp1, zp2 = solutions[0], solutions[1]

         first_extrema = (a)*(zp1)**5 + (b)*(zp1)**4 + (c)*(zp1)**3 + (d)*(zp1)**2 + (e)*(zp1)**1 + (f)*(zp1)**0
         second_extrema = (a)*(zp2)**5 + (b)*(zp2)**4 + (c)*(zp2)**3 + (d)*(zp2)**2 + (e)*(zp2)**1 + (f)*(zp2)**0

         print("E1:", [zp1, first_extrema])
         print("E2:", [zp2, second_extrema], "\n")
         return f"E1: {[zp1, first_extrema]} \nE2: {[zp2, second_extrema]}"

    elif (a == 0) and (b == 0) and (c == 0) and (d != 0):
         zp1 = solutions[0]

         first_extrema = (a)*(zp1)**5 + (b)*(zp1)**4 + (c)*(zp1)**3 + (d)*(zp1)**2 + (e)*(zp1)**1 + (f)*(zp1)**0

         print("E1:", [zp1, first_extrema], "\n")
         return f"E1: {[zp1, first_extrema]}"

    elif (a == 0) and (b == 0) and (c == 0) and (d == 0):
         print("No extrema.\n")
         return "No extrema."


def turning_points(a, b, c, d, e, f):
    print('{:s}'.format('\u0332'.join('Turning points')))

    solutions = second_derivative.r

    if (a != 0):
         zp1, zp2, zp3 = solutions[0], solutions[1], solutions[2]

         wp1 = (a)*(zp1)**5 + (b)*(zp1)**4 + (c)*(zp1)**3 + (d)*(zp1)**2 + (e)*(zp1)**1 + (f)*(zp1)**0
         wp2 = (a)*(zp2)**5 + (b)*(zp2)**4 + (c)*(zp2)**3 + (d)*(zp2)**2 + (e)*(zp2)**1 + (f)*(zp2)**0
         wp3 = (a)*(zp3)**5 + (b)*(zp3)**4 + (c)*(zp3)**3 + (d)*(zp3)**2 + (e)*(zp3)**1 + (f)*(zp3)**0

         print("TP1:", [zp1, wp1])
         print("TP2:", [zp2, wp2])
         print("TP3:", [zp3, wp3], "\n")
         return f"TP1: {[zp1, wp1]} \nTP2: {[zp2, wp2]} \nTP3: {[zp3, wp3]}"
    elif (a == 0) and (b != 0):
         zp1, zp2 = solutions[0], solutions[1]

         wp1 = (a)*(zp1)**5 + (b)*(zp1)**4 + (c)*(zp1)**3 + (d)*(zp1)**2 + (e)*(zp1)**1 + (f)*(zp1)**0
         wp2 = (a)*(zp2)**5 + (b)*(zp2)**4 + (c)*(zp2)**3 + (d)*(zp2)**2 + (e)*(zp2)**1 + (f)*(zp2)**0

         print("TP1:", [zp1, wp1])
         print("TP2:", [zp2, wp2], "\n")
         return f"TP1: {[zp1, wp1]} \nTP2: {[zp2, wp2]}"
    elif (a == 0) and (b == 0) and (c != 0):
         zp1 = solutions[0]

         wp1 = (a)*(zp1)**5 + (b)*(zp1)**4 + (c)*(zp1)**3 + (d)*(zp1)**2 + (e)*(zp1)**1 + (f)*(zp1)**0
         print("TP1:", [zp1, wp1], "\n")
         return f"TP1: {[zp1, wp1]}"

    elif (a == 0) and (b == 0) and (c == 0):
         print("No turning points.\n")
         return "No turning points."



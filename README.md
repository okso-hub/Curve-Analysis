# Curve analysis

## Inspiration for this project

I created this project when I had curve analysis back in tenth grade. My problem was that if I wanted to check my solutions, I always had to google a website and put in my function using bad syntax (e.g. 13x^2 - 4/3x^2).

I was quite experienced with Python and thought about creating a solution for myself. Also, my teacher did the same thing in Microsoft Excel, so it was sort of a competition.

### How to run the project

Direct to the directory, where the main script is scored. Then run the program using the `python main.py` command.

Now you'll be asked for all of the factors. Let's say we have the following function:

f(x) = x^4 - 19x^2 + 48

Then we would enter the factors as you see here:

```
python main.py
Factor of x^5 = 0
Factor of x^4 = 1
Factor of x^3 = 0
Factor of x^2 = -19
Factor of x^1 = 0
Factor of x^0 = 48
```
After entering the last factor, the program will solve it and display the solution like this:

```
python main.py
Factor of x^5 = 0
Factor of x^4 = 1
Factor of x^3 = 0
Factor of x^2 = -19
Factor of x^1 = 0
Factor of x^0 = 48

O̲r̲i̲g̲i̲n̲a̲l̲ ̲f̲u̲n̲c̲t̲i̲o̲n
   4      2
1 x - 19 x + 48

F̲i̲r̲s̲t̲ ̲d̲e̲r̲i̲v̲a̲t̲i̲v̲e
   3
4 x - 38 x

S̲e̲c̲o̲n̲d̲ ̲d̲e̲r̲i̲v̲a̲t̲i̲v̲e
    2
12 x - 38

T̲h̲i̲r̲d̲ ̲d̲e̲r̲i̲v̲a̲t̲i̲v̲e

24 x
R̲a̲n̲g̲e̲ ̲o̲f̲ ̲d̲e̲f̲i̲n̲i̲t̲i̲o̲n
D = R (Real numbers)

B̲e̲h̲a̲v̲i̲o̲u̲r̲ ̲t̲o̲ ̲i̲n̲f̲i̲n̲i̲t̲y
The graph moves from oo to oo.

A̲x̲i̲s̲ ̲i̲n̲t̲e̲r̲c̲e̲p̲t
The axis intercept is at Py( 0 | 48.0)

S̲y̲m̲m̲e̲t̲r̲y
The graph is axially symmetric to the y axis, since all exponents of the variable x are even.

Z̲e̲r̲o̲p̲o̲i̲n̲t̲s
zp1: -4.0000000000000036
zp2: 3.9999999999999996
zp3: -1.7320508075688779
zp4: 1.7320508075688772

E̲x̲t̲r̲e̲m̲a
E1: [-3.082207001484488, -42.25]
E2: [3.0822070014844885, -42.25]
E3: [0.0, 48.0]

T̲u̲r̲n̲i̲n̲g̲ ̲p̲o̲i̲n̲t̲s
TP1: [-1.7795130420052185, -2.1388888888888857]
TP2: [1.7795130420052185, -2.1388888888888857] 
```

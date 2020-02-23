# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def fact(n):
    return 1 if n <= 0 else n * fact(n-1)

def p(k, l):
    return (l**k * math.exp(-l)) / fact(k)

mean = float(input())

val = int(input())

print("{:.3f}".format(p(val, mean)))

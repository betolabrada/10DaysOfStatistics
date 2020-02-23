# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

def cdf(x, mean, std):
    return 0.5 * (1 + math.erf((x - mean) / (std * 2**0.5))) 

# Input mean and std
mean, std = [float(i) for i in input().split()]

# Input x for question 1
x1 = float(input())

# Input lower and upper range for question 2
x2l, x2u = [float(i) for i in input().split()]

# Less than x1
print("{:.3f}".format(cdf(x1, mean, std)))

# Between x2l and x2u
print("{:.3f}".format(cdf(x2u, mean, std) - cdf(x2l, mean, std)))




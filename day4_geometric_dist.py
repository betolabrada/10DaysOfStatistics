# Enter your code here. Read input from STDIN. Print output to STDOUT

# The probability that a machine produces a defective product is 1/3
# What is the probability that the 1st defect is found during the
# 5th inspection

def g(n, p, q):
    return q**(n - 1) * p


u, d = [int(i) for i in input().rstrip().split()]

n = int(input())

p = u / d

q = 1 - p

print("{:.3f}".format(g(n, p, q)))



# Enter your code here. Read input from STDIN. Print output to STDOUT
# A manufacturer of metal pistons finds that, on average, 12% of the
# pistons they manufacture are rejected because they are 
# incorrectly sized. What is the probability that a batch of 10
# pistons will contain:
#    No more than 2 rejects?
#    At least 2 rejects

# Factorial function
def fact(n):
    return 1 if n <= 1 else n * fact(n-1)

# Combinations nCr
def c(n, r):
    return fact(n) / (fact(n - r) * fact(r))

# Binomial distribution
def b(x, n, p):
    return c(n, x) * p**x * (1 - p)**(n - x)

input_data = input().split()

p = float(input_data[0]) / 100;

n = int(input_data[1])

print("{:.3f}".format(sum([b(i, n, p) for i in range(3)])))
print("{:.3f}".format(1 - sum([b(i, n, p) for i in range(2)])))

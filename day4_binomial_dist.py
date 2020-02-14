# The ratio of boys to girls for babies born in Russia is 
# 1.09 to 1. If there is 1 child born per birth, what 
# proportion of Russian families with exactly 6 children 
# will have at least 3 boys?

# Factorial function
def fact(n):
    return 1 if n <= 1 else n * fact(n-1)

# Combinations nCr
def c(n, r):
    return fact(n) / (fact(n - r) * fact(r))

# Binomial distribution
def b(x, n, p):
    return c(n, x) * p**x * (1 - p)**(n - x)


boy, girl = [float(i) for i in input().split()]

# Get the odds of getting a boy against getting a girl
odds = boy / girl

# Convert to probability
# (you can also do p = boy / (boy + girl))
p = odds / (1 + odds)

# Cumulative probability for at least 3
result = sum([b(i, 6, p) for i in range(3, 7)])

print("{:.3f}".format(result))


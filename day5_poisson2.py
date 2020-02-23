# Enter your code here. Read input from STDIN. Print output to STDOUT

a, b = [float(i) for i in input().split()]

print("{:.3f}".format(160 + 40 * (a + a**2)))
print("{:.3f}".format(128 + 40 * (b + b**2)))
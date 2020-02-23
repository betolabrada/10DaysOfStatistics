# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def mean(x):
    return sum(x) / len(x)

def std(x):
    m = mean(x)
    return math.sqrt(sum([(i - m)**2 for i in x]) / len(x))

def pcc(x, y, n):
    m_x = mean(x)
    m_y = mean(y)
    return sum([(x[i] - m_x) * (y[i] - m_y) for i in range(n)]) / (n * std(x) * std(y))

n = int(input())

x = [float(i) for i in input().split()]

y = [float(i) for i in input().split()]

print("{:.3f}".format(pcc(x, y, n)))




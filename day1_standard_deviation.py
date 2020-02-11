# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

n = int(input())

x = [int(i) for i in input().split()]

mean = sum(x) / n

squared_distances = [(i - mean)**2 for i in x]

std_deviation = math.sqrt(sum(squared_distances) / n)

print("{:.1f}".format(std_deviation))
# calculate the weighted mean

n = int(input())

x = [int(i) for i in input().split()]

w = [int(i) for i in input().split()]

weighted_mean = sum([(x[i] * w[i]) for i in range(n)]) / sum(w)

print("{:.1f}".format(weighted_mean))



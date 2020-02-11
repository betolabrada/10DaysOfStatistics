# Enter your code here. Read input from STDIN. Print output to STDOUT

# Calculating Inter-Quartile-Range (IQR) from a frequencies table

def median(numbers):
    if len(numbers) % 2 != 0:
        return numbers[len(numbers) // 2]  
    else: 
        return (numbers[len(numbers) // 2] + numbers[len(numbers) // 2 - 1]) / 2

n = int(input())

x = [int(i) for i in input().split()]

f = [int(i) for i in input().split()]

# Convert to data set list
data_set = []
for i in range(n):
    for j in range(f[i]):
        data_set.append(x[i])

# Sort data set and update length
data_set.sort()
n = len(data_set)

# Obtain Q1 and Q3 from splitting the array
offset = 0
if n % 2 != 0: offset = 1

q1 = median(data_set[:n // 2])
q3 = median(data_set[n // 2 + offset:n])

iqr = q3 - q1

print("{:.1f}".format(iqr))
         


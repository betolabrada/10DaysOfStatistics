# Enter your code here. Read input from STDIN. Print output to STDOUT

# calculate quartiles: q1, q2(median) and q3

def median(numbers):
    if len(numbers) % 2 != 0:
        return numbers[len(numbers) // 2]  
    else: 
        return (numbers[len(numbers) // 2] + numbers[len(numbers) // 2 - 1]) / 2

n = int(input())

x = sorted([int(i) for i in input().split()])

offset = 0
if n % 2 != 0: offset = 1

q1 = median(x[:n // 2])
q2 = median(x)
q3 = median(x[n // 2 + offset:n])

if int(q1) == q1: q1 = int(q1)
if int(q2) == q2: q2 = int(q2)
if int(q3) == q3: q3 = int(q3)

print(q1)
print(q2)
print(q3)




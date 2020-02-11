from collections import Counter

def mean(numbers):
    return sum(numbers) / len(numbers)

def median(numbers):
    if len(numbers) % 2 != 0:
        return numbers[len(numbers) // 2]  
    else: 
        return (numbers[len(numbers) // 2] + numbers[len(numbers) // 2 - 1]) / 2

def mode(numbers):
    counter = Counter(numbers)
    frequencies = dict(counter)
    max_freq = 0
    result = -1
    for k in sorted(frequencies):
        if frequencies[k] > max_freq:
            max_freq = frequencies[k]
            result = k
    return result


n = int(input())
x = [int(i) for i in input().split()]

print(mean(x), median(sorted(x)), mode(x), sep="\n")





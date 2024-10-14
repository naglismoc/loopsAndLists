
#          0  1  2
numbers = [1, 5, 10]

print(numbers)
print(numbers[0])
print(numbers[1])
print(numbers[2])

numbers[0] = 6

print(numbers[0])

print(len(numbers))
#01234
"labas"

# numbers[3] = 7 #veiktu PHP
numbers.append(7)
print(numbers)
numbers.extend([8, 10])
print(numbers)
numbers.insert(1,10)
print(numbers)
numbers.pop()
print(numbers)
num = numbers.pop(4)
print(numbers)
print(num)
print(numbers.index(10))
print(5 in numbers)
print(numbers.count(10))
print("---")
sortedNumbers = sorted(numbers)
print(sortedNumbers)
print(numbers)

numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

print(numbers[::2])
print(numbers[1:3])

nums = [1,2,3,4]


nums2d = [
    [1,2,3,4],
    [1,2,3,4],
    [1,2,3,4]
]

nums2d = [ [1,2,3,4], [1,2,3,4], [1,2,3,4]]

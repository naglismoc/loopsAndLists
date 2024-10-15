import random

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


masinos = ['audi', 'bmw', 'volvo', 'mercedes', 'opel']
masinos[4] = 'bentley'
print(masinos)
kopija = masinos[:]
print(kopija)
masinos[1] = 'NAUJAS'
print(masinos)
print(kopija)


masinos = ['audi', 'bmw', 'volvo', 'mercedes', 'opel']
masinos[4] = 'bentley'
print(masinos)
kopija = masinos
print(kopija)
masinos[1] = 'NAUJAS'
print(masinos)
print(kopija)

m2 = masinos.copy()

masinos[0] = "feraris"

print(masinos)
print(m2)


print(list(range(10)))
print(list(range(7,10)))
print(list(range(0,10,2)))

for i in range(4):
    print("labas")
    print("rytas")
print(":)")

for i in range(5):
    print(i)

for car in masinos:
    print(car)

for letter in "kastonas":
    print(letter)



for car in masinos:
    print(f'{car} yra {len(car)} simboliu ilgio')

for i in range(1, 100):
    if i % 2 != 0:
        continue
    print(i)
print("------------------------------")
for i in range(1, 100):
    if i % 7 == 0:
        break
    print(i)
print("------------------------------")
for i in range(1, 100):
    print(i)
    if i % 7 == 0:
        break

countSymbols = 0
countWords = 0
for car in masinos:
    print(car)
    countSymbols += len(car)
    countWords += 1

print(f'masinos uzima {countSymbols} simboliu')
print(f'masinos simboliu vidurkis yra {countSymbols / len(masinos)} ')
print(f'masinos simboliu vidurkis yra {countSymbols /countWords} ')

print(masinos)

carsInfo = "Siuo metu pardavime turime: "
for car in masinos:
    carsInfo += car + ", "
print(carsInfo[:-2]+".")


for i in range(3):
    for a in range(5):
        print(a)

print("------------------------------")

for y in range(1, 11):
    line = ""
    for x in range(1, 11):
        # line += str(y * x) + " "
        line += f'{y * x} '
    print(line)
print("------------------------------")

hiCounter = 0
while True:
    print("hi")
    hiCounter += 1
    if hiCounter == 5:
        break

print("------------------------------")


while True:
    coinFlip = random.randint(0,1)
    if coinFlip == 0:
        print("iskrito herbas")
        break
    print("iskrito skaicius")


while True:
    arr = []
    for i in range(random.randint(0,10)):
        arr.append(random.randint(1,5))
    print(arr)
    if len(arr) == 10:
        break


# задача A

for i in range(1, (x := int(input())) + 1):
    for j in range(1, x + 1):
        if j < x:
            print(i * j, end=' ')
        else:
            print(i * j)    
# задача B

for i in range(1, (x := int(input())) + 1):
    for j in range(1, x + 1):
        print(f'{j} * {i} = {i * j}')
# задача C

for z in range(1, x := int(input()) + 1):
    if z in (sum(range(i)) for i in range(x)):
        print(z)
    else:
        print(z, end=' ')
# задача D
summ = 0
for _ in range(int(input())):
    summ += sum(map(int, list(input())))
print(summ)
# задача E

counter, temp = 0, 0
for _ in range(int(input())):
    while (x := input()) != 'ВСЁ':
        if x == 'зайка':
            temp += 1
    if temp:
        counter += 1
        temp = 0
print(counter)
# задача F

n, a = int(input()), int(input())
for _ in range(n - 1):
    b = int(input())
    while b:
        a, b = b, a % b
print(a)
# задача G

for i in range(int(input())):
    for j in range(3 + i, 0, -1):
        print(f'До старта {j} секунд(ы)')
    print(f'Старт {i + 1}!!!')
# задача H

name, summ = '', 0
for _ in range(int(input())):
    temp_name, temp_summ = input(), sum(map(int, input()))
    if temp_summ >= summ:
        name, summ = temp_name, temp_summ
print(name)
# задача I

number = ''
for _ in range(int(input())):
    number += max(input())
print(number)
# задача J

for i in range(1, (n := int(input())) - 1):
    if i == 1:
        print('А Б В')
    for j in range(1, n - i):
        print(f'{i} {j} {n - i - j}')
# задача K

counter = 0
for i in range(int(input())):
    j = 2
    if (n := int(input())) > 1:
        counter += 1
        if n == 2:
            counter += 1
        while n % j:
            if j > n ** 0.5:
                break
            j += 1
        else:
            counter -= 1
print(counter)
# задача L

n, k = int(input()), int(input())
width = len(str(n * k))
for i in range(1, n + 1):
    for j in range(k * (i - 1) + 1, k * i + 1):
        if j == k * i:
            print(str(j).rjust(width, ' '))
        else:
            print(str(j).rjust(width, ' '), end=' ')
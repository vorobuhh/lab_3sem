# задача A

while input() != 'Три!':
    print('Режим ожидания...')
print('Ёлочка, гори!')    
# задача B

counter = 0
while (x := input()) != 'Приехали!':
    if 'зайка' in x:
        counter += 1
print(counter)
# задача C

a, b = int(input()), int(input())
for i in range(a, b + 1):
    print(i, end=' ')
# задача D

a, b = int(input()), int(input())
if a < b:
    for i in range(a, b + 1):
        print(i, end=' ')
else:
    for i in range(a, b - 1, -1):
        print(i, end=' ')
# задача E

counter = 0
while (x := input()) != '0':
    if float(x) >= 500:
        counter += 0.9 * float(x)
    else:
        counter += float(x)
print(counter)
# задача F

a, b = int(input()), int(input())
while b:
    a, b = b, a % b
print(a)
# задача G

a, b = c, d = int(input()), int(input())
while b:
    a, b = b, a % b
print(c * d // a)
# задачаH

line, number = input(), int(input())
for _ in range(number):
    print(line)
# задача I
a = int(input())
factorial = 1
for i in range(1, a + 1):
    factorial *= i
print(factorial)
# задача J

x, y = 0, 0
while (direction := input()) != 'СТОП':
    n = int(input())
    if direction == 'ВОСТОК':
        x += n
    elif direction == 'ЗАПАД':
        x -= n
    elif direction == 'СЕВЕР':
        y += n
    elif direction == 'ЮГ':
        y -= n
print(y, x, sep='\n')
# задача K

print(sum(map(int, input())))
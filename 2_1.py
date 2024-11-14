# задача A

print("Привет, Яндекс!")    
# задача B

print("Как Вас зовут?")
print("Привет,",  input())
# задача C

print((input() + '\n') * 3)
# задача D

print(int(int(input()) - 2.5 * 38))
# задача E

price = int(input())
weight = int(input())
money = int(input())
print(money - price * weight)
# задача F

item = input()
price = int(input())
weight = int(input())
money = int(input())
print('Чек', f'{item} - {weight}кг - {price}руб/кг', sep='\n')
print(f'Итого: {int(price * weight)}руб')
print(f'Внесено: {money}руб')
print(f'Сдача: {int(money - price * weight)}руб')
# задача G

print(('Купи слона!' + '\n') * int(input()))
# задача H

number = int(input())
punish = input()
print((f'Я больше никогда не буду писать "{punish}"!\n') * number)
# задача I

print(int(input()) * int(input()) // 2)
# задача J

name = input()
locker = input()
print(f'Группа №{locker[0]}.')
print(f'{locker[2]}. {name}.')
print(f'Шкафчик: {locker}.')
print(f'Кроватка: {locker[1]}.')
# задача K

number = input()
print(f'{number[1]}{number[0]}{number[3]}{number[2]}')
# задача L

num1 = list(map(int, input().rjust(3, '0')))
num2 = list(map(int, input().rjust(3, '0')))
num_0 = str((num1[0] + num2[0]) % 10)
num_1 = str((num1[1] + num2[1]) % 10)
num_2 = str((num1[2] + num2[2]) % 10)
print((num_0 + num_1 + num_2).lstrip('0'))
# задача M

children = int(input())
candies = int(input())
print(candies // children)
print(candies % children)
# задача N

red = int(input())
green = int(input())
blue = int(input())
print(red + blue + 1)
# задача O

hours = int(input())
minutes = int(input())
delivery_time = int(input())
new_minutes = str((minutes + delivery_time) % 60)
new_hours = str((hours + (minutes + delivery_time) // 60) % 24)
print(f'{new_hours.rjust(2, "0")}:{new_minutes.rjust(2, "0")}')
# задача P

stock = int(input())
market = int(input())
speed = int(input())
time = abs(market - stock) / speed
print(f'{time:.2f}')
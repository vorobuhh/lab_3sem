# задача A

print(''.join(set(input())))   
# задача B

print(''.join(set(input()).intersection(set(input()))))
# задача C

objects = []
for _ in range(int(input())):
    objects.extend(input().split())
print('\n'.join(set(objects)))
# задача D

a, b = int(input()), int(input())
semolina, oatmeal = set(), set()
for _ in range(a):
    semolina.add(input())
for _ in range(b):
    oatmeal.add(input())
both = len(semolina & oatmeal)
print(both if both else 'Таких нет')
# задача E

a, b = int(input()), int(input())
porridges = []
for _ in range(a + b):
    porridges.append(input())
both = len([i for i in porridges if porridges.count(i) == 1])
print(both if both else 'Таких нет')
# задача F

a, b = int(input()), int(input())
porridges = []
for _ in range(a + b):
    if (x := input()) not in porridges:
        porridges.append(x)
    else:
        porridges.remove(x)
if len(porridges):
    for kid in sorted(porridges):
        print(kid)
else:
    print('Таких нет')
# задача G
MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', ' ': ' ',
}
line = input()
for letter in line:
    print(MORSE[letter.upper()], end=' ' if letter != ' ' else '\n')
# задача  H

a, kids = int(input()), []
for _ in range(a):
    kids.extend([input().split()])
kids.sort()
key, counter = input(), 0
for kid in kids:
    if key in kid[1:]:
        print(kid[0])
        counter += 1
if not counter:
    print('Таких нет')
# задачаI

d = {}
while x := input().split():
    for i in x:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
for j in d:
    print(j, d[j])
# задача J

LITER = {
    'А': 'A', 'Б': 'B', 'В': 'V',
    'Г': 'G', 'Д': 'D', 'Е': 'E',
    'Ё': 'E', 'Ж': 'ZH', 'З': 'Z',
    'И': 'I', 'Й': 'I', 'К': 'K',
    'Л': 'L', 'М': 'M', 'Н': 'N',
    'О': 'O', 'П': 'P', 'Р': 'R',
    'С': 'S', 'Т': 'T', 'У': 'U',
    'Ф': 'F', 'Х': 'KH', 'Ц': 'TC',
    'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH',
    'Ы': 'Y', 'Э': 'E', 'Ю': 'IU',
    'Я': 'IA', 'Ь': '', 'Ъ': '',
}
for i in (x := input()):
    if i.upper() in LITER:
        print(LITER[i.upper()].lower().capitalize() if i == i.upper() else LITER[i.upper()].lower(), end='')
    else:
        print(i, end='')
# задача K

people = []
for _ in range(int(input())):
    people.append(input())
print(len([i for i in people if people.count(i) > 1]))
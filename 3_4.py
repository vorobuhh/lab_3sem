#Задача A
for index, word in enumerate(input().split(), start=1):
    print(f'{index}. {word}')

#Задача B
for kids in zip(a := input().split(', '), b := input().split(', ')):
    print(f'{kids[0]} - {kids[1]}')

#Задача C
from itertools import count

a, b, step = list(map(float, input().split()))
for value in count(a, step):
    if value <= b:
        print(f'{value:.2f}')
    else:
        break

#Задача D
from itertools import accumulate

for value in accumulate(map(lambda x: ' ' + x, input().split())):
    print(value[1:])

#Задача E
items = set()
for _ in range(3):
    items = items.union({item for item in input().split(', ')})
for i, item in enumerate(sorted(items), start=1):
    print(f'{i}. {item}')

#Задача F
from itertools import product

nominal = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'валет', 'дама', 'король', 'туз']
suits = ['пик', 'треф', 'бубен', 'червей']
suits.remove(input())
for card in product(nominal, suits):
    print(card[0], card[1])

#Задача G
from itertools import product

players, games = [], []
for _ in range(int(input())):
    players.append(input())
for i in product(players, players):
    if i[0] != i[1] and [i[1], i[0]] not in games:
        games.append([i[0], i[1]])
        print(f'{i[0]} - {i[1]}')

#Задача H
cereals = []
for _ in range(int(input())):
    cereals.append(input())
amount = int(input())
cereals *= amount // len(cereals) + 1
for i in range(amount):
    print(cereals[i])

#Задача I
from itertools import product

for i in (n := range(1, int(input()) + 1)):
    print(' '.join(map(lambda x: str(x[0] * x[1]), product(n, [i]))))

#Задача J
for i in range(1, (n := int(input())) - 1):
    if i == 1:
        print('А Б В')
    for j in range(1, n - i):
        print(f'{i} {j} {n - i - j}')

#Задача K
from itertools import product

n, m = int(input()), int(input())
for i in range(n):
    line = product(range(1, m + 1), [i * m])
    print(' '.join(map(lambda x: str(sum(x)).rjust(len(str((n - 1 - i) * m + sum(x))), ' '), line)))

#Задача L
items = []
for _ in range(int(input())):
    items.extend([item for item in input().split(', ')])
for i, item in enumerate(sorted(items), start=1):
    print(f'{i}. {item}')

#Задача M
from itertools import permutations

items = []
for _ in range(int(input())):
    items.append(input())
for i in sorted(permutations(items)):
    print(', '.join(i))

#Задача N
from itertools import permutations

items = []
for _ in range(int(input())):
    items.append(input())
for i in sorted(permutations(items, 3)):
    print(', '.join(i))

#Задача O
from itertools import permutations

items = []
for _ in range(int(input())):
    items.extend([item for item in input().split(', ')])
for item in sorted(permutations(items, 3)):
    print(' '.join(item))

#Задача P
from itertools import product, permutations

suits_ro = ["бубен", "пик", "треф", "червей"]
suit, exception = input(), input()
best_suit = [s for s in suits_ro if s.startswith(suit[0:3])][0]
nominal = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
nominal.remove(exception)
comb = permutations(product(sorted(nominal), sorted(suits_ro)), 3)
y = [', '.join(' '.join(j) for j in sorted(i)) for i in comb]
triads = [i for i in y if best_suit in i][:10]
for triad in triads:
    print(triad)

# задача A

for _ in range(int(input())):
    if (word := input())[0] not in 'абв':
        print('NO')
        break
else:
    print('YES')    
# задача B

for i in input():
    print(i)
    # задача C

length = int(input())
for _ in range(int(input())):
    line = input()
    print(line[:length - 3].ljust(length, ".") if len(line) > length else line)
# задача D

while (n := input()):
    if not n.endswith('@@@'):
        if n.startswith('##'):
            print(n[2:])
        else:
            print(n)
# задача E

print('YES' if (line := input()) == line[::-1] else 'NO')
# задача F

counter = 0
for _ in range(int(input())):
    counter += input().count("зайка")
print(counter)
# задача G

print(sum(map(int, input().split())))
# задача H

for _ in range(int(input())):
    if "зайка" in (place := input()):
        print(place.index("зайка") + 1)
    else:
        print("Заек нет =(")
# задача I

while (n := input()):
    if not n.startswith('#'):
        print(n[:(n.index('#') if '#' in n else len(n))])
# задача J
data = []
while (n := input()) != 'ФИНИШ':
    data.extend(n.lower().split())
max_count, data = 0, ''.join(data)
for symbol in set(data):
    max_count = max(max_count, data.count(symbol))
print(min([i for i in set(data) if data.count(i) == max_count]))
# задача K

headings = []
for _ in range(int(input())):
    headings.append(input())
word = input()
for heading in headings:
    if word.lower() in heading.lower():
        print(heading)
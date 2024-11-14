#Задача A
[number ** 2 for number in range(a, b + 1)]

#Задача B
[[i * j for i in range(1, n + 1)] for j in range(1, n + 1)]

#Задача C
[len(word) for word in sentence.split()]

#Задача D
{number for number in numbers if number % 2}

#Задача E
{number for number in numbers if number in [i ** 2 for i in range(1, int(max(numbers) ** 0.5 + 1))]}

#Задача F
{letter: text.lower().count(letter) for letter in text.lower() if letter.isalpha()}

#Задача G
{number: [i for i in range(1, number + 1) if not number % i] for number in numbers}

#Задача H
''.join(word[0] for word in string.split()).upper()

#Задача I
' - '.join(str(i) for i in sorted(set(numbers)))

#Задача J
''.join(i * j for i, j in rle)

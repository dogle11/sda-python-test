# USHTRIMI 1
from uppercase import new_word

x: str = 'Ana Toti'
print(x.split())

# USHTRIMI 2

y = x[::-1]
print(y)

# USHTRIMI 3

z = x.replace('Toti', 'Frasheri')
print(z)

# USHTRIMI 4

countA = x.lower().count('a')
print(countA)

# USHTRIMI 5

x += ' Frasheri'
print(x)

# USHTRIMI 6

word = x.split()
new_word = word.insert(1, ('Anastasia'))
new_word1 = ' '.join(new_word)
print(new_word1)

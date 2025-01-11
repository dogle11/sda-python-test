# USHTRIMI 1

menu: list[str] = []
menu.append('Pizza')
menu.append('Spaghetti')
menu.append('Fish')

print(menu)
#menu.remove('Spaghetti')
print(menu)
if 'Spaghetti' in menu:
    print('Po, Spaghetti eshte ne menu')
else:
    print('Jo, Spaghetti nuk eshte ne menu')

# USHTRIMI 2

prices: list[float] = []
prices.append(4.0)
prices.append(6.5)
prices.append(9.5)
print(prices)

def myfunc():
    largest = max(prices)
    global position
    position = prices.index(largest)
    print('Produkti me i shtrenjte eshte ', menu[position])

myfunc()
menu.pop(position)
prices.pop(position)

print(menu)
print(prices)

myfunc()
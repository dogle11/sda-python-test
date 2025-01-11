# Ushtrimi 1

# x: float = float(input())
# y: float = float(input())
#
# def find_sum(x, y):
#     result = x + y
#     print(f'Shuma eshte {result}')
# find_sum(x, y)

# Ushtrimi 2

#
# def find_total_positive_sum(numbers):
#     sum = 0
#     for i in range(0, len(numbers)):
#         if numbers[i] > 0:
#             sum += numbers[i]
#
#         return sum
#
#     print(f'Shuma totale eshte {sum}')
#
#
# result = find_total_positive_sum([2, 4, -7, 8, -9])
#
# print(f'Rezultati i numrave eshte {result}')


# Ushtrimi 3

names: list[str]

def find_shortest_name():
    shortest = names[0]
    for i in names:
        if len(i) < len(shortest):
            shortest = i
    return shortest

names = find_shortest_name(["Bledi", "Ana", "Sara"])
print(f"The shortest name is: {result}")
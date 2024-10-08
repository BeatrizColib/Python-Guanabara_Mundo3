numbers = [[], []]
for c in range(0,7):
    num = int(input('digite um número: '))
    if num % 2 == 0:
        numbers[0].append(num)
    else:
        numbers[1].append(num)
print(f'{sorted(numbers[0]), sorted(numbers[1])}')

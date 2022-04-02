def sum_of_numbers(digit):
    result = 0
    while digit != 0:
        result += digit % 10
        digit = digit // 10
    return result


numbers = []
for num in range(1, 1001):
    if num % 2 != 0:
        numbers.append(num**3)


first_total = 0
for number in numbers:
    if sum_of_numbers(number) % 7 == 0:
        first_total += number


second_total = 0
for idx, number in enumerate(numbers):
    number += 17
    if sum_of_numbers(number) % 7 == 0:
        second_total += number


print(f"Список чисел: {numbers}")
print(f"Начальная сумма: {first_total}")
print(f"Конечная сумма: {second_total}")
def odd_nums(x: int):
    nums_gen = (num for num in range(1, x+1, 2))
    return nums_gen


print(type(odd_nums(15)))
odd_to_15 = odd_nums(15)
for _ in range(8):
    print(next(odd_to_15))

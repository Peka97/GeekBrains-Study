def odd_nums(x: int):
    for num in range(1, x+1, 2):
        yield num


odd_to_15 = odd_nums(15)
for _ in range(8):
    print(next(odd_to_15))

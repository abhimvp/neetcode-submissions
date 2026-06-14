def add_two_numbers() -> int:
    inp = input()
    nums = inp.split(",")
    l = [int(x) for x in nums]
    return sum(l)


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())

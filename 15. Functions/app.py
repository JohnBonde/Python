def increment(number: int, by: int = 1) -> tuple:
    return (number, number + by)


print(increment(2, by=3))


def multiply(*list):
    total = 1
    for number in list:
        total *= number
    return total


print(multiply(2, 3, 4, 5))

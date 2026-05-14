def read_integer() -> int | None:
    try:
        return int(input())
    except ValueError:
        pass


def read_float() -> float:
    return float(input())


# do not modify below this line
print(read_integer())
print(read_integer())
print(read_integer())

print(read_float())
print(read_float())
print(read_float())

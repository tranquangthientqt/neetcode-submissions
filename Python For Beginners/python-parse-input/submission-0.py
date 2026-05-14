from typing import List

def read_integers() -> List[int]:
    nums = input()
    return [int(num) for num in nums.split(',')]

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())

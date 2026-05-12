from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    dict_ = {}
    for char in word:
        if char not in dict_:
            dict_.update({char : 1})
        else:
            dict_[char] += 1
    return dict_




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))

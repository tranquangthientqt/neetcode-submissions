def remove_fourth_character(word: str) -> str:
    if len(word) < 4:
        return word
    prefix = word[:3]
    suffix = word[4:]
    return prefix + suffix

    

# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))

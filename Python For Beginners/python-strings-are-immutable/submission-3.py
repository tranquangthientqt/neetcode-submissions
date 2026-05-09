def remove_fourth_character(word: str) -> str:
  # Nếu từ ngắn hơn 4 ký tự, không có ký tự thứ 4 để xóa
    if len(word) < 4:
        return word
    # Ghép phần trước index 3 và phần sau index 3
    return word[:3] + word[4:]

    

# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))

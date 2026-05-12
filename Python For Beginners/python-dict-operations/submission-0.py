from typing import Dict

your_dict = { 
  "a": 10, 
  "apple": 12,
  "bat": 7
}
def check(dict_ : Dict[str, int], target : str) -> bool:
    return target in dict_




print(your_dict)
print(your_dict["a"])
print(check(your_dict, "d"))
your_dict["a"] = 4
print(your_dict)
from typing import List

def contains_duplicate(words: List[str]) -> bool:
    
    my_set = set(words)

    result = bool

    x = 0
    y = 0

    for nums in my_set:
        x += 1
    
    for nums in words:
        y += 1
    
    if x < y:
        result = True
    else:
        result = False
    
    return result


# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))

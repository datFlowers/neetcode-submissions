def first_n_characters(s: str, n: int) -> str:
    result = s[:n]
    return result

def last_n_characters(s: str, n: int) -> str:
    index = len(s) - n
    
    result = s[index:]
    return result


# do not modify below this line
print(first_n_characters("NeetCode", 3))
print(first_n_characters("NeetCode", 4))
print(first_n_characters("NeetCode", 8))

print(last_n_characters("NeetCode", 3))
print(last_n_characters("NeetCode", 4))
print(last_n_characters("NeetCode", 8))

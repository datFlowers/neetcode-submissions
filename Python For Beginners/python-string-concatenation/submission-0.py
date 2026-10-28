def concatenate(s1: str, s2: str) -> str:
    concat = s1 + s2

    length = len(concat)

    if length <= 10:
        return concat
    else:
        return "Too long!"




# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))

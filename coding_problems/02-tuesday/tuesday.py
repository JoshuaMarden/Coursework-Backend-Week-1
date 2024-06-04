def length_of_last_word(s: str) -> int:

    index = s.rfind(" ")

    while index == len(s) - 1:
        s = s[:-1]
        index = s.rfind(" ")

    return len(s[index + 1:])


if __name__ == "__main__":
    print(length_of_last_word("This is a test"))

    print(length_of_last_word("Test number two   "))

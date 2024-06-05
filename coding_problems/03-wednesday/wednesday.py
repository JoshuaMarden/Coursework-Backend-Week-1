def is_valid(s: str) -> bool:

    brackets = ["{", "[", "(", "}", "]", ")"]

    s_simple = set([char for char in list(s) if char in brackets])

    for index, bracket in enumerate(brackets[:4]):
        if bracket in s_simple and not brackets[index+3] in s_simple:
            return False

    return True


if __name__ == "__main__":
    print(is_valid("{test 1}"))
    print(is_valid("[test 2)"))

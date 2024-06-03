def kebabize(st: str) -> str:

    st = list(st)
    new_list = []
    for char in st:

        if char.isnumeric():
            continue
        elif char.islower():
            new_list.append(char)
        elif char.isupper():
            char = char.lower()
            new_list.append("-")
            new_list.append(char)

    if len(new_list) > 0 and new_list[0] == "-":
        new_list = new_list[1:]

    kebab_casing = "".join(new_list)

    return kebab_casing


if __name__ == "__main__":
    print(kebabize("thisIsATest"))

    print(kebabize("42"))

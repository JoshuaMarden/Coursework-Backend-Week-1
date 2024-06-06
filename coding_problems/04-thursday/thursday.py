def missing_number(nums: list[int]) -> int:

    length = len(nums)

    for number in range(length+1):
        if not number in nums:
            return number


if __name__ == "__main__":
    print(missing_number([0, 1]))

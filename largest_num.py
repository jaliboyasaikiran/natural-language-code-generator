def find_largest(numbers):
    """
    Return the largest number in the list `numbers`.
    Raises ValueError if the list is empty.
    """
    if not numbers:
        raise ValueError("The list is empty.")
    max_val = numbers[0]
    for num in numbers[1:]:
        if num > max_val:
            max_val = num
    return max_val
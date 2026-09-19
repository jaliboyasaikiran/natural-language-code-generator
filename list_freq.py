def count_frequencies(lst):
    """
    Count the frequency of each element in the given list.

    Args:
        lst (list): The list of elements to count.

    Returns:
        dict: A dictionary where keys are elements from the list and values are their counts.
    """
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return freq
# TODO: Implement the following functions based on the descriptions.

def reverse_list(lst):
    """
    Reverses the given list.
    :param lst: List of integers.
    :return: A list with elements in reverse order.
    """
     # Implement this
    
    return lst[::-1]

def count_occurrences(lst, element):
    """
    Counts how many times the given element appears in the list.
    :param lst: List of elements.
    :param element: Element to count.
    :return: Integer count of occurrences.
    """
    # Implement this
    count = 0
    for i in lst:
            count =+ 1
    return int(count)

def get_keys_with_value(dct, value):
    """
    Returns a list of keys that have the given value in the dictionary.
    :param dct: Dictionary to search.
    :param value: Value to find.
    :return: List of keys.
    """
    # Implement this
    for value in dct:
        return dct[value]

def merge_sorted_lists(lst1, lst2):
    """
    Merges two sorted lists into one sorted list.
    :param lst1: First sorted list.
    :param lst2: Second sorted list.
    :return: Merged sorted list.
    """
    # Implement this
    new_lst = lst1 + lst2
    return sorted(new_lst) 

def find_second_largest(numbers):
    """
    Finds the second largest number in a list.
    :param numbers: List of integers.
    :return: The second largest integer.
    """
    # Implement this
    numbers = int(numbers) 
    for i in range(0, numbers + 1):
        if i < numbers[-1]:
            return i
        else:
            return None

def is_anagram(str1, str2):
    """
    Checks if two strings are anagrams.
    
    An anagram is a word or phrase formed by rearranging the letters of another,
    using all the original letters exactly once. For example, "listen" and "silent"
    are anagrams because they use the same letters in a different order.
    
    :param str1: First string.
    :param str2: Second string.
    :return: True if the strings are anagrams, False otherwise.
    """
    # Implement this
    for i in str1:
        for j in str2:
            if i in j:
                return True
            else:
                return False


def flatten_list(nested_list):
    """
    Flattens a nested list into a single list.
    :param nested_list: List of lists.
    :return: A flat list with all elements.
    """
    # Implement this
    for lst in nested_list:
        return lst



def remove_duplicates(lst):
    """
    Removes duplicates from the list while maintaining order.
    :param lst: List of elements.
    :return: List without duplicates.
    """
    # Implement this
    return set(lst)

def find_common_elements(lst1, lst2):
    """
    Finds common elements between two lists.
    :param lst1: First list.
    :param lst2: Second list.
    :return: List of common elements.
    """
    # Implement this
    common_lst = []
    for item in lst1:
        if item in lst2:
            print(common_lst.append(item))
        else: 
            return common_lst
find_common_elements([1, 2, 3], [3, 4, 5])
                
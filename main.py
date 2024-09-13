# ------------------------------------------------------------------------

# Lab 1
# Problem 1
1. Create a list called my_list with the values [1, 5, 'apple', 20.5].
my_list = [1, 5, 'apple', 20.5]
2.Using indexing, print the value 'apple' from my_list.
print(my_list[2])
3.Add the value 10 to the end of my_list using the append() method. Print the updated list.
my_list.append(10)
print("Updated list after append:", my_list)
4.Remove the value 20.5 from my_list using the remove() method. Print the updated list.
my_list.remove(20.5)
print("Updated list after remove:", my_list)
5.Reverse the order of the elements in my_list using a method. Print the reversed list.
my_list.reverse()
print("Reversed list:", my_list)

# Problem 2
1.Create a dictionary called person with keys 'name', 'age', 'job' and values 'John', 30, 'teacher'.
person = {"name": 'John', 'age': 30, 'job': "teacher"}
2.Print the value corresponding to the 'job' key.
print("Job:", person['job'])
3.Add a new key-value pair: 'city': 'Paris' to the person dictionary. Print the updated dictionary.
person['city'] = 'Paris'
print("Updated dictionary:", person)
4.Remove the 'age' key-value pair from person. Print the updated dictionary.
person.pop('age')
print("Updated dictionary after removing 'age':", person)
5.Iterate through the person dictionary and print out each key-value pair on a separate line.
for key, value in person.items():
    print(f"{key}: {value}")
# -----------------------------------------------------------------------------


# Importing sys for test function
import sys


# Custom Test Function
def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    msg = f"Test at line {linenum} {'PASSED' if did_pass else 'FAILED'}."
    print(msg)


# Function 1: count_vowels
def count_vowels(s: str) -> int:
    """
    Count the number of vowels in a string.

    Parameters:
    - s (str): The input string

    Returns:
    - int: The number of vowels in the string
    """
    # Define a set of vowels (both lowercase and uppercase)
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    
    # Initialize counter
    count = 0
    
    # Loop through the string
    for char in s:
        # Check if the character is a vowel
        if char in vowels:
            count += 1
            
    return count
    # TODO: Implement this function
    pass


# Unit Tests for count_vowels
def test_count_vowels():
    test(count_vowels("hello") == 2)
    test(count_vowels("why") == 0)
    test(count_vowels("aeiou") == 5)
    test(count_vowels("") == 0)
    test(count_vowels("bcdfg") == 0)
    test(count_vowels("aeiouAEIOU") == 10)
    test(count_vowels("HELLO") == 2)
    test(count_vowels("aEiOu") == 5)
    test(count_vowels("a e i o u") == 5)
    test(count_vowels("rhythm") == 0)


# Function 2: merge_lists
def merge_lists(list1: list, list2: list) -> list:
    """
    Merge two sorted lists into a single sorted list.

    Parameters:
    - list1 (list): The first sorted list
    - list2 (list): The second sorted list

    Returns:
    - list: A new sorted list containing all elements from list1 and list2
    """
    print(f"{list1=}::{list2=}")
    if not list1:
        return list2
    if not list2:
        return list1
    merged_list = []
    i1, i2 = 0, 0
    print(f"{i1=} | {i2=} | {list1[i1]=} | {list2[i2]=} | {merged_list=}")
    while len(merged_list) < len(list1) + len(list2):
        if list1[i1] <  list2[i2]:
           merged_list.append(list1[i1])
           if i1 + 1 == len(list1):
              for item in list2[i2:]:
                  merged_list.append(item)
           else:
             i1 += 1
        else:
            merged_list.append(list2)[i2:])
            if i2 + 1 == len(list2):
                for item in list1[i1:]:
                    merged_list.append(item)
            else:
               i2 += 1
    print(f"{i1=} | {i2=} | {list1[i1]=} | {list2[i2]=} | {merged_list=}")
return merged_list  
    # TODO: Implement this function
    pass


# Unit Tests for merge_lists
def test_merge_lists():
    list1 = [1, 3, 5]
    list2 = [2, 4, 6]
    merged = merge_lists(list1, list2)
    test(merged == [1, 2, 3, 4, 5, 6])
    test(merge_lists([], []) == [])
    test(merge_lists([1], [2]) == [1, 2])
    test(merge_lists([1, 1], [2, 2]) == [1, 1, 2, 2])
    test(merge_lists([1, 3, 5], []) == [1, 3, 5])
    test(merge_lists([], [2, 4, 6]) == [2, 4, 6])
    test(merge_lists([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6])
    test(merge_lists([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    test(merge_lists([1, 1, 2, 3], [1, 2, 2, 3]) == [1, 1, 1, 2, 2, 2, 3, 3])


# Function 3: word_lengths
def word_lengths(words: list) -> list:
    """
    Get the lengths of words in a list.

    Parameters:
    - words (list): The list of words

    Returns:
    - list: A list containing the lengths of the words
    """
    lengths = []  # Initialize an empty list to store lengths
    for word in words:
        lengths.append(len(word))  # Calculate and append the length of each word
    return lengths

    # TODO: Implement this function
    pass


# Unit Tests for word_lengths
def test_word_lengths():
    words = ["hello", "world", "python"]
    lengths = word_lengths(words)
    test(lengths == [5, 5, 6])
    test(word_lengths([]) == [])
    test(word_lengths(["word"]) == [4])
    test(word_lengths(["short", "mediummm", "longesttttt"]) == [5, 8, 10])
    test(word_lengths(["", "a", "ab", "abc"]) == [0, 1, 2, 3])
    test(word_lengths(["  ", "a b", " c "]) == [2, 3, 3])


# Function 4: reverse_string
def reverse_string(s: str) -> str:
    """
    Reverse a string.

    Parameters:
    - s (str): The input string

    Returns:
    - str: The reversed string
    """
     # Initialize an empty string to store the reversed result
    reversed_str = ""
    
    # Loop through the original string in reverse order
    for i in range(len(s) - 1, -1, -1):
        reversed_str += s[i]
    
    return reversed_str
    # TODO: Implement this function
    pass


# Unit Tests for reverse_string
def test_reverse_string():
    text = "python"
    reversed_text = reverse_string(text)
    test(reversed_text == "nohtyp")
    test(reverse_string("") == "")
    test(reverse_string("a") == "a")
    test(reverse_string("aaa") == "aaa")
    test(reverse_string("Hello, World!") == "!dlroW ,olleH")
    test(reverse_string("12345") == "54321")
    test(reverse_string("  spaces  ") == "  secaps  ")


# Function 5: intersection
def intersection(list1: list, list2: list) -> list:
    """
    Find the intersection of two lists.

    Parameters:
    - list1 (list): The first list
    - list2 (list): The second list

    Returns:
    - list: The intersection of the two lists
    """
     # Initialize an empty list to store the intersection
    result = []
    
    # Loop through each element in list1
    for item1 in list1:
        # Check if the element is in list2 and not already in result to avoid duplicates
        if item1 in list2 and item1 not in result:
            result.append(item1)
    
    return result
    # TODO: Implement this function
    pass


# Unit Tests for intersection
def test_intersection():
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    result = intersection(list1, list2)
    test(result == [3, 4])
    test(intersection([], []) == [])
    test(intersection([1, 2], [3, 4]) == [])
    test(intersection([1, 2], [1, 2]) == [1, 2])
    test(intersection([1, 2, 2, 3], [2, 2, 3, 4]) == [2, 3])
    test(intersection([1, 2, 3], [4, 5, 6]) == [])
    test(intersection([1, 2, 3], [1, 2, 3]) == [1, 2, 3])


# Test Suite
def test_suite():
    print(f"Count Vowels Test Results:")
    test_count_vowels()
    print(f"Merge Lists Test Results:")
    test_merge_lists()
    print(f"Word Lengths Test Results:")
    test_word_lengths()
    print(f"Reverse String Test Results:")
    test_reverse_string()
    print(f"Intersection Test Results:")
    test_intersection()


test_suite()

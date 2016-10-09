"""Dictionaries Practice

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""


# def without_duplicates(words):
#     """Given a list of words, return list with duplicates removed.

#     For example::

#         >>> sorted(without_duplicates(
#         ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
#         ['a', 'is', 'rose']

#     You should treat differently-capitalized words as different:

#         >>> sorted(without_duplicates(
#         ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
#         ['Rose', 'a', 'is', 'rose']

#         An empty list should return an empty list::

#         >>> sorted(without_duplicates(
#         ...     []))
#         []

#     The function should work for a list containing integers::

#         >>> sorted(without_duplicates([111111, 2, 33333, 2]))
#         [2, 33333, 111111]
#     """
#     dictionary = {}
#     for index, word in enumerate(words):
#         dictionary[word] = index
#         index += 1
    
#     word_list = []
#     for word, index in dictionary.items():
#         word_list.append(word)

#     return word_list


# def find_unique_common_items(items1, items2):
#     """Produce the set of *unique* common items in two lists.

#     Given two lists, return a list of the *unique* common items
#     shared between the lists.

#     **IMPORTANT**: you may not use `'if ___ in ___``
#     or the method `list.index()`.

#     This should find [1, 2]::

#         >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
#         [1, 2]

#     However, now we only want unique items, so for these lists,
#     don't show more than 1 or 2 once::

#         >>> sorted(find_unique_common_items([3, 2, 1], [1, 1, 2, 2]))
#         [1, 2]

#     The elements should not be treated as duplicates if they are
#     different data types::

#         >>> sorted(find_unique_common_items(["2", "1", 2], [2, 1]))
#         [2]
#     """

#     dictionary1 = {}
#     for index, item in enumerate(items1):
#         dictionary1[item] = index
#         index += 1
#     dictionary2 = {}
#     for index, item in enumerate(items2):
#         dictionary2[item] = index
#         index += 1

#     word_list1 = []
#     for item, index in dictionary1.items():
#         word_list1.append(item)
#     word_list2 = []
#     for item, index in dictionary2.items():
#         word_list2.append(item)

# TRY GET METHOD INSTEAD OF DOUBLE FOR LOOPS TURNING DICTIONARIES INTO LISTS
#     return list(set(word_list1).intersection(word_list2))


def get_sum(numbers):
    """Given list of numbers, return list of pair summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.

    For example::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself)::

        >>> sort_pairs( get_sum_zero_pairs([1, 3, -1, 1, 1, 0]) )
        [[-1, 1], [0, 0]]
    """

    # for number in numbers:


    numbers_dictionary = {}
    index = 0
    for number in range(len(numbers) - 3):
        key = numbers[index]
        value = numbers[index+1]
        numbers_dictionary[key] = value
        index += 2
    
    numbers_list = []
    for number, index in numbers_dictionary.items():
        key = number[0]
        value = number[1]
        if sum(key,value) is 0:
            number_list.append([key, value])
    print numbers_list

# 
# def top_chars(phrase):
#     """Find most common character(s) in string.

#     Given an input string, return a list of character(s) which
#     appear(s) the most the input string.

#     If there is a tie, the order of the characters in the returned
#     list should be alphabetical.

#     For example::

#         >>> top_chars("The rain in spain stays mainly in the plain.")
#         ['i', 'n']

#     If there is not a tie, simply return a list with one item.

#     For example::

#         >>> top_chars("Shake it off, shake it off.")
#         ['f']

#     Do not count spaces, but count all other characters.

#     """

#     return []

# #####################################################################
# # You can ignore everything below this.

# def print_dict(d):
#     # This method is used to print dictionaries in key-alphabetical
#     # order, and is only for our doctests. You can ignore it.
#     if isinstance(d, dict):
#         print "{" + ", ".join(
#             "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
#     else:
#         print d


# def sort_pairs(l):
#     # Print sorted list of pairs where the pairs are sorted. This is
#     # used only for documentation tests. You can ignore it.
#     return sorted(sorted(pair) for pair in l)


# if __name__ == "__main__":
#     print
#     import doctest
#     if doctest.testmod().failed == 0:
#         print "*** ALL TESTS PASSED ***"
#     print

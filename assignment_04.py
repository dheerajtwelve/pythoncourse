__author__ = 'Khali'

notes = '''
1. Read instructions for each function carefully.
2. Feel free to create new functions if needed. Give good names though :)
3. Try to use builtins and datastructures instead of writing your own.
4. If something about the function spec is not clear, use the corresponding test
   for clarification
'''

from placeholders import *
import collections
import operator
# Sort the words that are passed in by word length instead of word content.
# e.g ["apple", "dog", "elephant"] should result in ["elephant", "apple", "dog"]
# hint: use list.sort, don't write your own
def sort_by_length(words):
    return sorted(words,key=len,reverse=True)

# return the top n most frequently occurring chars and their respective counts
# e.g aaaaaabbbbcccc, 2 should return [(a 5) (b 4)]
# in case of a tie, return char which comes earlier in alphabet ordering
# e.g. cdbba,2 -> [(b,2) (a,1)]
# use standard types and builtin functions and no control flow statements.
def top_chars(word, n):
    a= collections.Counter(word)
    b=dict(a)
    c=sorted(list(b.items()),key=operator.itemgetter(1),reverse=True)
    c.sort(key=lambda c: (-c[1], c[0]))
    return c[:n]



def test_sort_by_length():
    assert ["apple", "bear", "dog"] == sort_by_length(["dog", "apple", "bear"])
    assert ["apple", "bear", "dog"] == sort_by_length(["apple", "dog",  "bear"])
    assert ["apple", "dog", "cat"] == sort_by_length(["dog", "apple", "cat"])
    assert ["elephant", "apple"] == sort_by_length(["apple", "elephant"])
    assert ["three", "four", "one", "two"] == sort_by_length(["one", "two", "three", "four"])
    assert [] == sort_by_length([])


def test_top_chars():
    assert [('p', 2)] == top_chars("app",1)
    assert [('p', 2), ('a',1)] == top_chars("app",2)
    assert [('p', 2), ('a',1)] == top_chars("app",3)

    assert [('a', 2)] == top_chars("aabc", 1)
    assert [('a', 2), ('b', 1)] == top_chars("aabc", 2)
    assert [('a', 2), ('b', 1), ('c', 1)] == top_chars("aabc", 3)

    assert [('e', 3)] == top_chars("irreversible", 1)
    assert [('e', 3), ('r', 3)] == top_chars("irreversible", 2)
    assert [('e', 3), ('r', 3), ('i',2), ('b', 1)] == top_chars("irreversible", 4)

three_things_i_learnt = """
-
-
-
"""

time_taken_minutes = ___

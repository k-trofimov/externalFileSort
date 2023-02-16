import string
from collections import Counter
from io import StringIO

from char_sort.sort import counts_to_str_buffer, str_buffer_to_counts

STR_TO_SORT_SIMPLE = "babaac33A-\n"
STR_TO_SORT_EMPTY = ""
STR_TO_SORT_SINGLE_CHAR_REPEATED = "aaa"
STR_TO_TEST_SPECIAL_CHARS = string.punctuation


def test_str_buffer_to_counts():
    assert str_buffer_to_counts(StringIO(STR_TO_SORT_SIMPLE), 3) == Counter(
        STR_TO_SORT_SIMPLE
    ), "Simple string file is not counted correctly"
    assert str_buffer_to_counts(StringIO(STR_TO_SORT_EMPTY), 3) == Counter(
        STR_TO_SORT_EMPTY
    ), "Empty string file is not counted correctly"
    assert str_buffer_to_counts(
        StringIO(STR_TO_SORT_SINGLE_CHAR_REPEATED), 4
    ) == Counter(
        STR_TO_SORT_SINGLE_CHAR_REPEATED
    ), "Repeated char file is not counted correctly"

    # Right not the below test is redundant,
    # but if in the future we would try to reformat function to sort in bytes that might become an issue
    assert str_buffer_to_counts(StringIO(STR_TO_TEST_SPECIAL_CHARS), 3) == Counter(
        STR_TO_TEST_SPECIAL_CHARS
    ), "Special chars file is not counted correctly"


def test_counts_to_str_buffer():
    outfile = StringIO()
    counts_to_str_buffer(outfile, Counter(STR_TO_SORT_SIMPLE), 3)
    assert outfile.getvalue() == "".join(sorted(STR_TO_SORT_SIMPLE))

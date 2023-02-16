
import logging
import typing

from collections import Counter

from char_sort.memory_profiler import profile


def str_buffer_to_counts(file_obj: typing.TextIO, chunk_size: int) -> Counter:
    """
    Reads file in chunks and counts occurrences of chars in each chunk
    :param file_obj:
    :param chunk_size:
    :return:
    """
    char_counts = Counter()
    i = 0
    while True:
        i += 1
        logging.info(f"reading chunk {i}")
        chunk = file_obj.read(chunk_size)

        if not chunk:
            break
        char_counts.update(chunk)
    return char_counts


def counts_to_str_buffer(file_obj: typing.TextIO, char_counts: Counter, chunk_size: int):
    """
    Writes sorted chars to file in chunks
    :param file_obj:
    :param char_counts:
    :param chunk_size:
    """
    for char, count in sorted(char_counts.items()):

        while count > 0:
            batch = char * min(chunk_size, count)
            count -= chunk_size
            file_obj.write(batch)

@profile
def sort_file(input: str, output: str, chunk_size: int):
    """
    Sorts utf-8 file in chunks
    :param input:
    :param output:
    :param chunk_size:
    """
    logging.info(f"Sorting file {input}\n Using chunk_size: {chunk_size}")

    with open(input, 'r', encoding='utf-8') as f:
        char_counts = str_buffer_to_counts(f, chunk_size)

    logging.info(f"writing to file {output}")
    with open(output, 'w', encoding='utf-8') as f:
        counts_to_str_buffer(f, char_counts, chunk_size)


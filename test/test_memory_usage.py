import os
import tempfile

from char_sort.memory_profiler import process_memory
from char_sort.sort import sort_file
from test.utils.mock_data_generator import generate_random_file


def test_memory_usage(file_size_mb: int = 100, chunk_size_mb: int = 10, memory_limit_mb: int = 100):
    with tempfile.TemporaryDirectory() as tmpdirname:
        input_file = os.path.join(tmpdirname, 'input.txt')
        output_file = os.path.join(tmpdirname, 'output.txt')
        generate_random_file(input_file, file_size_mb)
        mem_before = process_memory()
        sort_file(input_file, output_file, chunk_size_mb * 1048576)
        mem_after = process_memory()
    assert mem_after - mem_before < memory_limit_mb, f"Memory usage is {mem_after}mb, which is more than {memory_limit_mb}mb"

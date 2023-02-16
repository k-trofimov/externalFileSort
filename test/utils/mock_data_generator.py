import sys
import random
import string



CHUNK_SIZE =  1048576



def generate_random_file(file_name:str, file_size_mb:int):
    """
    Generate a file with random characters
    :param file_name:
    :param file_size_mb:
    """
    utf_chars=tuple([*string.printable])
    # Open a file in binary mode and write random characters in chunks
    with open(file_name, 'wb') as file:
        for i in range(file_size_mb):
            # Generate a chunk of random characters
            random_chunk = ''.join(random.choices(utf_chars, k=CHUNK_SIZE)).encode('utf-8')
            # Write the chunk to the file
            file.write(random_chunk)

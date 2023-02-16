# External File Sort

A simple program to sort characters in a UTF-8 file. Reads the file in chunks, sorts the chunks, counts character frequencies,
and then writes to a new file after sorting keys of the character frequency map.

### Requirements
 - psutil

### Usage
    - `python3 external_file_sort.py <file>` -- Sorts the file and outputs to the file with extension .sorted

### Optional arguments:
- `-h, --help`          -- Show this help message and exit
- `--output`            -- Output file path
- `--replace`           -- Replace the original file after sorting
- `--chunk`             -- Chunk size in MB

### Future Improvements
Implement multiprocessing to speed up the sorting process. 
Currently, the bottleneck of the algorithm is the calculation of character frequency maps. 
This step could be greatly sped up by dividing batches into mini batches, counting chars in multiple processes,
and then merging the counts (i.e. mapreduce). Unfortunately, it is not possible at the moment as multiprocessing will introduce 
enough memory overhead to surpass our 100mb memory limit.

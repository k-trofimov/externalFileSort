import argparse
import os
import logging


from char_sort.sort import sort_file








if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A sc of your program')
    parser.add_argument('source', type=str, help='Path to file to be sorted')
    parser.add_argument('--output', type=str, default=None, help='Path to output file')
    parser.add_argument('--replace', type=bool, default=False, help='Replace origial file')
    parser.add_argument('--chunk', type=int, default=10, help='Chunk size in mb')
    args = parser.parse_args()

    source_path = args.source
    if not args.output:
        if args.replace:
            output_path = source_path
        else:
            output_path = source_path + '.sorted'
    else:
        output_path = args.output
    os.chdir('/Users/konstantintrofimov/PycharmProjects/externalFileSort')
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
    sort_file(source_path, output_path, args.chunk * 1048576)






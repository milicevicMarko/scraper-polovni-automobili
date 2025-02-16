import argparse
from pathlib import Path
import pandas as pd
from .read_existing import import_file
from .read_batch import read_batch_file


def read_args():
    parser = argparse.ArgumentParser(
        description='Process and export data files.')
    parser.add_argument('--file', type=str, default=None, required=True,
                        help='File to be updated or new file to be created to store the results.')
    parser.add_argument('--batch', type=str, default=None,
                        help='Run in Batch mode reading from a file.')
    parser.add_argument('--url', type=str, default=None,
                        help='URL to be processed')

    args = parser.parse_args()

    has_url = args.url is not None
    has_batch = args.batch is not None

    if not has_url and not has_batch:
        parser.error('No URL or batch file provided.')
    if has_url and has_batch:
        parser.error(
            'Both URL and batch file provided. Please provide only one.')

    return args


def prepare_file(args_file):
    input_path = Path(args_file)
    input_file = import_file(
        input_path) if input_path.exists() else pd.DataFrame()
    file_name = input_path.stem
    file_type = input_path.suffix[1:]
    file_type = 'excel' if file_type in ['xls', 'xlsx'] else file_type
    return input_file, file_name, file_type


def prepare_url(file_args):
    if file_args.batch:
        return read_batch_file(Path(file_args.batch))
    else:
        return [file_args.url]


def command_line():
    args = read_args()
    previous_data, file_name, type = prepare_file(args.file)

    urls = prepare_url(args)

    return previous_data, file_name, type, urls


def main():
    args = read_args()

    df, output_name, type = prepare_file(args)

    urls = args.urls

    print('Processing URL: ', urls)
    print('Output file: ', output_name)
    print('Output type: ', type)
    print('Input file: ', df)


if __name__ == '__main__':
    main()

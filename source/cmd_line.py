import argparse
from pathlib import Path
import pandas as pd
from .read_existing import import_file
from datetime import datetime


def read_args():
    parser = argparse.ArgumentParser(
        description='Process and export data files.')
    parser.add_argument('--a', type=str, default=None,
                        help='Path to the input file (csv, json, or excel) to Update')
    parser.add_argument(
        '--o', type=str, default=f'results/result-{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}', help='Name for the output file')
    parser.add_argument(
        '--t', type=str, choices=['csv', 'json', 'excel'], help='Type of the output file')
    parser.add_argument('--url', type=str, required=True,
                        help='URL to be processed')

    args = parser.parse_args()
    print(args)
    if args.a is None and (args.o is None or args.t is None):
        parser.error(
            "You must provide either extend a file (--a), or create a new one (--o) (--t).")
    if args.url is None:
        parser.error("You must provide a URL to be processed.")

    return args


def append_mode(file_args):
    print('Using exiting file: ', file_args.a)
    input_path = Path(file_args.a)
    df = import_file(input_path)
    output_name = input_path.stem
    type = input_path.suffix[1:]
    type = 'excel' if type in ['xls', 'xlsx'] else type
    return df, output_name, type


def create_mode(file_args):
    print('Creating new file: ', file_args.o)
    df = pd.DataFrame()
    output_name = Path(file_args.o)
    type = file_args.t
    return df, output_name, type


def prepare(file_args):
    if file_args.a:
        return append_mode(file_args)
    else:
        return create_mode(file_args)


def command_line():
    args = read_args()
    df, output_name, type = prepare(args)

    url = args.url

    return df, output_name, type, url


def main():
    args = read_args()

    df, output_name, type = prepare(args)

    url = args.url

    print('Processing URL: ', url)
    print('Output file: ', output_name)
    print('Output type: ', type)
    print('Input file: ', df)


if __name__ == '__main__':
    main()

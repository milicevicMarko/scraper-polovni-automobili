from pathlib import Path
import pandas as pd


def import_file(file_path: Path):
    if not file_path.exists():
        raise FileNotFoundError(f"File {file_path} does not exist")
    print(f"Importing file {file_path}...")
    if file_path.suffix == '.csv':
        return pd.read_csv(file_path)
    elif file_path.suffix == '.json':
        return pd.read_json(file_path)
    elif file_path.suffix == '.xlsx':
        return pd.read_excel(file_path)
    else:
        raise Exception(f"Unknown file type: {file_path.suffix}")


if __name__ == '__main__':
    file_path = Path('results/test.csv')
    result = import_file(file_path)
    print("csv: ")
    print(result)
    print()
    file_path = Path('results/test.json')
    result = import_file(file_path)
    print("json: ")
    print(result)
    print()
    file_path = Path('results/test.xlsx')
    result = import_file(file_path)
    print("excel: ")
    print(result)
    print()

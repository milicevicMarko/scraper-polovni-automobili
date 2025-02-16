from pathlib import Path
import pandas as pd


def export_file(result: pd.DataFrame, name: str, type: str):
    path_base = Path('results')
    path_base.mkdir(parents=True, exist_ok=True)

    if type == 'excel':
        full_path = path_base / f'{name}.xlsx'
        print(f'Exporting to {full_path}...')
        result.to_excel(full_path, index=False)
    elif type == 'csv':
        full_path = path_base / f'{name}.csv'
        print(f'Exporting to {full_path}...')
        result.to_csv(full_path, index=False)
    elif type == 'json':
        full_path = path_base / f'{name}.json'
        print(f'Exporting to {full_path}...')
        result.to_json(full_path, orient='records', force_ascii=False)
    else:
        raise Exception('Unknown export type')


if __name__ == '__main__':
    result = pd.DataFrame([{'a': 1, 'b': 2}])
    export_file(result, 'test', 'json')
    export_file(result, 'test', 'csv')
    export_file(result, 'test', 'excel')

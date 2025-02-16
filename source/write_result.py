from pathlib import Path
import pandas as pd


def export(result: pd.DataFrame, name: str, type: str):
    path_base = Path('results')
    path_base.mkdir(parents=True, exist_ok=True)

    if type == 'excel':
        full_path = path_base / f'{name}.xlsx'
        result.to_excel(full_path, index=False)
    elif type == 'csv':
        full_path = path_base / f'{name}.csv'
        result.to_csv(full_path, index=False)
    elif type == 'json':
        full_path = path_base / f'{name}.json'
        result.to_json(full_path, orient='records')
    else:
        raise Exception('Unknown export type')


if __name__ == '__main__':
    result = pd.DataFrame([{'a': 1, 'b': 2}])
    export(result, 'test', 'json')
    export(result, 'test', 'csv')
    export(result, 'test', 'excel')

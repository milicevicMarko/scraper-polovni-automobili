import pandas as pd


def append_data(input, result):
    input, result = prepare_dataframes(input, result)
    if input.empty:
        return result
    else:
        return pd.concat([input, result], ignore_index=True)


def prepare_dataframes(input, result):
    input = clean_column_names(input)
    result = clean_column_names(result)

    input, result = delete_row_if_already_exists(input, result)
    input, result = expand_columns(input, result)
    input, result = ensure_boolen(input), ensure_boolen(result)
    return input, result


def clean_column_names(df):
    if not df.empty:
        df.columns = df.columns.str.lower().str.replace(' ', '_')
        df.columns = df.columns.str.replace(':', '')
    return df


def delete_row_if_already_exists(input, result):
    if 'broj_oglasa' in input.columns:
        input['broj_oglasa'] = input['broj_oglasa'].astype(str)
    if 'broj_oglasa' in result.columns:
        result['broj_oglasa'] = result['broj_oglasa'].astype(str)
    if 'broj_oglasa' in input.columns and 'broj_oglasa' in result.columns:
        input = input[~input['broj_oglasa'].isin(result['broj_oglasa'])]
    return input, result


def expand_columns(input, result):
    input_columns = set(input.columns)
    result_columns = set(result.columns)
    for column in input_columns - result_columns:
        result[column] = False
    for column in result_columns - input_columns:
        input[column] = False

    return input, result


def ensure_boolen(df):
    for column in df.columns:
        if df[column].dtype == 'bool':
            df[column] = df[column].astype(bool)
    return df

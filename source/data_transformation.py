import pandas as pd


def prepare_dataframes(input, result):
    input_columns = set(input.columns)
    result_columns = set(result.columns)
    for column in input_columns - result_columns:
        result[column] = False
    for column in result_columns - input_columns:
        input[column] = False
    return input, result


def append_data(input, result):
    if input.empty:
        return result
    else:
        input, result = prepare_dataframes(input, result)
        # return input.append(result, ignore_index=True)
        return pd.concat([input, result], ignore_index=True)

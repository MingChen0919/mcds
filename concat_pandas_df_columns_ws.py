def concat_pandas_df_columns_ws(df: pd.DataFrame, sep: str = ''):
    """
    Concatenate all columns in `df` into one single column with an optional separator `sep`.

    :param df: a pd.DataFrame object.
    :param sep: a separator str between elements of each column.
    :return:
    """

    def as_char(l: list):
        return [str(x) for x in l]

    df = pd.DataFrame({'concat_col': [sep.join(as_char(row)) for row in df.values]})

    return df

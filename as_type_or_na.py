# ------------------------------------------------------------------------------
# This function casts values of a pd.Series into one of ['Int64', 'float', 'str']
# types using int(), float(), and str(), respectively. If any values can't be 
# coerced to the specified dtype, it will be replaced with NAs.
# ------------------------------------------------------------------------------

def as_type_or_na(s: pd.Series, dtype: str):
    """
    Cast each value in s to `dtype`. If error is raised, replace the value with NA.

    :param s: a pd.Series
    :param dtype: one of the three dtypes: ['Int64', 'float', 'str']
    :return:
    >>> s = pd.Series(['1', '2', 'a'])
    >>> as_type_or_na(s, 'Int64')
    """

    if dtype not in ['Int64', 'float', 'str']:
        raise ValueError("`dtype` has to be one of ['Int64', 'float', 'str'].")

    def cast(scalar, as_type):
        try:
            return as_type(scalar)
        except:
            return None

    as_type = str
    if dtype == 'Int64':
        as_type = int
    if dtype == 'float':
        as_type = float

    new_s = pd.array([cast(v, as_type) for v in s], dtype=dtype)
    new_s = pd.Series(new_s)

    return new_s
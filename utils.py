import pandas as pd
import numpy as np


def naify_extreme_values(x, n_iqr=3):
	"""
	Replace extreme values in a pd.Series with NAs.

	:param pd.Series x: a pandas Series which potentially has extreme values
	:param int n_iqr: the number of IQR used to define extreme values. Default is 3.
	:return:
	"""
	Q1 = np.nanquantile(x, 0.25)
	Q3 = np.nanquantile(x, 0.75)
	IQR = Q3 - Q1
	lower_b = Q1 - n_iqr * IQR
	upper_b = Q3 + n_iqr * IQR
	if Q3 > Q1:
		x[(x < lower_b) | (x > upper_b)] = np.nan
	return x


def get_missing_rate(df, features=None):
	"""
	Calculate missing rate on selected features from a data frame. If features=None, it returns missing rates for
	all features.
	:param df:
	:param features:
	:return:
	"""

	df = df.copy(deep=True)
	df = df.loc[:, features].apply(lambda x: x.isna().sum() / len(x)).sort_values(
		ascending=False).reset_index()
	df.columns = ['feature', 'missing_rate']
	return df

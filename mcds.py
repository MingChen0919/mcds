import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime


def create_output_dir(prefix='', suffix=''):
	"""
	Create a directory named prefix + current time + suffix for storing current analysis results.
	Exp directory name: prefix_201905211430_suffix.
	:param str prefix: str,
	:param str suffix:
	:return str:
	"""

	dir_path = Path(prefix + datetime.now().strftime('%Y%m%d%H%M') + suffix)
	dir_path.mkdir(parents=True, exist_ok=True)
	print(str(dir_path))
	return str(dir_path)


class FeatureBag:
	"""
	Create an instance that stores features by type.
	"""

	def __init__(self, numeric_f=(), ordinal_f=(), binary_class_f=(), multi_class_f=(), datetime_f=(), id_f=(),
				 unused_f=()):
		"""

		:param list numeric_f: a list of numeric features
		:param list ordinal_f: a list of ordinal features
		:param list binary_class_f: a list of binary features
		:param list multi_class_f: a list of multi-class features
		:param list datetime_f: a list of datetime features
		:param list id_f: a list of features that are used for grouping, data frame merging, etc.
		:param list unused_f: a list of features that
		"""
		self.numeric_f = list(set(numeric_f))
		self.ordinal_f = list(set(ordinal_f))
		self.binary_class_f = list(set(binary_class_f))
		self.multi_class_f = list(set(multi_class_f))
		self.datetime_f = list(set(datetime_f))
		self.id_f = list(set(id_f))
		self.unused_f = list(set(unused_f))

	def add_to_numeric_f(self, add_features=()):
		"""

		:param list add_features: a list of features to be added to the numeric_f bag.
		:return:
		"""

		self.numeric_f = list(set(self.numeric_f + add_features))

	def remove_from_numeric_f(self, remove_features=()):
		"""

		:param list remove_features: a list of features to be removed from the numeric_f bag.
		:return:
		"""

		self.numeric_f = list(set(self.numeric_f) - set(remove_features))

	def add_to_ordinal_f(self, add_features=()):
		"""

		:param list add_features: a list of features to be added to the ordinal_f bag.
		:return:
		"""

		self.ordinal_f = list(set(self.ordinal_f + add_features))

	def remove_from_ordinal_f(self, remove_features=()):
		"""

		:param list remove_features: a list of features to be removed from the ordinal_f bag.
		:return:
		"""

		self.ordinal_f = list(set(self.ordinal_f) - set(remove_features))

	def add_to_binary_class_f(self, add_features=()):
		"""

		:param list add_features: a list of features to be added to the binary_class_f bag.
		:return:
		"""

		self.binary_class_f = list(set(self.binary_class_f + add_features))

	def remove_from_binary_class_f(self, remove_features=()):
		"""

		:param list remove_features: a list of features to be removed from the binary_class_f bag.
		:return:
		"""

		self.binary_class_f = list(set(self.binary_class_f) - set(remove_features))

	def add_to_multi_class_f(self, add_features=()):
		"""

		:param list add_features: a list of features to be added to the multi_class_f bag.
		:return:
		"""

		self.multi_class_f = list(set(self.multi_class_f + add_features))

	def remove_from_multi_class_f(self, remove_features=()):
		"""

		:param list remove_features: a list of features to be removed from the multi_class_f bag.
		:return:
		"""

		self.multi_class_f = list(set(self.multi_class_f) - set(remove_features))

	def add_to_datetime_f(self, add_features=()):
		"""

		:param list add_features: a list of features to be added to the datetime_f bag.
		:return:
		"""

		self.datetime_f = list(set(self.datetime_f + add_features))

	def remove_from_datetime_f(self, remove_features=()):
		"""

		:param list remove_features: a list of features to be removed from the datetime_f bag.
		:return:
		"""

		self.datetime_f = list(set(self.datetime_f) - set(remove_features))

	def add_to_id_f(self, add_features=()):
		"""

		:param list add_features: a list of features to be added to the id_f bag.
		:return:
		"""

		self.id_f = list(set(self.id_f + add_features))

	def remove_from_id_f(self, remove_features=()):
		"""

		:param list remove_features: a list of features to be removed from the id_f bag.
		:return:
		"""

		self.id_f = list(set(self.id_f) - set(remove_features))


def fill_numeric_features_na_by_group_mean(df, numeric_f, group_by=()):
	"""
	Fill NAs in numeric columns from df with group average.

	:param DataFrame df: the data frame in which numeric features are manipulated to fill in NAs.
	:param list numeric_f: a list of numeric features exist in df.
	:param list group_by: a list of features used to group the data frame.
	:return: the same df but with NAs in the numeric features being processed.
	"""
	df = df.copy(deep=True)

	if len(group_by) > 0:
		none_df_features = [i for i in group_by if i not in df.columns]
		if len(none_df_features) > 0:
			raise Exception('These features are not in the data: {}'.format(none_df_features))
		df.loc[:, numeric_f] = df.loc[:, group_by + numeric_f].grouby(group_by).transform(lambda x: x.fillna(x.mean()))
	else:
		df.loc[:, numeric_f] = df.loc[:, numeric_f].transform(lambda x: x.fillna(x.mean()))
	return df


def fill_categorical_features_na_by_group_mode(df, categorical_f, group_by=()):
	"""
	Fill NAs in categorical features from df with group mode.

	:param DataFrame df: the data frame in which categorical features are manipulated to fill in NAs.
	:param list categorical_f: a list of categorical features exist in df.
	:param list group_by: a list of features used to group the data frame.
	:return: the same df but with NAs in the categorical features being processed.
	"""
	df = df.copy(deep=True)

	def fill_na_with_mode(series):
		"""
		Fill NAs in a pandas Series with most frequent element value.

		:param pandas.Series series: a pandas series
		:return: a pandas series with NAs being replaced with the most frequent element values.
		"""
		mode = series.value_counts().index[0]
		return series.fillna(mode)

	if (len(group_by)) > 0:
		none_df_features = [i for i in group_by if i not in df.columns]
		if len(none_df_features) > 0:
			raise Exception('These features are not in the data: {}'.format(none_df_features))
		df.loc[:, categorical_f] = df.loc[:, group_by + categorical_f].groupby(group_by).transform(fill_na_with_mode)
	else:
		df.loc[:, categorical_f] = df.loc[:, categorical_f].transform(fill_na_with_mode)
	return df


class DatasetsVersionController:
	"""
	During the data analysis process, I find that sometimes I need to apply different data manipulation processes to the
	same dataset. I end up with several different versions of preprocessed datasets and many times it is hard to determine
	which version should be used in the modeling process. This class aims to create an instance to handle different
	dataset versions in the analysis. Each dataset should have a log to record what kind of processing has been done to it.
	"""

	def __init__(self, datasets=None):
		self.datasets = datasets

	def add_dataset(self, dataset, dataset_name):
		"""
		Add a new dataset to the datasets dictionary.

		:param DataFrame dataset:
		:param str dataset_name:
		:return:
		"""
		if self.datasets == None:
			self.datasets = {}

		if dataset_name in list(self.datasets.keys()):
			raise Exception(
				'{} already exists. Please choose a different name or update the corresponding dataset.'.format(
					dataset_name))
		else:
			self.datasets[dataset_name] = {
				'data': dataset,
				'log': pd.DataFrame(columns=['time', 'message'])
			}

	def log(self, dataset_name, log_message):
		"""
		Add dataset processing log to a dataset.

		:param dataset_name:
		:param log_message:
		:return:
		"""
		if dataset_name not in list(self.datasets.keys()):
			raise Exception(
				'{} does not exit. Available datasets are: {}.'.format(dataset_name, list(self.datasets.keys())))

		self.datasets[dataset_name]['log'] = self.datasets[dataset_name]['log'].append({
			'time': datetime.now(),
			'message': log_message
		}, ignore_index=True)

	def get_dataset(self, dataset_name):
		"""
		Get dataset by name.

		:param dataset_name:
		:return:
		"""
		if dataset_name not in list(self.datasets.keys()):
			raise Exception(
				'"{}" does not exit. Available datasets are: {}.'.format(dataset_name, list(self.datasets.keys())))

		return self.datasets[dataset_name]['data']

	def get_dataset_log(self, dataset_name):
		"""
		Get dataset log messages by name.

		:param dataset_name:
		:return:
		"""
		if dataset_name not in list(self.datasets.keys()):
			raise Exception(
				'"{}" does not exit. Available datasets are: {}.'.format(dataset_name, list(self.datasets.keys())))

		return self.datasets[dataset_name]['log']

	def list_all_datasets(self):
		"""
		List all registered datasets.

		:return:
		"""
		return list(self.datasets.keys())

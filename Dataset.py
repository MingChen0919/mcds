import pandas as pd
import numpy as np
from datetime import datetime


class Dataset:
	def __init__(self, dataset):
		self.dataset = dataset
		self.numeric_f = []
		self.ordinal_f = []
		self.binary_class_f = []
		self.multi_class_f = []
		self.datetime_f = []
		self.id_f = []
		self.unused_f = self.dataset.columns.to_list()
		self.all_f = self.dataset.columns.to_list()
		self.log = pd.DataFrame(columns=["time", "note"])
		self.remove_functions = [self.remove_from_unused_f,
								 self.remove_from_numeric_f,
								 self.remove_from_ordinal_f,
								 self.remove_from_binary_class_f,
								 self.remove_from_multi_class_f,
								 self.remove_from_datetime_f,
								 self.remove_from_id_f,
								 self.remove_from_datetime_f]

	def add_to_numeric_f(self, add_features=()):
		"""

		:param list add_features: a list of features to be added to the numeric_f bag.
		:return:
		"""
		# remove add_features from all feature bags first
		[rm_f(add_features) for rm_f in self.remove_functions]

		# add add_features to current feature bag
		self.numeric_f = sorted(list(set(self.numeric_f + add_features)))

	def add_to_ordinal_f(self, add_features=()):
		"""

		:param list add_features: a list of features to be added to the ordinal_f bag.
		:return:
		"""
		# remove add_features from all feature bags first
		[rm_f(add_features) for rm_f in self.remove_functions]

		# add add_features to current feature bag
		self.ordinal_f = sorted(list(set(self.ordinal_f + add_features)))

	def add_to_binary_class_f(self, add_features=()):
		"""

		:param list add_features: a list of features to be added to the binary_class_f bag.
		:return:
		"""

		# remove add_features from all feature bags first
		[rm_f(add_features) for rm_f in self.remove_functions]

		# add add_features to current feature bag
		self.binary_class_f = sorted(list(set(self.binary_class_f + add_features)))

	def add_to_multi_class_f(self, add_features=()):
		"""

		:param list add_features: a list of features to be added to the multi_class_f bag.
		:return:
		"""

		# remove add_features from all feature bags first
		[rm_f(add_features) for rm_f in self.remove_functions]

		# add add_features to current feature bag
		self.multi_class_f = sorted(list(set(self.multi_class_f + add_features)))

	def add_to_datetime_f(self, add_features=()):
		"""

		:param list add_features: a list of features to be added to the datetime_f bag.
		:return:
		"""

		# remove add_features from all feature bags first
		[rm_f(add_features) for rm_f in self.remove_functions]

		# add add_features to current feature bag
		self.datetime_f = list(set(self.datetime_f + add_features))

	def add_to_id_f(self, add_features=()):
		"""

		:param list add_features: a list of features to be added to the id_f bag.
		:return:
		"""
		# remove add_features from all feature bags first
		[rm_f(add_features) for rm_f in self.remove_functions]

		# add add_features to current feature bag
		self.id_f = sorted(list(set(self.id_f + add_features)))

	def add_to_unused_f(self, add_features=()):
		"""

		:param list add_features: a list of features to be added to the unused_f bag.
		:return:
		"""
		# remove add_features from all feature bags first
		[rm_f(add_features) for rm_f in self.remove_functions]

		# add add_features to current feature bag
		self.unused_f = sorted(list(set(self.unused_f + add_features)))

	def remove_from_numeric_f(self, remove_features=()):
		"""

		:param list remove_features: a list of features to be removed from the numeric_f bag.
		:return:
		"""

		self.numeric_f = list(set(self.numeric_f) - set(remove_features))

	def remove_from_ordinal_f(self, remove_features=()):
		"""

		:param list remove_features: a list of features to be removed from the ordinal_f bag.
		:return:
		"""

		self.ordinal_f = list(set(self.ordinal_f) - set(remove_features))

	def remove_from_binary_class_f(self, remove_features=()):
		"""

		:param list remove_features: a list of features to be removed from the binary_class_f bag.
		:return:
		"""

		self.binary_class_f = sorted(list(set(self.binary_class_f) - set(remove_features)))

	def remove_from_multi_class_f(self, remove_features=()):
		"""

		:param list remove_features: a list of features to be removed from the multi_class_f bag.
		:return:
		"""

		self.multi_class_f = sorted(list(set(self.multi_class_f) - set(remove_features)))

	def remove_from_datetime_f(self, remove_features=()):
		"""

		:param list remove_features: a list of features to be removed from the datetime_f bag.
		:return:
		"""

		self.datetime_f = sorted(list(set(self.datetime_f) - set(remove_features)))

	def remove_from_id_f(self, remove_features=()):
		"""

		:param list remove_features: a list of features to be removed from the id_f bag.
		:return:
		"""

		self.id_f = sorted(list(set(self.id_f) - set(remove_features)))

	def remove_from_unused_f(self, remove_features=()):
		"""

		:param list remove_features: a list of features to be removed from the unused_f bag.
		:return:
		"""

		self.unused_f = sorted(list(set(self.unused_f) - set(remove_features)))

	def as_type(self):
		"""
		Cast features into correct types.
		"""
		types = {
			'float': self.numeric_f,
			'bool': self.binary_class_f,
			'str': self.multi_class_f + self.id_f,
			'datetime64[ns]': self.datetime_f
		}

		for i in types.keys():
			if len(types[i]) > 0:
				if i == 'bool':
					self.dataset.loc[:, types[i]] = self.dataset.loc[:, types[i]].astype(i).astype('float')
				else:
					self.dataset.loc[:, types[i]] = self.dataset.loc[:, types[i]].astype(i)

	def fill_numeric_features_na_with_mean(self, group_by_ids=True):
		"""
		Fill NAs in numeric columns from df with group average.
		"""
		if group_by_ids:
			if len(self.id_f) > 0:
				self.dataset.loc[:, self.numeric_f] = self.dataset.loc[:, self.id_f + self.numeric_f].groupby(
					self.id_f).transform(lambda x: x.fillna(x.mean()))
		else:
			self.dataset.loc[:, self.numeric_f] = self.dataset.loc[:, self.numeric_f].transform(
				lambda x: x.fillna(x.mean()))

	def fill_categorical_features_na_with_mode(self, group_by_ids=True):
		"""
		Fill NAs in categorical features from df with group mode.
		"""

		def fill_na_with_mode(series):
			"""
			Fill NAs in a pandas Series with most frequent element value.

			:param pandas.Series series: a pandas series
			:return: a pandas series with NAs being replaced with the most frequent element values.
			"""
			mode = series.value_counts().index[0]
			return series.fillna(mode)

		all_class_f = self.binary_class_f + self.multi_class_f
		if group_by_ids:
			if len(self.id_f) > 0:
				self.dataset.loc[:, all_class_f] = self.dataset.loc[:, self.id_f + all_class_f].groupby(
					self.id_f).transform(lambda x: x.fillna(x.mean()))
		else:
			self.dataset.loc[:, self.all_class_f] = self.dataset.loc[:, self.all_class_f].transform(
				lambda x: x.fillna(x.mean()))

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

	def __init__(self, numeric_f=[], ordinal_f=[], binary_class_f=[], multi_class_f=[], datetime_f=[]):
		self.numeric_f = list(set(numeric_f))
		self.ordinal_f = list(set(ordinal_f))
		self.binary_class_f = list(set(binary_class_f))
		self.multi_class_f = list(set(multi_class_f))
		self.datetime_f = list(set(datetime_f))

	def add_to_numeric_f(self, add_features=[]):
		"""

		:param list add_features: a list of features to be added to the numeric_f bag.
		:return:
		"""

		self.numeric_f = list(set(self.numeric_f + add_features))

	def remove_from_numeric_f(self, remove_features=[]):
		"""

		:param list remove_features: a list of features to be removed from the numeric_f bag.
		:return:
		"""

		self.numeric_f = list(set(self.numeric_f) - set(remove_features))

	def add_to_ordinal_f(self, add_features=[]):
		"""

		:param list add_features: a list of features to be added to the ordinal_f bag.
		:return:
		"""

		self.ordinal_f = list(set(self.ordinal_f + add_features))

	def remove_from_ordinal_f(self, remove_features=[]):
		"""

		:param list remove_features: a list of features to be removed from the ordinal_f bag.
		:return:
		"""

		self.ordinal_f = list(set(self.ordinal_f) - set(remove_features))

	def add_to_binary_class_f(self, add_features=[]):
		"""

		:param list add_features: a list of features to be added to the binary_class_f bag.
		:return:
		"""

		self.binary_class_f = list(set(self.binary_class_f + add_features))

	def remove_from_binary_class_f(self, remove_features=[]):
		"""

		:param list remove_features: a list of features to be removed from the binary_class_f bag.
		:return:
		"""

		self.binary_class_f = list(set(self.binary_class_f) - set(remove_features))

	def add_to_multi_class_f(self, add_features=[]):
		"""

		:param list add_features: a list of features to be added to the multi_class_f bag.
		:return:
		"""

		self.multi_class_f = list(set(self.multi_class_f + add_features))

	def remove_from_multi_class_f(self, remove_features=[]):
		"""

		:param list remove_features: a list of features to be removed from the multi_class_f bag.
		:return:
		"""

		self.multi_class_f = list(set(self.multi_class_f) - set(remove_features))

	def add_to_datetime_f(self, add_features=[]):
		"""

		:param list add_features: a list of features to be added to the datetime_f bag.
		:return:
		"""

		self.datetime_f = list(set(self.datetime_f + add_features))

	def remove_from_datetime_f(self, remove_features=[]):
		"""

		:param list remove_features: a list of features to be removed from the datetime_f bag.
		:return:
		"""

		self.datetime_f = list(set(self.datetime_f) - set(remove_features))

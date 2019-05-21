from pathlib import Path
from datetime import datetime


def create_output_dir(prefix='', suffix=''):
	"""
	Create a directory named prefix + current time + suffix for storing current analysis results.
	Exp directory name: prefix_201905211430_suffix.
	:param prefix: str,
	:param suffix:
	:return:
	"""

	dir_path = Path(prefix + datetime.now().strftime('%Y%m%d%H%M') + suffix)
	dir_path.mkdir(parents=True, exist_ok=True)
	print(str(dir_path))
	return str(dir_path)

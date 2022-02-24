# ==================================================================================================================== #
#             _____           _ _               ____ _     ___    _    _         _                  _   _              #
#  _ __  _   |_   _|__   ___ | (_)_ __   __ _  / ___| |   |_ _|  / \  | |__  ___| |_ _ __ __ _  ___| |_(_) ___  _ __   #
# | '_ \| | | || |/ _ \ / _ \| | | '_ \ / _` || |   | |    | |  / _ \ | '_ \/ __| __| '__/ _` |/ __| __| |/ _ \| '_ \  #
# | |_) | |_| || | (_) | (_) | | | | | | (_| || |___| |___ | | / ___ \| |_) \__ \ |_| | | (_| | (__| |_| | (_) | | | | #
# | .__/ \__, ||_|\___/ \___/|_|_|_| |_|\__, (_)____|_____|___/_/   \_\_.__/|___/\__|_|  \__,_|\___|\__|_|\___/|_| |_| #
# |_|    |___/                          |___/                                                                          #
# ==================================================================================================================== #
# Authors:                                                                                                             #
#   Patrick Lehmann                                                                                                    #
#                                                                                                                      #
# License:                                                                                                             #
# ==================================================================================================================== #
# Copyright 2017-2022 Patrick Lehmann - Bötzingen, Germany                                                             #
# Copyright 2007-2016 Technische Universität Dresden - Germany, Chair of VLSI-Design, Diagnostics and Architecture     #
#                                                                                                                      #
# Licensed under the Apache License, Version 2.0 (the "License");                                                      #
# you may not use this file except in compliance with the License.                                                     #
# You may obtain a copy of the License at                                                                              #
#                                                                                                                      #
#   http://www.apache.org/licenses/LICENSE-2.0                                                                         #
#                                                                                                                      #
# Unless required by applicable law or agreed to in writing, software                                                  #
# distributed under the License is distributed on an "AS IS" BASIS,                                                    #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.                                             #
# See the License for the specific language governing permissions and                                                  #
# limitations under the License.                                                                                       #
#                                                                                                                      #
# SPDX-License-Identifier: Apache-2.0                                                                                  #
# ==================================================================================================================== #
#
"""This module contains all possible command line option and parameter forms."""
from pathlib import Path
from typing import ClassVar, List, Union, Iterable

from pyTooling.Decorators import export


@export
class CommandLineArgument:
	"""Base-class (and meta-class) for all *Arguments* classes."""

	_pattern: ClassVar[str]

	def __init_subclass__(cls, *args, pattern: str = None, **kwargs):
		super().__init_subclass__(*args, **kwargs)
		cls._pattern = pattern

	def AsArgument(self) -> Union[str, Iterable[str]]:
		raise NotImplementedError(f"")  # XXX: add message here

	def __repr__(self) -> str:
		raise NotImplementedError(f"")  # XXX: add message here

	def __str__(self) -> str:
		raise NotImplementedError(f"")  # XXX: add message here


@export
class ExecutableArgument(CommandLineArgument):
	"""Represents the executable."""

	_executable: ClassVar[Path]

	def __init_subclass__(cls, *args, executablePath: Path = None, **kwargs):
		super().__init_subclass__(*args, **kwargs)
		cls._executable = executablePath

	def __init__(self, executable: Path):
		self._executable = executable

	@property
	def Value(self) -> Path:
		return self._executable

	@Value.setter
	def Value(self, value: Path):
		if isinstance(value, Path):
			self._executable = value
		else:
			raise TypeError("Parameter 'value' is not of type 'Path'.")

	@property
	def Executable(self) -> Path:
		return self._executable

	@Executable.setter
	def Executable(self, value):
		if isinstance(value, Path):
			self._executable = value
		else:
			raise TypeError("Parameter 'value' is not of type 'Path'.")

	def AsArgument(self) -> Union[str, Iterable[str]]:
		return f"{self._executable}"

	def __repr__(self) -> str:
		return f"\"{self._executable}\""

	__str__ = __repr__


@export
class DelimiterArgument(CommandLineArgument):
	"""Represents a delimiter symbol like ``--``."""

	def AsArgument(self) -> Union[str, Iterable[str]]:
		return f"{self._pattern}"

	def __repr__(self) -> str:
		return f"\"{self._pattern}\""

	__str__ = __repr__


@export
class NamedArgument(CommandLineArgument, pattern="{0}"):
	"""Base-class for all command line arguments with a name."""

	_name: ClassVar[str]

	def __init_subclass__(cls, *args, name: str = None, pattern: str = "{0}", **kwargs):
		kwargs["pattern"] = pattern
		super().__init_subclass__(*args, **kwargs)
		cls._name = name

	@property
	def Name(self) -> str:
		if self._name is None:
			raise ValueError(f"")  # XXX: add message

		return self._name

	def AsArgument(self) -> Union[str, Iterable[str]]:
		if self._name is None:
			raise ValueError(f"")  # XXX: add message

		return self._pattern.format(self._name)

	def __repr__(self) -> str:
		return f"\"{self.AsArgument()}\""

	__str__ = __repr__


@export
class ValuedArgument(CommandLineArgument):
	"""Base-class for all command line arguments with a value."""
	_value: str

	def __init__(self, value: str):
		if value is None:
			raise ValueError(f"")  # XXX: add message

		self._value = value

	@property
	def Value(self) -> str:
		return self._value

	@Value.setter
	def Value(self, value: str) -> None:
		if value is None:
			raise ValueError(f"")  # XXX: add message

		self._value = value

	def AsArgument(self) -> Union[str, Iterable[str]]:
		return self._pattern.format(self._value)

	def __repr__(self) -> str:
		return f"\"{self.AsArgument()}\""

	__str__ = __repr__


# TODO: make generic
class NamedAndValuedArgument(NamedArgument, ValuedArgument):
	"""Base-class for all command line arguments with a name and a value."""

	def __init__(self, value: str):
		if value is None:
			raise ValueError(f"Parameter 'value' is None.")

		self._value = value

	@property
	def Value(self) -> str:
		return self._value

	@Value.setter
	def Value(self, value: str) -> None:
		if value is None:
			raise ValueError(f"Value to set is None.")

		self._value = value

	def AsArgument(self) -> Union[str, Iterable[str]]:
		return self._pattern.format(self._name, self._value)

	def __repr__(self) -> str:
		return f"\"{self.AsArgument()}\""

	__str__ = __repr__


class NamedTupledArgument(NamedArgument):
	"""Base-class for all command line arguments with a name."""
	_valuePattern: ClassVar[str]
	_value: str

	def __init_subclass__(cls, *args, valuePattern: str="{0}", **kwargs):
		super().__init_subclass__(*args, **kwargs)
		cls._valuePattern = valuePattern

	def __init__(self, value: str):
		if value is None:
			raise ValueError(f"")  # XXX: add message


		self._value = value

	@property
	def ValuePattern(self) -> str:
		if self._valuePattern is None:
			raise ValueError(f"")  # XXX: add message

		return self._valuePattern

	@property
	def Value(self) -> str:
		return self._value

	@Value.setter
	def Value(self, value: str) -> None:
		if value is None:
			raise ValueError(f"")  # XXX: add message

		self._value = value

	def AsArgument(self) -> Union[str, Iterable[str]]:
		if self._name is None:
			raise ValueError(f"")  # XXX: add message

		return (
			self._pattern.format(self._name),
			self._valuePattern.format(self._value)
		)

	def __repr__(self) -> str:
		return ", ".join([f"\"{item}\"" for item in self.AsArgument()])

	def __str__(self) -> str:
		return " ".join([f"\"{item}\"" for item in self.AsArgument()])


@export
class StringArgument(ValuedArgument, pattern="{0}"):
	"""Represents a simple string argument."""

	def __init_subclass__(cls, *args, pattern="{0}", **kwargs):
		kwargs["pattern"] = pattern
		super().__init_subclass__(*args, **kwargs)


# @export
# class StringListArgument(CommandLineArgument):
# 	"""Represents a list of string arguments."""
# 	_pattern =  "{0}"
#
# 	@property
# 	def Value(self):
# 		return self._value
#
# 	@Value.setter
# 	def Value(self, value):
# 		if (value is None):           self._value = None
# 		elif isinstance(value, (tuple, list)):
# 			self._value = []
# 			try:
# 				for item in value:        self._value.append(str(item))
# 			except TypeError as ex:     raise ValueError("Item '{0}' in parameter 'value' cannot be converted to type str.".format(item)) from ex
# 		else:                         raise ValueError("Parameter 'value' is no list or tuple.")
#
# 	def __str__(self):
# 		if (self._value is None):     return ""
# 		elif self._value:             return " ".join([self._pattern.format(item) for item in self._value])
# 		else:                         return ""
#
# 	def AsArgument(self):
# 		if (self._value is None):      return None
# 		elif self._value:              return [self._pattern.format(item) for item in self._value]
# 		else:                          return None


@export
class PathArgument(CommandLineArgument):
	"""Represents a path argument."""
	# The output format can be forced to the POSIX format with :py:data:`_PosixFormat`.
	_path: ClassVar[Path]

	def __init__(self, path: Path):
		self._path = path

	@property
	def Value(self) -> Path:
		return self._path

	@Value.setter
	def Value(self, value: Path):
		if isinstance(value, Path):
			self._path = value
		else:
			raise TypeError("Parameter 'value' is not of type 'Path'.")

	def AsArgument(self) -> Union[str, Iterable[str]]:
		return f"{self._path}"

	def __repr__(self) -> str:
		return f"\"{self._path}\""

	__str__ = __repr__


@export
class PathListArgument(CommandLineArgument):
	"""Represents a path argument."""
	# The output format can be forced to the POSIX format with :py:data:`_PosixFormat`.
	_paths: ClassVar[List[Path]]

	def __init__(self, paths: Iterable[Path]):
		self._paths = []
		for path in paths:
			if not isinstance(path, Path):
				raise TypeError(f"Parameter 'paths' contains elements which are not of type 'Path'.")

			self._paths.append(path)

	@property
	def Value(self) -> List[Path]:
		return self._paths

	@Value.setter
	def Value(self, value: Iterable[Path]):
		self._paths.clear()
		for path in value:
			if not isinstance(path, Path):
				raise TypeError(f"Parameter 'paths' contains elements which are not of type 'Path'.")
			self._paths.append(path)

	def AsArgument(self) -> Union[str, Iterable[str]]:
		return [f"{path}" for path in self._paths]

	def __repr__(self) -> str:
		return " ".join([f"\"{path}\"" for path in self._paths])

	__str__ = __repr__


# @export
# class ValuedFlagListArgument(NamedCommandLineArgument):
# 	"""Class and base-class for all ValuedFlagListArgument classes, which represents a list of :py:class:`ValuedFlagArgument` instances.
#
# 	Each list item gets translated into a :py:class:`ValuedFlagArgument`, with the same flag name, but differing values. Each
# 	:py:class:`ValuedFlagArgument` is passed as a single argument to the executable, even if the delimiter sign is a whitespace
# 	character.
#
# 	Example: ``file=file1.txt file=file2.txt``
# 	"""
# 	_pattern = "{0}={1}"
#
# 	@property
# 	def Value(self):
# 		return self._value
#
# 	@Value.setter
# 	def Value(self, value):
# 		if (value is None):                    self._value = None
# 		elif isinstance(value, (tuple,list)):  self._value = value
# 		else:                                  raise ValueError("Parameter 'value' is not of type tuple or list.")
#
# 	def __str__(self):
# 		if (self._value is None):     return ""
# 		elif (len(self._value) > 0):  return " ".join([self._pattern.format(self._name, item) for item in self._value])
# 		else:                         return ""
#
# 	def AsArgument(self):
# 		if (self._value is None):     return None
# 		elif (len(self._value) > 0):  return [self._pattern.format(self._name, item) for item in self._value]
# 		else:                         return None


# @export
# class ShortValuedFlagListArgument(ValuedFlagListArgument):
# 	"""Represents a :py:class:`ValuedFlagListArgument` with a single dash.
#
# 	Example: ``-file=file1.txt -file=file2.txt``
# 	"""
# 	_pattern = "-{0}={1}"
#
#
# @export
# class LongValuedFlagListArgument(ValuedFlagListArgument):
# 	"""Represents a :py:class:`ValuedFlagListArgument` with a double dash.
#
# 	Example: ``--file=file1.txt --file=file2.txt``
# 	"""
# 	_pattern = "--{0}={1}"
#
#
# @export
# class WindowsValuedFlagListArgument(ValuedFlagListArgument):
# 	"""Represents a :py:class:`ValuedFlagListArgument` with a single slash.
#
# 	Example: ``/file:file1.txt /file:file2.txt``
# 	"""
# 	_pattern = "/{0}:{1}"

# XXX: delimiter argument "--"



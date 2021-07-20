# =============================================================================
#                ____ _     ___    _    _         _                  _   _
#   _ __  _   _ / ___| |   |_ _|  / \  | |__  ___| |_ _ __ __ _  ___| |_(_) ___  _ __
#  | '_ \| | | | |   | |    | |  / _ \ | '_ \/ __| __| '__/ _` |/ __| __| |/ _ \| '_ \
#  | |_) | |_| | |___| |___ | | / ___ \| |_) \__ \ |_| | | (_| | (__| |_| | (_) | | | |
#  | .__/ \__, |\____|_____|___/_/   \_\_.__/|___/\__|_|  \__,_|\___|\__|_|\___/|_| |_|
#  |_|    |___/
# =============================================================================
# Authors:            Patrick Lehmann
#
# Python Module:      Basic abstraction layer for executables.
#
# License:
# ============================================================================
# Copyright 2017-2021 Patrick Lehmann - Bötzingen, Germany
# Copyright 2007-2016 Technische Universität Dresden - Germany
#                     Chair of VLSI-Design, Diagnostics and Architecture
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#		http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0
# ============================================================================
#
# load dependencies
from pathlib import Path

from pydecor import export


@export
class CommandLineArgument(type):
	"""Base class (and meta class) for all Arguments classes."""
	_value = None

	# def __new__(mcls, name, bases, nmspc):
	# 	print("CommandLineArgument.new: %s - %s" % (name, nmspc))
	# 	return super(CommandLineArgument, mcls).__new__(mcls, name, bases, nmspc)


@export
class ExecutableArgument(CommandLineArgument):
	"""Represents the executable."""

	@property
	def Value(self):
		return self._value

	@Value.setter
	def Value(self, value):
		if isinstance(value, str):      self._value = value
		elif isinstance(value, Path):   self._value = str(value)
		else:                           raise ValueError("Parameter 'value' is not of type str or Path.")

	def __str__(self):
		if (self._value is None):       return ""
		else:                           return self._value

	def AsArgument(self):
		if (self._value is None):       raise ValueError("Executable argument is still empty.")
		else:                           return self._value


@export
class NamedCommandLineArgument(CommandLineArgument):
	"""Base class for all command line arguments with a name."""
	_name = None  # set in sub-classes

	@property
	def Name(self):
		return self._name


@export
class CommandArgument(NamedCommandLineArgument):
	"""Represents a command name.

	It is usually used to select a sub parser in a CLI argument parser or to hand
	over all following parameters to a separate tool. An example for a command is
	'checkout' in ``git.exe checkout``, which calls ``git-checkout.exe``.
	"""
	_pattern =    "{0}"

	@property
	def Value(self):
		return self._value

	@Value.setter
	def Value(self, value):
		if (value is None):           self._value = None
		elif isinstance(value, bool): self._value = value
		else:                         raise ValueError("Parameter 'value' is not of type bool.")

	def __str__(self):
		if (self._value is None):      return ""
		elif self._value:              return self._pattern.format(self._name)
		else:                          return ""

	def AsArgument(self):
		if (self._value is None):      return None
		elif self._value:              return self._pattern.format(self._name)
		else:                          return None


@export
class ShortCommandArgument(CommandArgument):
	"""Represents a command name with a single dash."""
	_pattern = "-{0}"


@export
class LongCommandArgument(CommandArgument):
	"""Represents a command name with a double dash."""
	_pattern = "--{0}"


@export
class WindowsCommandArgument(CommandArgument):
	"""Represents a command name with a single slash."""
	_pattern = "/{0}"


@export
class StringArgument(CommandLineArgument):
	"""Represents a simple string argument."""
	_pattern =  "{0}"

	@property
	def Value(self):
		return self._value

	@Value.setter
	def Value(self, value):
		if (value is None):            self._value = None
		elif isinstance(value, str):  self._value = value
		else:
			try:                        self._value = str(value)
			except Exception as ex:      raise ValueError("Parameter 'value' cannot be converted to type str.") from ex

	def __str__(self):
		if (self._value is None):      return ""
		elif self._value:              return self._pattern.format(self._value)
		else:                          return ""

	def AsArgument(self):
		if (self._value is None):      return None
		elif self._value:              return self._pattern.format(self._value)
		else:                          return None


@export
class StringListArgument(CommandLineArgument):
	"""Represents a list of string arguments."""
	_pattern =  "{0}"

	@property
	def Value(self):
		return self._value

	@Value.setter
	def Value(self, value):
		if (value is None):           self._value = None
		elif isinstance(value, (tuple, list)):
			self._value = []
			try:
				for item in value:        self._value.append(str(item))
			except TypeError as ex:     raise ValueError("Item '{0}' in parameter 'value' cannot be converted to type str.".format(item)) from ex
		else:                         raise ValueError("Parameter 'value' is no list or tuple.")

	def __str__(self):
		if (self._value is None):     return ""
		elif self._value:             return " ".join([self._pattern.format(item) for item in self._value])
		else:                         return ""

	def AsArgument(self):
		if (self._value is None):      return None
		elif self._value:              return [self._pattern.format(item) for item in self._value]
		else:                          return None


@export
class PathArgument(CommandLineArgument):
	"""Represents a path argument.

	The output format can be forced to the POSIX format with :py:data:`_PosixFormat`.
	"""
	_PosixFormat = False

	@property
	def Value(self):
		return self._value

	@Value.setter
	def Value(self, value):
		if (value is None):              self._value = None
		elif isinstance(value, Path):    self._value = value
		else:                            raise ValueError("Parameter 'value' is not of type Path.")

	def __str__(self):
		if (self._value is None):        return ""
		elif (self._PosixFormat):        return "\"" + self._value.as_posix() + "\""
		else:                            return "\"" + str(self._value) + "\""

	def AsArgument(self):
		if (self._value is None):        return None
		elif (self._PosixFormat):        return self._value.as_posix()
		else:                            return str(self._value)


@export
class FlagArgument(NamedCommandLineArgument):
	"""Base class for all FlagArgument classes, which represents a simple flag argument.

	A simple flag is a single boolean value (absent/present or off/on) with no data.
	"""
	_pattern =    "{0}"

	@property
	def Value(self):
		return self._value

	@Value.setter
	def Value(self, value):
		if (value is None):           self._value = None
		elif isinstance(value, bool): self._value = value
		else:                         raise ValueError("Parameter 'value' is not of type bool.")

	def __str__(self):
		if (self._value is None):     return ""
		elif self._value:             return self._pattern.format(self._name)
		else:                         return ""

	def AsArgument(self):
		if (self._value is None):     return None
		elif self._value:             return self._pattern.format(self._name)
		else:                         return None


@export
class ShortFlagArgument(FlagArgument):
	"""Represents a flag argument with a single dash.

	Example: ``-optimize``
	"""
	_pattern = "-{0}"


@export
class LongFlagArgument(FlagArgument):
	"""Represents a flag argument with a double dash.

	Example: ``--optimize``
	"""
	_pattern = "--{0}"


@export
class WindowsFlagArgument(FlagArgument):
	"""Represents a flag argument with a single slash.

	Example: ``/optimize``
	"""
	_pattern = "/{0}"


@export
class ValuedFlagArgument(NamedCommandLineArgument):
	"""Class and base class for all ValuedFlagArgument classes, which represents a flag argument with data.

	A valued flag is a flag name followed by a value. The default delimiter sign is equal (``=``). Name and
	value are passed as one arguments to the executable even if the delimiter sign is a whitespace character.

	Example: ``width=100``
	"""
	_pattern = "{0}={1}"

	@property
	def Value(self):
		return self._value

	@Value.setter
	def Value(self, value):
		if (value is None):           self._value = None
		elif isinstance(value, str):  self._value = value
		else:
			try:                        self._value = str(value)
			except Exception as ex:     raise ValueError("Parameter 'value' cannot be converted to type str.") from ex

	def __str__(self):
		if (self._value is None):     return ""
		elif self._value:             return self._pattern.format(self._name, self._value)
		else:                         return ""

	def AsArgument(self):
		if (self._value is None):     return None
		elif self._value:             return self._pattern.format(self._name, self._value)
		else:                         return None


@export
class ShortValuedFlagArgument(ValuedFlagArgument):
	"""Represents a :py:class:`ValuedFlagArgument` with a single dash.

	Example: ``-optimizer=on``
	"""
	_pattern = "-{0}={1}"


@export
class LongValuedFlagArgument(ValuedFlagArgument):
	"""Represents a :py:class:`ValuedFlagArgument` with a double dash.

	Example: ``--optimizer=on``
	"""
	_pattern = "--{0}={1}"


@export
class WindowsValuedFlagArgument(ValuedFlagArgument):
	"""Represents a :py:class:`ValuedFlagArgument` with a single slash.

	Example: ``/optimizer:on``
	"""
	_pattern = "/{0}:{1}"


@export
class OptionalValuedFlagArgument(NamedCommandLineArgument):
	"""Class and base class for all OptionalValuedFlagArgument classes, which represents a flag argument with data.

	An optional valued flag is a flag name followed by a value. The default delimiter sign is equal (``=``).
	Name and value are passed as one arguments to the executable even if the delimiter sign is a whitespace
	character. If the value is None, no delimiter sign and value is passed.

	Example: ``width=100``
	"""
	_pattern =          "{0}"
	_patternWithValue = "{0}={1}"

	@property
	def Value(self):
		return self._value

	@Value.setter
	def Value(self, value):
		if (value is None):           self._value = None
		elif isinstance(value, str):  self._value = value
		else:
			try:                        self._value = str(value)
			except Exception as ex:     raise ValueError("Parameter 'value' cannot be converted to type str.") from ex

	def __str__(self):
		if (self._value is None):     return ""
		elif self._value:             return self._pattern.format(self._name, self._value)
		else:                         return ""

	def AsArgument(self):
		if (self._value is None):     return None
		elif self._value:             return self._pattern.format(self._name, self._value)
		else:                         return None


@export
class ShortOptionalValuedFlagArgument(OptionalValuedFlagArgument):
	"""Represents a :py:class:`OptionalValuedFlagArgument` with a single dash.

	Example: ``-optimizer=on``
	"""
	_pattern =          "-{0}"
	_patternWithValue = "-{0}={1}"


@export
class LongOptionalValuedFlagArgument(OptionalValuedFlagArgument):
	"""Represents a :py:class:`OptionalValuedFlagArgument` with a double dash.

	Example: ``--optimizer=on``
	"""
	_pattern =          "--{0}"
	_patternWithValue = "--{0}={1}"


@export
class WindowsOptionalValuedFlagArgument(OptionalValuedFlagArgument):
	"""Represents a :py:class:`OptionalValuedFlagArgument` with a single slash.

	Example: ``/optimizer:on``
	"""
	_pattern =          "/{0}"
	_patternWithValue = "/{0}={1}"


@export
class ValuedFlagListArgument(NamedCommandLineArgument):
	"""Class and base class for all ValuedFlagListArgument classes, which represents a list of :py:class:`ValuedFlagArgument` instances.

	Each list item gets translated into a :py:class:`ValuedFlagArgument`, with the same flag name, but differing values. Each
	:py:class:`ValuedFlagArgument` is passed as a single argument to the executable, even if the delimiter sign is a whitespace
	character.

	Example: ``file=file1.txt file=file2.txt``
	"""
	_pattern = "{0}={1}"

	@property
	def Value(self):
		return self._value

	@Value.setter
	def Value(self, value):
		if (value is None):                    self._value = None
		elif isinstance(value, (tuple,list)):  self._value = value
		else:                                  raise ValueError("Parameter 'value' is not of type tuple or list.")

	def __str__(self):
		if (self._value is None):     return ""
		elif (len(self._value) > 0):  return " ".join([self._pattern.format(self._name, item) for item in self._value])
		else:                         return ""

	def AsArgument(self):
		if (self._value is None):     return None
		elif (len(self._value) > 0):  return [self._pattern.format(self._name, item) for item in self._value]
		else:                         return None


@export
class ShortValuedFlagListArgument(ValuedFlagListArgument):
	"""Represents a :py:class:`ValuedFlagListArgument` with a single dash.

	Example: ``-file=file1.txt -file=file2.txt``
	"""
	_pattern = "-{0}={1}"


@export
class LongValuedFlagListArgument(ValuedFlagListArgument):
	"""Represents a :py:class:`ValuedFlagListArgument` with a double dash.

	Example: ``--file=file1.txt --file=file2.txt``
	"""
	_pattern = "--{0}={1}"


@export
class WindowsValuedFlagListArgument(ValuedFlagListArgument):
	"""Represents a :py:class:`ValuedFlagListArgument` with a single slash.

	Example: ``/file:file1.txt /file:file2.txt``
	"""
	_pattern = "/{0}:{1}"


@export
class TupleArgument(NamedCommandLineArgument):
	"""Class and base class for all TupleArgument classes, which represents a switch with separate data.

	A tuple switch is a command line argument followed by a separate value. Name and value are passed as
	two arguments to the executable.

	Example: ``width 100``
	"""
	_switchPattern =  "{0}"
	_valuePattern =   "{0}"

	@property
	def Value(self):
		return self._value

	@Value.setter
	def Value(self, value):
		if (value is None):           self._value = None
		elif isinstance(value, str):  self._value = value
		else:
			try:                        self._value = str(value)
			except TypeError as ex:     raise ValueError("Parameter 'value' cannot be converted to type str.") from ex

	def __str__(self):
		if (self._value is None):     return ""
		elif self._value:             return self._switchPattern.format(self._name) + " \"" + self._valuePattern.format(self._value) + "\""
		else:                         return ""

	def AsArgument(self):
		if (self._value is None):     return None
		elif self._value:             return [self._switchPattern.format(self._name), self._valuePattern.format(self._value)]
		else:                         return None


@export
class ShortTupleArgument(TupleArgument):
	"""Represents a :py:class:`TupleArgument` with a single dash in front of the switch name.

	Example: ``-file file1.txt``
	"""
	_switchPattern = "-{0}"


@export
class LongTupleArgument(TupleArgument):
	"""Represents a :py:class:`TupleArgument` with a double dash in front of the switch name.

	Example: ``--file file1.txt``
	"""
	_switchPattern = "--{0}"


@export
class WindowsTupleArgument(TupleArgument):
	"""Represents a :py:class:`TupleArgument` with a single slash in front of the switch name.

	Example: ``/file file1.txt``
	"""
	_switchPattern = "/{0}"

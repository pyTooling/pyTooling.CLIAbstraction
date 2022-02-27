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
"""Valued tuple-flag arguments represent a name and a value as a 2-tuple.

.. seealso::

   * For flags with a value. |br|
     |rarr| :mod:`~pyTooling.CLIAbstraction.ValuedFlag`
   * For flags that have an optional value. |br|
     |rarr| :mod:`~pyTooling.CLIAbstraction.NamedOptionalValuedFlag`
"""
from typing import ClassVar, Union, Iterable

from pyTooling.Decorators import export

from pyTooling.CLIAbstraction.Argument import NamedArgument, ValuedArgument


@export
class ValuedTupleArgument(NamedArgument, ValuedArgument):
	"""Class and base-class for all TupleArgument classes, which represents an argument with separate value.

	A tuple argument is a command line argument followed by a separate value. Name and value are passed as
	two arguments to the executable.

	**Example: **

	* `width 100``
	"""
	_valuePattern: ClassVar[str]

	def __init_subclass__(cls, *args, valuePattern: str = "{0}", **kwargs):
		super().__init_subclass__(*args, **kwargs)
		cls._valuePattern = valuePattern

	def __new__(cls, *args, **kwargs):
		if cls is ValuedTupleArgument:
			raise TypeError(f"Class '{cls.__name__}' is abstract.")
		return super().__new__(cls, *args, **kwargs)

	def __init__(self, value: str):
		ValuedArgument.__init__(self, value)

	def AsArgument(self) -> Union[str, Iterable[str]]:
		"""Convert this argument instance to a sequence of string representations with proper escaping using the matching
		pattern based on the internal name and value.

		:return: Formatted argument.
		:raises ValueError: If internal name is None.
		"""
		if self._name is None:
			raise ValueError(f"Internal value '_name' is None.")

		return (
			self._pattern.format(self._name),
			self._valuePattern.format(self._value)
		)

	def __str__(self) -> str:
		"""Return a string representation of this argument instance.

		:return: Argument formatted and enclosed in double quotes.
		"""
		return " ".join([f"\"{item}\"" for item in self.AsArgument()])

	def __repr__(self) -> str:
		"""Return a string representation of this argument instance.

		:return: Argument formatted and enclosed in double quotes.
		"""
		return ", ".join([f"\"{item}\"" for item in self.AsArgument()])


@export
class ShortTupleFlag(ValuedTupleArgument, pattern="-{0}"):
	"""Represents a :class:`ValuedTupleArgument` with a single dash in front of the switch name.

	**Example:**

	* ``-file file1.txt``
	"""
	def __init_subclass__(cls, *args, pattern="-{0}", **kwargs):
		kwargs["pattern"] = pattern
		super().__init_subclass__(*args, **kwargs)

	def __new__(cls, *args, **kwargs):
		if cls is ShortTupleFlag:
			raise TypeError(f"Class '{cls.__name__}' is abstract.")
		return super().__new__(cls, *args, **kwargs)


@export
class LongTupleFlag(ValuedTupleArgument, pattern="--{0}"):
	"""Represents a :class:`ValuedTupleArgument` with a double dash in front of the switch name.

	**Example:**

	* ``--file file1.txt``
	"""
	def __init_subclass__(cls, *args, pattern="--{0}", **kwargs):
		kwargs["pattern"] = pattern
		super().__init_subclass__(*args, **kwargs)

	def __new__(cls, *args, **kwargs):
		if cls is LongTupleFlag:
			raise TypeError(f"Class '{cls.__name__}' is abstract.")
		return super().__new__(cls, *args, **kwargs)


@export
class WindowsTupleFlag(ValuedTupleArgument, pattern="/{0}"):
	"""Represents a :class:`ValuedTupleArgument` with a single slash in front of the switch name.

	**Example:**

	* ``/file file1.txt``
	"""
	def __init_subclass__(cls, *args, pattern="/{0}", **kwargs):
		kwargs["pattern"] = pattern
		super().__init_subclass__(*args, **kwargs)

	def __new__(cls, *args, **kwargs):
		if cls is WindowsTupleFlag:
			raise TypeError(f"Class '{cls.__name__}' is abstract.")
		return super().__new__(cls, *args, **kwargs)

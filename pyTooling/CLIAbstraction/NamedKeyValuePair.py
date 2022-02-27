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
"""Flag arguments represent simple boolean values by being present or absent.

.. seealso::

   * For flags with different pattern based on the boolean value itself. |br|
     |rarr| :mod:`~pyTooling.CLIAbstraction.BooleanFlag`
   * For flags with a value. |br|
     |rarr| :mod:`~pyTooling.CLIAbstraction.ValuedFlag`
   * For flags that have an optional value. |br|
     |rarr| :mod:`~pyTooling.CLIAbstraction.NamedOptionalValuedFlag`
"""
from typing import Union, Iterable, ClassVar

from pyTooling.Decorators import export

from pyTooling.CLIAbstraction import NamedAndValuedArgument


class NamedKeyValuePairsArgument(NamedAndValuedArgument):
	"""Base-class for all command line arguments with a name and a key-value pair."""
	_key: str

	def __init__(self, key: str, value: str):
		super().__init__(value)
		if key is None:
			raise ValueError(f"Parameter 'key' is None.")

		self._key = key

	@property
	def Key(self) -> str:
		return self._key

	@Key.setter
	def Key(self, key: str) -> None:
		if key is None:
			raise ValueError(f"Key to set is None.")

		self._key = key

	def AsArgument(self) -> Union[str, Iterable[str]]:
		"""Convert this argument instance to a string representation with proper escaping using the matching pattern based
		on the internal name.

		:return: Formatted argument.
		:raises ValueError: If internal name is None.
		"""
		if self._name is None:
			raise ValueError(f"Internal value '_name' is None.")
		if self._key is None:
			raise ValueError(f"")  # XXX: add message
		if self._value is None:
			raise ValueError(f"")  # XXX: add message

		return self._pattern.format(self._name, self._key, self._value)

	def __str__(self) -> str:
		"""Return a string representation of this argument instance.

		:return: Argument formatted and enclosed in double quotes.
		"""
		return f"\"{self.AsArgument()}\""

	__repr__ = __str__


@export
class NamedKeyValueFlagArgument(NamedKeyValuePairsArgument):
	"""
	Class and base-class for all NamedKeyValueFlagArgument classes, which represents a flag with a name and a key-value pair.

	Example: ``DDEBUG=TRUE``
	"""
	_pattern: ClassVar[str]

	def __init_subclass__(cls, *args, pattern: str = "{0}{1}={2}", **kwargs):
		super().__init_subclass__(*args, **kwargs)
		cls._pattern = pattern


@export
class ShortNamedKeyValueFlagArgument(NamedKeyValueFlagArgument, pattern="-{0}{1}={2}"):
	"""Represents a :py:class:`NamedKeyValueFlagArgument` with a single dash in front of the switch name.

	Example: ``-DDEBUG=TRUE``
	"""
	def __init_subclass__(cls, *args, pattern="-{0}{1}={2}", **kwargs):
		kwargs["pattern"] = pattern
		super().__init_subclass__(*args, **kwargs)


@export
class LongNamedKeyValueFlagArgument(NamedKeyValueFlagArgument, pattern="--{0}{1}={2}"):
	"""Represents a :py:class:`NamedKeyValueFlagArgument` with a double dash in front of the switch name.

	Example: ``--DDEBUG=TRUE``
	"""
	def __init_subclass__(cls, *args, pattern="--{0}{1}={2}", **kwargs):
		kwargs["pattern"] = pattern
		super().__init_subclass__(*args, **kwargs)

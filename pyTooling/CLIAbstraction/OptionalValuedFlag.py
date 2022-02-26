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
"""

.. TODO:: Write module documentation.

"""
from typing import ClassVar, Optional as Nullable, Union, Iterable

from pyTooling.Decorators import export

from pyTooling.CLIAbstraction import NamedAndValuedArgument


@export
class OptionalValuedFlag(NamedAndValuedArgument, pattern="{0"):
	"""Class and base-class for all OptionalValuedFlag classes, which represents a flag argument with data.

	An optional valued flag is a flag name followed by a value. The default delimiter sign is equal (``=``).
	Name and value are passed as one arguments to the executable even if the delimiter sign is a whitespace
	character. If the value is None, no delimiter sign and value is passed.

	Example: ``width=100``
	"""
	_patternWithValue: ClassVar[str]

	def __init_subclass__(cls, *args, pattern="{0}", patternWithValue: str = "{0}={1}", **kwargs):
		kwargs["pattern"] = pattern
		super().__init_subclass__(*args, **kwargs)
		cls._patternWithValue = patternWithValue

	def __new__(cls, *args, **kwargs):
		if cls is OptionalValuedFlag:
			raise TypeError(f"Class '{cls.__name__}' is abstract.")
		return super().__new__(cls, *args, **kwargs)

	def __init__(self, value: str = None):
		self._value = value

	@property
	def Value(self) -> Nullable[str]:
		return self._value

	@Value.setter
	def Value(self, value: Nullable[str]) -> None:
		self._value = value

	def AsArgument(self) -> Union[str, Iterable[str]]:
		if self._name is None:
			raise ValueError(f"")  # XXX: add message

		pattern = self._pattern if self._value is None else self._patternWithValue
		return pattern.format(self._name, self._value)

	def __repr__(self) -> str:
		return f"\"{self.AsArgument()}\""

	__str__ = __repr__


@export
class ShortOptionalValuedFlag(OptionalValuedFlag, pattern="-{0}", patternWithValue="-{0}={1}"):
	"""Represents a :py:class:`OptionalValuedFlag` with a single dash.

	Example: ``-optimizer=on``
	"""
	def __init_subclass__(cls, *args, pattern="-{0}", patternWithValue="-{0}={1}", **kwargs):
		kwargs["pattern"] = pattern
		kwargs["patternWithValue"] = patternWithValue
		super().__init_subclass__(*args, **kwargs)

	def __new__(cls, *args, **kwargs):
		if cls is ShortOptionalValuedFlag:
			raise TypeError(f"Class '{cls.__name__}' is abstract.")
		return super().__new__(cls, *args, **kwargs)


@export
class LongOptionalValuedFlag(OptionalValuedFlag, pattern="--{0}", patternWithValue="--{0}={1}"):
	"""Represents a :py:class:`OptionalValuedFlag` with a double dash.

	Example: ``--optimizer=on``
	"""
	def __init_subclass__(cls, *args, pattern="--{0}", patternWithValue="--{0}={1}", **kwargs):
		kwargs["pattern"] = pattern
		kwargs["patternWithValue"] = patternWithValue
		super().__init_subclass__(*args, **kwargs)

	def __new__(cls, *args, **kwargs):
		if cls is LongOptionalValuedFlag:
			raise TypeError(f"Class '{cls.__name__}' is abstract.")
		return super().__new__(cls, *args, **kwargs)


@export
class WindowsOptionalValuedFlag(OptionalValuedFlag, pattern="/{0}", patternWithValue="/{0}:{1}"):
	"""Represents a :py:class:`OptionalValuedFlag` with a single slash.

	Example: ``/optimizer:on``
	"""
	def __init_subclass__(cls, *args, pattern="/{0}", patternWithValue="/{0}:{1}", **kwargs):
		kwargs["pattern"] = pattern
		kwargs["patternWithValue"] = patternWithValue
		super().__init_subclass__(*args, **kwargs)

	def __new__(cls, *args, **kwargs):
		if cls is WindowsOptionalValuedFlag:
			raise TypeError(f"Class '{cls.__name__}' is abstract.")
		return super().__new__(cls, *args, **kwargs)

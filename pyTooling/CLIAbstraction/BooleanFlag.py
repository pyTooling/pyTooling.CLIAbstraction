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
from typing import ClassVar, Union, Iterable

from pyTooling.Decorators import export

from pyTooling.CLIAbstraction import ValuedCommandLineArgument


@export
class BooleanFlag(ValuedCommandLineArgument):
	"""
	Class and base-class for all BooleanFlagArgument classes, which represents a flag argument with different pattern	for
	an enabled/positive (``True``) or disabled/negative (``False``) state.

	Example:

	* True: ``with-checks``
	* False: ``without-checks``
	"""
	_truePattern: ClassVar[str]
	_falsePattern: ClassVar[str]

	def __init_subclass__(cls, *args, truePattern: str = "with-{0}", falsePattern: str = "without-{0}", **kwargs):
		super().__init_subclass__(*args, **kwargs)
		cls._truePattern = truePattern
		cls._falsePattern = falsePattern

	def __init__(self, value: bool):
		self._value = value

	@property
	def Value(self) -> bool:
		return self._value

	@Value.setter
	def Value(self, value: bool) -> None:
		self._value = value

	def AsArgument(self) -> Union[str, Iterable[str]]:
		if self._name is None:
			raise ValueError(f"")  # XXX: add message

		pattern = self._truePattern if self._value is True else self._falsePattern
		return pattern.format(self._name)

	def __repr__(self) -> str:
		return f"\"{self.AsArgument()}\""

	__str__ = __repr__


@export
class ShortBooleanFlag(BooleanFlag, truePattern="-{0}", falsePattern="-{0}"):
	"""Represents a :py:class:`BooleanFlagArgument` with a single dash.

	Example:
	* True: ``-with-checks``
	* False: ``-without-checks``
	"""
	def __init_subclass__(cls, *args, truePattern="-{0}", falsePattern="-{0}", **kwargs):
		kwargs["truePattern"] = truePattern
		kwargs["falsePattern"] = falsePattern
		super().__init_subclass__(*args, **kwargs)


@export
class LongBooleanFlag(BooleanFlag, truePattern="--{0}", falsePattern="--{0}"):
	"""Represents a :py:class:`BooleanFlagArgument` with a double dash.

	Example:
	* True: ``--with-checks``
	* False: ``--without-checks``
	"""
	def __init_subclass__(cls, *args, truePattern="--{0}", falsePattern="--{0}", **kwargs):
		kwargs["truePattern"] = truePattern
		kwargs["falsePattern"] = falsePattern
		super().__init_subclass__(*args, **kwargs)


@export
class WindowsBooleanFlag(BooleanFlag, truePattern="/{0}", falsePattern="/{0}"):
	"""Represents a :py:class:`BooleanFlagArgument` with a slash.

	Example:
	* True: ``/with-checks``
	* False: ``/without-checks``
	"""
	def __init_subclass__(cls, *args, truePattern="/{0}", falsePattern="/{0}", **kwargs):
		kwargs["truePattern"] = truePattern
		kwargs["falsePattern"] = falsePattern
		super().__init_subclass__(*args, **kwargs)

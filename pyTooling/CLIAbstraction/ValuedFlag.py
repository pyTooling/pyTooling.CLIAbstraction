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
from pyTooling.Decorators import export

from pyTooling.CLIAbstraction import NameValuedArgument


@export
class ValuedFlagArgument(NameValuedArgument, pattern="{0}={1}"):
	"""Class and base-class for all ValuedFlagArgument classes, which represents a flag argument with data.

	A valued flag is a flag name followed by a value. The default delimiter sign is equal (``=``). Name and
	value are passed as one arguments to the executable even if the delimiter sign is a whitespace character.

	Example: ``width=100``
	"""
	def __init_subclass__(cls, *args, pattern="{0}={1}", **kwargs):
		kwargs["pattern"] = pattern
		super().__init_subclass__(*args, **kwargs)


@export
class ShortValuedFlagArgument(ValuedFlagArgument, pattern="-{0}={1}"):
	"""Represents a :py:class:`ValuedFlagArgument` with a single dash.

	Example: ``-optimizer=on``
	"""
	def __init_subclass__(cls, *args, pattern="-{0}={1}", **kwargs):
		kwargs["pattern"] = pattern
		super().__init_subclass__(*args, **kwargs)


@export
class LongValuedFlagArgument(ValuedFlagArgument, pattern="--{0}={1}"):
	"""Represents a :py:class:`ValuedFlagArgument` with a double dash.

	Example: ``--optimizer=on``
	"""
	def __init_subclass__(cls, *args, pattern="--{0}={1}", **kwargs):
		kwargs["pattern"] = pattern
		super().__init_subclass__(*args, **kwargs)


@export
class WindowsValuedFlagArgument(ValuedFlagArgument, pattern="/{0}:{1}"):
	"""Represents a :py:class:`ValuedFlagArgument` with a single slash.

	Example: ``/optimizer:on``
	"""
	def __init_subclass__(cls, *args, pattern="/{0}:{1}", **kwargs):
		kwargs["pattern"] = pattern
		super().__init_subclass__(*args, **kwargs)

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

from pyTooling.CLIAbstraction.Argument import NamedArgument


@export
class CommandArgument(NamedArgument):
	"""Represents a command name.

	It is usually used to select a sub parser in a CLI argument parser or to hand
	over all following parameters to a separate tool. An example for a command is
	'checkout' in ``git.exe checkout``, which calls ``git-checkout.exe``.
	"""


@export
class ShortCommandArgument(CommandArgument, pattern="-{0}"):
	"""Represents a command name with a single dash."""

	def __init_subclass__(cls, *args, pattern="-{0}", **kwargs):
		kwargs["pattern"] = pattern
		super().__init_subclass__(*args, **kwargs)


@export
class LongCommandArgument(CommandArgument, pattern="--{0}"):
	"""Represents a command name with a double dash."""

	def __init_subclass__(cls, *args, pattern="--{0}", **kwargs):
		kwargs["pattern"] = pattern
		super().__init_subclass__(*args, **kwargs)


@export
class WindowsCommandArgument(CommandArgument, pattern="/{0}"):
	"""Represents a command name with a single slash."""

	def __init_subclass__(cls, *args, pattern="/{0}", **kwargs):
		kwargs["pattern"] = pattern
		super().__init_subclass__(*args, **kwargs)

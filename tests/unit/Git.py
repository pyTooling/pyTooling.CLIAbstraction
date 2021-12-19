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
# Copyright 2017-2021 Patrick Lehmann - Bötzingen, Germany                                                             #
# Copyright 2007-2016 Technische Universität Dresden - Germany                                                         #
#                     Chair of VLSI-Design, Diagnostics and Architecture                                               #
#                                                                                                                      #
# Licensed under the Apache License, Version 2.0 (the "License");                                                      #
# you may not use this file except in compliance with the License.                                                     #
# You may obtain a copy of the License at                                                                              #
#                                                                                                                      #
#		http://www.apache.org/licenses/LICENSE-2.0                                                                         #
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
Testcase for operating system program ``mkdir``.

:copyright: Copyright 2007-2021 Patrick Lehmann - Bötzingen, Germany
:license: Apache License, Version 2.0
"""
from pathlib import Path
from platform     import system
from typing import Dict, Optional
from unittest     import TestCase

from pyTooling.Exceptions                import PlatformNotSupportedException

from pyTooling.CLIAbstraction import DryRunException
from pyTooling.CLIAbstraction.Argument import ExecutableArgument, ShortFlagArgument, LongFlagArgument, CommandArgument, CommandLineArgument
from pyTooling.CLIAbstraction.Executable import Executable, CommandLineArgumentList


if __name__ == "__main__": # pragma: no cover
	print("ERROR: you called a testcase declaration file as an executable module.")
	print("Use: 'python -m unitest <testcase module>'")
	exit(1)


class ShellException(Exception):
	pass


class Git(Executable):
	def __init__(self):
		# super().__init__()
		self._platform = system()
		self._binaryDirectoryPath = Path("C:\Program Files\Git\cmd")
		self._dryrun = False

		if (self._platform == "Windows"):
			executablePath = self._binaryDirectoryPath / "git.exe"
		elif (self._platform == "Linux"):
			executablePath = self._binaryDirectoryPath / "git"
		else:
			raise PlatformNotSupportedException(self._platform)

		super().__init__(self._platform, self._dryrun, executablePath, environment=None)

		self[self.Executable] = executablePath

	class Executable(metaclass=ExecutableArgument):
		_executable = None

		def __init__(self, executable: Path):
			self._executable = executable

	def AsArgument(self):
		if self._executable is None:
			raise ValueError("Executable argument is still empty.")

		return str(self._executable)

	class FlagVersion(metaclass=LongFlagArgument):
		_name =   "version"
		_value =  None

		def __init__(self, value: bool):
			self._value = value

	class FlagHelp(metaclass=LongFlagArgument):
		_name =   "help"
		_value =  None

		def __init__(self, value: bool):
			self._value = value

	class CommandHelp(metaclass=CommandArgument):
		_name =   "help"
		_value =  None

		def __init__(self, value: bool):
			self._value = value

	# Parameters = CommandLineArgumentList(
	# 		Executable,
	# 		FlagVersion,
	# 		FlagHelp,
	# 		CommandHelp
	# 	)

	Parameters: Dict[CommandLineArgument, Optional[CommandLineArgument]] = {
			Executable: None,
			FlagVersion: None,
			FlagHelp: None,
			CommandHelp: None
	}

	def __getitem__(self, key):
		return self.Parameters[key]

	def __setitem__(self, key, value):
		parameter = self.Parameters[key]
		if parameter is None:
			self.Parameters[key] = key(value)
		else:
			parameter.Value = value

	def ToArgumentList(self):
		result = []
		for key, value in self.Parameters.items():
			arg = value.AsArgument()
			if (arg is None):           pass
			elif isinstance(arg, str):  result.append(arg)
			elif isinstance(arg, list): result += arg
			else:                       raise TypeError()
		return result

	def Create(self):
		parameterList = self.ToArgumentList()
#		self.LogVerbose("command: {0}".format(" ".join(parameterList)))

		try:
			self.StartProcess(parameterList)
		except Exception as ex:
			raise ShellException("Failed to launch 'mkdir'.") from ex

		try:
			iterator = iter(self.GetReader())

			line = next(iterator)

			while True:
				print(line)
				line = next(iterator)

		except DryRunException:
			pass
		except StopIteration:
			pass
		finally:
			pass


class CommonOptions(TestCase):
	def test_VersionFlag(self):
		tool = Git()
		tool[tool.FlagVersion] = True

		tool.Create()

	def test_HelpFlag(self):
		tool = Git()
		tool[tool.FlagHelp] = True

#		tool.Create()

	def test_HelpCommand(self):
		tool = Git()
		tool[tool.CommandHelp] = True

#		tool.Create()

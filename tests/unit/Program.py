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
from unittest     import TestCase

from pyTooling.CLIAbstraction          import CLIOption, Program
from pyTooling.CLIAbstraction.Argument import CommandArgument, ShortFlagArgument, LongFlagArgument, ShortTupleArgument


if __name__ == "__main__": # pragma: no cover
	print("ERROR: you called a testcase declaration file as an executable module.")
	print("Use: 'python -m unitest <testcase module>'")
	exit(1)


class Git(Program):
	_executableNames = {
		"Windows": "git.exe",
		"Linux": "git"
	}

	@CLIOption()
	class FlagVersion(LongFlagArgument, name="version"): ...

	@CLIOption()
	class FlagHelp(LongFlagArgument, name="help"): ...

	@CLIOption()
	class CommandHelp(CommandArgument, name="help"): ...

	@CLIOption()
	class CommandInit(CommandArgument, name="init"): ...

	@CLIOption()
	class CommandStage(CommandArgument, name="add"): ...

	@CLIOption()
	class CommandCommit(CommandArgument, name="commit"): ...

	@CLIOption()
	class ValueCommitMessage(ShortTupleArgument, name="m"): ...


class CommonOptions(TestCase):
	_binaryDirectoryPath = Path("/usr/bin")

	def test_VersionFlag(self):
		tool = Git(binaryDirectoryPath=self._binaryDirectoryPath)
		tool[tool.FlagVersion] = True

		print()
		# print(f"CommonOptions.test_VersionFlag - Options:")
		# for opt in tool.__cliOptions__:
		# 	print(f"  {opt}")
		# print(f"CommonOptions.test_VersionFlag - Parameters:")
		# for param, value in tool.__cliParameters__.items():
		# 	print(f"  {param} - {value}")
		print(f"CommonOptions.test_VersionFlag - Arguments:")
		for arg in tool.ToArgumentList():
			print(f"  {arg}")

	def test_HelpFlag(self):
		tool = Git(binaryDirectoryPath=self._binaryDirectoryPath)
		tool[tool.FlagHelp] = True

		print()
		# print(f"CommonOptions.test_VersionFlag - Options:")
		# for opt in tool.__cliOptions__:
		# 	print(f"  {opt}")
		# print(f"CommonOptions.test_VersionFlag - Parameters:")
		# for param, value in tool.__cliParameters__.items():
		# 	print(f"  {param} - {value}")
		print(f"CommonOptions.test_VersionFlag - Arguments:")
		for arg in tool.ToArgumentList():
			print(f"  {arg}")

	def test_HelpCommand(self):
		tool = Git(binaryDirectoryPath=self._binaryDirectoryPath)
		tool[tool.CommandHelp] = True

		print()
		# print(f"CommonOptions.test_VersionFlag - Options:")
		# for opt in tool.__cliOptions__:
		# 	print(f"  {opt}")
		# print(f"CommonOptions.test_VersionFlag - Parameters:")
		# for param, value in tool.__cliParameters__.items():
		# 	print(f"  {param} - {value}")
		print(f"CommonOptions.test_VersionFlag - Arguments:")
		for arg in tool.ToArgumentList():
			print(f"  {arg}")

class Commit(TestCase):
	_binaryDirectoryPath = Path("/usr/bin")

	def test_CommitWithMessage(self):
		tool = Git(binaryDirectoryPath=self._binaryDirectoryPath)
		tool[tool.CommandCommit] = True
		tool[tool.ValueCommitMessage] = "Initial commit."

		print()
		print(f"CommonOptions.test_VersionFlag - Arguments:")
		for arg in tool.ToArgumentList():
			print(f"  {arg}")

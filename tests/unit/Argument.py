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
"""Testcases for arguments without a prefix."""
from pathlib import Path
from unittest import TestCase

from pyTooling.CLIAbstraction import ExecutableArgument
from pyTooling.CLIAbstraction.Argument import StringArgument, DelimiterArgument, CommandLineArgument, NamedArgument, \
	ValuedArgument, NamedAndValuedArgument
from pyTooling.CLIAbstraction.Command import CommandArgument


if __name__ == "__main__": # pragma: no cover
	print("ERROR: you called a testcase declaration file as an executable module.")
	print("Use: 'python -m unitest <testcase module>'")
	exit(1)


class WithoutPrefix(TestCase):
	def test_CommandLineArgument(self):
		with self.assertRaises(TypeError):
			_ = CommandLineArgument()

	def test_ExecutableArgument(self):
		executablePath = Path("program.exe")
		argument = ExecutableArgument(executablePath)

		self.assertIs(executablePath, argument.Executable)
		self.assertEqual(f"{executablePath}", argument.AsArgument())
		self.assertEqual(f"\"{executablePath}\"", str(argument))
		self.assertEqual(str(argument), repr(argument))

		executablePath2 = Path("script.sh")
		argument.Executable = executablePath2
		self.assertIs(executablePath2, argument.Executable)


	def test_DelimiterArgument(self):
		pattern = "--"
		argument = DelimiterArgument()

		self.assertEqual(f"{pattern}", argument.AsArgument())
		self.assertEqual(f"\"{pattern}\"", str(argument))
		self.assertEqual(str(argument), repr(argument))

	def test_DerivedDelimiterArgument(self):
		pattern = "--"

		class Delimiter(DelimiterArgument, pattern=pattern):
			pass

		argument = Delimiter()

		self.assertEqual(f"{pattern}", argument.AsArgument())
		self.assertEqual(f"\"{pattern}\"", str(argument))
		self.assertEqual(str(argument), repr(argument))

	def test_AbstractCommandArgument(self):
		with self.assertRaises(TypeError):
			_ = CommandArgument()

	def test_CommandArgument(self):
		name = "command"

		class Command(CommandArgument, name=name):
			pass

		argument = Command()

		self.assertIs(name, argument.Name)
		self.assertEqual(f"{name}", argument.AsArgument())
		self.assertEqual(f"\"{name}\"", str(argument))
		self.assertEqual(str(argument), repr(argument))

	def test_NamedArgument(self):
		with self.assertRaises(TypeError):
			_ = NamedArgument()

	def test_DerivedNamedArgument(self):
		name = "command"

		class Command(CommandArgument, name=name):
			pass

		argument = Command()
		self.assertIs(name, argument.Name)
		self.assertEqual(f"{name}", argument.AsArgument())
		self.assertEqual(f"\"{name}\"", str(argument))
		self.assertEqual(str(argument), repr(argument))

	def test_ValuedArgument(self):
		value = "value"
		argument = ValuedArgument(value)

		self.assertIs(value, argument.Value)
		self.assertEqual(f"{value}", argument.AsArgument())
		self.assertEqual(f"\"{value}\"", str(argument))
		self.assertEqual(str(argument), repr(argument))

	def test_NamedAndValuedArgument(self):
		with self.assertRaises(TypeError):
			_ = NamedAndValuedArgument()

	def test_DerivedNamedAndValuedArgument(self):
		name = "flag"
		value = "value"

		class Flag(NamedAndValuedArgument, name=name):
			pass

		argument = Flag(value)
		self.assertIs(name, argument.Name)
		self.assertEqual(f"{name}={value}", argument.AsArgument())
		self.assertEqual(f"\"{name}={value}\"", str(argument))
		self.assertEqual(str(argument), repr(argument))

	def test_StringArgument(self):
		value = "value"
		argument = StringArgument(value)

		self.assertIs(value, argument.Value)
		self.assertEqual(f"{value}", argument.AsArgument())
		self.assertEqual(f"\"{value}\"", str(argument))
		self.assertEqual(str(argument), repr(argument))

		value2 = "value2"
		argument.Value = value2
		self.assertIs(value2, argument.Value)


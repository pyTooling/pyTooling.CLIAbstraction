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
from pathlib                  import Path
from platform                 import system
from subprocess               import Popen				as Subprocess_Popen
from subprocess               import PIPE					as Subprocess_Pipe
from subprocess               import STDOUT				as Subprocess_StdOut
from typing import Dict, Optional, ClassVar, Type

from pyTooling.Decorators import export
from pyTooling.Exceptions import PlatformNotSupportedException

from . import ExecutableException, DryRunException
from .Argument import CommandLineArgument, CLIOption, ExecutableArgument


@export
class CommandLineArgumentList(list):
	"""Represent a list of all available commands, flags and switch of an executable."""

	def __init__(self, *args):
		super().__init__()
		for arg in args:
			self.append(arg)

	# def __getitem__(self, key):
	# 	i = self.index(key)
	# 	return super().__getitem__(i).Value
	#
	# def __setitem__(self, key, value):
	# 	i = self.index(key)
	# 	super().__getitem__(i).Value = value

	# def __delitem__(self, key):
	# 	i = self.index(key)
	# 	super().__getitem__(i).Value = None

	def ToArgumentList(self):
		result = []
		for item in self:
			arg = item.AsArgument()
			if (arg is None):           pass
			elif isinstance(arg, str):  result.append(arg)
			elif isinstance(arg, list): result += arg
			else:                       raise TypeError()
		return result


@export
class Environment:
	def __init__(self):
		self.Variables = {}


@export
class Program: # (ILogable):
	"""Represent an executable."""
	_platform:         str
	_executableNames:  ClassVar[Dict[str, str]]
	_executablePath:   Path
	_environment:      Optional[Dict[str, str]]
	_dryrun:           bool
	__cliOptions__:    ClassVar[Dict[Type[CommandLineArgument], Optional[CommandLineArgument]]]
	__cliParameters__: Dict[Type[CommandLineArgument], Optional[CommandLineArgument]]

	def __init_subclass__(cls, **kwargs):
		cls.__cliOptions__: Dict[CommandLineArgument, Optional[CommandLineArgument]] = {}

		for option in CLIOption.GetClasses():
			cls.__cliOptions__[option] = None

	def __init__(self, executablePath: Path = None, binaryDirectoryPath: Path = None, dryRun: bool = False, environment: Environment = None): #, logger : Logger =None):
		self._platform =    system()
		self._dryrun =      dryRun
		self._environment = environment  # if (environment is not None) else Environment()

		if executablePath is not None:
			if isinstance(executablePath, Path):
				if not executablePath.exists():
					raise FileNotFoundError(f"Program '{executablePath}' not found.")
			else:
				raise TypeError(f"Parameter 'executablePath' is not of type 'Path'.")
		elif binaryDirectoryPath is not None:
			if isinstance(binaryDirectoryPath, Path):
				try:
					executablePath = binaryDirectoryPath / self._executableNames[self._platform]
				except KeyError:
					raise PlatformNotSupportedException(self._platform)

				if not binaryDirectoryPath.exists():
					raise FileNotFoundError(f"Binary directory '{binaryDirectoryPath}' not found.")
				elif not executablePath.exists():
					raise FileNotFoundError(f"Program '{executablePath}' not found.")
			else:
				raise TypeError(f"Parameter 'binaryDirectoryPath' is not of type 'Path'.")
		else:
			raise ValueError(f"Neither parameter 'executablePath' nor 'binaryDirectoryPath' was set.")

		self._executablePath = executablePath
		self.__cliParameters__ = {}

		self.__cliParameters__[self.Executable] = self.Executable(executablePath)

		self._process =  None
		self._iterator = None

		# if not executablePath.exists():
		# 	if dryRun:
		# 		self.LogDryRun(f"File check for '{executablePath}' failed. [SKIPPING]")
		# 	else:
		# 		raise ExecutableException(f"Program '{executablePath}' not found.") from FileNotFoundError(str(executablePath))

	def __getitem__(self, key):
		return self.__cliOptions__[key]

	def __setitem__(self, key, value):
		if key not in self.__cliOptions__:
			raise KeyError(f"Option '{key}' is not allowed on executable '{self.__class__.__name__}'")
		elif key in self.__cliParameters__:
			raise KeyError(f"Option '{key}' is already set to a value.")

		self.__cliParameters__[key] = True #key(value)

	@CLIOption()
	class Executable(ExecutableArgument, executablePath=None):   # XXX: no argument here
		def __init__(self, executable: Path):
			self._executable = executable



	@property
	def Path(self) -> Path:
		return self._executablePath


@export
class Executable(Program):  # (ILogable):
	"""Represent an executable."""
	_pyIPCMI_BOUNDARY = "====== pyIPCMI BOUNDARY ======"

	def StartProcess(self, parameterList):
		# start child process
		# parameterList.insert(0, str(self._executablePath))
		if (not self._dryrun):
			if (self._environment is not None):
				envVariables = self._environment.Variables
			else:
				envVariables = None

			try:
				self._process = Subprocess_Popen(
					parameterList,
					stdin=Subprocess_Pipe,
					stdout=Subprocess_Pipe,
					stderr=Subprocess_StdOut,
					env=envVariables,
					universal_newlines=True,
					bufsize=256
				)
			except OSError as ex:
				raise ExecutableException("Error while accessing '{0!s}'.".format(self._executablePath)) from ex
		else:
			self.LogDryRun("Start process: {0}".format(" ".join(parameterList)))

	def Send(self, line, end="\n"):
		self._process.stdin.write(line + end)
		self._process.stdin.flush()

	def SendBoundary(self):
		self.Send("puts \"{0}\"".format(self._pyIPCMI_BOUNDARY))

	def Terminate(self):
		self._process.terminate()

	def GetReader(self):
		if (not self._dryrun):
			try:
				for line in iter(self._process.stdout.readline, ""):
					yield line[:-1]
			except Exception as ex:
				raise ex
			# finally:
				# self._process.terminate()
		else:
			raise DryRunException()

	def ReadUntilBoundary(self, indent=0):
		__indent = "  " * indent
		if (self._iterator is None):
			self._iterator = iter(self.GetReader())

		for line in self._iterator:
			print(__indent + line)
			if (self._pyIPCMI_BOUNDARY in line):
				break
		self.LogDebug("Quartus II is ready")

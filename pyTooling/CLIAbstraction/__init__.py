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
# Copyright 2017-2023 Patrick Lehmann - Bötzingen, Germany                                                             #
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
"""Basic abstraction layer for executables."""
__author__ =    "Patrick Lehmann"
__email__ =     "Paebbels@gmail.com"
__copyright__ = "2014-2023, Patrick Lehmann"
__license__ =   "Apache License, Version 2.0"
__version__ =   "0.4.1"
__keywords__ =  ["abstract", "executable", "cli", "cli arguments"]

from pathlib              import Path
from platform             import system
from shutil               import which as shutil_which
from subprocess           import (
	Popen		as Subprocess_Popen,
	PIPE		as Subprocess_Pipe,
	STDOUT	as Subprocess_StdOut
)
from typing import Dict, Optional, ClassVar, Type, List, Tuple, Iterator, Generator

from pyTooling.Decorators import export
from pyTooling.Exceptions import ExceptionBase, PlatformNotSupportedException
from pyAttributes         import Attribute

from .Argument import (
	CommandLineArgument, ExecutableArgument,
	NamedAndValuedArgument, ValuedArgument, PathArgument,
	PathListArgument, NamedTupledArgument
)
from .ValuedFlag import ValuedFlag


@export
class CLIAbstractionException(ExceptionBase):
	pass


@export
class DryRunException(CLIAbstractionException):
	"""This exception is raised if an executable is launched while in dry-run mode."""


@export
class CLIArgument(Attribute):
	"""An attribute to annotate nested classes as an CLI argument."""


@export
class Program:
	"""Represent a simple command line interface (CLI) executable (program or script)."""

	_platform:         str                                                            #: Current platform the executable runs on (Linux, Windows, ...)
	_executableNames:  ClassVar[Dict[str, str]]                                       #: Dictionary of platform specific executable names.
	_executablePath:   Path                                                           #: The path to the executable (binary, script, ...).
	_dryRun:           bool                                                           #: True, if program shall run in *dry-run mode*.
	__cliOptions__:    ClassVar[Dict[Type[CommandLineArgument], int]]                 #: List of all possible CLI options.
	__cliParameters__: Dict[Type[CommandLineArgument], Optional[CommandLineArgument]] #: List of all CLI parameters (used CLI options).

	def __init_subclass__(cls, *args, **kwargs):
		"""
		Whenever a subclass is derived from :class:``Program``, all nested classes declared within ``Program`` and which are
		marked with pyAttribute ``CLIOption`` are collected and then listed in the ``__cliOptions__`` dictionary.
		"""
		super().__init_subclass__(*args, **kwargs)

		# register all available CLI options (nested classes marked with attribute 'CLIOption')
		cls.__cliOptions__: Dict[Type[CommandLineArgument], int] = {}
		order: int = 0
		for option in CLIArgument.GetClasses(scope=cls):
			cls.__cliOptions__[option] = order
			order += 1

	def __init__(self, executablePath: Path = None, binaryDirectoryPath: Path = None, dryRun: bool = False):
		self._platform =    system()
		self._dryRun =      dryRun

		if executablePath is not None:
			if isinstance(executablePath, Path):
				if not executablePath.exists():
					if dryRun:
						self.LogDryRun(f"File check for '{executablePath}' failed. [SKIPPING]")
					else:
						raise CLIAbstractionException(f"Program '{executablePath}' not found.") from FileNotFoundError(executablePath)
			else:
				raise TypeError(f"Parameter 'executablePath' is not of type 'Path'.")
		elif binaryDirectoryPath is not None:
			if isinstance(binaryDirectoryPath, Path):
				if not binaryDirectoryPath.exists():
					if dryRun:
						self.LogDryRun(f"Directory check for '{binaryDirectoryPath}' failed. [SKIPPING]")
					else:
						raise CLIAbstractionException(f"Binary directory '{binaryDirectoryPath}' not found.") from FileNotFoundError(binaryDirectoryPath)

				try:
					executablePath = binaryDirectoryPath / self._executableNames[self._platform]
				except KeyError:
					raise CLIAbstractionException(f"Program is not supported on platform '{self._platform}'.") from PlatformNotSupportedException(self._platform)

				if not executablePath.exists():
					if dryRun:
						self.LogDryRun(f"File check for '{executablePath}' failed. [SKIPPING]")
					else:
						raise CLIAbstractionException(f"Program '{executablePath}' not found.") from FileNotFoundError(executablePath)
			else:
				raise TypeError(f"Parameter 'binaryDirectoryPath' is not of type 'Path'.")
		else:
			try:
				executablePath = Path(self._executableNames[self._platform])
			except KeyError:
				raise CLIAbstractionException(f"Program is not supported on platform '{self._platform}'.") from PlatformNotSupportedException(self._platform)

			resolvedExecutable = shutil_which(str(executablePath))
			if dryRun:
				if resolvedExecutable is None:
					pass
					# XXX: log executable not found in PATH
					# self.LogDryRun(f"Which '{executablePath}' failed. [SKIPPING]")
				else:
					fullExecutablePath = Path(resolvedExecutable)
					if not fullExecutablePath.exists():
						pass
						# XXX: log executable not found
						# self.LogDryRun(f"File check for '{fullExecutablePath}' failed. [SKIPPING]")
			else:
				if resolvedExecutable is None:
					raise CLIAbstractionException(f"Program could not be found in PATH.") from FileNotFoundError(executablePath)

				fullExecutablePath = Path(resolvedExecutable)
				if not fullExecutablePath.exists():
					raise CLIAbstractionException(f"Program '{fullExecutablePath}' not found.") from FileNotFoundError(fullExecutablePath)

			# TODO: log found executable in PATH
			# TODO: check if found executable has execute permissions
			# raise ValueError(f"Neither parameter 'executablePath' nor 'binaryDirectoryPath' was set.")

		self._executablePath = executablePath
		self.__cliParameters__ = {}

	@staticmethod
	def _NeedsParameterInitialization(key):
		return issubclass(key, (ValuedFlag, ValuedArgument, NamedAndValuedArgument, NamedTupledArgument, PathArgument, PathListArgument))

	def __getitem__(self, key):
		"""Access to a CLI parameter by CLI option (key must be of type :class:`CommandLineArgument`), which is already used."""
		if not issubclass(key, CommandLineArgument):
			raise TypeError(f"Key '{key}' is not a subclass of 'CommandLineArgument'.")

		# TODO: is nested check
		return self.__cliParameters__[key]

	def __setitem__(self, key, value):
		if not issubclass(key, CommandLineArgument):
			raise TypeError(f"Key '{key}' is not a subclass of 'CommandLineArgument'.")
		elif key not in self.__cliOptions__:
			raise KeyError(f"Option '{key}' is not allowed on executable '{self.__class__.__name__}'")
		elif key in self.__cliParameters__:
			raise KeyError(f"Option '{key}' is already set to a value.")

		if self._NeedsParameterInitialization(key):
			self.__cliParameters__[key] = key(value)
		else:
			self.__cliParameters__[key] = key()

	@property
	def Path(self) -> Path:
		return self._executablePath

	def ToArgumentList(self) -> List[str]:
		result: List[str] = []

		result.append(str(self._executablePath))

		def predicate(item: Tuple[Type[CommandLineArgument], int]) -> int:
			return self.__cliOptions__[item[0]]

		for key, value in sorted(self.__cliParameters__.items(), key=predicate):
			param = value.AsArgument()
			if isinstance(param, str):
				result.append(param)
			elif isinstance(param, (Tuple, List)):
				result += param
			else:
				raise TypeError(f"")  # XXX: needs error message

		return result

	def __repr__(self):
		return "[" + ", ".join([f"\"{item}\"" for item in self.ToArgumentList()]) + "]"

	def __str__(self):
		return " ".join([f"\"{item}\"" for item in self.ToArgumentList()])


# @export
# class Environment:
# 	def __init__(self):
# 		self.Variables = {}


@export
class Executable(Program):  # (ILogable):
	"""Represent a CLI executable derived from :class:`Program`, that adds an abstraction of :class:`subprocess.Popen`."""

	_BOUNDARY = "====== BOUNDARY pyTooling.CLIAbstraction BOUNDARY ======"

	_environment: Dict[str, str] = None
	_process: Subprocess_Popen = None
	_iterator: Iterator = None

	def __init__(self, executablePath: Path = None, binaryDirectoryPath: Path = None, dryRun: bool = False): #, environment: Environment = None):
		super().__init__(executablePath, binaryDirectoryPath, dryRun)

	def StartProcess(self):
		# start child process

		if self._dryRun:
			self.LogDryRun(f"Start process: {self!r}")
			return

		if (self._environment is not None):
			envVariables = self._environment.Variables
		else:
			envVariables = None

		# FIXME: verbose log start process
		# FIXME: debug log - parameter list
		try:
			self._process = Subprocess_Popen(
				self.ToArgumentList(),
				stdin=Subprocess_Pipe,
				stdout=Subprocess_Pipe,
				stderr=Subprocess_StdOut,
				env=envVariables,
				universal_newlines=True,
				bufsize=256
			)
		except OSError as ex:
			raise CLIAbstractionException(f"Error while launching a process for '{self._executablePath}'.") from ex

	def Send(self, line: str, end: str="\n") -> None:
		try:
			self._process.stdin.write(line + end)
			self._process.stdin.flush()
		except Exception as ex:
			raise CLIAbstractionException(f"") from ex     # XXX: need error message

	# This is TCL specific ...
	# def SendBoundary(self):
	# 	self.Send("puts \"{0}\"".format(self._pyIPCMI_BOUNDARY))

	def GetLineReader(self) -> Generator[str, None, None]:
		if self._dryRun:
			raise DryRunException()  # XXX: needs a message

		try:
			for line in iter(self._process.stdout.readline, ""):     # FIXME: can it be improved?
				yield line[:-1]
		except Exception as ex:
			raise CLIAbstractionException() from ex     # XXX: need error message
		# finally:
			# self._process.terminate()

	def Terminate(self):
		self._process.terminate()

	# This is TCL specific
	# def ReadUntilBoundary(self, indent=0):
	# 	__indent = "  " * indent
	# 	if (self._iterator is None):
	# 		self._iterator = iter(self.GetReader())
	#
	# 	for line in self._iterator:
	# 		print(__indent + line)
	# 		if (self._pyIPCMI_BOUNDARY in line):
	# 			break
	# 	self.LogDebug("Quartus II is ready")

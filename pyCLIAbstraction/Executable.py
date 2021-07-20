# =============================================================================
#                ____ _     ___    _    _         _                  _   _
#   _ __  _   _ / ___| |   |_ _|  / \  | |__  ___| |_ _ __ __ _  ___| |_(_) ___  _ __
#  | '_ \| | | | |   | |    | |  / _ \ | '_ \/ __| __| '__/ _` |/ __| __| |/ _ \| '_ \
#  | |_) | |_| | |___| |___ | | / ___ \| |_) \__ \ |_| | | (_| | (__| |_| | (_) | | | |
#  | .__/ \__, |\____|_____|___/_/   \_\_.__/|___/\__|_|  \__,_|\___|\__|_|\___/|_| |_|
#  |_|    |___/
# =============================================================================
# Authors:            Patrick Lehmann
#
# Python Module:      Basic abstraction layer for executables.
#
# License:
# ============================================================================
# Copyright 2017-2021 Patrick Lehmann - Bötzingen, Germany
# Copyright 2007-2016 Technische Universität Dresden - Germany
#                     Chair of VLSI-Design, Diagnostics and Architecture
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#		http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0
# ============================================================================
#
# load dependencies
from pathlib                  import Path
from subprocess               import Popen				as Subprocess_Popen
from subprocess               import PIPE					as Subprocess_Pipe
from subprocess               import STDOUT				as Subprocess_StdOut

from pydecor                  import export

# __all__ = __api__
from pyCLIAbstraction import ExecutableException, DryRunException


@export
class CommandLineArgumentList(list):
	"""Represent a list of all available commands, flags and switch of an executable."""

	def __init__(self, *args):
		super().__init__()
		for arg in args:
			self.append(arg)

	def __getitem__(self, key):
		i = self.index(key)
		return super().__getitem__(i).Value

	def __setitem__(self, key, value):
		i = self.index(key)
		super().__getitem__(i).Value = value

	def __delitem__(self, key):
		i = self.index(key)
		super().__getitem__(i).Value = None

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
class Executable: # (ILogable):
	"""Represent an executable."""
	_pyIPCMI_BOUNDARY = "====== pyIPCMI BOUNDARY ======"

	def __init__(self, platform : str, dryrun : bool, executablePath : Path, environment : Environment = None): #, logger : Logger =None):
#		super().__init__(logger)

		self._platform =    platform
		self._dryrun =      dryrun
		self._environment = environment #if (environment is not None) else Environment()
		self._process =     None

		if isinstance(executablePath, str):
			executablePath = Path(executablePath)
		elif (not isinstance(executablePath, Path)):
			raise ValueError("Parameter 'executablePath' is not of type str or Path.")

		if (not executablePath.exists()):
			if dryrun:
				self.LogDryRun("File check for '{0!s}' failed. [SKIPPING]".format(executablePath))
			else:
				raise ExecutableException("Executable '{0!s}' not found.".format(executablePath)) from FileNotFoundError(str(executablePath))

		# prepend the executable
		self._executablePath =    executablePath
		self._iterator =          None

	@property
	def Path(self):
		return self._executablePath

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

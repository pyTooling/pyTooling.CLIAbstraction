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
from pydecor      import export
from pyExceptions import ExceptionBase


@export
class ExecutableException(ExceptionBase):
	"""This exception is raised by all executable abstraction classes."""
	def __init__(self, message=""):
		super().__init__(message)
		self.message = message


@export
class DryRunException(ExecutableException):
	"""This exception is raised if a simulator runs in dry-run mode."""

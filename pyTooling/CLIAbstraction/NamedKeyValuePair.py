from typing import Union, Iterable, ClassVar

from pyTooling.Decorators import export

from pyTooling.CLIAbstraction import NamedAndValuedArgument


class NamedKeyValuePairsArgument(NamedAndValuedArgument):
	"""Base-class for all command line arguments with a name and a key-value pair."""
	_key: str

	def __init__(self, key: str, value: str):
		super().__init__(value)
		if key is None:
			raise ValueError(f"Parameter 'key' is None.")

		self._key = key

	@property
	def Key(self) -> str:
		return self._key

	@Key.setter
	def Key(self, key: str) -> None:
		if key is None:
			raise ValueError(f"Key to set is None.")

		self._key = key

	def AsArgument(self) -> Union[str, Iterable[str]]:
		if self._name is None:
			raise ValueError(f"")  # XXX: add message
		if self._key is None:
			raise ValueError(f"")  # XXX: add message
		if self._value is None:
			raise ValueError(f"")  # XXX: add message

		return self._pattern.format(self._name, self._key, self._value)

	def __repr__(self) -> str:
		return f"\"{self.AsArgument()}\""

	__str__ = __repr__


@export
class NamedKeyValueFlagArgument(NamedKeyValuePairsArgument):
	"""
	Class and base-class for all NamedKeyValueFlagArgument classes, which represents a flag with a name and a key-value pair.

	Example: ``DDEBUG=TRUE``
	"""
	_pattern: ClassVar[str]

	def __init_subclass__(cls, *args, pattern: str = "{0}{1}={2}", **kwargs):
		super().__init_subclass__(*args, **kwargs)
		cls._pattern = pattern


@export
class ShortNamedKeyValueFlagArgument(NamedKeyValueFlagArgument, pattern="-{0}{1}={2}"):
	"""Represents a :py:class:`NamedKeyValueFlagArgument` with a single dash in front of the switch name.

	Example: ``-DDEBUG=TRUE``
	"""
	def __init_subclass__(cls, *args, pattern="-{0}{1}={2}", **kwargs):
		kwargs["pattern"] = pattern
		super().__init_subclass__(*args, **kwargs)


@export
class LongNamedKeyValueFlagArgument(NamedKeyValueFlagArgument, pattern="--{0}{1}={2}"):
	"""Represents a :py:class:`NamedKeyValueFlagArgument` with a double dash in front of the switch name.

	Example: ``--DDEBUG=TRUE``
	"""
	def __init_subclass__(cls, *args, pattern="--{0}{1}={2}", **kwargs):
		kwargs["pattern"] = pattern
		super().__init_subclass__(*args, **kwargs)

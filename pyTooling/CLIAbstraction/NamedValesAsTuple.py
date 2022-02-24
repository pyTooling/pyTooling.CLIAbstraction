from typing import ClassVar, Union, Iterable

from pyTooling.Decorators import export

from pyTooling.CLIAbstraction.Argument import NamedArgument


@export
class TupleArgument(NamedArgument):
	"""Class and base-class for all TupleArgument classes, which represents a switch with separate data.

	A tuple switch is a command line argument followed by a separate value. Name and value are passed as
	two arguments to the executable.

	Example: ``width 100``
	"""
	_valuePattern: ClassVar[str]
	_value: str

	def __init_subclass__(cls, *args, valuePattern: str = "{0}", **kwargs):
		super().__init_subclass__(*args, **kwargs)
		cls._valuePattern = valuePattern

	def __init__(self, value: str):
		if value is None:
			raise ValueError(f"")  # XXX: add message

		self._value = value

	@property
	def Value(self) -> str:
		return self._value

	@Value.setter
	def Value(self, value: str) -> None:
		if value is None:
			raise ValueError(f"")  # XXX: add message

		self._value = value

	def AsArgument(self) -> Union[str, Iterable[str]]:
		if self._name is None:
			raise ValueError(f"")  # XXX: add message

		return (
			self._pattern.format(self._name),
			self._valuePattern.format(self._value)
		)

	def __repr__(self) -> str:
		return ", ".join([f"\"{item}\"" for item in self.AsArgument()])

	def __str__(self) -> str:
		return " ".join([f"\"{item}\"" for item in self.AsArgument()])


@export
class ShortTupleArgument(TupleArgument, pattern="-{0}"):
	"""Represents a :py:class:`TupleArgument` with a single dash in front of the switch name.

	Example: ``-file file1.txt``
	"""
	def __init_subclass__(cls, *args, pattern="-{0}", **kwargs):
		kwargs["pattern"] = pattern
		super().__init_subclass__(*args, **kwargs)


@export
class LongTupleArgument(TupleArgument, pattern="--{0}"):
	"""Represents a :py:class:`TupleArgument` with a double dash in front of the switch name.

	Example: ``--file file1.txt``
	"""
	def __init_subclass__(cls, *args, pattern="--{0}", **kwargs):
		kwargs["pattern"] = pattern
		super().__init_subclass__(*args, **kwargs)


@export
class WindowsTupleArgument(TupleArgument, pattern="/{0}"):
	"""Represents a :py:class:`TupleArgument` with a single slash in front of the switch name.

	Example: ``/file file1.txt``
	"""
	def __init_subclass__(cls, *args, pattern="/{0}", **kwargs):
		kwargs["pattern"] = pattern
		super().__init_subclass__(*args, **kwargs)

Program
#######

The :class:`~pyTooling.CLIAbstraction.Program` represents an executable command line program. It offers an interface to
define and enabled command line arguments.

**Features:**

* Abstract a command line program as a Python class.
* Abstract arguments of that program as nested classes derived from pre-defined Argument classes. |br|
  See :ref:`ARG`.
* Construct a list of arguments in correct order and with proper escaping ready to be used with e.g. :mod:`subprocess`.

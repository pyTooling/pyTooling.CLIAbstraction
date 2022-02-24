Executable
##########

The :class:`~pyTooling.CLIAbstraction.Executable` is derived from :class:`~pyTooling.CLIAbstraction.Program`, which
represents an executable command line program. In addition, it offers an API to :class:`subprocess.Popen`, so an
abstracted command line program can be launched.

**Features:**

* Launch an abstracted CLI program using :class:`subproess.Popen`.
* Setup and modify the environment for the launched program.
* Provide a line-based STDOUT reader as generator.

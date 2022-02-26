.. include:: shields.inc

.. image:: _static/logo_on_light.svg
   :height: 90 px
   :align: center
   :target: https://GitHub.com/pyTooling/pyTooling.CLIAbstraction

.. raw:: html

    <br>

.. raw:: latex

   \part{Introduction}

.. only:: html

   |  |SHIELD:svg:CLIAbstraction-github| |SHIELD:svg:CLIAbstraction-src-license| |SHIELD:svg:CLIAbstraction-ghp-doc| |SHIELD:svg:CLIAbstraction-doc-license|
   |  |SHIELD:svg:CLIAbstraction-pypi-tag| |SHIELD:svg:CLIAbstraction-pypi-status| |SHIELD:svg:CLIAbstraction-pypi-python|
   |  |SHIELD:svg:CLIAbstraction-gha-test| |SHIELD:svg:CLIAbstraction-lib-status| |SHIELD:svg:CLIAbstraction-codacy-quality| |SHIELD:svg:CLIAbstraction-codacy-coverage| |SHIELD:svg:CLIAbstraction-codecov-coverage|

.. Disabled shields: |SHIELD:svg:CLIAbstraction-lib-dep| |SHIELD:svg:CLIAbstraction-req-status| |SHIELD:svg:CLIAbstraction-lib-rank|

.. only:: latex

   |SHIELD:png:CLIAbstraction-github| |SHIELD:png:CLIAbstraction-src-license| |SHIELD:png:CLIAbstraction-ghp-doc| |SHIELD:png:CLIAbstraction-doc-license|
   |SHIELD:png:CLIAbstraction-pypi-tag| |SHIELD:png:CLIAbstraction-pypi-status| |SHIELD:png:CLIAbstraction-pypi-python|
   |SHIELD:png:CLIAbstraction-gha-test| |SHIELD:png:CLIAbstraction-lib-status| |SHIELD:png:CLIAbstraction-codacy-quality| |SHIELD:png:CLIAbstraction-codacy-coverage| |SHIELD:png:CLIAbstraction-codecov-coverage|

.. Disabled shields: |SHIELD:png:CLIAbstraction-lib-dep| |SHIELD:png:CLIAbstraction-req-status| |SHIELD:png:CLIAbstraction-lib-rank|

--------------------------------------------------------------------------------

The pyTooling.CLIAbstraction Documentation
##########################################

pyTooling.CLIAbstraction is an abstraction layer and wrapper for command line programs, so they can be used easily in
Python. All parameters like ``--value=42`` are implemented as argument classes on the executable.


.. _goals:

Main Goals
**********

* Offer access to CLI programs as Python classes.
* Abstract CLI arguments (a.k.a. parameter, option, flag, ...) as members on such a Python class.
* Derive program variants from existing programs.
* Assemble parameters in list format for handover to :class:`subprocess.Popen` with proper escaping and quoting.
* Launch a program with :class:`~subprocess.Popen` and hide the complexity of Popen.
* Get a generator object for line-by-line output reading to enable postprocessing of outputs.


.. _usecase:

Use Cases
*********

* Wrap command line interfaces of EDA tools (Electronic Design Automation) in Python classes.


Examples
********

The following example implements a portion of the ``git`` program and its ``--version`` argument.

.. rubric:: Program Definition

.. code-block:: Python
   :name: HOME:Example
   :caption: Git program defining --version argument.

   # Definition
   # ======================================
   class Git(Executable):
     _executableNames = {
       "Windows": "git.exe",
       "Linux": "git",
       "Darwin": "git"
     }

     @CLIArgument()
     class FlagVerbose(LongFlag, name="verbose"):
       """Print verbose messages."""

     @CLIArgument()
     class CommandCommit(CommandArgument, name="commit"):
       """Command to commit staged files."""

     @CLIArgument()
     class ValueCommitMessage(ShortTupleArgument, name="m"):
       """Specify the commit message."""

     def GetCommitTool(self):
       """Derive a new program from a configured program."""
       tool = self.__class__(executablePath=self._executablePath)
       tool[tool.CommandCommit] = True
       self._CopyParameters(tool)

       return tool

   # Usage
   # ======================================
   # Create a program instance and set common parameters.
   git = Git()
   git[git.FlagVerbose] = True

   # Derive a variant of that pre-configured program.
   commit = git.getCommitTool()
   commit[commit.ValueCommitMessage] = "Bumped dependencies."

   # Launch the program and parse outputs line-by-line.
   commit.StartProcess()
   for line in commit.GetLineReader():
     print(line)


Consumers
*********

* 🚧 pyEDAA.CLITool


.. _news:

News
****

.. only:: html

   Feb. 2022 - Major Update
   ========================

.. only:: latex

   .. rubric:: Major Update

* Reworked names of Argument classes.
* Added missing argument formats like PathArgument.
* Added more unit tests and improved code-coverage.
* Added doc-strings and extended documentation pages.


.. only:: html

   Dec. 2021 - Extracted CLIAbstraction from pyIPCMI
   =================================================

.. only:: latex

   .. rubric:: Extracted CLIAbstraction from pyIPCMI

* The CLI abstraction has been extracted from `pyIPCMI <https://GitHub.com/Paebbels/pyIPCMI>`__.


.. _contributors:

Contributors
************

* `Patrick Lehmann <https://GitHub.com/Paebbels>`__ (Maintainer)
* `and more... <https://GitHub.com/pyTooling/pyTooling.CLIAbstraction/graphs/contributors>`__


.. _license:

License
*******

.. only:: html

   This Python package (source code) is licensed under `Apache License 2.0 <Code-License.html>`__. |br|
   The accompanying documentation is licensed under `Creative Commons - Attribution 4.0 (CC-BY 4.0) <Doc-License.html>`__.

.. only:: latex

   This Python package (source code) is licensed under **Apache License 2.0**. |br|
   The accompanying documentation is licensed under **Creative Commons - Attribution 4.0 (CC-BY 4.0)**.

------------------------------------

.. |docdate| date:: %d.%b %Y - %H:%M

.. only:: html

   This document was generated on |docdate|.


.. toctree::
   :hidden:

   Part of pyTooling ➚ <https://pyTooling.github.io/>


.. toctree::
   :caption: Introduction
   :hidden:

   Installation
   Dependency


.. raw:: latex

   \part{Main Documentation}

.. toctree::
   :caption: Main Documentation
   :hidden:

   Tutorial
   Program
   Executable
   Arguments


.. raw:: latex

   \part{References}

.. toctree::
   :caption: References
   :hidden:

   pyTooling.CLIAbstraction/index


.. raw:: latex

   \part{Appendix}

.. toctree::
   :caption: Appendix
   :hidden:

   Coverage Report ➚ <coverage/index>
   Static Type Check Report ➚ <typing/index>
   License
   Doc-License
   Glossary
   genindex
   py-modindex

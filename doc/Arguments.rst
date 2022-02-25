.. _ARG:

Arguments
#########

.. _ARG:Overview:

Overview
********

.. mermaid::

   graph LR;
     CLA[CommandLineArgument]
     style CLA stroke-dasharray: 5 5

     EA[ExecutableArgument]

     NA[NamedArgument]
     style NA stroke-dasharray: 5 5

     VA[ValuedArgument]
     style VA stroke-dasharray: 5 5

     NVA[NamedAndValuedArgument]
     style NVA stroke-dasharray: 5 5

     NTA[NamedTupledArgument]
     style NTA stroke-dasharray: 5 5

     NKVPA[NamedKeyValuePairsArgument]
     style NKVPA stroke-dasharray: 5 5

     CLA ----> EA
     CLA --> NA
     CLA --> VA
     NA --> NVA
     VA --> NVA
     NA --> NTA
     VA --> NTA
     NA --> NKVPA
     VA --> NKVPA

     CA["<b>CommandArgument</b><br/><div style='font-family: monospace'>command</div>"]
     FA[FlagArgument]
     style FA stroke-dasharray: 5 5

     NA ---> CA
     NA ---> FA

     SA["<b>StringArgument</b><br/><div style='font-family: monospace'>value</div>"]
     SLA["<b>StringListArgument</b><br/><div style='font-family: monospace'>value1 value2</div>"]
     PA["<b>PathArgument</b><br/><div style='font-family: monospace'>file1.txt</div>"]
     PLA["<b>PathListArgument</b><br/><div style='font-family: monospace'>file1.txt file2.txt</div>"]

     VA ---> SA
     VA ---> SLA
     VA ---> PA
     VA ---> PLA

     NVFA["<b>NamedAndValuedFlagArgument</b><br/><div style='font-family: monospace'>output=file.txt</div>"]
     style NVFA stroke-dasharray: 5 5
     NOVFA["<b>NamedAndOptionalValuedFlagArgument</b><br/><div style='font-family: monospace'>output=file.txt</div>"]
     style NOVFA stroke-dasharray: 5 5

     NVA --> NVFA
     NVA --> NOVFA


.. _ARG:WithPrefix:

Without Prefix Character(s)
***************************

+--------------------------+--------------------------------+-------------------------------------------------------------------+
| **RAW Format**           | **Examples**                   | **Argument Class**                                                |
+--------------------------+--------------------------------+-------------------------------------------------------------------+
| ``executable``           | ``prog``                       | :class:`~pyTooling.CLIAbstraction.Argument.ExecutableArgument`    |
+--------------------------+--------------------------------+-------------------------------------------------------------------+
| ``--``                   | ``prog -option -- file1.txt``  | :class:`~pyTooling.CLIAbstraction.Argument.DelimiterArgument`     |
+--------------------------+--------------------------------+-------------------------------------------------------------------+
| ``command``              | ``prog help``                  | :class:`~pyTooling.CLIAbstraction.Command.CommandArgument`        |
+--------------------------+--------------------------------+-------------------------------------------------------------------+
| ``string``               | ``prog value``                 | :class:`~pyTooling.CLIAbstraction.Argument.StringArgument`        |
+--------------------------+--------------------------------+-------------------------------------------------------------------+
| ``string1`` ``string2``  | ``prog value1 value2``         | :class:`~pyTooling.CLIAbstraction.Argument.StringListArgument`    |
+--------------------------+--------------------------------+-------------------------------------------------------------------+
| ``path``                 | ``prog file1.txt``             | :class:`~pyTooling.CLIAbstraction.Argument.PathArgument`          |
+--------------------------+--------------------------------+-------------------------------------------------------------------+
| ``path1`` ``path2``      | ``prog File1.log File1.log``   | :class:`~pyTooling.CLIAbstraction.Argument.PathListArgument`      |
+--------------------------+--------------------------------+-------------------------------------------------------------------+

Executable
==========

An executable argument represents a program/executable. The internal value is a :class:`Path` object.


Command
=======

.. TODO:: Write documentation.


String
======

.. TODO:: Write documentation.


List of Strings
===============

.. TODO:: Write documentation.


Path
====

.. TODO:: Write documentation.


List of Paths
=============

.. TODO:: Write documentation.


.. _ARG:WithoutPrefix:

With Prefix Character(s)
************************

Commonly used prefix characters are: single and double dash, single slash, or plus character(s).

+-----------------------------------+-------------------------------------+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Single Dash Argument Format**   | **Double Dash Argument Format**     | **Single Slash Argument Format**  | **Argument Class**                                                                                                                                                                                                   |
+-----------------------------------+-------------------------------------+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``-command``                      | ``--command``                       | ``/command``                      | :class:`~pyTooling.CLIAbstraction.ShortCommandArgument`            |br| :class:`~pyTooling.CLIAbstraction.LongCommandArgument`            |br| :class:`~pyTooling.CLIAbstraction.WindowsCommandArgument`             |
+-----------------------------------+-------------------------------------+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``-flag``                         | ``--flag``                          | ``/flag``                         | :class:`~pyTooling.CLIAbstraction.ShortFlag`                       |br| :class:`~pyTooling.CLIAbstraction.LongFlag`                       |br| :class:`~pyTooling.CLIAbstraction.WindowsFlag`                        |
+-----------------------------------+-------------------------------------+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``-flag=value``                   | ``--flag=value``                    | ``/flag=value``                   | :class:`~pyTooling.CLIAbstraction.ShortValuedFlagArgument`         |br| :class:`~pyTooling.CLIAbstraction.LongValuedFlagArgument`         |br| :class:`~pyTooling.CLIAbstraction.WindowsValuedFlagArgument`          |
+-----------------------------------+-------------------------------------+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``-flag`` |br| ``-no-flag``       | ``--flag`` |br| ``--no-flag``       | ``/flag`` |br| ``/no-flag``       | :class:`~pyTooling.CLIAbstraction.ShortOptionalValuedFlagArgument` |br| :class:`~pyTooling.CLIAbstraction.LongOptionalValuedFlagArgument` |br| :class:`~pyTooling.CLIAbstraction.WindowsOptionalValuedFlagArgument`  |
+-----------------------------------+-------------------------------------+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``-flag`` |br| ``-flag=value``    | ``--flag`` |br| ``--flag=value``    | ``/flag`` |br| ``/flag=value``    | :class:`~pyTooling.CLIAbstraction.ShortOptionalValuedFlagArgument` |br| :class:`~pyTooling.CLIAbstraction.LongOptionalValuedFlagArgument` |br| :class:`~pyTooling.CLIAbstraction.WindowsOptionalValuedFlagArgument`  |
+-----------------------------------+-------------------------------------+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``-flag=value1 -flag=value2``     | ``--flag=value1 --flag=value2``     | ``/flag=value1 /flag=value2``     | :class:`~pyTooling.CLIAbstraction.ShortValuedFlagListArgument`     |br| :class:`~pyTooling.CLIAbstraction.LongValuedFlagListArgument`     |br| :class:`~pyTooling.CLIAbstraction.WindowsValuedFlagListArgument`      |
+-----------------------------------+-------------------------------------+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``-flag value``                   | ``--flag value``                    | ``/flag value``                   | :class:`~pyTooling.CLIAbstraction.ShortTupleArgument`              |br| :class:`~pyTooling.CLIAbstraction.LongTupleArgument`              |br| :class:`~pyTooling.CLIAbstraction.WindowsTupleArgument`               |
+-----------------------------------+-------------------------------------+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


Command
=======

.. TODO:: Write documentation.

.. mermaid::

   graph LR;
     CLA[CommandLineArgument]
     style CLA stroke-dasharray: 5 5
     CLA --> NA[NamedArgument]
     style NA stroke-dasharray: 5 5
     NA --> CA["<b>CommandArgument</b><br/><div style='font-family: monospace'>command</div>"];
     CA --> SCA["<b>ShortCommandArgument</b><br/><div style='font-family: monospace'>-command</div>"];
     CA --> LCA["<b>LongCommandArgument</b><br/><div style='font-family: monospace'>--command</div>"];
     CA --> WCA["<b>WindowsCommandArgument</b><br/><div style='font-family: monospace'>/command</div>"];


Flag
====

A flag is a command line argument that is either present or not. If present that argument is said to be activated or
true.

3 variants are predefined with prefixes ``-``, ``--`` and ``/``.

.. rubric:: Variants

.. mermaid::

   graph LR;
     CLA[CommandLineArgument]
     style CLA stroke-dasharray: 5 5
     CLA --> NA[NamedArgument]
     style NA stroke-dasharray: 5 5
     NA --> FA[FlagArgument]
     style FA stroke-dasharray: 5 5
     FA --> SFA["<b>ShortFlagArgument</b><br/><div style='font-family: monospace'>-flag</div>"]
     FA --> LFA["<b>LongFlagArgument</b><br/><div style='font-family: monospace'>--flag</div>"]
     FA --> WFA["<b>WindowsFlagArgument</b><br/><div style='font-family: monospace'>/flag</div>"]


Flag with Value
===============

.. TODO:: Write documentation.


Boolean Flag
============

.. TODO:: Write documentation.


Flag with Optional Value
========================

.. TODO:: Write documentation.


List of Flags with Value
========================

.. TODO:: Write documentation.


Flag with Value as a Tuple
==========================

.. TODO:: Write documentation.

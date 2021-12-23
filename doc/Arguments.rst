Arguments
#########

.. mermaid::

   graph LR;
     CLA[CommandLineArgument] ----> EA[ExecutableArgument];
     CLA --> NCLA[NamedCommandLineArgument];
     NCLA ---> FA[FlagArgument];
     FA --> SFA[ShortFlagArgument];
     FA --> LFA[LongFlagArgument];
     FA --> WFA[WindowsFlagArgument];
     CLA ---> VCLA[ValuedCommandLineArgument];
     VCLA --> SA[StringArgument];
     NCLA ---> CA[CommandArgument];
     CA --> SCA[ShortCommandArgument];
     CA --> LCA[LongCommandArgument];
     CA --> WCA[WindowsCommandArgument];
     NCLA --> NVCLA[NameValuedCommandLineArgument];
     NVCLA --> VFA[ValuedFlagArgument];
     VFA --> SVFA[ShortValuedFlagArgument];
     VFA --> LVFA[LongValuedFlagArgument];
     VFA --> WVFA[WindowsValuedFlagArgument];
     NVCLA --> OVFA[OptionalValuedFlagArgument];
     OVFA --> SOVFA[ShortOptionalValuedFlagArgument];
     OVFA --> LOVFA[LongOptionalValuedFlagArgument];
     OVFA --> WOVFA[WindowsOptionalValuedFlagArgument];
     NCLA --> NTCLA[NamedTupledCommandLineArgument];
     NTCLA --> TA[TupleArgument];
     TA --> STA[ShortTupleArgument];
     TA --> LTA[LongTupleArgument];
     TA --> WTA[WindowsTupleArgument];


+----------------------+-----------------------------------------------------+------------------------------------------------------------------------+
| **Format**           | **Example**                                         | **Argument Class**                                                     |
+======================+=====================================================+========================================================================+
| ``executable``       | ``git``                                             | :class:`~pyTooling.CLIAbstraction.ExecutableArgument`                  |
+----------------------+-----------------------------------------------------+------------------------------------------------------------------------+
| ``command``          | ``git help``                                        | :class:`~pyTooling.CLIAbstraction.CommandArgument`                     |
+----------------------+-----------------------------------------------------+------------------------------------------------------------------------+
| ``-command``         | ``git -h``                                          | :class:`~pyTooling.CLIAbstraction.ShortCommandArgument`                |
+----------------------+-----------------------------------------------------+------------------------------------------------------------------------+
| ``--command``        | ``git --help``                                      | :class:`~pyTooling.CLIAbstraction.LongCommandArgument`                 |
+----------------------+-----------------------------------------------------+------------------------------------------------------------------------+
| ``/command``         | ``git /help``                                       | :class:`~pyTooling.CLIAbstraction.WindowsCommandArgument`              |
+----------------------+-----------------------------------------------------+------------------------------------------------------------------------+
| ``value``            | ``git value``                                       | :class:`~pyTooling.CLIAbstraction.StringArgument`                      |
+----------------------+-----------------------------------------------------+------------------------------------------------------------------------+
|                      | ``git value1 value2``                               | :class:`~pyTooling.CLIAbstraction.StringListArgument`                  |
+----------------------+-----------------------------------------------------+------------------------------------------------------------------------+
|                      | ``git file1.txt``                                   | :class:`~pyTooling.CLIAbstraction.PathArgument`                        |
+----------------------+-----------------------------------------------------+------------------------------------------------------------------------+
| ``-flag``            | ``git -v``                                          | :class:`~pyTooling.CLIAbstraction.ShortFlagArgument`                   |
+----------------------+-----------------------------------------------------+------------------------------------------------------------------------+
| ``--flag``           | ``git --version``                                   | :class:`~pyTooling.CLIAbstraction.LongFlagArgument`                    |
+----------------------+-----------------------------------------------------+------------------------------------------------------------------------+
| ``/flag``            | ``git /version``                                    | :class:`~pyTooling.CLIAbstraction.WindowsFlagArgument`                 |
+----------------------+-----------------------------------------------------+------------------------------------------------------------------------+
|                      |                                                     | :class:`~pyTooling.CLIAbstraction.ShortValuedFlagArgument`             |
+----------------------+-----------------------------------------------------+------------------------------------------------------------------------+
| ``--flag=value``     | ``exe --strategy=recursive``                        | :class:`~pyTooling.CLIAbstraction.LongValuedFlagArgument`              |
+----------------------+-----------------------------------------------------+------------------------------------------------------------------------+
|                      |                                                     | :class:`~pyTooling.CLIAbstraction.WindowsValuedFlagArgument`           |
+----------------------+-----------------------------------------------------+------------------------------------------------------------------------+
|                      |                                                     | :class:`~pyTooling.CLIAbstraction.ShortOptionalValuedFlagArgument`     |
+----------------------+-----------------------------------------------------+------------------------------------------------------------------------+
| ``--flag=value``     | ``exe --strategy=recursive``                        | :class:`~pyTooling.CLIAbstraction.LongOptionalValuedFlagArgument`      |
+----------------------+-----------------------------------------------------+------------------------------------------------------------------------+
|                      |                                                     | :class:`~pyTooling.CLIAbstraction.WindowsOptionalValuedFlagArgument`   |
+----------------------+-----------------------------------------------------+------------------------------------------------------------------------+
|                      |                                                     | :class:`~pyTooling.CLIAbstraction.ShortValuedFlagListArgument`         |
+----------------------+-----------------------------------------------------+------------------------------------------------------------------------+
| ``--flag=value``     | ``exe --strategy=recursive``                        | :class:`~pyTooling.CLIAbstraction.LongValuedFlagListArgument`          |
+----------------------+-----------------------------------------------------+------------------------------------------------------------------------+
|                      |                                                     | :class:`~pyTooling.CLIAbstraction.WindowsValuedFlagListArgument`       |
+----------------------+-----------------------------------------------------+------------------------------------------------------------------------+
|                      |                                                     | :class:`~pyTooling.CLIAbstraction.ShortTupleArgument`                  |
+----------------------+-----------------------------------------------------+------------------------------------------------------------------------+
| ``--flag=value``     | ``exe --strategy=recursive``                        | :class:`~pyTooling.CLIAbstraction.LongTupleArgument`                   |
+----------------------+-----------------------------------------------------+------------------------------------------------------------------------+
|                      |                                                     | :class:`~pyTooling.CLIAbstraction.WindowsTupleArgument`                |
+----------------------+-----------------------------------------------------+------------------------------------------------------------------------+

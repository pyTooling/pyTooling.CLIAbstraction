Arguments
#########

.. mermaid::

   graph LR;
     CLA[CommandLineArgument] ----> EA[ExecutableArgument];
     CLA --> NCLA[NamedCommandLineArgument];
     NCLA ---> FA[FlagArgument];
     FA --> SFA["<b>ShortFlagArgument</b><br/><div style='font-family: monospace'>-flag</div>"];
     FA --> LFA["<b>LongFlagArgument</b><br/><div style='font-family: monospace'>--flag</div>"];
     FA --> WFA["<b>WindowsFlagArgument</b><br/><div style='font-family: monospace'>/flag</div>"];
     CLA ---> VCLA[ValuedCommandLineArgument];
     VCLA --> SA["<b>StringArgument</b><br/><div style='font-family: monospace'>command</div>"];
     NCLA ---> CA["<b>CommandArgument</b><br/><div style='font-family: monospace'>command</div>"];
     CA --> SCA["<b>ShortCommandArgument</b><br/><div style='font-family: monospace'>-c</div>"];
     CA --> LCA["<b>LongCommandArgument</b><br/><div style='font-family: monospace'>--c</div>"];
     CA --> WCA["<b>WindowsCommandArgument</b><br/><div style='font-family: monospace'>/c</div>"];
     NCLA --> NVCLA[NameValuedCommandLineArgument];
     NVCLA --> VFA["<b>ValuedFlagArgument</b><br/><div style='font-family: monospace'>output=file.txt</div>"];
     VFA --> SVFA["<b>ShortValuedFlagArgument</b><br/><div style='font-family: monospace'>-output=file.txt</div>"];
     VFA --> LVFA["<b>LongValuedFlagArgument</b><br/><div style='font-family: monospace'>--output=file.txt</div>"];
     VFA --> WVFA["<b>WindowsValuedFlagArgument</b><br/><div style='font-family: monospace'>/output=file.txt</div>"];
     NVCLA --> OVFA[OptionalValuedFlagArgument];
     OVFA --> SOVFA["<b>ShortOptionalValuedFlagArgument</b><br/><div style='font-family: monospace'>-output</div><br/><div style='font-family: monospace'>-output=file.txt</div>"];
     OVFA --> LOVFA["<b>LongOptionalValuedFlagArgument</b><br/><div style='font-family: monospace'>--output</div><br/><div style='font-family: monospace'>--output=file.txt</div>"];
     OVFA --> WOVFA["<b>WindowsOptionalValuedFlagArgument</b><br/><div style='font-family: monospace'>/output</div><br/><div style='font-family: monospace'>/output=file.txt</div>"];
     NCLA --> NTCLA[NamedTupledCommandLineArgument];
     NTCLA --> TA[TupleArgument];
     TA --> STA["<b>ShortTupleArgument</b><br/><div style='font-family: monospace'>-output file.txt</div>"];
     TA --> LTA["<b>LongTupleArgument</b><br/><div style='font-family: monospace'>--output file.txt</div>"];
     TA --> WTA["<b>WindowsTupleArgument</b><br/><div style='font-family: monospace'>/output file.txt</div>"];


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

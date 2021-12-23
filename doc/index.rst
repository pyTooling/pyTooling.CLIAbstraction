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

   |  |SHIELD:svg:CLIAbstraction-github| |SHIELD:svg:CLIAbstraction-src-license| |SHIELD:svg:CLIAbstraction-ghp-doc| |SHIELD:svg:CLIAbstraction-doc-license| |SHIELD:svg:CLIAbstraction-gitter|
   |  |SHIELD:svg:CLIAbstraction-pypi-tag| |SHIELD:svg:CLIAbstraction-pypi-status| |SHIELD:svg:CLIAbstraction-pypi-python|
   |  |SHIELD:svg:CLIAbstraction-gha-test| |SHIELD:svg:CLIAbstraction-lib-status| |SHIELD:svg:CLIAbstraction-codacy-quality| |SHIELD:svg:CLIAbstraction-codacy-coverage| |SHIELD:svg:CLIAbstraction-codecov-coverage|

.. Disabled shields: |SHIELD:svg:CLIAbstraction-lib-dep| |SHIELD:svg:CLIAbstraction-req-status| |SHIELD:svg:CLIAbstraction-lib-rank|

.. only:: latex

   |SHIELD:png:CLIAbstraction-github| |SHIELD:png:CLIAbstraction-src-license| |SHIELD:png:CLIAbstraction-ghp-doc| |SHIELD:png:CLIAbstraction-doc-license| |SHIELD:svg:CLIAbstraction-gitter|
   |SHIELD:png:CLIAbstraction-pypi-tag| |SHIELD:png:CLIAbstraction-pypi-status| |SHIELD:png:CLIAbstraction-pypi-python|
   |SHIELD:png:CLIAbstraction-gha-test| |SHIELD:png:CLIAbstraction-lib-status| |SHIELD:png:CLIAbstraction-codacy-quality| |SHIELD:png:CLIAbstraction-codacy-coverage| |SHIELD:png:CLIAbstraction-codecov-coverage|

.. Disabled shields: |SHIELD:png:CLIAbstraction-lib-dep| |SHIELD:png:CLIAbstraction-req-status| |SHIELD:png:CLIAbstraction-lib-rank|

--------------------------------------------------------------------------------

The pyTooling.CLIAbstraction Documentation
##########################################

pyTooling.CLIAbstraction is an abstraction layer and wrapper for command line programs, so they can be used easily in
Python. All parameters like ``--value=42`` are described as parameters of the executable.


.. _goals:

Main Goals
**********

* Offer access to CLI programs as Python classes.
* Abstract CLI options as members on a Python class.
* Derive program variants.
* Assemble parameters in list format for handover to ``subprocess.Popen``.


.. _usecase:

Use Cases
*********

*tbd*


.. _news:

News
****

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

   Arguments
   Executable


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

   Coverage Report ➚ <https://pyTooling.GitHub.io/pyTooling.CLIAbstraction/coverage/>
   Static Type Check Report ➚ <https://pyTooling.GitHub.io/pyTooling.CLIAbstraction/typing/>
   License
   Doc-License
   Glossary
   genindex
   py-modindex

tinyecs-compsys
===============

This is the namespace to contain all other ``tinyecs-compsys-XXXX`` packages.

Synopsis
--------

.. code:: python

   from tinyecs.compsys import Comp, Prop

Usage
-----

This package has no direct functionality, but all sub modules will register
their component IDs in the ``tinyecs.compsys.Comp`` enum.

Installation
------------

Installation instructions + requirements (should come automagically with
pyproject.toml)

.. code:: console

   pip install tinyecs[base]
   # or
   pip install tinyecs
   pip install tinyecs-compsys
   pip install tinyecs-compsys-base

Support / Contributing
----------------------

Issues can be opened on `github issues`_

.. _github issues: https://forgejo.indieandmore.photography/dickerdackel/tinyecs-compsys/issues

.. include:: AI-policy.rst


License
-------

This software is provided under the MIT license.

See LICENSE file for details.

tinyecs-compsys
===============

This is the namespace to contain all other ``tinyecs-compsys-XXXX`` packages.

Synopsis
--------

.. code:: python

   import tinyecs.compsys as cs

   cs.register()

Usage
-----

This package provides the namespace and a starting point for all
``tinyecs-compsys-<CATEGORY>`` packages.

Importing this package and calling its ``register`` function will import all immediate
subpackages and have those inject their component IDs into the ``Comp`` enum.

.. note:: The ``Comp`` contains symbols to use as component IDs in
   ``tinyecs``.  While every hashable is a valid component ID, and it's
   completely fine to just use strings for small projects, using the provided
   enum has the benefit of finding typing errors much easier.  It's
   recommended to make use of that.

   This package makes use of `aenum`, an advanced and extendable
   implementation of python enums, written by the same author that also
   maintains the official python version.

   If you create your own components and systems, you can add those to
   ``Comp`` as well::

      from aenum import extend_enum

      extend_enum(cs.Comp, 'YOUR_COMPONENT')
      ...

Installation
------------

It's up to you, if you install the currently provided `compsys` packages from
`tinyecs` by using

.. code:: console

   pip install tinyecs[base]

or include them by adding specific dependencies:

.. code:: console

   pip install tinyecs
   pip install tinyecs-compsys
   pip install tinyecs-compsys-base

Support / Contributing
----------------------

Issues can be opened on `github issues`_

.. _github issues: https://github.com/dickerdackel/tinyecs-compsys/issues

License
-------

This software is provided under the MIT license.

See LICENSE file for details.

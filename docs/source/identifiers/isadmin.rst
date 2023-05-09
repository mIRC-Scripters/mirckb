$isadmin
========

$isadmin Returns $true if mIRC is running in an elevated, administrator state, otherwise $false.

Synopsis
--------

.. code:: text

    $isadmin

Parameters
----------

None

Properties
----------

None

Notes
-----

If mIRC is running in elevated 'run as administrator' state:
* all executibles launched with /run will also have elevated state, even if /run's -a switch is not used.
* The UAC prompt will not appear when using /run -a to launch a program.
Example
-------

.. code:: text

    //echo -a $isadmin

Compatibility
-------------

.. compatibility:: 7.58

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/run </commands/run>`

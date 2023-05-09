$cmdline
========

$cmdline return the value passed to the executable when mIRC is ran.

Synopsis
--------

.. code:: text

    $cmdline

Parameters
----------

None

Properties
----------

None

Example
-------

.. code:: text

    on *:start:{
      if ($cmdline == debug) { echo -a debug }
    }
    ;//run $mircexe debug

Compatibility
-------------

.. compatibility:: 6.0

See also
--------

.. hlist::
    :columns: 4


$scriptline
===========

$scriptline returns the number of the line in the current script.

Synopsis
--------

.. code:: text

    $scriptline

Parameters
----------

None

Properties
----------

None

Example
-------

Put this code in a new remote file:

.. code:: text

    alias test {
      echo -a $scriptline
    }
 would show '2'

Compatibility
-------------

.. compatibility:: 5.8

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$scriptdir </identifiers/scriptdir>`

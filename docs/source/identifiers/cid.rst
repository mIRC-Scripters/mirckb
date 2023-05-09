$cid
====

$cid returns the connection id to the script that requests it.

Synopsis
--------

.. code:: text

    $cid

Parameters
----------

None

Example
-------

Echo to the currently active window the connection ID it is related to

.. code:: text

    //echo -a $cid

Code an alias to echo to the active window the connection ID for that script

.. code:: text

    alias showcid {
      echo -a $cid
    }

Compatibility
-------------

.. compatibility:: 6.0

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$activecid </identifiers/activecid>`
    * :doc:`$lactivecid </identifiers/lactivecid>`
    * :doc:`$scid </identifiers/scid>`
    * :doc:`$scon </identifiers/scon>`
    * :doc:`/scid </commands/scid>`


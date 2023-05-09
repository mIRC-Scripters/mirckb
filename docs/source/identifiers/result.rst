$result
=======

$result returns the value passed to the last :doc:`/return </commands/return>` (or :doc:`/returnex </commands/returnex>`) command only if the alias was called as a command (as of 7.51, may be extended to any aliases call in the future).

Synopsis
--------

.. code:: text

    $result

Parameters
----------

None

Properties
----------

None

Example
-------

.. code:: text

    alias test {
      return 5
    }
    alias testing {
      test
      echo -a $result
    }

Compatibility
-------------

.. compatibility:: 4.52

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/return </commands/return>`
    * :doc:`/returnex </commands/returnex>`


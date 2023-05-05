/return
=======

The **/return** command immediately leaves the current subroutine and returns a given value back to the calling routine (if one exists). This command behaves like most commands do when it comes to retaining spaces (i.e. multiple spaces are collapsed, leading and trailing are trimmed). If you are looking for a way to preserve spaces consider using the :doc:`/returnex </commands/returnex>` command instead.

Synopsis
--------

.. code:: text

    /return [value]

Switches
--------

None

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - [value]
      - The value to return to the calling routine

Example
-------

.. code:: text

    ; /return_example
    ;
    alias return_example {
    ;return the addition of two values
    echo -a $add(2, 5)
    }
    /* add two numbers
    */
    alias add {
    return $calc($1 + $2)
    }

Compatibility
-------------

Added: mIRC v4.5 (06 Jul 1996)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$result </identifiers/result>`
    * :doc:`/alias </commands/alias>`
    * :doc:`/returnex </commands/returnex>`

/maxdepth
=========

{{Deprecated feature}}

The **/maxdepth** command could be used to change the maximum allowable recursion limit for a single alias. A depth of 1 indicates no direct recursion is allowed. The maximum depth is 100. Calling an alias from within itself recursively has been disabled.

Synopsis
--------

.. code:: text

    /maxdepth <depth>

Switches
--------

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <depth>
      - The new recursion depth limit (1-100).

Example
-------

.. code:: text

    example {
    ;set max recursion depth to 3
    maxdepth 3
    set %a 1
    test
    }
    test {
    echo test %a
    inc %a
    test
    }

Output:

.. code:: text

    * Max depth is 3
    -
    test 1
    test 2
    -
    TEST Unknown command
    -

Another Example:

.. code:: text

    example {
    maxdepth 10
    set %a 1
    test
    }
    test {
    echo test %a
    inc %a
    test
    }

Output:

.. code:: text

    -
    * Max depth is 10
    -
    test 1
    test 2
    test 3
    test 4
    test 5
    test 6
    test 7
    test 8
    test 9
    -
    TEST Unknown command
    -

Compatibility
-------------

Added: mIRC v4.5 (06 Jul 1996)

Removed: 07/09/1996

Removed On:mIRC v4.6

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/scid </commands/scid>`
    * :doc:`/scon </commands/scon>`

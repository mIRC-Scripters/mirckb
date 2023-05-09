$chr
====

$chr returns the character attached to a specified Unicode code point number.

Synopsis
--------

.. code:: text

    $chr(<N>)

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
    * - N
      - This is the Unicode code point value that you wish to retrieve the character for.

Example
-------

Echo the character attached to Unicode code point ''63'' to the active window

.. code:: text

    //echo -a $chr(63)

Echo the character attached to Unicode code point ''85'' to the active window

.. code:: text

    //echo -a $chr(85)

Compatibility
-------------

.. compatibility:: 4.5

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$asc </identifiers/asc>`


$line
=====

$line returns the Nth line in a window

Synopsis
--------

.. code:: text

    $line(win,N,T)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - win
      - a channel/query/status or custom window
    * - N
      - The Nth line, returns the total number of lines if N = 0
    * - T
      - If T = 1, it references the listbox (nicklist in channel window), T = 0 references the display area

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - .state
      - returns selection state for a line in a listbox.
    * - .color
      - returns the color of the line, if any.

Example
-------

.. code:: text

    //echo -a $line($chan(1),1)

Compatibility
-------------

.. compatibility:: 5.3

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$sline </identifiers/sline>`
    * :doc:`$fline </identifiers/fline>`
    * :doc:`$window </identifiers/window>`


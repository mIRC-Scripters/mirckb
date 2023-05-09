$fline
======

$fline returns the number of the Nth line matching the expression in a window

.. note:: $fline strips lines from control code before matching

Synopsis
--------

.. code:: text

    $fline(win,expr,N,T,S)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - win
      - a channel/query/status or custom window
    * - expr
      - the expression to search, :ref:`matching_tools-wildcard` by default
    * - N
      - The Nth matching line, returns the total number of matching lines if N = 0
    * - T
      - If T = 1, it references the listbox (nicklist in channel window), T = 2 means the expression is a regular expression, T = 3 means both 1 & 2
    * - S
      - The search will start from the starting line number S, helping speeding up the search, you must provide the N and T parameter.

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - .text
      - return the line matched rather than the line number

Example
-------

.. code:: text

    //echo -a $fline($chan(1),*mirc*)

Compatibility
-------------

.. compatibility:: 5.4

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$flinen </identifiers/flinen>`
    * :doc:`$line </identifiers/line>`
    * :doc:`$sline </identifiers/sline>`
    * :doc:`$window </identifiers/window>`


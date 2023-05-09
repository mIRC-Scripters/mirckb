$sline
======

$sline returns the Nth selected line in a listbox.

Synopsis
--------

.. code:: text

    $sline(win,N)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - win
      - The window with a listbox, can be a channel window or a custom window
    * - N
      - The Nth selected line in the window

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - .ln
      - returns the line number of the Nth selected line

Example
-------

.. code:: text

    //echo -a $sline(0)

Compatibility
-------------

.. compatibility:: 5.0

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/sline </commands/sline>`


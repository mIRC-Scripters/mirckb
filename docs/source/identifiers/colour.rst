$colour
=======

The $colour identifier allows mIRC to return the proper color code associated with the specified target. (same as $color)

Synopsis
--------

.. code:: text

    $colour(name/N)[.property]

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Argument
      - Description
    * - name
      - Returns the color code for the specified name/action/event. Partial matches work as well: $colour(action)
    * - N
      - Specifies that the color code to be looked up is the RGB value for a specific color box target from the CTRL+K list.

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Argument
      - Description
    * - dd
      - Allows the color codes to be returned in double-digit format, eg: 02 instead of 2. Does not work on RGB-returned values.

Examples
--------

Echo the color code for action events:

.. code:: text

    //echo -a $colour(action)

Echo the RGB code for the 4th color box:

.. code:: text

    //echo -a $colour(4)

Compatibility
-------------

.. compatibility:: 5.3

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/color </commands/color>`
    * :doc:`$color </identifiers/color>`


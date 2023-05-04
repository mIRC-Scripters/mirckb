/strip
======

The '*/strip* command is used to essentially enable or disable certain control-code stripping within mIRC.

Synopsis
--------

.. code:: text

    /strip [+-burc]

Switches
--------

You can chain +letter and -letter combo where + enables and - disables

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - o
      - Turns off stripping entirely
    * - b
      - Bold
    * - u
      - Underline
    * - r
      - Reverse
    * - c
      - Color
    * - i
      - Italic
    * - e
      - StrikeThrough

Parameters
----------

None

Examples
--------

**Disable all control code stripping**

.. code:: text

    /strip -burc

**Enable stripping on bold, disable on color codes**

.. code:: text

    /strip -b+c

**Enable stripping on reverse and underline, disable on bold and color codes**

.. code:: text

    /strip +ru-bc

See also
--------

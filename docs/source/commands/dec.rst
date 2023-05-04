/dec
====

The **/dec** command decreases the value of a variable by a given value. If no value is specified, mIRC will decrease the variable by one. The /dec command works with both positive and negative values alike.

.. note:: /dec always keeps the unset time if there is one for the current variable, as though there was a -k switch from :doc: `/set </commands/set>` , there's no switch to prevent this behavior and unset the time while setting the value.

Synopsis
--------

.. code:: text

    /dec [-crszeuN] <%var> [value]

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -s
      - Prints out the value of the variable

Global variables only:

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -c
      - Decreases the variable once per second
    * - -r
      - Decreases the variable once per second (same as -c)
    * - -z
      - Decreases the variable every second until it reaches zero at which point the variable will get removed.
    * - -e
      - Unsets the variable when mIRC exits
    * - -uN
      - Decrease the variable once and unsets the variable after N seconds.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - %var
      - The variable's name
    * - [value]
      - Optional numeric value to decrease the variable by

Example
-------

.. code:: text

    Alias Example {
    ;Create a local variable and set it to 10
    var %x 10
    ;Decrease %x by 5
    dec %x 5
    ;Print out %x's content
    echo -a %x
    }

Compatibility
-------------

Added: mIRC v4.0 (20 Mar 1996)

See also
--------

.. hlist::
    :columns: 4

    * :doc: `$var </identifiers/$var>`
    * :doc: `/inc </commands/inc>`
    * :doc: `/set </commands/set>`
    * :doc: `/unset </commands/unset>`
    * :doc: `/var </commands/var>`

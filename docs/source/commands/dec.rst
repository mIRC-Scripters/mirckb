/dec
====

The **/dec** command decreases the value of a variable by a given value. If no value is specified, mIRC will decrease the variable by one. The /dec command works with both positive and negative values alike.

Synopsis
--------

.. code:: text

    /dec [-crszeuNk] <%var> [value]

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
    * - -k
      - Keeps the unset time of the variable if it exists. Watch out, currently -k in /dec does not behave the same as in {{mIRC|/set}}, as in, if you provide another -uN switch AND a -k switch, it will use this new unset time and won't preserve the original one.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Parameters
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

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$var </identifiers/var>`
    * :doc:`/inc <inc>`
    * :doc:`/set <set>`
    * :doc:`/unset <unset>`
    * :doc:`/var <var>`
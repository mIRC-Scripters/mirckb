/iuser
======

The **/iuser** command can be used to set or remove the info appended to an user list entry.

Synopsis
--------

.. code:: text

    /iuser <nick|address> [info]

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
    * - <nick|address>
      - The exact nick or address to be used
    * - [info]
      - If not provided, clear the info

Example
--------

.. code:: text

    ;Add an address; Info can be retrieved using $ulist(*!*@Example.com).info
    /auser 5 *!*@example.com Cool people

    ;Update the info
    /iuser *!*@example.com Uncool!

Compatibility
-------------

Added: mIRC v2.1a (28 Feb 1995)

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$ulevel </identifiers/ulevel>`
    * :doc:`$ulist </identifiers/ulist>`
    * :doc:`/flush <flush>`
    * :doc:`/guser <guser>`
    * :doc:`/auser <auser>`
    * :doc:`/rlevel <rlevel>`
    * :doc:`/ruser <ruser>`
    * :doc:`/ulist <ulist>`

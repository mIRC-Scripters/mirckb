/ialmark
========

The **/ialmark** command marks the IAL entry for a nickname with the specified text.

Synopsis
--------

.. code:: text

    /ialmark [-nrw] <nickname> [text]

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -n
      - the [name] of the mark. If -n is not used, the default name 'default' is used.
    * - -r
      - removes the mark
    * - -w
      - used with -rn to treat name as wildcard

Marks can be accessed using ``$ialmark(nick,N/name)`` and properties **name** and **mark**.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <nickname>
      - The nickname you want to mark
    * - [text]
      - The text you want to add. If not specified, the mark is cleared

Example
-------

.. code:: text

    ;Mark the nickname with the text "test"
    /ialmark Ouims test


Compatibility
-------------

Added: mIRC v5.9 (26 Apr 2001)

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/ialclear <ialclear>`
    * :doc:`/ial <ial>`
    * :doc:`$ial </identifiers/ial>`
    * :doc:`$address </identifiers/address>`
    * :doc:`$ialchan </identifiers/ialchan>`

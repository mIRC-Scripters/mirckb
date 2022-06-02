/hop
====

The **/hop** command parts the current channel and joins a new one. If no channel was specified, mIRC will part and join the current channel without closing the window.

Synopsis
--------

.. code:: text

    /hop -cnmdx [#channel] [message]

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -c
      - Cycles the specified channel by parting and rejoining it
    * - -n
      - Minimizes the channel window
    * - -x
      - maximizes the channel window.
    * - -m
      - sets the mdi state for the channel window.
    * - -d
      - set the desktop state for the channel window

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - [#channel]
      - This optional parameter can be used to specify which user from the address book to select. The user must already be in your address book.
    * - [message]
      - The part message to be sent

Example
-------

.. code:: text

    /* Suppose you are on #Foo;
       Part #Foo with "moving on" message and join #Bar
    */
    /hop #Bar moving on

Compatibility
-------------

Added: mIRC v5.71 (07 May 2000)

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$chan </aliases/chan>`
    * :doc:`/partall <partall>`

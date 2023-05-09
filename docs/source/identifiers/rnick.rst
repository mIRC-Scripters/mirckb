$rnick
======

.. attention:: This feature has essentially been replaced by :doc:`$nick </identifiers/nick>`

'''$rnick returns regular nickname on a channel

Synopsis
--------

.. code:: text

    $rnick(chan,N|nick)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - chan
      - the channel name
    * - N
      - The Nth regular nickname, if N is 0, returns the total number of regular nickname in the channel
    * - nick
      - is you specify a nickname, use that nickname with property, without property, returns the Nth position in the list of regular user for that channel

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - .pnick
      - Returns the target result with their elevation level, eg: @,+,%. Regular users display normal.
    * - .idle
      - Returns the current idle time for the nickname on the channel specified
    * - .color
      - Returns the color for that user as set up in the Nick color dialog

Example
-------

.. code:: text

    //echo -a $rnick($chan,0)

Compatibility
-------------

.. compatibility:: 5.5

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$nick </identifiers/nick>`


$ialchan
========

$ialchan returns the Nth address matching a mask in the given channel from the IAL

Synopsis
--------

.. code:: text

    $ialchan(nick/mask,#chan,N) - returns the Nth address matching a mask in the channel

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - nick/mask
      - a nickname or a mask
    * - #chan
      - the channel
    * - N
      - optional, the Nth matching entry in the IAL, use N = 0 for the total number of matches

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - .nick
      - returns the nickname of the matched entry
    * - .user
      - returns the username of the matched entry
    * - .host
      - returns the host of the matched entry
    * - .addr
      - returns the address in the format "user@host" of the matched entry
    * - .mark
      - returns the mark for that entry, set with :doc:`/ialmark </commands/ialmark>`
    * - .account
      - returns the account name of the entry (need CAP support for extended-join and account-notify)
    * - .away
      - returns the away status for that entry
    * - .gecos
      - returns the fullname of that entry
    * - .id
      - returns an unique ID to uniquely reference that nickname over any connection
    * - .pnick
      - Returns the target result with their elevation level, eg: @,+,%. Regular users display normal.

Example
-------

.. code:: text

    //echo -a $ialchan(*,$chan,0)

Compatibility
-------------

.. compatibility:: 5.1

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$ial </identifiers/ial>`


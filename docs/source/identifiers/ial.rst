$ial
====

$ial returns the Nth address matching a mask in the IAL

Synopsis
--------

.. code:: text

    $ial - returns $true or $false depending on whether the IAL is on or off.
    $ial(nick/mask,N) - returns the Nth address matching a mask in the IAL

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - nick/mask
      - a nickname or a mask
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
      - returns the username (ident) of the matched entry
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

Example
-------

.. code:: text

    //echo -a $ial(*,0)

Compatibility
-------------

.. compatibility:: 4.7

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$ialchan </identifiers/ialchan>`


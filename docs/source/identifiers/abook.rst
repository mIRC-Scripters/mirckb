$abook
======

$abook will return information about nicknames listed inside of the mIRC Address Book.

Synopsis
--------

.. code:: text

    $abook(nick/N[,N])[.property]

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - nick/N
      - The nickname that you wish to look up in the address book. This can be a :ref:`matching_tools-wildcard` such as ''ni*'', which would find all nicknames beginning with ''ni''. It can also be the Nth nickname in the book.
    * - N
      - This will return the Nth matching nickname relative to the nick parameter. If N is 0, it will return the total matches.

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - nick
      - Returns the nickname attached to the specific address book match.
    * - info
      - Returns the info area of the address book for the match, specifically the address.
    * - email
      - Returns the email associated with the address book match.
    * - website
      - Returns the website URL associated with the address book match.
    * - picture
      - Returns the filename of the picture, if any, associated with the address book match.
    * - ipaddr
      - Returns the ip address, if any, associated with the address book match.
    * - noteN
      - Returns the information in the notes area for the address book match where N is the Nth line

Example
-------

Echo all address matches to the active window

.. code:: text

    //echo -a $abook(*,0)

Echo the filename for the picture of the first address book match to the active window

.. code:: text

    //echo -a $abook(*,1).picture

Compatibility
-------------

.. compatibility:: 5.6

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/abook </commands/abook>`


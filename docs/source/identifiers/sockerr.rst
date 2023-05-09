$sockerr
========

$sockerr returns the sock error number if an error occurred.

$sockerr is not a local identifier only set inside event, it is set after any /sock* command as well, meaning that $sockerr can change in value inside the same on sockread event.

Synopsis
--------

.. code:: text

    $sockerr

Parameters
----------

None

Properties
----------

None

Error codes
-----------

Remember that using a /sock* command will change the $sockerr value, so these error codes must be checked prior any /sock* command

on SOCKOPEN
^^^^^^^^^^^

* 0: success
* 3: failure establishing socket connection (W)
* 4: error resolving given hostname

on SOCKLISTEN
^^^^^^^^^^^^^

* 0: new socket successfully accepted
* 1: error occurred on listening socket (W)
* 2: error accepting new socket (W)
* 4: not enough memory for new socket

on SOCKREAD
^^^^^^^^^^^

* 0: data received
* 3: error on connected socket occurred (W)

on SOCKWRITE
^^^^^^^^^^^^

* 0: all data successfully written
* 3: error trying to send data (W)

on SOCKCLOSE
^^^^^^^^^^^^

* 0: EOF from other end received
* 3: an error occurred while receiving data, or a SSL error occurred (W)
* 5: a certain(?) SSL error occurred during sockopen

Note 1: (W) = For these errors, $sock().wserr contains a specific WinSock error number and $sock().wsmsg the Winsock error text

Note 2: These codes were taken from http://www.xise.nl/mirc/wiki/doku.php/doku.php?id=sockerr

Example
-------

.. code:: text

    on *:sockread:name:{
      if ($sockerr) return
      …
    }

Compatibility
-------------

.. compatibility:: 5.3

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$sock </identifiers/sock>`
    * :doc:`$sockname </identifiers/sockname>`
    * :doc:`$sockbr </identifiers/sockbr>`


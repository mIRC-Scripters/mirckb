$serverip
=========

$serverip returns the ip address of the IRC server you are connected to.

Since mIRC 7.1+, $serverip is also filled by /dns $server for SOCK5 users, but note that this result in a DNS leak.

Synopsis
--------

.. code:: text

    $serverip

Parameters
----------

None

Properties
----------

None

Example
-------

.. code:: text

    //echo -a $serverip

Compatibility
-------------

.. compatibility:: 6.03

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$server </identifiers/server>`
    * :doc:`$servertarget </identifiers/servertarget>`


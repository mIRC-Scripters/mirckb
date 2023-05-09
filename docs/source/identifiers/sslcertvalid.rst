$sslcertvalid
=============

$sslcertvalid Returns $true if the IRC network's SSL certificate is valid for the current SSL connection. Returns $false if not connected or connection is non-SSL.

Synopsis
--------

.. code:: text

    $sslcertvalid

Parameters
----------

None

Properties
----------

Example
-------

.. code:: text

    //if (($server) && (+* iswm $port)) echo -a current SSL connection is $iif($sslcertvalid,valid,invalid)

Compatibility
-------------

.. compatibility:: 7.58

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$sslcertsha1 </identifiers/sslcertsha1>`
    * :doc:`$sslcertsha256 </identifiers/sslcertsha256>`
    * :doc:`$ssl </identifiers/ssl>`
    * :doc:`$sslready </identifiers/sslready>`
    * :doc:`$sslversion </identifiers/sslversion>`
    * :doc:`$ssldll </identifiers/ssldll>`
    * :doc:`$ssllibdll </identifiers/ssllibdll>`

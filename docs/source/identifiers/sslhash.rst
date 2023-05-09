$sslhash
========

$sslhash returns the SSL certificates for the active connection, or $null if no active certificate

Synopsis
--------

.. code:: text

    $sslhash(<method>,<type>)

.. code:: text

    $sslhash(<md5|sha1|sha256|sha512>,<p|s>)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
* <method> (md5, sha256, sha512, ecdsa)
* <type> p = client certificate, s = server certificate
Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
* .babble = returns bubble babble string instead of hash digest
* .colons = returns hash digest with pairs of hex digits separated by colons
Example
-------

.. code:: text

    //echo -a The $server certificate shown in context menu of status window has sha1 fingerprint $sslhash(sha1,s).colons
    //echo -a The client certificate used to connect to $server has sha512 fingerprint $sslhash(sha512,p)

Notes:
* The fingerprint is shown for the certificate used to connect to the server, or $null if none, and does not change if editing configuration while remaining connected. This should match your own certificate fingerprint seen in the /whois command, if you use the matching hashname.
* You can override the global certificate in serverlist, by unchecking 'use global certificate' and selecting a different filename. If that box is unchecked with no server certificate checked, then you are not seen by the server as using a certificate.
* Your client certificate cannot be seen by the server unless you connect to a +port
* MD5 is available because some server software uses it as the default when admins have not configured the fingerprint type used.
* $sslcertsha1 and $sslcertsha256 remain valid but are removed from /help
Error Messages
--------------

* Invalid parameters: $sslhash
Caused by the 1st parm not being one of the 5 valid types, or the 2nd parm not being 's' or 'p'
Compatibility
-------------

.. compatibility:: 7.68

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$sslcertsha1 </identifiers/sslcertsha1>`
    * :doc:`$sslcertsha256 </identifiers/sslcertsha256>`

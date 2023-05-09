$sreq
=====

$sreq returns the current parameter settings for DCC Sends for mIRC.

Synopsis
--------

.. code:: text

    $sreq

Switches
--------

None

Results
-------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Value
      - Description
    * - ask
      - DCC Send requests will popup an authorization window asking you whether you wish to accept or decline all incoming DCC Sends.
    * - auto
      - All incoming DCC Sends will be automatically accepted.
    * - ignore
      - All incoming DCC Sends will be ignored.

Examples
--------

Echo the current status of DCC Sends to the active window:

.. code:: text

    //echo -a $sreq

Compatibility
-------------

.. compatibility:: 5.4

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/creq </commands/creq>`
    * :doc:`/sreq </commands/sreq>`
    * :doc:`$creq </identifiers/creq>`


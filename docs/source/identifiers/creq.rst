$creq
=====

$creq returns the current parameter settings for DCC Chat requests.

Synopsis
--------

.. code:: text

    $creq

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
      - DCC Chat requests will popup an authorization window asking you whether you wish to accept or decline all incoming DCC Sends.
    * - auto
      - All incoming DCC Chats will be automatically accepted.
    * - ignore
      - All incoming DCC Chats will be ignored.

Examples
--------

Echo the current status of DCC Chats to the active window:

.. code:: text

    //echo -a $creq

Compatibility
-------------

.. compatibility:: 5.4

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/creq </commands/creq>`
    * :doc:`/sreq </commands/sreq>`


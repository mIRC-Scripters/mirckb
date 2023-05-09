On Sendfail
===========

The ON SENDFAIL event triggers whenever mIRC fails to send a remote user Dcc - mIRC|DCC.

This event fills :doc:`$filename </identifiers/filename>`, :doc:`$address </identifiers/address>`, and :doc:`$nick </identifiers/nick>` with the filename, user's address, and the user's nickname (if available), respectively.

Synopsis
--------

.. code:: text

    ON <level>:SENDFAIL:<filename[,filename]>:<commands>

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <level>
      - The level for the event to trigger.
    * - <filename[,filename]>
      - The filename(s) that should match the failed file. These can be :ref:`matching_tools-wildcard`. Example: ''*.txt,*.doc,my*.txt''
    * - <commands>
      - The commands to be performed when the event listener's criteria is met.

Examples
--------

Echo the name of the filename, along with both the user's nickname and address if available:

.. code:: text

    ON *:SENFAIL:*:echo -a Failed to send $filename $iif($nick,to $nick - ,to) Address: $address

Compatibility
-------------

.. compatibility:: 5.0

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/dcc </commands/dcc>`
    * :doc:`on filercvd </events/on_filercvd>`
    * :doc:`on filesent </events/on_filesent>`
    * :doc:`on getfail </events/on_getfail>`


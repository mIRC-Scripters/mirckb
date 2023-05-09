On Filercvd
===========

The ON FILERCVD event triggers whenever a file is received successfully via :doc:`dcc send </commands/dcc>`.

This event fills :doc:`$filename </identifiers/filename>`, :doc:`$address </identifiers/address>`, and :doc:`$nick </identifiers/nick>` with the filename, user's address, and the user's nickname (if available), respectively.

Synopsis
--------

.. code:: text

    ON <level>:FILERCVD:<filename[,filename]>:<commands>

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <level>
      - The corresponding :doc:`access levels </intermediate/events>` for the event to trigger.
    * - <filename>
      - The filename(s) that should match the received file. Seperate multiple values by commas. These can be :ref:`matching_tools-wildcard`. Example: \*.txt,\*.doc,my\*.txt
    * - <commands>
      - The commands to be performed when the event listener's criteria is met.

Local identifiers
-----------------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - :doc:`$filename </identifiers/filename>`
      - Returns the complete filename of the received file.

Examples
--------

Echo the name of the filename received to the active window:

.. code:: text

    ON *:FILERCVD:*:echo -a Received filename: $filename

Echo the name of the filename, along with both the user's nickname and address if available:

.. code:: text

    ON *:FILERCVD:*:echo -a Received filename: $filename $iif($nick,from $nick - ,from) Address: $address

Compatibility
-------------

.. compatibility:: 4.5

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/dcc </commands/dcc>`
    * :doc:`on filesent </events/on_filesent>`
    * :doc:`on getfail </events/on_getfail>`
    * :doc:`on sendfail </events/on_sendfail>`


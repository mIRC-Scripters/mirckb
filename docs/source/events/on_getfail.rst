On Getfail
==========

The ON GETFAIL event triggers whenever a remote user sends a file via :doc:`DCC send </commands/dcc>` and it fails.

Synopsis
--------

.. code:: text

    ON <level>:GETFAIL:<filename[,filename]>:<commands>

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
      - The filename(s) that should match the received file. Seperate multiple values by commas. These can be :ref:`matching_tools-wildcard`. Example: ''*.txt,*.doc,my*.txt
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

Echo the name of the filename, along with both the user's nickname and address if available:

.. code:: text

    ON *:GETFAIL:*:echo -a Failed to receive $filename $iif($nick,from $nick - ,from) Address: $address

Compatibility
-------------

.. compatibility:: 5.0

See also
--------

.. hlist::
    :columns: 4

    * :doc:`dcc command </commands/dcc>`
    * :doc:`on filercvd </events/on_filercvd>`
    * :doc:`on filesent </events/on_filesent>`
    * :doc:`on sendfail </events/on_sendfail>`


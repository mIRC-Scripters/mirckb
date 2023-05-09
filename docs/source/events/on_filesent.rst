On Filesent
===========

The ON FILESENT event triggers whenever a file is sent successfully via :doc:`/dcc send </commands/dcc>`.

Synopsis
--------

.. code:: text

    ON <level>:FILESENT:<filename[,filename]>:<commands>

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
      - Returns the complete filename of the file sent.

Example
-------

Echo the name of the filename sent to the active window, along with the user's nickname and address if available:

.. code:: text

    ON *:FILESENT:*:echo -a Successfully sent $filename $iif($nick,to $nick - ,to) Address: $address

Compatibility
-------------

.. compatibility:: 4.5

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/dcc </commands/dcc>`
    * :doc:`on filercvd </events/on_filercvd>`
    * :doc:`on getfail </events/on_getfail>`
    * :doc:`on sendfail </events/on_sendfail>`


/fserve
=======

The **/fserve** command can initiate a DCC fileserver transaction with a specific user.

Synopsis
--------

.. code:: text

    /fserve <nickname> <maxgets> <homedirectory> [welcomefile]

Switches
--------

None

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <nickname>
      - the nickname you want to initiate a fileserver with <maxgets> - the maximum number of simulataneous files (dcc get) the user can download
    * - <homedirectory>
      - the home directory for that session
    * - [welcomefile]
      - if specified, the file is sent when the user first connect

Example
-------

.. code:: text

    /fserve goat 5 c:\users\level1 level1.txt

Compatibility
-------------
Added: mIRC v3.3 - v3.4

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
--------

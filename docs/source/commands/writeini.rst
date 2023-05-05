/writeini
=========

The **/writeini** command is used to write and update a standard :doc:`initialization file </intermediate/data_storage.html#ini-files>` .

Overview
--------

The Standard INI file has the following format:

.. code:: text

    [Section]
    Item=value
    Item2=value
    ;some comment
    [Section2]
    Item=value
    Item2=value

.. note::

For *mIRC <= 6.35:* Writing to a file bigger than 64KB requires the -n switch, otherwise an error will be generated, halting the script. ([http://support.microsoft.com/kb/78346 This is a limitation of the standard Win32 API] GetPrivateProfileString() and WritePrivateProfileString())

For *mIRC >= 7.00:* mIRC now uses its own custom INI routine, the -n switch is obsolete.

Synopsis
--------

.. code:: text

    /writeini [-nz] <inifile> <section> <item> <value>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -n

.. note:: above)

    * - -z
      - Write an empty value

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <inifile>
      - The filename to write to
    * - <section>
      - Section name
    * - <item>
      - Item name
    * - <value>
      - The data to store for the item

Example
-------

.. code:: text

    ;Write a few items to a file
    /writeini abb.ini abbreviations lol Laughing Out Loud
    /writeini abb.ini abbreviations rofl Rolling On the Floor, Laughing

    /*
    abb.ini format:

    [abbreviations]
    lol=Laughing Out Loud
    rofl=Rolling On the Floor, Laughing
    */

    ;Retrieve 'lol'
    //echo -a $readini(abb.ini, n, abbreviations, lol)

    ;Prints out: Laughing Out Loud

Compatibility
-------------

Added: mIRC v4.5 (06 Jul 1996)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$readini </identifiers/readini>`
    * :doc:`$ini </identifiers/ini>`
    * :doc:`$read </identifiers/read>`
    * :doc:`$mircini </identifiers/mircini>`
    * :doc:`$mircdir </identifiers/mircdir>`
    * :doc:`/write </commands/write>`

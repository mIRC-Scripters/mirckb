/writeini
=========

The /writeini command is used to write and update a standard INI Files. (:ref:`ini_files`)

Overview
--------

The Standard INI file has the following format:

.. code:: ini

    [Section]
    Item=value
    Item2=value
    ;some comment
    [Section2]
    Item=value
    Item2=value

.. note:: For ''mIRC <= 6.35:'' Writing to a file bigger than 64KB requires the -n switch, otherwise an error will be generated, halting the script. ([http://support.microsoft.com/kb/78346 This is a limitation of the standard Win32 API] GetPrivateProfileString() and WritePrivateProfileString())
    For ''mIRC >= 7.00:'' mIRC now uses its own custom INI routine, the -n switch is obsolete.

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
      - Forces mIRC to write to an INI file, even if it's bigger then 64k (see note above)
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

.. compatibility:: 4.5

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


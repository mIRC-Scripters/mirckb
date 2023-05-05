/hload
======

The **/load** command loads a text file to an hash table. /hload does not create the table, it must already have been created by :doc:`/hmake </commands/hmake>` then saved to disk using :doc:`/hsave </commands/hsave>` .

Synopsis
--------

.. code:: text

    /hload -sBbnmN <name> <filename>
    /hload -sinmN <name> <filename> [section]

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -s
      - display a message if successful: "* Loaded hash table '<name>' from '<filename>'
    * - -b
      - loads binary files, :doc:`$cr </identifiers/cr>` and :doc:`$lf </identifiers/lf>` and 0x00's etc are preserved when saving as binary files
    * - -B
      - uses a larger index than -b to allow longer binary data to be saved. This is not compatible with files created by the -b switch.
    * - -n
      - loads files as data only, each item is a sequential integer, starting at N = 1
    * - -i
      - treats the file as an ini file format
    * - -mN
      - create the hash table if it does not exist, you can optionally specify N for the number of buckets in the range 1-10000, default 100 if N not used.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <name>
      - the name of the hash table
    * - <filename>
      - the file from which you want to load. Filename containing space much be enclosed in doublequotes.
    * - [section]
      - if -i is used, you can specify a section to be loaded. Default section name when parameter not used: hashtable (Should not use the square braces around the Section name.)

Notes
-----

.. note:: /hload uses the same syntax as /hsave except /hload has the -mN switch but does not have /hsave's -u switch.

.. note:: If using /hload -i or -b or -n switches, it assumes the data was /hsave'ed to disk using those same switches.

.. note:: If /hload into a table containing existing items, any match between existing item name and the items loaded from disk replaces the existing item's value with the value from disk, but any other existing items in the table are not affected by an /hload command.

Example
-------

.. code:: text

    //hfree -w test | hload -im1n test $nopath($mircini) colors | var %tot $hget(test,0).item , %i 1 | while (%i <= %tot) { echo -a $ord(%i) item is $hget(test,%i).item containing $hget(test,$hget(test,%i).item) | inc %i }
    * Loads color scheme names and event colors into items named after the integers 1 and greater. These are contained in the colors section of mirc.ini. If the 'n' switch were not used, the item names would instead be named the same as the items in mirc.ini; n0 n1 etc.
    * If using the -n switch, do not expect the same values to be loaded into the same integer item names from which they were /hsave'ed to disk, even if using 1 bucket.

    //hload -m test no_such_file | echo -a does not display
    * Attempting to load a non-existent filename is an error which halts execution of the script.

    //bset &var 1 $regsubex($str(x,256),/x/gi,$calc(\n -1) $chr(32)) | hfree -w test | hadd -mb test ascii &var | hsave -b test test.dat | hload -mb test2 test.dat | noop $hget(test,ascii,&copy) | echo 4 -a $bvar(&copy,1-)
    * Binary variable can be accurately saved to a hashtable item, then /hsave'ed to disk with the -b switch, then /hload'ed from disk with the -b switch. The display shows &copy containing an un-altered copy of the original binary variable.

Compatibility
-------------

Added: mIRC v5.8 (14 Dec 2000)
See also
--------

.. hlist::
    :columns: 4

    * :doc:`/hmake </commands/hmake>`
    * :doc:`/hfree </commands/hfree>`
    * :doc:`/hsave </commands/hsave>`
    * :ref:`dAta_sTorage-hash_tables`
    * :doc:`/hadd </commands/hadd>`
    * :doc:`/hdel </commands/hdel>`
    * :doc:`/hinc </commands/hinc>`
    * :doc:`/hdec </commands/hdec>`
    * :doc:`$hget </identifiers/hget>`
    * :doc:`$hfind </identifiers/hfind>`

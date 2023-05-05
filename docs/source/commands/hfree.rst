/hfree
======

The **/hfree** command destroys previously created hash table(s) along with all item/data pairs within them. A hash table can be created via the :doc:`/hmake </commands/hmake>` command.

Synopsis
--------

.. code:: text

    /hfree [-sw] <nowiki><table></nowiki>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -s
      - Displays debug information
    * - -w
      - Treats <nowiki><table></nowiki> as a :doc:`wildcard </intermediate/matching_tools.html#wildcard>` and deletes all matching tables.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <nowiki><table></nowiki>
      - the table you wish to delete.

Example
-------

.. code:: text

    alias del_hash {
    ;makes the hash table 'hash'
    hmake hash
    echo -a $hget(hash) : $hget(hash).size
    ;makes the hash table 'h' with 10 buckets
    hmake h 10
    ;makes the hash table 'has' with 20 buckets
    hmake has 20
    ;deletes hash table 'hash'
    hfree -s hash
    echo -a $hget(h) : $hget(h).size - $hget(has) : $hget(has).size
    ;deletes any hash tables matching h*
    hfree -sw h*
    }

.. code:: text

    //hfree -s test | hfree -s test | echo -a test message
    * When not using the -w switch, trying to free a non-existent table is an error which halts execution of a script, so the echo does not display

    //hfree -sw test | hfree -sw test | echo -a test message
    * Using the -w switch allows deleting zero tables matching the wildcard, enabling the echo to display.

Compatibility
-------------

Added: mIRC v5.8 (14 Dec 2000)
See also
--------

.. hlist::
    :columns: 4

    * :doc:`/hmake </commands/hmake>`
    * :doc:`/hload </commands/hload>`
    * :doc:`/hsave </commands/hsave>`
    * :doc:`hAsh tAbles </intermediate/data_storage.html#hash-tables>`
    * :doc:`/hadd </commands/hadd>`
    * :doc:`/hdel </commands/hdel>`
    * :doc:`/hinc </commands/hinc>`
    * :doc:`/hdec </commands/hdec>`
    * :doc:`$hget </identifiers/hget>`
    * :doc:`$hfind </identifiers/hfind>`

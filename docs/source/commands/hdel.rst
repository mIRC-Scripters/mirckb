/hdel
=====

The **/hdel** command deletes an item/data-value pair from an existing hash table.

Synopsis
--------

.. code:: text

    /hdel [-sw] <nowiki><table></nowiki> <item>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -s
      - Displays the Deletion action if the variable exists, displays error if table doesn't exist, no display if the table exists but the item does not.
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
      - The table which contains the item you are deleting
    * - <item>
      - the item-name associated with a value to delete. Can be a :doc:`wildcard </intermediate/matching_tools.html#wildcard>` when using -w switch.

Example
-------

.. code:: text

    alias hdel_example {
    ;add items
    hadd -m example academic a
    hadd example academy a
    hadd example accelerate a
    hadd example accelerator a
    hadd example accept a
    hadd example access a
    hadd example accident a
    hadd example because b

    ;number of items
    echo -a $hget(example, 0).item

    ;remove everything by one
    hdel -w example a*

    ;number of items
    echo -a $hget(example, 0).item

    ;free table
    hfree example
    }

.. code:: text

    //hfree -sw test | hadd -m1 test item1 | hadd test item* | echo -a 1st item is $hget(test,1).item | hdel -w test item* | echo -a there are $hget(test,0).item items remaining
    * Demonstrates that an item can be created and deleted containing an asterisk. If the -w switch is deleted, only 1 of the 2 items is deleted because of an exact item-name match with "item*".

    //hfree -sw test | hmake -s test | hdel -s test itemname | echo -a message 1 | hfree -s test | hdel -s test itemname | echo -a message 2
    * Demonstrates that deleting a non-existent item from an existing table allows the script flow to continue, but deleting an item from a non-existent table is an error halting the script flow preventing the 2nd message from displaying.

Compatibility
-------------

Added: mIRC v5.8 (14 Dec 2000)
See also
--------

.. hlist::
    :columns: 4

    * :doc:`/hmake </commands/hmake>`
    * :doc:`/hfree </commands/hfree>`
    * :doc:`/hload </commands/hload>`
    * :doc:`/hsave </commands/hsave>`
    * :doc:`/hadd </commands/hadd>`
    * :doc:`/hinc </commands/hinc>`
    * :doc:`/hdec </commands/hdec>`
    * :doc:`hAsh tAbles </intermediate/data_storage.html#hash-tables>`
    * :doc:`$hget </identifiers/hget>`
    * :doc:`$hfind </identifiers/hfind>`

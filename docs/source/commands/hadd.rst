/hadd
=====

The **/hadd** command inserts a new item/value pair in the hash table by the <nowiki><table></nowiki> name. If that item name already exists, its old value is replaced. If the table does not exist, the -m switch can be used to create the table however it defaults to have 100 buckets, which may or may not be suitable depending on your table size. See :doc:`/hmake </commands/hmake>` for more details.

Synopsis
--------

.. code:: text

    /hadd [-m[N]szuNk] <nowiki><table></nowiki> <item> [value]
    /hadd -b[cm[N]szuNk] <nowiki><table></nowiki> <item> <&bvar>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -m[N]
      - Creates the hash table if it does not exist, you can optionally specify N for the number of buckets. If table already exists, this does not change the number of buckets.
    * - -s
      - Displays the assignment information
    * - -z
      - Decreases the value by 1.0 every second; unsets at zero
    * - -uN
      - Removes the item/value after N seconds
    * - -k
      - Keeps the remaining time left from the -uN and -z switches (undocumented in help file)
    * - -b
      - Treats the value as a binary variable
    * - -c
      - Truncates the &bvar at the first null value

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <nowiki><table></nowiki>
      - The handle name of the table to operate on
    * - <item>
      - The item key associated with the value
    * - [value]
      - The optional value associated with the item key
    * - <&bvar>
      - The binary variable value associated with the item key

Examples
--------

A basic usage for a hash table.

.. code:: text

    ; call the setup once
    ; /abbr_setup
    ;
    ; //echo -a $abbr(lol)
    ;
    alias abbr_setup {
    ; populate the table, create it if it does not exist
    hadd -m abbr lol laughing out load
    hadd abbr omg oh my gosh
    hadd abbr lmao laughing my a?? off
    hadd abbr brb be right back
    }
    ; get the abbreviation
    alias abbr return $hget(abbr, $1)

.. code:: text

    //hadd -sm50 test time $ctime
    * Creates item named "time" in hashtable "test". If table "test" did not already exist, that table is first created with 50 buckets. If it already existed, the number of buckets remains the same, and any other existing item/data are not affected.

    //hadd -z test countdown 123.45 | .timerX 5 1 echo 4 -a value $!hget(test,countdown) unsets in $!hget(test,countdown).unset
    * Creates item named "countdown" with the value 123.45 then decrements it by 1 each second, preserving fractions, as long as the number remains positive. If decrementing results in the value being zero or negative, the item is unset. At creation, the item is given the unset value of 2^31-1 seconds in the future, regardless of the value. This item is not guaranteed to be unset 124 seconds from now, because /hinc or /hdec used with the -k switch can change the value while preserving the countdown behavior.

    //hadd -zu3 test countdown 123.45 | .timerX 5 1 echo 4 -a value $!hget(test,countdown) unsets in $!hget(test,countdown).unset
    * Same as above, except -u3 causes the item to unset 3 seconds in the future before it decements to zero.

    //hadd -mu30 Voting Open 30 | echo 4 -a val $hget(voting,open) unset delay $hget(voting,open).unset | hadd -z Voting Open 10 | .timerX 5 1 echo 3 -a val $!hget(voting,open) unset delay $!hget(voting,open).unset
    * Creates table "Voting" if it doesn't already exist, with default buckets 100. Creates an item named "Open" containing the value 1, which unsets 30 seconds in the future. Then it updates the variable to value 10, and -z resets the unset delay from 30 seconds to be 2^31-1 seconds in the future.

    //hadd -mu30 Voting Open 30 | echo 4 -a val $hget(voting,open) unset delay $hget(voting,open).unset | hadd Voting Open 10 | .timerX 5 1 echo 3 -a val $!hget(voting,open) unset delay $!hget(voting,open).unset
    * Same as above, except re-creating the variable without any switches resets the unset delay to 0, where it will not unset in the future.

    //hadd -mu30 Voting Open 30 | hdel Voting Open | .timerX 5 1 hadd -ku99 Voting Open $!asctime $(|) echo 3 -a val $!hget(voting,open) unset delay $!hget(voting,open).unset
    * -k is ignored the first time because the item does not exist, causing the item to be given a 99 seconds delay. But after that, the item having a non-zero unset delay means the -k switch causes the -u99 to be ignored, preserving the unset delay of an existing item. If the item had been created using the -z switch, it retains the non-zero unset delay (in excess of 2 billion seconds) but loses the property of decrementing by 1 each second if -z is not used again.

    //hfree -w test | hadd -mz test item1 33 | hadd test item2 44 | hadd -u30 test item3 55 | hsave -u test deleteme.txt
    * All 3 items written to disk. If edited to remove hsave's -u switch, only item2 is written to disk because -z gives item1 an unset property over 2 billion seconds in the future, and item3 also has an unset property for 30 seconds in the future.

    //bset &var1 1 97 98 99 00 100 101 | hadd -smb test bintest &var1 | noop $hget(test,bintest,&var2) | echo -a $bvar(&var2,0) $bvar(&var2,1-)
    * after the &var1 is created, the 6 binary bytes are added to table 'test' as item 'bintest'. &var2 contains 6 bytes including the ASCII 0x00.

    //bset &var1 1 97 98 99 00 100 101 | hadd -smbc test bintest &var1 | noop $hget(test,bintest,&var2) | echo -a $bvar(&var2,0) $bvar(&var2,1-)
    * same except the contents of item 'bintest' is truncated, containing only the bytes prior to the first 0x00 byte if any.

    //hfree -w test | hadd -m test $ $+ version $+ $chr(32) $+ foo % $+ variable | echo 4 -a item= $hget(test,1).item data= $hget(test,1).data
    * There is little restriction on the name given to items, but the 1st and 2nd space-delimited parameters are the table and item names, and everything beyond that is the data

    //hfree -w test | hadd -m test itemname | echo 4 -a item= $hget(test,1).item data= $hget(test,1).data
    * As with /set and /var, there is not a restriction against creating itemnames with null content.

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
    * :doc:`/hdel </commands/hdel>`
    * :doc:`/hinc </commands/hinc>`
    * :doc:`/hdec </commands/hdec>`
    * :doc:`hAsh tAbles </intermediate/data_storage.html#hash-tables>`
    * :doc:`$hget </identifiers/$hget>`
    * :doc:`$hfind </identifiers/$hfind>`

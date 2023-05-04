/hinc
=====

The **/hinc** command increases the value of a hashtable item by [num]. If the optional number value is not specified, the default increment value is 1. It uses the same syntax as /hadd except -b's &binvar is the [num] parameter not the destination.

Synopsis
--------

.. code:: text

    /hinc [-m[N]szuN] <nowiki><table></nowiki> <item> [num]
    /hinc -b[m[N]szuN] <nowiki>‹table></nowiki> <item> <&bvar>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -m[N]
      - Creates the hash table if it does not exist, optionally setting the number of buckets to N. (Valid N 1-10000)
    * - -s
      - Displays the assignment information
    * - -b
      - uses the .text contents of a &binvar as the [num] parameter.
    * - -z
      - After setting the data's value, decreases the value by 1 each second; unsets to prevent the data value being zero or negative
    * - -uN
      - Removes the hashtable item/value after N seconds

.. note:: If hashtable item has a non-zero $hget(table,item).unset property due to using -uN or -z switches when created or modified by /hinc /hdec or /hadd, then /hsave will not save that item to disk without the /hsave -u switch. /hinc preserves any existing unset delay when -z and -uN switches are not used.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <nowiki><table></nowiki>
      - The handle name of the table containing the 'item'
    * - <item>
      - The item name associated with the data value
    * - [num]
      - The optional value by which to increase the data value. If not present, increases by 1.0
    * - <&bvar>
      - The binary variable containing the value by which to decrease the 'item'

Example
-------

Example 1:

.. code:: text

    alias example {
    ;create the table
    hmake -s example

    ;add a few items
    hadd example item1 4
    hadd example item2 7
    hadd example item3 9

    ; print the items
    echo -a item1 = $hget(example, item1)
    echo -a item2 = $hget(example, item2)
    echo -a item3 = $hget(example, item3)

    ; increase the values
    hinc example item1 5
    hinc example item2 12
    hinc example item3 1
    echo -e -

    ; print the items
    echo -a item1 = $hget(example, item1)
    echo -a item2 = $hget(example, item2)
    echo -a item3 = $hget(example, item3)

    ;cleanup
    hfree -s example
    }

A counter example:

.. code:: text

    alias countup {
    ;adds the item up with a value of 0 to the table count
    hadd -m count up 0
    echo -a $hget(count,up) $+ !
    :repeat
    ;checks if the value of down returns true
    if ($hget(count,up) < 9) {
    ;increases down by 1
    hinc count up
    ;echos the current count
    echo -a $hget(count,up) $+ !
    ;repeats
    goto repeat
    }
    ;if the previous if statement returns false it carries on with this.
    else echo -a 10, done!
    hfree -s count
    }

.. code:: text

    //hfree -sw test | hinc -sm test foo 5 | echo -a item foo has value $hget(test,foo)
    Result: 5
    * If the item does not exist, /hinc behaves as if the item exists with a value of zero.

    //hfree -sw test | var %a 0 | hadd -sm test foo 5 | hinc test foo %a | echo -a item foo has value $hget(test,foo)
    Result: 5
    //hfree -sw test | var %a | hadd -sm test foo 5 | hinc test foo %a | echo -a item foo has value $hget(test,foo)
    Result: 6
    //hfree -sw test | var %a | hadd -sm test foo 5 | hinc test foo $+(0,%a) | echo -a item foo has value $hget(test,foo)
    Result: 5
    * If variable used to increment the item is $null the increment is the default 1 not zero.

    //hfree -sw test | hadd -sm50 test foo 9.123456789 | echo -a item foo has value $hget(test,foo) | hinc -s test foo 2 | echo -a item foo has value $hget(test,foo)
    * While a hash table value can be created having more than 6 decimals, the result of /hinc is rounded to nearest 6 decimals, the same result as if $calc(old_value + increment_value). If the [num] parameter is incorrectly set to be non-numeric, the item is unset 1 second later because $calc(string - 1) is zero.

    //hfree -sw test | hadd -sm50 test foo 30 | echo -a item foo has value $hget(test,foo) | .timer 5 1 hinc -z test foo 50 $(|) echo 4 -a item foo has value $!hget(test,foo) and will unset in $!hget(test,foo).unset secs
    * After the old value has been incremented (handles existing $null value as if zero), -z begins with the new incremented value then decreases it once per second, but also gives the item the characteristic as if -u2147483647 were also used. (2^31-1)

    //hfree -sw test | hadd -sm50 test foo 30 | echo -a item foo has value $hget(test,foo) | .timer 5 1 hinc -zu30 test foo 50 $(|) echo 4 -a item foo has value $!hget(test,foo) and will unset in $!hget(test,foo).unset secs
    * Same as above, except -u30 modifies the future unset time to be 30 seconds instead of 2147483647.

    .. note:: Any data value created or modified using the -z or -uN switch has the characteristic of being unset in the future, and /hsave will not save that item/data pair to disk unless the /hsave -u switch is used.

    //hfree -sw test | hinc -smzu10 test foo 30.4 | .timer 11 1 echo 4 -a value $!hget(test,foo) vs .unset $!hget(test,foo).unset
    //hfree -sw test | hinc -smzu10 test foo 5.44 | .timer 11 1 echo 4 -a value $!hget(test,foo) vs .unset $!hget(test,foo).unset
    * When item is created using both -z and -uN, the variable is unset to prevent the first of either .unset seconds reaching zero or the value decrements to be zero or negative.

    //hadd -m table item 123 | bset &v1 1 51 51 13 51 | echo -a inc $hget(table,item) by $bvar(&v1,1-).text | hinc table item $bvar(&v1,1-).text | echo 3 -a equals $hget(table,item)
    //hadd -m table item 123 | bset &v1 1 51 51 13 51 | echo -a inc $hget(table,item) by $bvar(&v1,1-).text | hinc -b table item &v1 | echo 3 -a equals $hget(table,item)
    * Using -b with &binvar as the NUM parameter is the same as using $bvar(&binvar).text as the NUM parameter without using -b
    * The 3rd 3 is ignored because /hinc strips non-numeric string from the ending, increasing the item value 123 by 33.

Compatibility
-------------

Added: mIRC v6.0 (16 Aug 2002)
See also
--------

.. hlist::
    :columns: 4

    * :doc:`/hmake </commands/hmake>`
    * :doc:`/hfree </commands/hfree>`
    * :doc:`/hload </commands/hload>`
    * :doc:`/hsave </commands/hsave>`
    * :doc:`/hadd </commands/hadd>`
    * :doc:`/hdel </commands/hdel>`
    * :doc:`/hdec </commands/hdec>`
    * :doc:`hAsh tAbles </intermediate/data_storage.html#hash-tables>`
    * :doc:`$hget </identifiers/$hget>`
    * :doc:`$hfind </identifiers/$hfind>`

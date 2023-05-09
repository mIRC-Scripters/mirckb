/hdec
=====

The /hdec command decreases the value of a hashtable item by [num]. If the optional number value is not specified, the default increment value is 1. It uses the same syntax as /hadd except -b's &binvar is the [num] parameter not the destination.

Synopsis
--------

.. code:: text

    /hdec [-m[N]szuN] ‹table› <item> [num]
    /hdec -b[m[N]szuN] ‹table> <item> <&bvar>

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

.. note:: If hashtable item has a non-zero $hget(table,item).unset property due to using -uN or -z switches when created or modified by /hinc /hdec or /hadd, then /hsave will not save that item to disk without the /hsave -u switch. /hdec preserves any existing unset delay when -z and -uN switches are not used.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <table>
      - The handle name of the table containing the 'item'
    * - <item>
      - The item name associated with the data value
    * - [num]
      - The optional value by which to decrease the data value. If not present, decreases by 1.0
    * - <&bvar>
      - The binary variable containing the value by which to decrease the 'item'

Example
-------

.. note:: For more examples see the :doc:`/hinc </commands/hinc>` page. /hdec is the same as /hinc except for decrementing by [num] instead of incrementing.

.. code:: text

    alias countdown {
      ;adds the item down with a value of 10 to the table count
      hadd -m count down 10
      echo -a $hget(count,down) $+ !
      :repeat
      ;checks if the value of down returns true
      if ($hget(count,down) > 1) {
        ;decreases down by 1
        hdec count down
        ;echos the current count
        echo -a $hget(count,down) $+ !
        ;repeats
        goto repeat
      }
      ;if the previous if statement returns false it carries on with this.
      else echo -a 0, Hurray!
      hfree -s count
    }

Compatibility
-------------

.. compatibility:: 6.0

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
    * :doc:`/hinc </commands/hinc>`
    * :ref:`data_storage-hash_tables`
    * :doc:`$hget </identifiers/hget>`
    * :doc:`$hfind </identifiers/hfind>`

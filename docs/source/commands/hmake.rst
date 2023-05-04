/hmake
======

The **/hmake** command can be used to create a new hash table by a specific handle name.

A hash table is stored entirely in memory and thus it is the programmer's responsibility to save the data to a file if necessary via the :doc: `/hsave </commands/hsave>` command (and load it back later via the :doc: `/hload </commands/hload>` command).

It's generally best to have the number of buckets be a prime number, and starting with v7.53 mIRC started forcing the buckets to be either 1 or a prime number. Prior to that, mIRC only incremented the buckets to avoid an even number. The default parameter for number of buckets is 100, with allowed values from 1 to 10000. The old behavior was to increment those to the odd 101 or 10001. Current behavior increments 2+ if it's needed to make the buckets be a prime number, so the default 100 increases to the prime 101, and 10000 max increases to the prime 10007.

A hash table name was formerly limited to 256 significant characters - any additional characters were simply ignored. Starting with v7.53 the limit is now 612 characters. ( :doc: `$maxlens </identifiers/$maxlens>` 's 512+100) In mIRC, a hash table is a much faster alternative to ini and normal text files. (Rephrase or Citation needed. hashtable

.. note:: For most practical purposes, if wanting to lessen the chance of more than 1 item per bucket, it's best to keep the ratio of <item count>:<maximum capacity> at 78% to maintain a good time-space tradeoff (i.e. 0.78 load factor). That means if you are planning on storing 78 items in the hash table, you should create a hash table with the size of 100 buckets. (A table of 1000 buckets is good to store up to about 780 items to maintain a maximum performance). The general equation to calculate optimal number of buckets is:

* [#_of_buckets] = [#_of_keys_that_will_be_used] / 0.78
Linked List
-----------

Because the hash table uses chaining to resolve collisions and due to the fact mIRC does not rehash or grows the array, using a hash table created with 1 bucket can be used to create a linked list. New items are added to the start of the chain (i.e. $hget(<table_name>, 1) will always be last item added). Additionally, changing the value or removing an item does not alter the overall order of the list.

Synopsis
--------

.. code:: text

    /hmake [-smNhL] <table_name> [num_buckets]

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -s
      - displays a successful creation, or reports the table already exists
    * - -mN
      - Specify the number of bucket, same as the N parameter.
    * - -hL
      - - Specify the name of the algorithm to be used for the hash function for this table, the value of L is a letter, it can be:

** **r** - rot

** **f** - fnv1a

** **l** - lookup3

** **m** - murmur3

** **x** - xxhash

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <table_name>
      - The name of the table you wish to make.
    * - [num_buckets]
      - The number of buckets to use as the table's capacity (If no number is specified, the default is 100 (effectively 101 buckets))

Example
-------

A basic usage for a hash table.

.. code:: text

    ; call the setup once
    ; /abbr_setup
    ;
    ; //echo -a $abbr(lol)
    ;
    alias abbr_setup {
    ;create the table
    hmake abbr 1000

    ; populate the table
    hadd abbr lol laughing out load
    hadd abbr omg oh my gosh
    hadd abbr lmao laughing my a?? off
    hadd abbr brb be right back

    ; ...
    }
    ; get the abbreviation
    alias abbr return $hget(abbr, $1)

Because a hash table of 1 buck is the same as a linked list, we can easily implement an almost-native stack data structure.

.. code:: text

    ;/stack_example
    ; Output:
    ; poped: DDD
    ; poped: CCC
    ; poped: BBB
    ; poped: AAA
    alias stack_example {
    ; create a linked-list
    hmake stack 1

    ; push items
    push stack AAA
    push stack BBB
    push stack CCC
    push stack DDD

    ; pop everything
    while ($pop(stack)) {
    echo -a poped: $v1
    }

    ; delete linked-list
    hfree stack
    }
    alias push {
    ; keep a counter so we keep a unique key each time
    if (!$hget($1,0).item) hadd $1 counter 1
    else hadd $1 counter $calc($hget($1, counter).data + 1)

    ; make it the first item
    hadd $1 key. $+ $hget($1, counter).data $2
    }
    alias pop {
    if ($hget($1, 1).item != counter && $hget($1, 1).data) {
    ; delete the item
    hdel $1 $hget($1, 1).item
    ; return value
    return $v1
    }
    }

* Demonstrates how table items are accessed by $hget(table,N) in reverse order of creation if table created with 1 bucket. Changing the hmake command to use a larger number of buckets causes the items to be associated with N in a non-sequential pattern:

.. code:: text

    //hfree -sw test | hmake -s test 1 | var %i 1 | while (%i isnum 1-10) { hadd test item $+ $base(%i,10,10,3) data | inc %i } | var %n 1 | while ($hget(test,%n).item) { echo -a $ord(%n) itemname is $v1 | inc %n }

* Through v7.52, demonstrates that the number of buckets is always an odd number. An even number of buckets and even+1 arrange the items in the same sequence. (This was true through v7.52 where $hget(tablename).size reported the buckets parameter used to create the table instead of the actual number of buckets. Beginning v7.53 the number of buckets is reported correctly, and now uses the prime number >= size parameter while allowing buckets=1. The max N for the buckets parameter is 10000, which uses the next available prime, 10007.

.. code:: text

    //hfree -sw test | hmake -s test 2 | var %i 1 , %a | while (%i isnum 1-999) { hadd test item $+ $base(%i,10,10,3) data | inc %i } | var %n 1 | while ($hget(test,%n).item) { var %a $sha1(%a $v1) | inc %n } | echo -a hash of item sequence %a

* Demonstrates that it can be 10x faster to create a hashtable containing 9999 items than to create 9999 local %variables:

.. code:: text

    //hfree -sw test | hmake -s test | var %i 9999 , %ticks $ticks | while (%i) { var %test $+ %i data %i | dec %i } | echo 4 -a done $calc($ticks - %ticks) ticks
    //hfree -sw test | hmake -s test | var %i 9999 , %ticks $ticks | while (%i) { hadd test %i data %i | dec %i } | echo 4 -a done $calc($ticks - %ticks) ticks

*It can be simpler to access dynamically named items from hash tables because hash tables don't require using $eval or [ braces ] to access the value in a hashtable item.

.. code:: text

    //var -s %nick foobar , %flood. $+ %nick $ticks , %test %flood. [ $+ [ %nick ] ]
    vs
    //var %nick foobar | hadd -sm flood %nick $ticks | echo -a %nick is $hget(flood,%nick)

To use hash tables instead of variables, there are a few extra differences to be aware of.
* You can receive $null from a $hget(no-such-table,item) or $hget(existing-table,no-such-item) without an error
* But you cannot create an item without first making sure that the table exists. If it's possible for the table to not exist, you can use /hadd's -m or -mN switch to create the table if needed.
* You cannot use the /hmake command to create a table without making certain the table does not already exist.

.. code:: text

    //if (!$hget(tablename)) hmake tablename

* You cannot delete a tablename with /hfree unless you make certain the table already exists, or use the -w switch without a wildcard

.. code:: text

    //if ($hget(tablename)) hfree tablename
    or
    /hfree -sw tablename

* The equivalent to /unset is /hdel, which can accept wildcards
* To retrieve data from a hashtable item:

.. code:: text

    //echo -a %variablename is the same as $hget(tablename,itemname)

* To check for the existence of a variable, scripts currently check if $var(%NonWildcardVariablName,1) is $null. To check if the item name exists, check if $hfind(tablename,itemname) is $null.

.. note:: that $hfind is able to do things $var() cannot do, such as finding items based on the wildcard or regex pattern of the itemnames or the data inside them.

* hashtables do not have the same global vs local scope as %variables do. While it's possible to use %var inside an alias to mask the value of a same-name global variable, you cannot do this with hashtables. While a local variable can be seen only inside the alias or :EVENT: where it was created, hashtables and their items are created only with global scope.
* mIRC handles saving global %variables to disk for you, but it doesn't do that with hashtables. If you need to save updated hashtable data for the next mIRC restart, you must use /hsave to save it to disk, then must use /hload to retrieve it after restart.
* As with %variables, hashtable items can be created with similar temporary status, but does not offer the same syntax, and not all features.
* Temporary item existing for 5 seconds:

.. code:: text

    //hadd -mu5 test item | echo -a $hget(test,item).unset | timer 5 1 echo -a $!hget(test,item).unset

.. note:: that items created or updated using the -uN property are by default not saved to disk without using /hsave's -u switch.

* Using -k to ignore the N in -uN only if the .unset is already non-zero

.. code:: text

    //hadd -mku5 test item | echo -a $hget(test,item).unset | timerx1 5 1 echo -a $!hget(test,item).unset | timerx2 1 2 hadd -ku10 test item

* -z decrements item each second. This example deletes item whenever the first of; either the item value reaching zero or the .unset time reaches zero:

.. code:: text

    //hadd -mku5z test item $rand(3,9) | timerx1 5 1 echo -a unset $!hget(test,item).unset value $!hget(test,item)

* There is no -e flag to 'delete on exit', but you can do the equivalent by setting a very long -uN time.

.. code:: text

    //set -e %varname 1 | hadd -mu $+ $calc(2^31-1) table item | echo -a $var(%varname,1).secs vs $hget(table,item).unset

* hinc and hdec have the same -c switch as /inc|/dec to inc or dec the value each second

.. code:: text

    //hfree -w test | hinc -mcu5 test item-hinc 5 | hdec -cu5 test item-hdec-c 5 | timerx1 5 1 echo -a item-hinc $!hget(test,item-hinc) item-hdec $!hget(test,item-hdec-c)

If needing items to always be in a predictable sequence, you can't count on using /hsave and /hload to preserve that order. **These series of commands should be pasted separately in sequence, as a demonstration of each bullet point.** When using buckets=1...
* Items listed in reverse order of creation. 1st created item is $hget(table,N) where N is the number of items in the table. i.e. $hget(table, $hget(table,0).item )

.. code:: text

    //hfree -sw test | hmake -s test 1 | var %i 1 | while (%i <= 10) { hadd test item $+ %i data | inc %i } | var %N 1 | while ($hget(test,%N).item) { echo 4 -a $ord(%N) item is $hget(test,%N).item | inc %N }

* When /hsave writes items to disk, they're written to disk in sequential N order, where the last created item in $hget(table,1) position is written first.

.. note:: pad test.dat</source>

* When /hload adds items from disk, it adds them in sequential order with the 1st item on disk added first, and the last item on disk added last. If the item name already exists in the table, it retains its current Nth position in the table, but all new additions are again added into reverse order of creation, where the final added item is in the $hget(table,1) position.

.. code:: text

    //hfree -w test2 | hadd -sm1 test2 item5 | hload -sm1 test2 test.dat | var %i 1 | while ($hget(test2,%i).item) { echo -a the $ord(%i) item is $hget(test2,%i).item | inc %i }

* If an item is deleted then added, it is moved to the $hget(table,1) position

.. code:: text

    //hdel -s test2 item7 | hadd -s test2 item7 | var %i 1 | while ($hget(test2,%i).item) { echo -a the $ord(%i) item is $hget(test2,%i).item | inc %i }

* To retain the original sequence where the original order of creation is preserved except in cases where items are deleted then added, giving them a newer creation order, you cannot simply /hsave the table ON EXIT then /hload ON START. During ON START you would either need to /hload + /hsave + /hfree + /hload which does extra disk writing:

.. code:: text

    //hfree -w test2 | hload -sm1 test2 test.dat | hsave test2 test2.dat | hfree -w test2 | hload -sm1 test2 test2.dat | var %i 1 | while ($hget(test2,%i).item) { echo -a the $ord(%i) item is $hget(test2,%i).item | inc %i }

* or /hload the table into a dummy table, from which you re-add them from 'dummy' to the 'real' table in the N=1-to-total sequence, giving the 'real' table the same 'reverse order of creation' order:

.. code:: text

    //hfree -w dummy | hfree -w test2 | hload -sm1 dummy test.dat | hmake -s test2 1 | var %i 1 | while ($hget(dummy,%i).item) { hadd -s test2 $v1 $hget(test2,$v1) | inc %i } | var %i 1 | hadd test2 newestitem | while ($hget(test2,%i).item) { echo -a the $ord(%i) item is $hget(test2,%i).item | inc %i }

    .. note:: If your table is in binary format, you need to preserve binary data by replacing

    hadd -s test2 $v1 $hget(test2,$v1)
    with
    noop $hget(dummy,$v1,&temp) | hadd -b test2 $v1 &temp

Compatibility
-------------

Added: mIRC v5.8 (14 Dec 2000)
See also
--------

.. hlist::
    :columns: 4

    * :doc: `/hfree </commands/hfree>`
    * :doc: `/hload </commands/hload>`
    * :doc: `/hsave </commands/hsave>`
    * :doc: `Hash Tables </intermediate/data_storage.html#hash-tables>`
    * :doc: `/hadd </commands/hadd>`
    * :doc: `/hdel </commands/hdel>`
    * :doc: `/hinc </commands/hinc>`
    * :doc: `/hdec </commands/hdec>`
    * :doc: `$hget </identifiers/$hget>`
    * :doc: `$hfind </identifiers/$hfind>`

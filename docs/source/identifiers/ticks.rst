$ticks
======

$ticks retrieves the number of milliseconds that have elapsed since the system was uptime|started. $ticks is most often used in benchmarking.

Details
-------

The $ticks identifier is used to retrieves the current system uptime in milliseconds. The identifier is limited to the resolution of the system timer which is typically in the range of 10 milliseconds to 16 milliseconds. Prior to mIRC version 7.33 the $ticks identifier used the GetTickCount - Win32|GetTickCount() function which meant the value $ticks returned would wrap around to zero after 49.71 days. In 7.33 the $ticks identifier was switched to use the GetTickCount64 - Win32|GetTickCount64() function, eliminating this issue (which wraps around once every 584.9 million years).

Synopsis
--------

.. code:: text

    $ticks

Parameters
----------

None

Properties
----------

None

Example
-------

.. code:: text

    ; time how long it takes to execute an empty loop 10,000 times.
    Alias example {
      var %ticks = $ticks, %x = 10000
      
      while (%x) {
        dec %x
      }
      
      echo -a 10,000 empty iterations took: $calc($ticks - %ticks) ms.
    }

As an example of the limited precision of $ticks, you can see from the following command that during an interval of 1000 milliseconds where the current $ticks result is continually added to a tokenized list, that it does not create a list of 1000 items, but instead creates a list of approximately 65 numbers which are generally separated by around 15-16.

.. code:: text

    //var %end $ticks + 1000 , %list | while ($ticks < %end) var %list $addtok(%list,$ticks,32) | echo -a $numtok(%list,32) items: %list

This means that scripts which use $ticks to create a unique name for a timer or a COM call can easily fail. If you need a fast way to create a unique string, you can use something like:

.. code:: text

    alias unique { hinc -m unique sequential | return $hget(unique,sequential) }

... where $unique always returns a different sequential number as long as the hashtable is not tampered with, and if the number does not reach $calc(2^53)<press tab key>.

Compatibility
-------------

.. compatibility:: 4.7

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$ctime </identifiers/ctime>`
    * :doc:`$timer </identifiers/timer>`
    * :doc:`$ctimer </identifiers/ctimer>`
    * :doc:`$time </identifiers/time>`
    * :doc:`$date </identifiers/date>`
    * :doc:`$gmt </identifiers/gmt>`
    * :doc:`$asctime </identifiers/asctime>`
    * :doc:`/noop </commands/noop>`

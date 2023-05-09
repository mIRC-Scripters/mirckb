$ticksqpc
=========

$ticksqpc uses QueryPerformanceCounter() to retrieve a high-resolution passage of time in milliseconds that approximates the time since the system was started. $ticksqpc is most often used in benchmarking scripts.

Details
-------

The $ticksqpc allows scripts to detect the passage of milliseconds of time more accurately than the $ticks number that's limited to the resolution of the system timer which is typically in the range of 10 milliseconds to 16 milliseconds intervals..

Synopsis
--------

.. code:: text

    $ticksqpc

Parameters
----------

None

Properties
----------

None

Example
-------

When benchmarking this script using $ticks, it returns either 0 or 16 for 'time1' due to the long interval of the system timer's resolution. For 'time2' which uses $ticksqpc, the answer is somewhere between the 0 and 16 extremes, and repeating this alias has a result which won't vary as much as $ticks does.

* /timer 10 1 example

.. code:: text

    ; time how long it takes to execute an empty loop 10,000 times.
    Alias example {
      var %i 500 , %ticks $ticks    | while (%i) { dec %i } | echo -a time1: $calc($ticks    - %ticks)
      var %i 500 , %ticks $ticksqpc | while (%i) { dec %i } | echo -a time2: $calc($ticksqpc - %ticks)
    }

.. note:: This is *NOT* a replacement for $ticks, and should not be used interchangeably with $ticks. While it returns a value very close to that of $ticks, it is calculated in a different manner, and the result slowly diverge further away from $ticks as the computer uptime increases. While ($ticks /1000) is very close to $ctime, that's not the case for ($ticksqpc /1000).

The source for the returned time value is QueryPerformanceCounter. QPC originally was similar to a counter for the number of cpu cycles since bootup. The rate at which it increased per second was QPF - QueryPerformanceFrequency - approximately 1/1000th of the gigahertz rating for the cpu. However, beginning with Win10 1809, QPF was changed to be 10 million regardless of the cpu's speed.

In order to have $ticksqpc return a milliseconds value instead of something that changes in the millions per second, it would need to obtain the QPF value and use that as a divisor. At least on Win 7 - where the $ticksqpc value would be something like (1000 * QPC/QPF) or (QPC / (QPF/1000)) - the value for $ticks and $ticksqpc are fairly well synchronized near bootup time, but as uptime increases the results drift further apart.

However, the $ticksqpc value is perfectly fine for benchmarking scripts with the expectation of getting a time value that's more accurate than being a multiple of 16 milliseconds. In the short term, the result of $calc($ticks - $ticksqpc) appears to fluctuate wildly, but that's because $ticksqpc is returning a more accurate passage of time, while the $ticks value is returning a value which may or may not have advanced by 16ms.

For fine-tuning benchmarks which have very short intervals, you should make the script wait until the time value has incremented before using that as the start-time. This first example counts how many times the while() loops within a millisecond. However, it will return results which fluctuate wildly because your command could have begun near the beginning or ending of that millisecond interval.

.. code:: text

    //var %count 0 , %t $ticksqpc | while (%t == $ticksqpc) inc %count | echo -a loops: %count

For a more accurate benchmark, you should use the above as a way to begin the milliseconds interval before then beginning your 'true' benchmark time. Note how this next variant has an occasional hiccup, but most of the time it returns a number in a very narrow range:

.. code:: text

    //var %t $ticksqpc | while (%t == $ticksqpc) noop | var %t $ticksqpc , %count 0 | while (%t == $ticksqpc) inc %count | echo -a loops: %count

Compatibility
-------------

.. compatibility:: 7.64

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$ticks </identifiers/ticks>`
    * :doc:`$ctime </identifiers/ctime>`
    * :doc:`$timer </identifiers/timer>`
    * :doc:`$ctimer </identifiers/ctimer>`
    * :doc:`$time </identifiers/time>`
    * :doc:`$date </identifiers/date>`
    * :doc:`$gmt </identifiers/gmt>`
    * :doc:`$asctime </identifiers/asctime>`
    * :doc:`/noop </commands/noop>`
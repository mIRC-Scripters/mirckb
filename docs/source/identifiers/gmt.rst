$gmt
====

$gmt return the current GMT time value in :doc:`$ctime </identifiers/ctime>` format. $gmt also accept optional time and/or format parameters, displaying the same format as :doc:`$asctime </identifiers/asctime>`, adjusted by $timezone/$daylight settings.

Synopsis
--------

.. code:: text

    $gmt
    $gmt(date [,format])

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - no parameters!
      - Returns ctime adjusted by the $timezone value
    * - date 
      - Optional ctime number, overrides the default ctime. Returns the GMT time string in $asctime format. Ignores any fractions.
    * - format
      - Optional format letters same as for :doc:`$asctime </identifiers/asctime>`

Properties
----------

None

Example
-------

.. code:: text

    //echo -a $gmt($ctime) is the same as $asctime($calc($ctime + $timezone  ) )
    //echo -a $gmt is same as $calc( $ctime + $timezone )
    //echo -a Current GMT is $gmt($ctime, ddd dd mmmm yyyy hh:nn:sstt)

Beginning v7.56, changes made to $gmt are:
1. The z|zz|zzz format strings now return the string for GMT zone instead of the user's zone.
2. Fixed bug where $gmt(number) handled all dates as if they were during the same $daylight zone as the current date, resulting in different output for $gmt(0), for most people, when script is run in January vs June.

.. code:: text

    //echo -a $gmt($calc(0+$iif($version isnum 7.56-,0,$daylight))) is Thu Jan 01 00:00:00 1970

3. New API recognizes larger date range. N can now be numbers which resolve to 1 second after midnight at the beginning of year 1601, through 1 second prior midnight at the end of the last day of year 9999. Returns $null of N is outside that range.

.. code:: text

    //echo -a $gmt($calc(0-86400*365.25*369+86400*3.25+1))) is Mon Jan 01 00:00:01 1601
    //echo -a $gmt($calc(0+86400*365.25*(9999-1970)+86400*304.75-1))) is Fri Dec 31 23:59:59 9999
    valid range is -11644473599 through +253402300799

Compatibility
-------------

.. compatibility:: 5.5

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$asctime </identifiers/asctime>`
    * :doc:`$date </identifiers/date>`
    * :doc:`$adate </identifiers/adate>`
    * :doc:`$time </identifiers/time>`
    * :doc:`$ctime </identifiers/ctime>`
    * :doc:`$fulldate </identifiers/fulldate>`
    * :doc:`$ticks </identifiers/ticks>`
    * :doc:`$day </identifiers/day>`
    * :doc:`$daylight </identifiers/daylight>`
    * :doc:`$timezone </identifiers/timezone>`
    * :doc:`$duration </identifiers/duration>`
    * :doc:`$uptime </identifiers/uptime>`

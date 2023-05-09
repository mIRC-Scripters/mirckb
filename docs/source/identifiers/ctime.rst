$ctime
======

$ctime allows you to retrieve the amount of seconds elapsed since 00:00:00 GMT, January 1, 1970 based on your system time.

Optionally, you can request the amount of seconds elapsed between 00:00:00 GMT, January 1, 1970 and a specified time.

Synopsis
--------

.. code:: text

    $ctime
    $ctime(text)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - text
      - The text can be any date for which you would like to find the $ctime.

Examples
--------

.. code:: text

    Echo the current $ctime to the active window
    //echo -a $ctime
    Echo the $ctime of a specfic date and time to the active window
    //echo -a $ctime(Thursday 2003-01-09 21:16)
    
    Accepts a variety of formats, but n/n/n string is *always* day/month/year format:
    //echo -a $ctime(January 1 1970 00:00:00) $ctime(3rd August 1987 3:46pm) $ctime(21/4/72 1:30:37) $ctime(Wed 1998-3-27 21:16)
    
    When text is a date only, without a time, the $ctime returned is for the current time on that day.
    
    $ctime returned for a fixed time string varies according to your computer's timezone and daylight saving settings:
    //echo -a Regardless of timezone/daylight settings $ctime(2/1/70 0:0) = 86400 + $timezone + $daylight
    
    Prior to 7.52 beta, max valid ctime as input to $asctime is 2^32-1, but max timestring as input to $ctime is 2^32-2:
    //echo -a $ctime(Mon Jan 18 21:14:06 2038) is the max ctime returned from number string
    
    With introduction of 64bit time related variables, the max time string is the time string which returns 32535244798.
    For USA Pacific zone this is $ctime(31/12/3000 23:59:58) and varies by an hour +east or -west of that zone.
    
    From v7.37 through v7.52, returns ctime too high by 1 month when time string is the last second of any year:
    //var %i 1970 | while (%i isnum 1970-2038) { var %a $ctime(31/12/ $+ %i 23:59:59 ) | if (*Jan 31 23:59:59* !iswm $asctime(%a)) echo -a year %i vs $v2 | inc %i }

Compatibility
-------------

.. compatibility:: 5.4

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$asctime </identifiers/asctime>`
    * :doc:`$date </identifiers/date>`
    * :doc:`$adate </identifiers/adate>`
    * :doc:`$time </identifiers/time>`
    * :doc:`$fulldate </identifiers/fulldate>`
    * :doc:`$gmt </identifiers/gmt>`
    * :doc:`$ticks </identifiers/ticks>`
    * :doc:`$day </identifiers/day>`
    * :doc:`$daylight </identifiers/daylight>`
    * :doc:`$timezone </identifiers/timezone>`
    * :doc:`$duration </identifiers/duration>`
    * :doc:`$uptime </identifiers/uptime>`

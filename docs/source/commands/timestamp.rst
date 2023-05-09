/timestamp
==========

The /timestamp command can be used to enable and disable timestamps as well as set their formats.

The -g and -f switches can only be used to set new formats.

Synopsis
--------

.. code:: text

    /timestamp <on|off|default>
    /timestamp [-sae] <on|off|default>
    /timestamp <on|off|default> [window_name]
    /timestamp -f <format>
    /timestamp -g <format>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -s
      - Turns status window time stamp on or off. This is the same as specifying "Status Window" for [window_name]
    * - -a
      - Turns timestamp on or off for the active window
    * - -e
      - Turns timestamp on or off for all windows
    * - -f
      - Sets timestamp format
    * - -g
      - Sets log timestamp format

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <on|off>
      - Turns logging on or off
    * - [window_name]
      - The name of the window to apply the settings to
    * - <format>
      - The new timestamp format

Formats
-------

Seconds:

.. code:: text

    s       Seconds, no leading zeros              0 to 59
    ss      Seconds, with leading zeros            00 through 59

Minutes:

.. code:: text

    n       Minutes, no leading zeros              0 to 59
    nn      Minutes, with leading zeros            00 to 59

Hours:

.. code:: text

    h       12-hour format of an hour, no          1 through 12
            leading zeros
    hh      12-hour format of an hour, with        01 through 12
            leading zeros
    H       24-hour format of an hour, no          0 through 23
            leading zeros
    HH      24-hour format of an hour, with        00 through 23
            leading zeros

Year:

.. code:: text

    yy      A two-digit representation of a year   98 or 09
    yyyy    A full numeric representation of,      2003 or 2005
            a year

Month:

.. code:: text

    m       Numeric representation of a month,     1 through 12
            without leading zeros
    mm      Numeric representation of a month,     01 through 12
            with leading zeros
    mmm     A short textual representation of a    Jan through Dec
            month
    mmmm    A full textual representation of a     January through December
            month

Day:

.. code:: text

    d       Day of month, no leading zeros         1 to 31
    dd      Day of month, leading zeros            01 to 31
    ddd     A short textual representation of a    Sun through Sat
            day
    dddd    A full textual representation of a     Sunday through Saturday
            day

AM/PM:

.. code:: text

    t       Lowercase Ante meridiem and Post       a or p
            meridiem, single letter                
    tt      Lowercase Ante meridiem and Post       am or pm
            meridiem
    T       Uppercase Ante meridiem and Post       A or P
            meridiem, no leading zeros
    TT      Uppercase Ante meridiem and Post       AM or PM
            meridiem, no leading zeros

Ordinal:

.. code:: text

    oo      Adds ordinal to a numeric              12th or 1st
            representation

TimeZone:

.. code:: text

    z       Difference to Greenwich time,          +0 or -5
            minimal size
    zz      Difference to Greenwich time           +0000 or -0500
    zzz     Difference to Greenwich time           +0100 GMT or -0500 GMT
            with GMT

Example
-------

.. code:: text

    ;set log timestamp
    /timestamp -g [hh:nn - mmoo mmmm, yyyy]
    
    ;turn on status window timestamp
    /timestamp -s on
    ;or (they are both the same)
    /timestamp on Status Window

Compatibility
-------------

.. compatibility:: 3.9

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$timestampfmt </identifiers/timestampfmt>`
    * :doc:`$logstampfmt </identifiers/logstampfmt>`
    * :doc:`$logstamp </identifiers/logstamp>`
    * :doc:`$timestamp </identifiers/timestamp>`
    * :doc:`$asctime </identifiers/asctime>`
    * :doc:`$ctime </identifiers/ctime>`
    * :doc:`$date </identifiers/date>`
    * :doc:`$day </identifiers/day>`
    * :doc:`$daylight </identifiers/daylight>`
    * :doc:`$fulldate </identifiers/fulldate>`
    * :doc:`$gmt </identifiers/gmt>`
    * :doc:`$ticks </identifiers/ticks>`
    * :doc:`$time </identifiers/time>`
    * :doc:`$timezone </identifiers/timezone>`


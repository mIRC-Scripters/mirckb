$timezone
=========

$timezone returns the current timezone setting in seconds. Positive is West/Earlier than UTC, negative is East/Later than UTC.

Synopsis
--------

.. code:: text

    $timezone

Parameters
----------

None

Properties
----------

None

Notes
-----

* $timezone contains the seconds to subtract from UTC to match your computer clock time.
* i.e. $gmt($ctime) == $asctime($calc($ctime + $timezone)), and $asctime($calc(0 + $timezone)) is "Thu Jan 01 00:00:00 1970" except for people whose $timezone is negative because $asctime does not accept negative time values.
* When you change your computer's timezone, the file date/times change, but mIRC's $ctime does not. $file($mircexe).mtime remains the same regardless of $timezone and $daylight values.
* $timezone changes when $daylight changes, so you'll find $timezone + $daylight remain the same total. In USA Eastern, you'll find that during the winter, $timezone is 18000 and $daylight is 0. In summer during Daylight/Summertime, $timezone drops by 3600 to 14400, and $daylight increases from 0 to 3600.

Example
-------

.. code:: text

    //echo -a $timezone

Compatibility
-------------

.. compatibility:: 5.1

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$timestampfmt </identifiers/timestampfmt>`
    * :doc:`$daylight </identifiers/daylight>`
    * :doc:`$gmt </identifiers/gmt>`
    * :doc:`$asctime </identifiers/asctime>`


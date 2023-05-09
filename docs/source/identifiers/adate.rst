$adate
======

$adate returns the current date in USA month/day/year format compared to $date returning day/month/year.

Synopsis
--------

.. code:: text

    $adate

.. note:: Same as $date except does not support optional time/format parameters, and returns date in mm/dd/yyyy format.

Parameters
----------

None

Example
-------

Echo the current date to the active window

.. code:: text

    //echo -a Today in mm/dd/yyyy format is $adate - today in dd/mm/yyyy format is $date

Compatibility
-------------

.. compatibility:: 3.9

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$asctime </identifiers/asctime>`
    * :doc:`$date </identifiers/date>`
    * :doc:`$fulldate </identifiers/fulldate>`
    * :doc:`$time </identifiers/time>`
    * :doc:`$ctime </identifiers/ctime>`
    * :doc:`$gmt </identifiers/gmt>`
    * :doc:`$ticks </identifiers/ticks>`
    * :doc:`$day </identifiers/day>`
    * :doc:`$daylight </identifiers/daylight>`
    * :doc:`$timezone </identifiers/timezone>`
    * :doc:`$duration </identifiers/duration>`
    * :doc:`$uptime </identifiers/uptime>`

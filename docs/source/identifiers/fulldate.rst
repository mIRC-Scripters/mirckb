$fulldate
=========

 $fulldate returns the current full date in the format: "Day Month Date hh:mm:ss Year", and is a duplication of $asctime used without parameters.

Synopsis
--------

.. code:: text

    $fulldate

Parameters
----------

None

Example
-------

.. code:: text

    Echo the full date to the active window:
    //echo -a $fulldate
    
    //if ($asctime  == $fulldate) echo -a These are the same string

Compatibility
-------------

.. compatibility:: 3.9

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$asctime </identifiers/asctime>`
    * :doc:`$date </identifiers/date>`
    * :doc:`$adate </identifiers/adate>`
    * :doc:`$time </identifiers/time>`
    * :doc:`$ctime </identifiers/ctime>`
    * :doc:`$gmt </identifiers/gmt>`
    * :doc:`$ticks </identifiers/ticks>`
    * :doc:`$day </identifiers/day>`
    * :doc:`$daylight </identifiers/daylight>`
    * :doc:`$timezone </identifiers/timezone>`
    * :doc:`$duration </identifiers/duration>`
    * :doc:`$uptime </identifiers/uptime>`

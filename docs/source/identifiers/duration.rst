$duration
=========

The $duration identifier can take a specified number of seconds and return it in weeks/days/hours/minutes/seconds format. After a value has been returned, the new value can even be used with the identifier in order to return the number of seconds.

Accept negative value

Synopsis
--------

.. code:: text

    $duration(seconds,N)

.. code:: text

    $duration(timestring)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Argument
      - Description
    * - seconds
      - The specific number of seconds to get the formatting for
    * - N
      - Can be either 2, which omits seconds from the results, or 3, which returns the time in hh:nn:ss format

Beginning v7.63 correctly handles negative durations.
Example
-------

Echo the formatting for 38711810 seconds:

.. code:: text

    //echo -a $duration(38711810)

Result

.. code:: text

    64wks 1hr 16mins 50secs

.. code:: text

    //echo -a $duration(38711810,2)

Same except does not display the seconds.
Result

.. code:: text

    64wks 1hr 16mins

.. code:: text

    //echo -a $duration(38711810,3)

Returns the display in HH:nn:ss format, with durations longer than 1 day returning hours > 23.
Result

.. code:: text

    10753:16:50

Echo the formatting for converting 64wks 1hr 16mins 50secs back to seconds:

.. code:: text

    //echo -a $duration(64wks 1hr 16mins 50secs)

Result

.. code:: text

    38711810

The displayed timestring contains the time units touching their integers, so you will need to use $replace if you don't wish this:

.. code:: text

    //echo -a This computer restarted $regsubex(foo,$duration($uptime(system,3)),/([a-z]+)/g,$chr(32) $+ \t) ago!

Compatibility
-------------

.. compatibility:: 4.7

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$asctime </identifiers/asctime>`
    * :doc:`$time </identifiers/time>`

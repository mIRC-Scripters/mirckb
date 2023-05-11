$asctime
========

$asctime can be used to return the time and date in an optional text format. The time and date can be taken from the current time, or you can use $asctime to format a date in relation to :doc:`$ctime </identifiers/ctime>`.

Synopsis
--------

.. code:: text

    $asctime[([N,]format)]

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - N
      - This parameter is optional, but normally would point to a value derived from :doc:`$ctime </identifiers/ctime>`.
    * - format
      - This is where the formatting options would go. If you do not specify a :doc:`$ctime </identifiers/ctime>` number N to evaluate, the formatting is performed on the current date and time.

Formatting Options
------------------

+----------+----------+-------------+
| Format   | Property | Result      |
+==========+==========+=============+
| Day      | d        | 1           |
|          +----------+-------------+
|          | dd       | 01          |
|          +----------+-------------+
|          | ddd      | Mon         |
|          +----------+-------------+
|          | dddd     | Monday      |
+----------+----------+-------------+
| Month    | m        | 1           |
|          +----------+-------------+
|          | mm       | 01          |
|          +----------+-------------+
|          | mmm      | Jan         |
|          +----------+-------------+
|          | mmmm     | January     |
+----------+----------+-------------+
| Year     | yy       | 14          |
|          +----------+-------------+
|          | yyyy     | 2014        |
+----------+----------+-------------+
| Hours    | h        | 5           |
|          +----------+-------------+
|          | hh       | 05          |
|          +----------+-------------+
|          | H        | 13          |
|          +----------+-------------+
|          | HH       | 13          |
+----------+----------+-------------+
| Minutes  | n        | 1           |
|          +----------+-------------+
|          | nn       | 01          |
+----------+----------+-------------+
| Seconds  | s        | 1           |
|          +----------+-------------+
|          | ss       | 01          |
+----------+----------+-------------+
| AM/FP    | t        | a/p         |
|          +----------+-------------+
|          | tt       | am/pm       |
|          +----------+-------------+
|          | T        | A/P         |
|          +----------+-------------+
|          | TT       | AM/PM       |
+----------+----------+-------------+
| Ordinal  | oo       | st nd rd th |
+----------+----------+-------------+
| Timezone | z        | +o          |
|          +----------+-------------+
|          | zz       | +oooo       |
|          +----------+-------------+
|          | zzz      | +oooo GMT   |
+----------+----------+-------------+


.. note:: All of the formatting parameters can touch each other, and they will be properly converted. For example: $asctime(hhnnss) would return the ``hours``, ``minutes``, and ``seconds`` all touching each other in a terrible format.

Examples
--------

Echo the current date and time

.. code:: text

    //echo -a $asctime

Echo the current date in the format Month Day, Year

.. code:: text

    //echo -a $asctime(mmmm $+(dd,$chr(44)) yyyy)

Using the $ctime of ``840240070``, format to Day Month Year hour:minute<am/pm>

.. code:: text

    //echo -a $asctime(840240070,dd mmmm yyyy hh:nntt)

Using the orbital format, we can add the proper orbitals to date digits

.. code:: text

    //echo -a $asctime(mmmm $+(doo,$chr(44)) yyyy)

Compatibility
-------------

.. compatibility:: 4.5

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$ctime </identifiers/ctime>`
    * :doc:`$date </identifiers/date>`
    * :doc:`$time </identifiers/time>`


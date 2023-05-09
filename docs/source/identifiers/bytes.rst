$bytes
======

$bytes allows you to format any number that you pass into various byte forms.

Synopsis
--------

.. code:: text

    $bytes(<N>[,bkmgtp3d])[.suf]

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - N
      - The byte number that you wish to format. You can use the letter 'e' or 'd' as ``*10^N, $bytes(5e6) = $bytes($calc(5*10^6))``
    * - b
      - Comma-formats the number for bytes.
    * - k
      - Comma, and decimal-formats the number for kilobytes.
    * - m
      - Comma, and decimal-formats the number for megabytes.
    * - g
      - Comma, and decimal-formats the number for gigabytes.
    * - t
      - Comma, and decimal-formats the number for terabytes.
    * - p
      - Comma, and decimal-formats the number for petabytes.
    * - 3
      - Returns the result in 3-digit format.
    * - d
      - Returns the value whilst retaining decimal point values.

.. note:: if you do not pass any of the bkmgt letter-switches, $bytes will smartly choose the unit, e.g displaying 1KB for 1024 bytes

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - .suf
      - Returns the formatted bytes with the proper suffixes, which are: B, KB, MB, GB, TB, and PB

(last 2 are terabyte and petabyte)
Examples
--------

Echo a large number with comma format to the active window

.. code:: text

    //echo -a $bytes(317889213,b)

Echo a byte value of GB to the active window with the suffix

.. code:: text

    //echo -a $bytes(10000000000,g).suf

When $bytes formats the number without being forced to use a specific suffix, it defaults to choosing a suffix which allows it to be presented as a number having no more than 3 numbers to the left of the decimal, and limits the fraction as no more than 2 digits. It doesn't display the suffix unless the .suf property is used. If the '3' switch is used, the display is modified so that the digits of the fraction also count as part of the 3 numbers, which can result in the fraction being shortened or even eliminated in order to limit the combined digit total to 3. The number is shortened into units of 1024's not 1000's.

Because of float rounding behavior, you cannot count on a completely accurate rounding if the rounding is chopping the '5' digit from the tail end of the fraction. Even for rounding of numbers to the left of the decimal, you should view these results only as an approximation.

This next example shows that a number 6 below 501kb is still being rounded as 500, and $bytes and $round both round this number down instead of rounding to be 11.4

.. code:: text

    //echo -a $round(11.35,1) vs $bytes(11.35,3d) and $bytes($calc(500*1024+1018),3)
    result: 11.3 and 11.3 and 500

The behavior of recognizing $bytes(1e4,b) as ten thousand is probably an incidental behavior similar to the way that other identifiers like $int and $abs also recognize scientific notation.

$bytes is not intended to handle extremely huge numbers, since the greatest suffix it recognizes is PB (terabytes), at which point it stops preventing the result from being presented with fewer numeric digits. There are no plans to give bigfloat support to this identifier, so scripts will need to use $round and string manipulation to achieve this goal. Here is an example demonstrating that $bytes does not have the bigfloat range accuracy, and demonstrates how to display numbers formatted with commas:

//var -s %a.bf $calc(2^127 + $pi), %int $gettok(%a.bf,1,46), %frac $gettok(%a.bf,2,46) | echo -a $bytes(%a.bf,b) | echo -a $regsubex(%int,/([0-9])(?=([0-9]{3})+$)/g,\1 $+ $chr(44)) $+ $iif(%frac != $null,. $+ %frac)

result:
170,141,183,460,469,230,000,000,000,000,000,000,000
170,141,183,460,469,231,731,687,303,715,884,105,731.14159265358979323846264338328
Compatibility
-------------

.. compatibility:: 5.71

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$abs </identifiers/abs>`
    * :doc:`$base </identifiers/base>`
    * :doc:`$calc </identifiers/calc>`

$gcd
====

$gcd returns the Greatest Common Denominator for 2 or more integers.

Details
-------

The Greatest Common Denominator is the largest integer that can be evenly divided into each input number, and is the product of all prime factors shared by all input numbers. Result for (0,0) is zero, but otherwise must always be a positive integer.

Synopsis
--------

.. code:: text

    $gcd(N1,N2[,N3]...)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - N
      - Integers 

Properties
----------

None

Example
-------

.. code:: text

    //var -s %num1 $calc(2*3*5*7*11*13*17*19) , %num2 $rand(11111,99999) | if ($gcd(%num1,%num2) > 1) echo -a %num2 is not a prime because it has a prime factor smaller than 20
    //echo -a $gcd(25,35) is 5 because 5 can be evenly divided into both numbers
    //echo -a $gcd(25,35,42) is 1 because there is no number greater than 1 which can be evenly divided into all 3 numbers

Compatibility
-------------

.. compatibility:: 7.72

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$lcm </identifiers/lcm>`

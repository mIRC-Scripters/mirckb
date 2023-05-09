$lcm
====

$lcm returns the Least Common Multiple for 2 or more integers.

Details
-------

The Least Common Multiple is the smallest positive integer that is divisible by each non-zero input number. For 2 non-zero numbers, the LCM is the absolute value of their product divided by their :doc:`$gcd </identifiers/gcd>`
Synopsis
--------

.. code:: text

    $lcm(N1,N2[,N3]...)

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

    //echo -a the smallest number divisible by each of 35 49 and 75 is $lcm(35,49,75)
    //echo -a the lcm of 35 and 25 is $calc( $abs($calc(35*25)) / $gcd(35,25) )

Compatibility
-------------

.. compatibility:: 7.72

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$gcd </identifiers/gcd>`

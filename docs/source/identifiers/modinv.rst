$modinv
=======

$modinv returns the Multiplicative Modular Inverse for an integer.

Details
-------

For integers (A,M) the Multiplicative Modular Inverse is a non-negative integer B less than M, which when multiplied by 'A' is 1 greater than a multiple of M. The modular inverse has a relationship with the :doc:`$gcd </identifiers/gcd>` where positive integers A and M can have $gcd(A,M) greater than 1, or there can be $modinv(A,M). But you cannot have both and you cannot have neither.
The result of $modinv(A,M) is the same as $powmod(A,-1,M)
Synopsis
--------

.. code:: text

    $modinv(N,modulus)

Returns -1 if no inverse exists
Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - N
      - Integer
    * - modulus
      - divisor used for obtaining the inverse of N

Properties
----------

None

Example
-------

.. code:: text

    //var -s %rand $rand(1,2016) | echo -a the mod inverse ( %rand ,2017) is $modinv(%rand,2017) because $calc( ($modinv( %rand ,2017) * %rand) % 2017 ) is 1
    
    Note: modinv(1,2017) = 1 because (1 * 1) is greater than (0*2017)
    
    //var %i 9 | var %a $rand(1,999) , %m $rand(1,999) | if ($gcd(%a,%m) > 1) echo 4 -a GCD( %a , %m ) = $v1 is greater than 1, so there is no mod inv(A,M): $modinv(%A,%M) | else echo 3 -a GCD( %A , %M ) = $gcd(%a,%m) so there is a mod inverse (A,M) and it is $modinv(%a,%m)

Compatibility
-------------

.. compatibility:: 7.72

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$gcd </identifiers/gcd>`
    * :doc:`$lcm </identifiers/lcm>`
    * :doc:`$powmod </identifiers/powmod>`

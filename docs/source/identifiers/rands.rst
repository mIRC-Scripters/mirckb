$rands
======

$rands returns a "cryptographically secure" random integer from the specified range, using the Microsoft's RtlGenRandom() and SystemFunction036() API. Syntax is exactly the same as for $rand except for the source being different.

Synopsis
--------

.. code:: text

    $rands(number1,number2)
    $rands(char1,char2)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - number1,number2
      - starting/ending range of integers
    * - char1,char2
      - starting/ending characters in range of characters. Valid range $chr(1) through $chr(65535)

Properties
----------

None

Examples
--------

See :doc:`$rand </identifiers/rand>` for examples, as this identifier differs only in the source of the random values.

.. code:: text

    //var %i 999999 , %t $ticks | while (%i) { noop | dec %i } | echo -a ms: $calc($ticks - %t)
    //var %i 999999 , %t $ticks | while (%i) { noop $rand(0,999999999) | dec %i } | echo -a ms: $calc($ticks - %t)
    //var %i 999999 , %t $ticks | while (%i) { noop $rands(0,999999999) | dec %i } | echo -a ms: $calc($ticks - %t)

This shows that only 1/3rd of the time is due to $rand, and the other 2/3rds is the scripting overhead. For the remaining time used by the $rand function, it appears that $rands is around 25% slower than $rand.

Compatibility
-------------

.. compatibility:: 7.55

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$rand </identifiers/rand>`

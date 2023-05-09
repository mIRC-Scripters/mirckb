$ifmatch2
=========

.. attention:: This feature has essentially been replaced by :doc:`$v2 </identifiers/v2>`

$ifmatch2 return the second part of the last conditional statement made.

Synopsis
--------

.. code:: text

    $ifmatch2

Parameters
----------

None

Properties
----------

None

Notes
-----

Just like $v1 $v2 and $ifmatch, this identifier return the value from the very last statement made:

.. code:: text

    alias test return $iif($1 == 1,1,2)
    alis testing if (a != b) echo -a $test(1) $ifmatch2

This will echo 1 as $ifmatch2 because $test is evaluated before $ifmatch2, so the $iif is the last statement made when $ifmatch2 evaluates.

Example
-------

.. code:: text

    //if (a != b) echo -a $ifmatch2

Compatibility
-------------

.. compatibility:: 5.4

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$ifmatch </identifiers/ifmatch>`
    * :doc:`$v1 </identifiers/v1>`
    * :doc:`$v2 </identifiers/v2>`
    * :doc:`/if </commands/if>`
    * :doc:`/while </commands/while>`

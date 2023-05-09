$ifmatch
========

.. attention:: This feature has essentially been replaced by :doc:`$v1 </identifiers/v1>`

$ifmatch return the first part of the last conditional statement made.

Synopsis
--------

.. code:: text

    $ifmatch

Parameters
----------

None

Properties
----------

None

Notes
-----

Just like $v1 $v2 and $ifmatch2, this identifier return the value from the very last statement made:

.. code:: text

    alias test return $iif($1 == 1,1,2)
    alis testing if (a != b) echo -a $test(1) $ifmatch

This will echo 1 for $ifmatch because $test is evaluated before $ifmatch, so the $iif is the last statement made when $ifmatch evaluates.

Example
-------

.. code:: text

    //if (a != b) echo -a $ifmatch

Compatibility
-------------

.. compatibility:: 5.4

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$ifmatch2 </identifiers/ifmatch2>`
    * :doc:`$v1 </identifiers/v1>`
    * :doc:`$v2 </identifiers/v2>`
    * :doc:`/if </commands/if>`
    * :doc:`/while </commands/while>`

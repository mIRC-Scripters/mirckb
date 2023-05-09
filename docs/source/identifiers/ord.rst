$ord
====

$ord appends "st", "nd", "rd", or "th" as appropriate, to the number N.

Synopsis
--------

.. code:: text

    $ord(N)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - N
      - The number

Properties
----------

None

Example
-------

.. code:: text

    //echo -a $ord(3)

Rules:
# If number ends with 11 12 or 13, suffix is th
# If number ends with 1        the suffix is st
# If number ends with 2        the suffix is nd
# If number ends with 3        the suffix is rd
# All other numbers end with th, including zero.

This code shows that following these 5 rules produces the same output as letting mIRC calculate the Ordinal. It repeatedly hashes a string consisting of the previous hash combined with the $ord of the next number, and both methods produce the identical hash:

.. code:: text

    //var %a , %a2 , %i 0 | while (%i isnum 0-999) { if ($istok(11 12 13,$right(%i,2),32)) var %ord th | elseif ($findtok(1 2 3,$right(%i,1),1,32)) var %ord $gettok(st nd rd,$v1,32) | else var %ord th | var %a $sha1(%a %i $+ %ord) , %a2 $sha1(%a2 $ord(%i)) | inc %i } | echo -a %a , %a2

For fractions, the $ord uses the last 1 or 2 digits of the fraction.

.. code:: text

    //echo -a $ord(2.1) and $ord($pi)

Compatibility
-------------

.. compatibility:: 5.61

See also
--------

.. hlist::
    :columns: 4


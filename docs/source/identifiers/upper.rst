$upper
======

$upper returns text in upper case

Synopsis
--------

.. code:: text

    $upper(text)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - text
      - the text you want in uppercase
Properties
----------

None

Example
-------

.. code:: text

    //echo -a $upper(ab)

.. note:: A-Z and a-z are the only ranges of characters which the == and != operators consider to be case-insensitive equivalents of each other. However $upper $lower $isupper and $islower and the operators isupper and islower also consider 1894 codepoints in the range 192-65535 to have an uppercase or lowercase versions of themselves. This next command displays 1946 lines showing all codepoints affected by either $upper or $lower:

.. code:: text

    //var %i 1 , %c 0 | while (%i isnum 1-65535) { var -p %a $chr(%i) , %v1 %a %a , %v2 $upper(%a) $lower(%a) | if (%v1 !=== %v2) { inc %c | echo -a $ord(%c) codepoint %i is $chr(%i) upper is codepoint $asc($upper(%a)) $upper(%a) lower is codepoint $asc($lower(%a)) $lower(%a) } | inc %i }

If you edit the above command by changing !=== to != you can see the display shows 1894 rows instead of 1946. The difference is caused by the case-insensitive != operator viewing only the A-Z a-z ranges among those affected by $upper or $lower to be case-insensitive equivalents of each other.

If it's essential that your code changes ONLY the A-Z a-z ranges, use the aliases below. If you edit the above command to use $upper26() and $lower26() in place of $upper() and $lower(), the 1946-line display changes to show only the 52 characters in the A-Z a-z ranges:

.. code:: text

    //echo -a $upper($chr(233)) vs $lower($chr(233))
    result: É vs é
    //echo -a $upper26($chr(233)) vs $lower26($chr(233))
    result: é vs é

.. code:: text

    alias upper26 { returnex $regsubex($1,/([a-z])/g,$chr($calc($asc(\t) -32))) }
    alias lower26 { returnex $regsubex($1,/([A-Z])/g,$chr($calc($asc(\t) +32))) }

Compatibility
-------------

.. compatibility:: 4.5

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$lower </identifiers/lower>`
    * :doc:`$isupper </identifiers/isupper>`
    * :doc:`$islower </identifiers/islower>`
* {{mIRC|operators}}


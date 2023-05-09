$max
====

$max returns the maximum from a list of tokens. $min and $max are effectively a short-cut to returning either the first or last token from a $sorttok list, and uses different .prop settings to replicate the different switches used by $sorttok. By default, $min and $max sort the tokens with the same rules used by the $sorttok 'n' switch.

Synopsis
--------

.. code:: text

    $max(<space delimited tokens>)
    $max(<comma,delimited,tokens>)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <list>
      - If only 1 parameter is passed, that parameter must be a list of tokens space delimited. Otherwise each parameter passed represent an element in the list.

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - .text
      - sorts tokens using the same text sorting rules used by $sorttok 'a' switch
    * - .textcs
      - sorts tokens using the same text sorting rules used by $sorttokcs 'a' switch
    * - .nick
      - sorts tokens using the same text sorting rules used by $sorttok 'c' switch

Examples
--------

.. code:: text

    //echo -a $max(11 2 3 5 8 13) $max(11,2,3,5,8,13)

.. code:: text

    //echo -a $max(c C).text vs $max(c C).textcs

Returns "c vs C" because, as case-insensitive text, 'C' and 'c' are the same, so the leftmost of the pair is returned.

Numeric sorting rules recognize exponential, so $man(1e2 1d2) handles both of them as 100.

.. code:: text

    //echo -a $max( 1:black 02:blue 14:grey 3:green 13:magenta 5:maroon 6:purple 04:red 7:tan 8:yellow 0:white)

result: 0:white

Compatibility
-------------

.. compatibility:: 7.62

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$sorttok </identifiers/sorttok>`
    * :doc:`$sorttokcs </identifiers/sorttokcs>`
    * :doc:`$gettok </identifiers/gettok>`
    * :doc:`$min </identifiers/min>`

$replacex
=========

$replacex Performs search/replace on text strings, but doesn't replace what's already been replaced. $replacexcs is the case sensitive version.

.. note:: $replace search each substring seperately, $replace(1234,234,z,123,u) is 1z, "234" was first checked against "1234" and then "123" isn't even checked because we reached the end of the string. But $replacex does not work like that, $replacex(1234,234,z,123,u) is u4, because the main loop is done on the input string, trying for each position to match any of the substring, so 123 is found first.

Synopsis
--------

.. code:: text

    $replacex(text, substring, replace, stringN, replaceN)
    $replacexcs(text , substring, replace, stringN, replaceN)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - text
      - The string you want to replace from
    * - substring
      - The 1st string you want to search for
    * - replace
      - the replacement for the 1st string
    * - substringN
      - The Nth string you want to search for
    * - replaceN
      - the replacement for the Nth string

.. note:: Excluding the first parameter (input string), there must be an even number of substring/replace parameters

Properties
----------

None

Examples
--------

.. code:: text

    //echo -a $replacex(abc,ab,c,cc,d) vs $replace(abc,ab,c,cc,d)

Compatibility
-------------

.. compatibility:: 6.15

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$replace </identifiers/replace>`
    * :doc:`$regsub </identifiers/regsub>`
    * :doc:`$regsubex </identifiers/regsubex>`

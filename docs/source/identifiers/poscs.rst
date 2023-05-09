$poscs
======

$poscs returns the case-sensitive position of the Nth substring within a text string. :doc:`$pos </identifiers/pos>` is the case-insensitive version.

Synopsis
--------

.. code:: text

    $poscs(text,substring [,N] )

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - %var/text
      - The string being searched
    * - substring
      - The string being searched for within text string
    * - N
      - The Nth occurrence of substring being searched for. Default is 1 if parameter not used.

*  Note: N=0 returns count of string's occurrences. Returns $null if Nth substring not found.

Switches
--------

None

Examples
--------

Compatibility
-------------

.. compatibility:: 5.71

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$pos </identifiers/pos>`
    * :doc:`$mid </identifiers/mid>`
    * :doc:`$left </identifiers/left>`
    * :doc:`$right </identifiers/right>`

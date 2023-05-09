$flinen
=======

$flinen returns the number of the line matching with $fline, which is meant to be used when you use the .text property of $fline().

.. note:: $flinen has a global value like $readn, always returning the value for the last search. Returns 0 if no search has been made, or if the most recent search failed to find a match.

Synopsis
--------

.. code:: text

    $flinen

Parameters
----------

None

Properties
----------

None

Example
-------

.. code:: text

    //echo -a $fline($chan(1),*mirc*) $flinen

Compatibility
-------------

.. compatibility:: 7.59

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$sline </identifiers/sline>`
    * :doc:`$line </identifiers/line>`
    * :doc:`$window </identifiers/window>`
    * :doc:`$fline </identifiers/fline>`

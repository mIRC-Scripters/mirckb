$mknickfn
=========

$mknickfn creates a valid filename from a nickname by removing characters which are not valid in a filename from text.

Synopsis
--------

.. code:: text

    $mknickfn(nickname)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - nickname
      - The nickname to be made a valid filename

Example
-------

.. code:: text

    //var %i 33 | var %f | while (%i isnum 33-126) { var %f %f $+ $chr(%i) | inc %i } | echo -a orig: %f | echo -a mknk: $mknickfn(%f) 

.. note:: While this ensures a string is a valid filename, it does not ensure 2 different strings wouldn't get assigned the same filename, with both having different characters removed.

Compatibility
-------------

.. compatibility:: 5.7

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$mkfn </identifiers/mkfn>`
    * :doc:`$mklogfn </identifiers/mklogfn>`

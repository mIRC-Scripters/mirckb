$mkfn
=====

$mkfn ensures a text string can be a valid filename by replacing characters not allowed in a filename with underscores.

Synopsis
--------

.. code:: text

    $mkfn(text)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - text
      - Text to be made a valid filename by replacing certain characters with underscores

Properties
----------

None

Example
-------

.. code:: text

    //var %i 33 | var %f | while (%i isnum 33-126) { var %f %f $+ $chr(%i) | inc %i } | echo -a orig: %f | echo -a mkfn: $mkfn(%f)

.. note:: While this ensures a string is a valid filename, it does not ensure 2 different strings wouldn't get assigned the same filename, with both having different characters replaced with the same underscore.

Compatibility
-------------

.. compatibility:: 5.7

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$mknickfn </identifiers/mknickfn>`
    * :doc:`$mklogfn </identifiers/mklogfn>`

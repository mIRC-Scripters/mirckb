$mklogfn
========

$mklogfn returns a the filename that would be used for such a nickname as a log file, it ensures a valid filename by doing the same underscores replacement as :doc:`$mkfn </identifiers/mkfn>`, and then applying your log setting (adding a network and .log etc)

Synopsis
--------

.. code:: text

    $mklogfn(text)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - text
      - Text to be made a valid log filename respecting your mIRC log settings 

Properties
----------

None

Example
-------

.. code:: text

    //var %i 33 | var %f | while (%i isnum 33-126) { var %f %f $+ $chr(%i) | inc %i } | echo -a orig: %f | echo -a mklogfn: $mklogfn(%f)

.. note:: While this ensures a string is a valid filename, it does not ensure 2 different strings wouldn't get assigned the same filename, with both having different characters replaced with the same underscore.

Compatibility
-------------

.. compatibility:: 5.7

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$mknickfn </identifiers/mknickfn>`
    * :doc:`$mkfn </identifiers/mkfn>`

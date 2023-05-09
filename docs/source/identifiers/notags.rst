$notags
=======

$notags returns the text stripped from all the possible tags for spoken text in :doc:`/gtalk </commands/gtalk>`

Synopsis
--------

.. code:: text

    $notags(text)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - text
      - the text containing tags for spoken text

Properties
----------

None

Example
-------

.. code:: text

    //echo -a $notags(te\spd=5\st)

Compatibility
-------------

.. compatibility:: 5.7

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/gtalk </commands/gtalk>`


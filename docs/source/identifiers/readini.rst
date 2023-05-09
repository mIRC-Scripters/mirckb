$readini
========

The $readini returns the associated value of the item name for the given topic in an INI structure disk file

Synopsis
--------

.. code:: text

    $readini(filename , np, topic, item)
    Legacy syntax:
    $readini [switches] topic item

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - filename
      - The file from which text is returned
    * - np
      - switches, 'n' = non evaluation of line, 'p' = treats command pipe seperator as code instead of plain text, same as :doc:`$read </identifiers/read>`

Switches
^^^^^^^^

Notes:
^^^^^^

* All searches are case-insensitive.
* Undocumented legacy syntax can be used  where parameters follow the identifier without being enclosed within quotes.

Examples
--------

Compatibility
-------------

.. compatibility:: 4.5

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/bread </commands/bread>`
    * :doc:`$fread </identifiers/fread>`
    * :doc:`$read </identifiers/read>`

$isupper
========

$isupper returns $true if text is all upper case, otherwise returns $false.

Synopsis
--------

.. code:: text

    $isupper(text)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - text
      - The string to be checked

Properties
----------

None

Example
-------

.. code:: text

    //echo -a $isupper(ABCDEFG)

will return $true

.. code:: text

    //echo -a $isupper(ABCDEFg)

will return $false because not all character are upper case.

Compatibility
-------------

.. compatibility:: 5.61

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$islower </identifiers/islower>`
    * :doc:`$true </identifiers/true>`
    * :doc:`$false </identifiers/false>`


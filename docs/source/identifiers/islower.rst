$islower
========

$islower Returns $true if text is all lower case, otherwise returns $false.

Synopsis
--------

.. code:: text

    $islower(text)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - text 
      - The input string to be checked

Properties
----------

None

Example
-------

.. code:: text

    //echo -a $islower(abcdefg)

will return $true

.. code:: text

    //echo -a $islower(abcdefG)

will return $false because not all the character are lower case

Compatibility
-------------

.. compatibility:: 5.61

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$isupper </identifiers/isupper>`
    * :doc:`$true </identifiers/true>`
    * :doc:`$false </identifiers/false>`


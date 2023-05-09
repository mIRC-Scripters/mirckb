$comval
=======

$comval returns the member value for the Nth instantiation of the enumerated collection in a COM object.

Synopsis
--------

.. code:: text

    $comval(name,N,member,&binvar)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - name
      - The name of the COM object connection
    * - N
      - The Nth item in the list
    * - member
      - The name of the member you want to access
    * - &binvar
      - If you use the .result property, a binvar which will be filled with the result.

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - .result
      - Goes with the fourth parameter being a binvar, the result is saved to a binary variable, this allows you to access array, which are returned as tokens separated by NULL bytes.

Example
-------

None

Compatibility
-------------

.. compatibility:: 5.9

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$com </identifiers/com>`
    * :doc:`$comerr </identifiers/comerr>`
    * :doc:`/comopen </commands/comopen>`
    * :doc:`/comclose </commands/comclose>`


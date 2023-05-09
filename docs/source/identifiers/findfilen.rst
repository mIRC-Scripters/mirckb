$findfilen
==========

$findfilen returns the Nth position of the found file inside a :doc:`$findfile </identifiers/findfile>` call executing commands.

Synopsis
--------

.. code:: text

    $findfilen

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
Nonen

Properties
----------

None

Example
-------

.. code:: text

    //echo -a $findfile($mircdir,*,0,0,echo -a $findfilen : $1-)

Compatibility
-------------

.. compatibility:: 6.17

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$finddir </identifiers/finddir>`
    * :doc:`$finddirn </identifiers/finddirn>`
    * :doc:`$findfile </identifiers/findfile>`


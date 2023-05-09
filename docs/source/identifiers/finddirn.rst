$finddirn
=========

$finddirn returns the Nth position of the found directory inside a :doc:`$finddir </identifiers/finddir>` call executing commands.

Synopsis
--------

.. code:: text

    $finddirn

Parameters
----------

Nonen

Properties
----------

None

Example
-------

.. code:: text

    //echo -a $finddir($mircdir,*,0,0,echo -a $finddirn : $1-)

Compatibility
-------------

.. compatibility:: 6.17

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$finddir </identifiers/finddir>`
    * :doc:`$findfile </identifiers/findfile>`
    * :doc:`$findfilen </identifiers/findfilen>`


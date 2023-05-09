$parseutf
=========

$parseutf returns $true if mIRC is going to utf encode/decode during the :doc:`on parseline </events/on_parseline>` event, $false otherwise.

Synopsis
--------

.. code:: text

    $parseutf

Parameters
----------

None

Properties
----------

None

Example
-------

.. code:: text

    on *:parseline:*:{
      echo -a $parseutf
    }

Compatibility
-------------

.. compatibility:: 7.42

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on parseline </events/on_parseline>`
    * :doc:`/parseline </commands/parseline>`
    * :doc:`$parseline </identifiers/parseline>`
    * :doc:`$parsetype </identifiers/parsetype>`


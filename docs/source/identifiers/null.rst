$null
=====

$null does not return a value; just like :doc:`$true </identifiers/true>` or :doc:`$timeout </identifiers/timeout>`, it's a value you can use in comparison in :doc:`/if </commands/if>` or :doc:`/while </commands/while>`. An empty variable also returns $null.

Synopsis
--------

.. code:: text

    $null

Parameters
----------

None

Properties
----------

None

Example
-------

.. code:: text

    //if ($? != $null) echo -a you entered $v1

Compatibility
-------------

.. compatibility:: 2.1a

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$false </identifiers/false>`
    * :doc:`$true </identifiers/true>`


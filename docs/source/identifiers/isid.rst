$isid
=====

$isid returns $true if the custom alias is called as an identifier, $false otherwise.

Synopsis
--------

.. code:: text

    $isid

Parameters
----------

None

Properties
----------

None

Example
-------

/echo -a IS: $test

/test

.. code:: text

    alias test {
      if ($isid) return $true
      else echo -a $false
    }

Compatibility
-------------

.. compatibility:: 5.6

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/alias </commands/alias>`


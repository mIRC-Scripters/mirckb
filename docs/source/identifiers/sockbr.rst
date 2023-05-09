$sockbr
=======

$sockbr returns the number of bytes read from the last /sockread command done for that socket.

Synopsis
--------

.. code:: text

    $sockbr

Parameters
----------

None

Properties
----------

None

Example
-------

.. code:: text

    on *:sockread:name:{
      if ($sockerr) return
      var %a
      ;sockread %a reads one line, or nothing
      ;we check if we read anything before comparing
      if (!$sockbr) return
      if (%a == something) echo -a ok
    }

Compatibility
-------------

.. compatibility:: 5.3

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$sock </identifiers/sock>`
    * :doc:`$sockname </identifiers/sockname>`
    * :doc:`$sockerr </identifiers/sockerr>`


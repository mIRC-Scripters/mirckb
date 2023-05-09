$md5
====

$md5 returns the md5 hash value for the specified data

Synopsis
--------

.. code:: text

    $md5(text|&binvar|filename,N)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - text
      - plain text, to be used with N = 0 (default)
    * - &binvar
      - the content of the binary variable is used to calculate the hash, to be used with N = 1
    * - filename
      - the content of the filename is used to calculate the hash,  to be used with N = 2

Properties
----------

None

Example
-------

.. code:: text

    //echo -a $md5($mircexe,2)

Compatibility
-------------

.. compatibility:: 6.03

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$sha1 </identifiers/sha1>`
    * :doc:`$sha256 </identifiers/sha256>`
    * :doc:`$sha384 </identifiers/sha384>`
    * :doc:`$sha512 </identifiers/sha512>`


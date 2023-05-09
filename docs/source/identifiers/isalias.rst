$isalias
========

$isalias returns informations about aliases.

Synopsis
--------

.. code:: text

    $isalias(name,[N])

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - name
      - The name of the alias
    * - N
      - returns the Nth line of a multiline alias, to be used with the .alias property

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - .fname
      - returns the filename in which the alias exists
    * - .ftype
      - returns the type of alias, if it's stored in a "remote" file or in an "alias" file
    * - .alias
      - returns the alias definition, you can access a multiline alias with the N parameter.

.. note:: If you have an alias named "test" inside a remote file A and another alias with the same name in another remote file B, even in B is loaded after A, if you execute the alias from an alias/event/etc inside file B, it will execute your alias in file B, you may be expecting this but the author here wasn't until recently. I was thinking it would always execute the first found alias in the order of loaded file unless the alias in B is local here. $isalias behaves the same way, if you call $isalias from a remote file, it will always use the alias defined inside that remote file if it exists, this suggests that alias are always local to a remote script, the -l switch when defining alias with the alias keyword wouldn't be that useful?

Example
-------

.. code:: text

    //echo -a $isalias(join)

Compatibility
-------------

.. compatibility:: 5.4

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$script </identifiers/script>`
    * :doc:`$alias </identifiers/alias>`


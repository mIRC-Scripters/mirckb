$var
====

$var returns informations about the Nth matching variable name

Synopsis
--------

.. code:: text

    $var(var,N)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - var
      - the variable name, you can omit the '%' sign; can be a :ref:`matching_tools-wildcard`.
    * - N
      - The Nth matching variable, if N is 0, returns the total number of matching variable.

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - .value
      - return the value of the variable
    * - .local
      - return $true if the variable is local, $false otherwise
    * - .secs
      - return the time left until the variable is automatically unset (-u switch of :doc:`/set </commands/set>`)
    * - .unset
      - return the original unset time N passed to /set -uN

Example
-------

.. code:: text

    //echo -a $var(%myscript*,0)

Compatibility
-------------

.. compatibility:: 5.9

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/var </commands/var>`
    * :doc:`/set </commands/set>`


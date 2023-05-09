$envvar
=======

The $envvar identifier returns the names of Windows environment variables and their values.

Synopsis
--------

.. code:: text

    $envvar( < name | N > )

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - name
      - Returns the value of the named environment variable
    * - N
      - Returns the name of the N'th environment variable. If N=0, returns total number of variables

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - .name
      - Forces return of the Name of the environment variable.
    * - .value
      - Forces return of the Value of the environment variable.

Same as with :doc:`$timer </identifiers/timer>`, If there's an environment variable named 3, $envvar(3).value returns the value of the 3rd variable not the value of the variable named 3.

Example
-------

.. code:: text

    //echo -a There are $envvar(0) environment variables, on the $envvar(username) account

.. code:: text

    ; list of all environment variables:
    //var %i 1 | while (%i isnum 1- $envvar(0) ) { echo -a %i $envvar(%i) $chr(22) $envvar(%i).value $chr(15) | inc %i }

Compatibility
-------------

.. compatibility:: 7.38

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$sysdir </identifiers/sysdir>`


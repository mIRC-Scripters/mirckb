$str
====

$str duplicates the specified text string n times.

Synopsis
--------

.. code:: text

    $str(<text>,<N>)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - Text
      - The text string that is being replicated.
    * - N
      - Integer 1+ is the number of times Text is replicated.

Returns $null if N is $null or is not greater than or equal to 1.

Example
-------

.. code:: text

    //echo -a $str(Yes,3)
    ; returns: YesYesYes
    //echo -a $str(Yes $+ $chr(32) ,3)
    ; returns: Yes Yes Yes

Identifier makes it easier to replicate long strings, or strings of variable lengths.

.. code:: text

    //echo -a $str(=+ ,39) $+ =
    //echo -a %Title
    //echo -a $str($chr(45),$len(%Title))

.. code:: text

    ; Initialize a 20-token comma-separated array
    //set %values $str(0 $+ $chr(44),19) $+ 0

Compatibility
-------------

.. compatibility:: 4.5

.. note:: Version 5.0 changed syntax from $str(N,text)


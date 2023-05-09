$ctimer
=======

The $ctimer identifier returns the name of the :doc:`/timer </commands/timer>`, if any, that triggered a certain script.

Synopsis
--------

.. code:: text

    $ctimer

Parameters
----------

None

Example
-------

Create an alias that fires off a timer to perform a command, and have the command echo the name of the timer that executed it:

.. code:: text

    ; Use /testCtimer
    alias testCtimer { .timermyTimer 1 1 testCtimerGO }
    alias -l testCtimerGO { echo -a The timer name was: $ctimer }

Result

.. code:: text

    The timer name was: mytimer

.. note:: The value is always lowercase.

Compatibility
-------------

.. compatibility:: 5.82

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$timer </identifiers/timer>`
    * :doc:`$ltimer </identifiers/ltimer>`
    * :doc:`/timer </commands/timer>`


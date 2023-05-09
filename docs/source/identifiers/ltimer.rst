$ltimer
=======

$ltimer returns the name (timer ID) of last timer created.

Synopsis
--------

.. code:: text

    $ltimer

Parameters
----------

None

Properties
----------

None

Example
-------

.. code:: text

    //.timerNAME 1 1 echo -a $!ltimer
    //timerfoobar $+ $rand(1,99) 1 5 noop | echo -a $ltimer
    //timerfoo 1 3 echo -a current timer is $!ctimer last timer created is $!ltimer | timer $+ $rand(11111,99999) 1 2 echo -a current timer is $!ctimer last timer created is $!ltimer

.. code:: text

    The 'name' can be numeric, in which case the string returned is the numeric name, and not the 'N' used in $timer(N) used to return the name of the Nth timer.
    //timer $+ $rand(11111,99999) 1 1 noop | echo -a $ltimer

Compatibility
-------------

.. compatibility:: 5.1

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$ctimer </identifiers/ctimer>`
    * :doc:`$timer </identifiers/timer>`
    * :doc:`/timer </commands/timer>`

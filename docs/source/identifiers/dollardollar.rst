$$
==

$$ is a construct which allows you to halt the script if the identifier returns $null. If used correctly it's a very short and simple way to halt a routine if a parameter is $null.

.. note:: $$ is not executing a /halt, it's effectively a way to halt completely the script execution, just like /halt, except that /halt also implies /haltdef, whereas $$ does not. This can be used inside events to /halt without /haltdef'ing. You can use the construct '$$null' for example.

Synopsis
--------

.. code:: text

    $$identifier

Examples
--------

Halts the echo unless the active window is a channel:

.. code:: text

    //echo -a $$chan test

.. note:: $$ without any following non-spaces touching it behaves as if an identifier returning the literal $$ string, however it does not recognize $$$ as if halting the $$ identifier. $$3 halts the script if $3 is null. Only the final command here is an error:

.. code:: text

    //tokenize 32 parm1 parm2 parm3 | echo 3 -a $ $$ | echo 4 -a $$3 | echo 5 -a $$3a,b | echo 5 -a $$,b

Compatibility
-------------

.. compatibility:: 2.8c

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/halt </commands/halt>`
    * :doc:`/haltdef </commands/haltdef>`

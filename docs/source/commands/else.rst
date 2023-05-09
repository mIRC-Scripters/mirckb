/else
=====

The /else command is a :doc:`construct in the mIRC scripting language </intermediate/control_flow_statements>` that perfomes the command if all the previous :doc:`/if </commands/if>` or :doc:`/elseif </commands/elseif>` failed, must be used after an :doc:`/if </commands/if>` or :doc:`/elseif </commands/elseif>` statement.

The else statement is used in conjunction with the :doc:`/if </commands/if>` statement and the :doc:`/elseif </commands/elseif>` statement to jump to certain blocks of code depending on the result of the conditional statement that was executed.

Synopsis
--------

.. code:: text

    else <command>
    else { <commands> }

Switches
--------

None

Parameters
----------

None

Example
-------

.. code:: text

    alias test {
      if ($1 == 1) echo -a 1!
      elseif ($1 isnum 2-7) echo -a 2-7!
      else echo -a 8-!
    }

Compatibility
-------------

.. compatibility:: 4.5

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$halted </identifiers/halted>`
    * :doc:`$result </identifiers/result>`
    * :doc:`$alias </identifiers/alias>`
    * :doc:`$isalias </identifiers/isalias>`
    * :doc:`$iif </identifiers/iif>`
    * :doc:`/alias </commands/alias>`
    * :doc:`/goto </commands/goto>`
    * :doc:`/halt </commands/halt>`
    * :doc:`/return </commands/return>`
    * :doc:`/while </commands/while>`
    * :doc:`/returnex </commands/returnex>`
    * :doc:`/elseif </commands/elseif>`
    * :doc:`/else </commands/else>`


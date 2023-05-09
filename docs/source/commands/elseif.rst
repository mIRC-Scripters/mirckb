/elseif
=======

The /elseif command is a :doc:`construct in the mIRC scripting language </intermediate/control_flow_statements>` that performs commands if all the previous :doc:`/if </commands/if>` or :doc:`/elseif </commands/elseif>` failed and if the condition is true, must be used after an if/elseif statement.

The elseif statement is used in conjunction with the :doc:`/if </commands/if>` statement and the :doc:`/else </commands/else>` statement to jump to certain blocks of code depending on the result of the conditional statement that was executed.

Synopsis
--------

.. code:: text

    elseif (<condition>) <command>
    elseif (<condition>) { <commands> }

Switches
--------

None

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <condition>
      - a conditional expression to be executed

Example
-------

.. code:: text

    alias test {
      if ($1 == 1) echo -a 1!
      elseif ($1 isnum 2-7) echo -a 2-7!
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


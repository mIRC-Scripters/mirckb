/elseif
=======

The **/elseif** command is a construct in the mIRC scripting language that performs commands if all the previous /if or /elseif failed and if the condition is true, must be used after an if/elseif statement.

The elseif statement is used in conjunction with the /if statement and the /else statement to jump to certain blocks of code depending on the result of the conditional statement that was executed.

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

Added: mIRC v4.5

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$halted </aliases/halted>`
    * :doc:`$result </aliases/result>`
    * :doc:`$alias </aliases/alias>`
    * :doc:`$isalias </aliases/isalias>`
    * :doc:`$iif </aliases/iif>`
    * :doc:`/alias <alias>`
    * :doc:`/goto <goto>`
    * :doc:`/halt <halt>`
    * :doc:`/return <return>`
    * :doc:`/while <while>`
    * :doc:`/returnex <returnex>`
    * :doc:`/elseif <elseif>`
    * :doc:`/else <else>`
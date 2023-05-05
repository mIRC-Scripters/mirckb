/if
===

The :doc:`conditional statements </intermediate/control_flow_statements.html#conditional_statements>` is a built-in construct capable of comparing a value and executing a set of commands based on the result of that condition. The if statement is used in conjunction with the :doc:`/else </commands/else>` statement and the :doc:`/elseif </commands/elseif>` statement to jump to certain blocks of code depending on the result of the conditional statement that was executed. The if statements supports the :doc:`operators </intermediate/control_flow_statements.html#operators>`

Synopsis
--------

.. code:: text

    if (<condition>) <statement>
    if (<condition>) { <statements> }

Switches
--------

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

Below is a simple example of checking for at least five arguments before proceeding.

.. code:: text

    alias example {
    if ($0 < 5) { echo -atc info * /example: You must provide at least 5 arguments! | halt }
    ; do something useful here
    echo -a works!
    }

Executing "/example a b c d" will result in:

.. code:: text

    * /example: You must provide at least 5 arguments!

While, executing "/example a b c d f" will result in:

.. code:: text

    works!

Compatibility
-------------

Added: mIRC v4.5 (06 Jul 1996)

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

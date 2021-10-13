/else
=====

The **/else** command is a construct in the mIRC scripting language that perfomes the command if all the previous /if or /elseif failed, must be used after an /if or /elseif statement.

The else statement is used in conjunction with the /if statement and the /elseif statement to jump to certain blocks of code depending on the result of the conditional statement that was executed.

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
/goto
=====

The **/goto** command allows you to jump to another part of the code. The goto command can only jump to a label within the same event, alias, or menu. The label must have been parsed by mIRC previously inside that event/alias/menu or the label is considered undefined. Calling a goto on an undefined label will result in a label not found error. Labels can be plain text strings or variables

.. note:: A goto cannot jump to a label that was skipped earlier in the code.

Synopsis
--------

.. code:: text

    :<label>
    /goto <label>

Switches
--------

None

Parameters
----------

None

Example
-------

.. code:: text

    ; /is_even <1-9>
    ;
    ; Example: /is_even 2
    ; 2 is an even number.
    ; 2 is a prime number.
    alias is_even {
    goto $1
    :0 | echo -a You typed zero. | return
    :4 | echo -a $1 is an even number.
    :1 | :9 | echo -a $1 is a perfect square. | return
    :2 | echo -a $1 is an even number.
    :3 | :5 | :7 | echo -a $1 is a prime number. | return
    :6 | :8 | echo -a $1 is an even number. | return
    :error
    echo -a Only single-digit numbers are allowed!
    reseterror
    }

.. note:: that skipped labels cannot be jumped into.

.. code:: text

    ; This example shows that a goto point not being parsed previously by mIRC cannot be reached.
    ;
    alias testing_goto {
    if (1) echo -a 1
    elseif (1) { echo -a 2 | :test }
    goto test
    }

The script above will produce the following error:

.. code:: text

    * /goto: 'test' not found (line 3, scriptfile.mrc)

Compatibility
-------------

Added: mIRC v4.5 (06 Jul 1996)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/break </commands/break>`
    * :doc:`/continue </commands/continue>`
    * :doc:`/if </commands/if>`
    * :doc:`/return </commands/return>`
    * :doc:`/while </commands/while>`

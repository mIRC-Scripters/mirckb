$
=

The $ character is a reference point for all identifiers, and some operations. $ is usually followed by any number of built-in mIRC identifier names, with which there are hundreds of properties to choose from.

Examples As Identifier
----------------------

Some examples of the $ used as an identifier include the following:

.. code:: text

    $dialog(mydialog).title

Retrieves the title for the specified dialog.

.. code:: text

    $1

Grabs the first word from an event, such as an :doc:`on events </events/on_events>`.

$() itself is a valid identifier which works much like :doc:`$eval </identifiers/eval>`

Examples As Operation
---------------------

The $ can also precede some characters and words in order to perform a specific operation, such as concatenating characters, or groups of characters together. Below are a few examples:

.. code:: text

    alias testme {
      var %myvar1 = Join m, %myvar2 = e with this, %join = %myvar1 $+ %myvar2
      echo -a %join
    }

This will join the two variables, resulting in the output: "Join me with this" being echoed to the active window.

.. code:: text

    alias testme {
      echo -a $calc(33 * 77)
    }

This will multiply "33" & "77", then output the result to the active window.

Others
------

There are just too many identifiers and operators that deal with $ to cover here. Refer to the List of identifiers - mIRC|identifier's index for a more thorough and complete list.

Compatibility
-------------

.. compatibility:: n/a

See also
--------
$!
==

The $! identifier returns the input value that the script was just given via user input ($input, $? etc). This identifier may avoid using a variable.

Example
-------

.. code:: text

    alias testme {
      $?="Type something"
      echo -a $!
    }

After you execute the alias, via /testme, you will be prompted by an input box. Whatever input you put in that box, upon clicking OK, will be immediately echoed to your active window.


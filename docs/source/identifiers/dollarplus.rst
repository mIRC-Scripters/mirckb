$+
==

$+ is the concatenation concatenation operator in mIRC. The operator can join together two strings end-to-end. In addition to its normal behavior, the $+ operator has a few special functions when used within :doc:` evaluation brackets </advanced/eval_brackets>`.

In its normal use, the $+ operator can be used to join together two strings end-to-end. For example:

.. code:: text

    echo -a A $+ B $+ C

Will result in:

.. code:: text

    ABC

Likewise, the $+ operator can be used with identifiers and variables as well:

.. code:: text

    var %x = A, %y = B
    echo -a %x $+ %y $+ $day

Will print (depending on the day of the week):

.. code:: text

    ABMonday

This identifier also accepts any number of parameters. The above code can be rewritten (with the same result) as:

.. code:: text

    var %x = A, %y = B
    echo -a $+(%x, %y, $day)

See also
--------

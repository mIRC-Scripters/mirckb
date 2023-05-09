$++
===


.. attention:: This feature has essentially been replaced by :doc:`$+ </identifiers/dollarplus>`

$++ is a very old construct, similar to $+ concatenator, which allowed a 'delay' to the $+ behavior.

The example:

.. code:: text

    " $+ $read c:\test.txt $++ "

can be found in the changelog of mIRC, suggesting that if that $+ were used instead of a $++, it would concatenate the " to the filename before the file could be read but nowadays the above example works with $+ and $++

However $++ does differ from $+, inside brackets. As you may know, $+ inside bracket evaluation [ ] is not really behaving like it is outside them, $++ will act as though $+ was used, but it will behave the way $+ does outside the bracket evaluation, for example [ $ $++ me ] will produce plain text $me instead of [ $ $+ me ] producing your nickname

Compatibility
-------------

.. compatibility:: 4.1

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$+ </identifiers/dollarplus>`

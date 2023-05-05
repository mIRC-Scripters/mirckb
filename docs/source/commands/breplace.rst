/breplace
=========

The **/breplace** command can be used to replace an ASCII value by another value in a binary variable. Multiple replacements are allowed.

Synopsis
--------

.. code:: text

    /breplace &binvar <oldvalue> <newvalue> [oldvalue newvalue...]
    /breplace &binvar <old-char/value> <old-char/value> [old-char/value new-char/value...]

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
    * - <oldvalue>
      - The old ASCII value to replaced (decimal 0-255)
    * - <newvalue>
      - The new ASCII value to replace the old one (decimal 0-255)

.. note::

      - Also accepts case-sensitive text characters/strings as parameters, using $asc(1st character of the string)

.. note:: This replaces individual bytes and does not allow replacing multi-byte patterns with new multi-byte patterns.<br />

.. note:: Bytes are replaced only once, even if the new_value is the old_value for the next old/new pair. This means that it mimics the behavior of $replacex not $replace. However the replacements are made in reverse order, with the first pair being replaced last of all.<br />

.. note:: You can have multiple old/new number pairs, and if the count of numbers is an odd number greater than 2, the last unpaired number is ignored.<br />

.. note:: You cannot breplace within a portion of a binary &string unless you bcopy that section to a &temp where you perform the breplace then bcopy &temp back to the original &string/position.

Example
-------

.. code:: text

    Alias Example {
    ;Create a binary variable set it to \"Hello World\"
    bset -t &Example 1 Hello World

    ;Replace e (ASCII value 101) with 3 (ASCII value 51)
    breplace &Example 101 51

    ;Echo our new string
    echo -a $bvar(&Example,1,$bvar(&Example,0)).text
    }

The above example will output:

.. code:: text

    H3llo World

.. code:: text

    .. note:: that long strings can be replaced. The replace is on the entire token - not finding the 0 within the 10:

    //bset &a 7654321 10 | echo -a $bvar(&a,7654300-) | breplace &a 0 1 | echo -a $bvar(&a,7654300-)
    shows the last 22 bytes changing:
    0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 10
    1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 10

.. code:: text

    The replacements are made in the same style as $replacexcs not $replace, but the replacement pairs are made in reverse order. Because of the reverse order, /breplace swaps the 11 for the 77 in the last pair before it can replace the 11 with the 88.

    //var %a 11 22 33 44 | bset &v 1 %a | breplace &v 11 88 44 66 11 77 | echo -a %a (original) | echo -a $bvar(&v,1-) (breplace) | echo -a $replace(%a,11,88,44,66,11,77,66,99) (replace) | echo -a $replacex(%a,11,88,44,66,11,77,66,99) (replacex)
    result:
    11 22 33 44 (original)
    77 22 33 66 (breplace)
    88 22 33 99 (replace)
    88 22 33 66 (replacex)

.. code:: text

    The first character of a string can substitute in place of a byte value, if it is non-numeric and is not UTF-8 encoded to more than 1 byte. In this example, the chr(233) is not replaced because there is no 1-byte character match. The next match fails because capital F is not a case-sensitive match for lower-case 'f'. The 'b' takes the place of byte value 98, and is replaced by $chr(33). The first character of 'abc' is found in the string, and is replaced by the 1st character of 'xyz'.

    //bset -t &v 1 abcdefé | breplace &v abc xyz b 33 F g $chr(233) $chr(234) | echo -a $bvar(&v,1-) / $bvar(&v,1-).text
    result: x!cdefé

.. code:: text

    The number of from/to byte pairs is an odd number greater than 2, so the last unpaired number is ignored without reporting an error, before the swaps are made in reverse-pair order:
    //bset &a 1 13 10 13 10 99 | breplace &a 10 13 13 10 99 | echo -a $bvar(&a,1-)
    returns: 10 13 10 13 99

Compatibility
-------------

Added: mIRC v5.6 (23 Sep 1999)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$bvar </identifiers/bvar>`
    * :doc:`$bfind </identifiers/bfind>`
    * :doc:`/bread </commands/bread>`
    * :doc:`/bset </commands/bset>`
    * :doc:`/bunset </commands/bunset>`
    * :doc:`/bwrite </commands/bwrite>`
    * :doc:`/btrunc </commands/btrunc>`
    * :doc:`/bcopy </commands/bcopy>`
    * :doc:`$replacex </identifiers/replacex>`
    * :doc:`$replace </identifiers/replace>`

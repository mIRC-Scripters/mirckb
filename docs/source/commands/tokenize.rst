/tokenize
=========

The **/tokenize** command replaces the existing $0 through $N'th tokens, filling $1 $2 ... $N identifiers with portions of a string, divided into tokens based on the location of the <C> delimiters. It also fills $0 with an integer containing the number of tokens filled from the string.

Synopsis
--------

.. code:: text

    /tokenize <C> <text>

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
    * - <C>
      - The code point ($asc() value) 1-65535 of the character used as the delimiter (If the codepoint is not present within <text> the entire string is filled into $1)
    * - <text>
      - The string of <C> delimited tokens which will fill the $N identifiers

Example
-------

Typing the following into the editbox returns a result:

.. code:: text

    //tokenize 58 one:two:three | echo -a Result of $!2: $2
    ;$asc(:) == 58

.. code:: text

    Result of $2: two

More examples using different delimiters:

.. code:: text

    //tokenize 32 Hello, how are you? | echo -a Result of $!3: $3
    ;$chr(32) is a space

.. code:: text

    Result of $3: are

.. code:: text

    //tokenize 44 This is, a comma delimited, list. | echo -a Result of $!1: $1

.. code:: text

    Result of $1: This is

.. code:: text

    Tokenizing follows the same rules as used by $gettok() and the other $*tok identifiers, where it strips leading, trailing, and consecutive delimiters. Consecutive delimiters does not result in a $null token:
    //tokenize 64 @1@@2@@3@@ | echo -a (1) $1 (2) $2 (3) $3 (4) $4
    returns: (1) 1 (2) 2 (3) 3 (4)
    This means that tokenizing by other than space 32 can result in tokens having leading or trailing spaces causing tokens to be treated differently:
    //tokenize 46 1 .2 .3 | echo -a $len($2) / $asc($mid($2,2)) | echo -a $!2 value is $2 which is $iif($2 isnum,numeric, non-numeric)
    returns: $2 value is 2 which is non-numeric

    .. note:: because this is a /command not an $identifier, leading trailing or consecutive spaces are removed from <text> before (but not after) the tokenizing. But if tokenizing by 32, the leading and trailing spaces are also removed from the created $1 ... $N'th tokens.

    Using /tokenize destroys the existing $1- tokens, so if you still need those, you should save them to a variable or use tokenize within another alias. If you use tokenize within an alias called from another alias, using tokenize does not affect the $1- values seen by the original alias.
    //tokenize 32 the quick brown fox jumps over the lazy dog | while ($1) { echo -a $1- | tokenize 32 $2- }

    //tokenize 32 1.0 2.0 3.0 4.0 | echo -a changes from: $1- | if (. isin $2) tokenize 32 $1 $int($2) $3- | echo -a changes to: $1-
    returns: 1.0 2 3.0 4.0

Compatibility
-------------

Added: mIRC v5.6 (23 Sep 1999)
See also
--------

.. hlist::
    :columns: 4

    * :doc:`$1- </identifiers/1->`
    * :doc:`$gettok </identifiers/gettok>`

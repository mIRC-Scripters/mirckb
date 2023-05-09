/bwrite
=======

The /bwrite command can be used to write a specified amount of bytes from the string/buffer to a given file starting at the start_pos position.

.. note:: the starting position is 0, not 1.

Synopsis
--------

.. code:: text

    /bwrite -act <filename> <start_pos> <length> <text|%var|&binvar>

.. note:: If you pass a %var to /bwrite, if the content of that %var is a %variable itself, of if the first token of %var is a %variable itself, the content of %variable is used and no tokenization on %variable occurs, effectively preserving spaces. See the example

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -t
      - Treats everything as plain text (i.e. $identifiers and %variables (but not contents of %variables) are evaluated, but binary variables are not evaluated, are treated as text strings beginning with &) This switch is needed if literal string begins with &  or string within %var begins with & or % characters.
    * - -c
      - Chops the file at the end of the written data (if your current disk file is 10 bytes and you write 3 bytes at position 3 (4th byte), the resulting disk file's filesize is 6 because the 3 bytes were written as the 4th through 6th bytes of the file)
    * - -a
      - Disables UTF-8 encoding of characters in the range 0-255, as long as the line contains no characters > 255

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <filename>
      - the file name to be modified
    * - <start_pos>
      - the position in the file to start writing at. First byte of the file is 0. Using -1 appends data to the end of existing file.
    * - [length]
      - Length of the data to be written. Using -1 writes entire length of source text or variable.
    * - <text|%var|&binvar>
      - data to be written to the file

Example
-------

.. code:: text

    ;Write some text to a file at beginning of the file
    /bwrite file.txt 0 hello there!
    ;Replace "there!" with "world!"
    /bwrite file.txt 6 world!

.. code:: text

    //var %b a $chr(32) b | var %a % $+ b | bwrite -c test 0 -1 %a | loadbuf -a test
    displays "a  b"
    because the first token in %a is a variable (%b). Adding the -t switch  would have instead written the literal string "%b".

Compatibility
-------------

.. compatibility:: 5.3

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$bvar </identifiers/bvar>`
    * :doc:`/bset </commands/bset>`
    * :doc:`/bcopy </commands/bcopy>`
    * :doc:`/bread </commands/bread>`
    * :doc:`/breplace </commands/breplace>`
    * :doc:`/btrunc </commands/btrunc>`
    * :doc:`/bunset </commands/bunset>`
    * :doc:`$bfind </identifiers/bfind>`
    * :doc:`/fwrite </commands/fwrite>`
    * :doc:`/write </commands/write>`


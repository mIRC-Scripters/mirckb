/bcopy
======

The **/bcopy** command can be used to copy any amount of bytes from one variable starting at a specific position into a second variable at a specific position. This command supports copying of overlapping buffers. 

If the number of bytes to copy is -1, all bytes available will be copied over to the destination variable. If the destination position is -1, the bytes will be appended.

.. note:: The first byte starts at the position/index 1, 0 is invalid and will procudes an error.

.. note:: Bytes between prior end of <&dest_binvar> and <dest pos> are zero-filled with $chr(0)

Synopsis
--------

.. code:: text

    /bcopy [-zc] <&dest_binvar> <dest_pos> <&src_binvar> <src_pos> <numBytes>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -z
      - Bytes in the source which are copied are zero-filled with $chr(0) after the copy
    * - -c
      - Truncates the destination variable to remove bytes following the bytes copied. Where both N and M are positive, the new destination length is <des_pos> + <numBytes> -1

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <dest_&binvar>
      - The destination binary variable. Source and destination can be the same variable.
    * - <dest_pos>
      - The position to which to copy the byte to (or -1 to append to destination).
    * - <&src_binvar>
      - The source binary variable.
    * - <src_pos>
      - The position from which to start copying bytes.
    * - <numBytes>
      - Number of bytes to copy beginning at <src pos> (or -1 for everything beginning at <src_pos>).

Example
-------

.. code:: text

    Alias Example {
    ; Create a binary variable 'example' and assign it some text
    bset -t &example 1 This is a cool test!

    ; Copy from '&example' all bytes from the 11th byte onward to a new variable
    ; Zero-fills the source variable's bytes which were copied to the destination
    bcopy -z &example2 1 &example 11 999

    ; Print out &example's content (up to the first null)
    echo -a $bvar(&example, 1-).text
    ; Print out &example's content as byte values including the nulls
    echo -a $bvar(&example, 1-)

    ; Print out &example2's content
    echo -a $bvar(&example2, 1-).text
    }

The above example will output:

.. code:: text

    This is a
    84 104 105 115 32 105 115 32 97 32 0 0 0 0 0 0 0 0 0 0
    cool test!

.. code:: text

    ;while these variables exist:
    //bset &to 1 11 22 33 44 55 66 | bset &from 1 77 88 99 123
    and &to contains "11 22 33 44 55 66" and &to contains "77 88 99 123"
    each of the following commands are based on the above values and are not executed after any of the other following alternatives...

    bcopy &to 2 &from 1 3
    ; copies 3 bytes at position 1 of &from to overwrite the 3 bytes at position 2 of &to. Length remains 6
    11 77 88 99 55 66

    bcopy -z &to 2 &from 1 3
    ; same alteration of &to, but all byte positions in &from which were copied are changed to 0x00's. &to is changed to the same 6 bytes as above, but now &from is altered to become "0 0 0 123"

    bcopy -c &to 2 &from 1 3
    ; adding the -c switch causes any destination bytes following the copied bytes to be removed, shortening &to to length 4
    11 77 88 99
    bcopy -c &to 2 &from 1 0
    ; does not generate an error, but does not truncate the destination because 0 bytes were copied
    11 22 33 44 55 66

    bcopy &to 2 &from 1 99
    ; M is larger than bytes available beginning at position 1 of &from, so the 4 bytes are copied to destination positions 2-5 without affecting the destination's 6th byte.
    11 77 88 99 0 66

    bcopy &to -1 &from 1 -1
    ; Destination position -1 causes bytes to be appended. Using -1 as number of bytes to copy copies the entire &from string beginning at position 1.
    11 22 33 44 55 66 77 88 99 123

    bcopy -c &to 1 &to 2 999
    ; entirely within the &to variable, copies positions 2-6 to 1-5 and chops length past the last byte copied into. Without the -c switch, the length would still be 6 with the 66 repeated.
    22 33 44 55 66

    bcopy &to -1 &to 1 999
    ; appends the 6 bytes, doubling the length to 12
    11 22 33 44 55 66 11 22 33 44 55 66

    bcopy -c &to 2 &to 1 999
    ; places the old contents of positions 1-6 into positions 2-7. The bytes are not update after each byte, so does not cause 11 to be replicated in each position.
    11 11 22 33 44 55 66

    bcopy -c &to 3 &to 3 1
    ; truncates a variable to length 3

Binary variables can be longer than the length which can be displayed on a mIRC line. This alias creates a 7mb variable containing all $chr(1) bytes:

.. code:: text

    /fill_with_ones 7654321

    fill_with_ones {
    if ($1 !isnum 1-) return
    bset &var 1 1
    while ($1 > $bvar(&var,0)) {
    bcopy &var -1 &var 1 $iif($calc($1 - $bvar(&var,0)) > $bvar(&var,0),$v2,$v1)
    echo -a current length: $bvar(&var,0)
    }
    echo -a variable length is $bvar(&var,0)
    }

Compatibility
-------------

Added: mIRC v5.7 (07 May 2000)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$bvar </identifiers/bvar>`
    * :doc:`$bfind </identifiers/bfind>`
    * :doc:`/bread </commands/bread>`
    * :doc:`/breplace </commands/breplace>`
    * :doc:`/bset </commands/bset>`
    * :doc:`/btrunc </commands/btrunc>`
    * :doc:`/bunset </commands/bunset>`
    * :doc:`/bwrite </commands/bwrite>`

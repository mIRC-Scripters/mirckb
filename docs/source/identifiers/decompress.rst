$decompress
===========

The $decompress identifier performs decompression of a disk file or binary variable.

Synopsis
--------

.. code:: text

    $decompress( <filename | BinaryVariable> ,[b] )

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - Data
      - First parameter can be either a disk file (default) or a Binary Variable
    * - b
      - Informs that first parameter should be treated as a Binary Variable instead of filename.

Example
-------

There are patterns that often appear near the beginning, but there's no guaranteed signature to be found at the beginning of a compressed file, except the 1st character is $chr(120) small-x.

Returns 1 if it decompressed the file, or 0 if it did not. A file can be compressed multiple times, so a decompressed file should either not begin with small-x or return 0 from a decompress attempt. 0 can indicate there's no-such-file, the file wasn't already compressed, or a failure to decompress corrupted data.

.. code:: text

    ; Compresses binary variable then decompresses it. Assumes you have at least 1 color scheme containing white.
    //bset -t &snip 1 $read($mircini,ntw,*16777215*) | echo 4 -a / $bvar(&snip,1-) | noop $compress(&snip,b) | echo 5 -a \ $bvar(&snip,1-) | noop $decompress(&snip,b) | echo 6 -a $bvar(&snip,1-)

.. note:: Cannot run as an identifier in a statement by itself, but should be an argument to another command or %variable.

.. code:: text

    on *:FILERCVD:*.txt:{
      bread $qt($filename) 0 1 &snip
      if ($bvar(&snip,1) == 120) {
        var %oldsize $file($filename).size
        var %i $decompress($filename)
        var %newsize $file($filename).size
        if (%i) echo -a Successfully decompressed incoming file from size %oldsize to %newsize $+ : $filename
        else echo -a Unsuccessful attempt to decompress incoming file: $filename
      }
    }

Compatibility
-------------

.. compatibility:: 6.1

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$compress </identifiers/compress>`


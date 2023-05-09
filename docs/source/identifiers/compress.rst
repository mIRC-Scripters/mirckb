$compress
=========

The $compress identifier performs compression of a disk file or binary variable.

Synopsis
--------

.. code:: text

    $compress( <filename | BinaryVariable> ,[b][lN][mN] )

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
    * - lN
      - Default compression level is 6 within the range 0-9. lN overrides to use compression level N, where N is integer 0-9. (l0 does not compress, is not the same as the absence of the l switch)
    * - mN
      - Default compression method is 2 (zlib). mN overrides to use compression method N, where N = 1 is raw, N = 2 is zlib (the default), and N = 3 is gzip. (0 uses default m2, invalid 4+ uses m3)

Example
-------

There are patterns that often appear near the beginning, but from observations, it appears you should not assume beyond:

m1 raw: No guaranteed signature because the data is 'raw'. (m1l0 is the same as the input data)
m2 Zlib: The 1st byte is $chr(120) (hex 78) small-x.
m3 gzip: The 1st 4 bytes in hex are: 1F 8B 08 00

Reminder that decompress works without being informed of the lN compression level. Files compressed with non-default m1 or m3 will fail without being informed of the compression method used to compress that file.

Returns 1 if it compressed the file, or 0 if it did not. It will repeatedly process the same file and return 1, even if the attempt to compress an already compressed file slightly increases the filesize. 0 can indicate there's no-such-file, the file wasn't already compressed, or a failure to decompress corrupted data.

.. code:: text

    //noop | $compress(versions.txt) | echo -a test
    //bset -t &snip 1 $read($mircini,ntw,*16777215*) | echo 4 -a / $bvar(&snip,1-) |      $compress(&snip,b) | echo 5 -a \ $bvar(&snip,1-)
    //bset -t &snip 1 $read($mircini,ntw,*16777215*) | echo 4 -a / $bvar(&snip,1-) | noop $compress(&snip,b) | echo 5 -a \ $bvar(&snip,1-)

In the above example, the first 2 lines are incorrect usage, and fail to alter the filename or binary variable, nor do they display the following echo. You must use $compress an argument to something else, which should be done in order to determine success or failure.

.. code:: text

    alias compress-then-send {
      if (!$comchan($1,1)) { echo 5 -a no shared channels with nick $1 | return }
      if (!$isfile($2-)) { echo 5 -a filename does not exist: $2- | return }
      bread $qt($2-) 0 1 &snip
      if ($bvar(&snip,1) != 120) { var %i $compress($2-) | if (%i == 0) echo 5 -a warning failure to zlib compress $1- }
      dcc send $1 $2-
    }

.. note:: Before making a script which automatically compresses all files before sending them and decompressing them when they finish, you should take several issues into account.

# You shouldn't automatically decompress or compress files without making certain that the same file isn't also being transferred to/from someone else.
# Besides :doc:`on filesent </events/on_filesent>`, Transfers can also terminate with :doc:`on sendfail </events/on_sendfail>`, clicking to close the send window, using the :doc:`/close </commands/close>` command with the -s switch, mIRC crashing, etc.
# To make certain all files get safely decompressed, the script should probably work from a file listing that doesn't remove lines until the file has been determined to be decompressed.
# Now that $compress supports gzip compression, a script must first determine which method was used to compress the file in order to successfully decompress the file.

Compatibility
-------------

.. compatibility:: 6.1

version 7.51 expanded lN from 1-6 to 0-9, and introduced mN

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$decompress </identifiers/decompress>`


$crc
====

$crc calculates the 32-bit checksum of a text, :ref:`binary_variables`, or file. Hash is 32-bits, shown as 8 upper-case hexadecimal characters.

Synopsis
--------

.. code:: text

    $crc(plaintext|&binaryvar|filename[,N])

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - plaintext
      - Used with N = 0, just the string you want the CRC-32 checksum hash of
    * - &binaryvar
      - A binary variable, used with N = 1, return the CRC-32 checksum of the content of the binary variable
    * - filename
      - A filename, used with N = 2, return the CRC-32 checksum of the content of the file
    * - N:
      - Optional integer 0-2, where 0 indicates data is treated as plaintext, 1 indicates a &binary variable, 2 treats data as contents of a filename

If the N parameter isn't used, the default 2 is used (which is different than $sha1 which has default of N=0.) Also different than $sha1, invalid N outside 0-2 range are treated as default 2 instead of creating an error.

Properties
----------

None

Example
-------

.. code:: text

    ; Echo the $crc hash of plain text string ''abc'' to the active window:
    ; The DATA is case-sensitive, so hash of "abc" is different than hash of "ABC"
    //echo -a abc $crc(abc,0) / ABC $crc(ABC,0)

.. code:: text

    ; Calculate the CRC-32 hash of the 256 bytes from $chr(0) through $chr(255):
    //var %i 0 | while (%i isnum 0-255) { bset &ascii $calc(1+%i) %i | inc %i } | echo -a $bvar(&ascii,1-) | echo -a $crc(&ascii,1) should be 29058C73 | write -c ascii.dat | bwrite ascii.dat 0 256 &ascii 

.. code:: text

    ; display the same CRC of filename ascii.dat as the above binary variable &ascii
    //echo -a filesize $file(ascii.dat).size $crc(ascii.dat) is the same as $crc(ascii.dat,2) because default N is 2
    ; append 4 bytes to ascii.dat to change the CRC value:
    //bset &b 1 176 84 33 47 | /bwrite ascii.dat -1 4 &b
    //echo -a filesize $file(ascii.dat).size has different CRC value $crc(ascii.dat,2)

Returns 00000000 if filename does not exist:

.. code:: text

    //echo -a $crc(no_such_file.txt,2)

Suggested Uses:
* Quick way to compare if 2 files are identical. (First check should always be comparing file sizes.)
* Quick way to check if a file's contents have changed since stored CRC checksum was made.
* Verify downloaded file hasn't been corrupted, matches the sender's original.

Note that because the default is N=2, $crc(versions.txt) is the CRC-32 for the contents of versions.txt (or 00000000 if the file doesn't exist). This differs from $sha1(versions.txt) giving the hash of the plaintext inside the parenthesis because $sha1 has default of N=0.
mIRC v7.x Unicode-encodes plaintext before providing to $crc, so v7.x and v6.x return different answers for //echo -a $crc($chr(233),0)

If the text doesn't have Unicode code points above 255, to avoid having Unicode points 128-255 encoded to 2-byte pairs, the text must be fed to $crc as a binary variable:

.. code:: text

    //var %name chloé | bset -ta &string1 1 %name | bset -t &string2 1 %name | echo -a $crc(&string1,1) / $crc(&string2,1) / $crc(%name,0)

.. note:: CRC-32 is good for detecting transfer errors. Any 1 bit changed in a file is guaranteed to change the CRC-32 value, which is not necessarily true for $sha1 or other 1-way hashes. However, CRC-32 is not good for detecting malicious tampering with a file. There is a 4-byte binary string which can change a file from any CRC-32 value to any CRC-32 value, and these 4 bytes can be quickly calculated without brute force testing of the 2^32 possible strings.

Error Messages
--------------

None

$crc differs from $sha1 in that it returns no error messages.

For non-existent filenames, it returns 00000000 instead of halting script with an error.
For calculating hash of $null string it returns nothing instead of the checksum of the null-string
When given invalid N outside the 0-2 range, it uses default 2 instead of halting script with an error.

Compatibility
-------------

For $crc(filename):

.. compatibility:: 5.6
 
For N=0-2 parameter:

.. compatibility:: 6.1
 

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$sha1 </identifiers/sha1>`
    * :doc:`$md5 </identifiers/md5>`
    * :doc:`$sha256 </identifiers/sha256>`
    * :doc:`$sha384 </identifiers/sha384>`
    * :doc:`$sha512 </identifiers/sha512>`


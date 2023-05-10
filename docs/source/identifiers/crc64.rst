$crc64
======

$crc64 calculates the 64-bit checksum of a text, :ref:`binary_variables`, or file. Hash is 64-bits, shown as 16 upper-case hexadecimal characters.

Synopsis
--------

.. code:: text

    $crc64(plaintext|&binaryvar|filename[,N])

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - plaintext
      - Used with N = 0, just the string for which you want the CRC-64 checksum
    * - &binaryvar
      - A binary variable, used with N = 1, return the CRC-64 checksum of the content of the binary variable
    * - filename
      - A filename, used with N = 2, return the CRC-64 checksum of the content of the file
    * - N:
      - Optional integer 0-2, where 0 indicates data is treated as plaintext, 1 indicates a &binary variable, 2 treats data as contents of a filename

If the N parameter isn't used, the default 2 is used (which is different than $sha1 which has default of N=0.) Also different than $sha1, invalid N outside 0-2 range are treated as default 2 instead of creating an error.

.. note:: $crc64 has the same defaults and behaviors as $crc does, except it returns a 64-bit checksum instead of 32 bits. Even though it they're both designed the same way, there is no obvious correlation between their outputs. Strings with identical $crc64 checksum are no more/less likely to have identical 32bit $crc checksums than strings whose $crc64 checksum differ.

.. note:: There are several variations of CRC64's published including several variants each claiming to be the ECMA-182 checksum created by this identifier. Before assuming this identifier is compatible with another program's CRC64, be sure they both have matching checksums for the same strings.

Properties
----------

None

Example
-------

.. code:: text

    ; Echo the $crc hash of plain text string ``abc`` to the active window:
    ; The DATA is case-sensitive, so hash of "abc" is different than hash of "ABC"
    //echo -a abc $crc64(abc,0) / ABC $crc64(ABC,0)
    result: abc 2CD8094A1A277627 / ABC AFA18655D86CC8D8

.. code:: text

    ; Calculate the CRC-64 hash of the 256 bytes from $chr(0) through $chr(255):
    //var %i 0 | while (%i isnum 0-255) { bset &ascii $calc(1+%i) %i | inc %i } | echo -a $bvar(&ascii,1-) | echo -a $crc64(&ascii,1) should be 72414B2F65DB3AB0 | write -c ascii.dat | bwrite ascii.dat 0 256 &ascii 

.. code:: text

    ; display the same CRC of filename ascii.dat as the above binary variable &ascii
    //echo -a filesize $file(ascii.dat).size $crc64(ascii.dat) is the same as $crc64(ascii.dat,2) because default N is 2

Returns 0000000000000000 if filename does not exist:

.. code:: text

    //echo -a $crc64(no_such_file.txt,2)

Suggested Uses:
* Quick way to compare if 2 files are identical. (First check should always be comparing file sizes.)
* Quick way to check if a file's contents have changed since stored CRC checksum was made.
* Verify downloaded file hasn't been corrupted, matches the sender's original.

Note that because the default is N=2, $crc(versions.txt) is the CRC-64 for the contents of versions.txt (or 00000000 if the file doesn't exist). This differs from $sha1(versions.txt) giving the hash of the plaintext inside the parenthesis because $sha1 has default of N=0.

.. note:: CRC-32 and CRC-64 are good for detecting transfer errors. Any 1 bit changed in a file is 100% guaranteed to change the CRC-32 and CRC-64 values, which is not necessarily true for $sha1 or other 1-way hashes. There is a known pair of short strings differing by 2 bits whose $md5 hashes hashes are identical, which could not happen with CRC. However, CRC-32/64 are not good for detecting malicious tampering with a file. There is an 8-byte binary string which can change a file from any CRC-64 value to any other CRC-64 value, and these 8 bytes can be quickly calculated without brute force testing of the 2^64 possible strings.<br>

Until the version where $crc64 is released, when scripts were wanting a quick way to detect when strings were different, the no-brainer choice was $md5 because it has a much longer hash which results in a much less chance of 2 strings having identical hashes. But most importantly, $md5 and $crc were benchmarking at almost identical speeds. However $crc was optimized at the same time $crc64 was added, and both are now close to 4x as fast as $md5.<br>

The advantage of CRC-64 over CRC-32 is that the longer checksum means there is a much smaller chance that 2 unrelated strings will have matching checksum. Because of 'birthday collisions', it would need approximately $sqrt(2^32)=2^16=65536 disk files before there's a 50% chance that there would be 2 files among them having matching CRC-32 checksums. Because the CRC-64 checksum is longer, it would require $sqrt(2^64)= 4 billion files before the 50% chance of matching checksums.

While you can use $base to translate the 32-bit output from $crc into a base10 number valid for $calc, the $crc64 output is too long for the 53-bit accuracy in $calc. If you need to feed the $crc64 output to $calc, you should do as you would do for the output from $sha1, where you use $left $right or $mid to take no more than 13 hex digits as input for $base.

Here's something demonstrating how similar strings can have similar-yet-not-matching CRC-64's. In the following example, it finds strings where 'test ' followed by a 6-digit number produces a CRC-64 ending with an arbitrarily chosen group of 3 digits. For that specific group of strings, if you insert 'foobar ' in front of those strings, the new hashes will all have the same final 3 digits as each other. If you change the wildcard match from *ACE to ACE* where you look for checksums with similar beginnings, the strings having 'foobar ' inserted will all have hashes whose first 3 digits (instead of final 3) match each other. If you substituted $md5 or one of the SHA* hashes, this behavior would not be there.

.. code:: text

    //var %i 99999 | while (%i) { if (*ace iswm $crc64(test $base(%i,10,10,6),0)) echo -a $v2 vs $crc64(foobar test $base(%i,10,10,6),0) %i | dec %i }

Error Messages
--------------

None

$crc and $crc64 differs from $sha1 in that they return no error messages.

For non-existent filenames, they return checksums of all 00's instead of halting script with an error.
When calculating checksum of the $null string they returns nothing instead returning a calculation based on the null-string
When given invalid N outside the 0-2 range, they use default 2 instead of halting script with an error.

Compatibility
-------------

.. compatibility:: 7.68

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$crc </identifiers/crc>`
    * :doc:`$hash </identifiers/hash>`
    * :doc:`$sha1 </identifiers/sha1>`
    * :doc:`$md5 </identifiers/md5>`
    * :doc:`$sha256 </identifiers/sha256>`
    * :doc:`$sha384 </identifiers/sha384>`
    * :doc:`$sha512 </identifiers/sha512>`

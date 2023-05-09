$sha1
=====

$sha1 calculates the sha1 hash of a text, :ref:`binary_variables`, or file. Hash is 160-bits, shown as 40 lower-case hexadecimal characters.

Synopsis
--------

.. code:: text

    $sha1(plaintext|&binaryvar|filename,[N])

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
plaintext - Used with N = 0, just the string you want the sha1 hash of

&binaryvar - A binary variable, used with N = 1, return the sha1 hash of the content of the binvar

filename - A filename, used with N = 2, return the sha1 hash of the content of the file

N: Optional integer 0-2, where 0 returns hash of the plaintext string, 1 returns the hash of the data contained inside the named &binary variable, 2 returns the hash of the contents of the named disk filename

If the N parameter isn't used, the default 0 is used (which is different than $crc which has default of N=2.)
Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
None
Example
-------

Echo the SHA1 hash of plain text string ''abc'' to the active window:

.. code:: text

    //echo -a $sha1(abc)
    or
    //echo -a $sha1(abc,0)

The DATA is case-sensitive, so hash of "abc" is different than hash of "ABC"

Echo the SHA1 hash of the contents of the mIRC program you're running to the active window:

.. code:: text

    //echo -a $sha1($mircexe,2)

Echo the SHA1 hash of the first 1000 bytes of the mIRC program you're running to the active window:

.. code:: text

    //bread $qt($mircexe) 0 1000 &snip | echo -a $sha1(&snip,1) and again $sha1(&snip,1)

Mode 0 allows string to be null, including %variable not existing.

.. code:: text

    //unset %a | var %b $null | echo -a $sha1(%a) is $sha1(%b) is $sha1()

Mode 1 allows binvar to be zero length generates an error if the &binvar is not defined.

.. code:: text

    //noop $regsubex(foo,$null,,,&v) | echo -a $bvar(&v) $sha1(&v,1) | echo -a $bvar(&v2) $sha1(&v2,1)

Mode 2 allows filesize to be zero but not missing.

.. code:: text

    //btrunc zero.dat 0 | echo -a $sha1(zero.dat,2) | remove zero.dat | echo -a $sha1(zero.dat,2)

Suggested Uses:
* Quick way to compare if 2 files are identical. (First check should always be comparing file sizes.)
* Quick way to check if a file's contents have changed since stored sha1 hash was made.
* Verify downloaded file hasn't been corrupted, matches the hash obtained from the sender.

Note that because the default is N=0, $sha1($mircexe) is the SHA1 hash for the plaintext text string of the drive:\path\filename for the mIRC you're running, and not the hash of the filename contents. This differs from $crc($mircexe) giving the checksum of the filename contents because $crc has default of N=2.
mIRC v7.x Unicode-encodes plaintext before providing to $sha1, so v7.x and v6.x return different answers for //echo -a $sha1($chr(233))

If the text doesn't have Unicode code points above 255, to avoid having Unicode points 128-255 encoded to 2-byte pairs, the text must be fed to $sha1 as a binary variable:

.. code:: text

    //bset -ta &string 1 chloé | echo -a $sha1(&string,1)

Warning
-------

From v7.54 back through at least v6.35, and probably as far back as v6.3 when it was added, $sha1 can corrupt the contents of the &binvar it is hashing. If the length is 128+, and the file is split into 64-byte chunks, the 1st chunk is never affected, but each of the other 64-byte chunks that are not consisting entirely of 0x00 bytes is corrupted. This can be seen in the above example hashing the first 1000 bytes of mirc.exe, where v7.54 and earlier versions produce different hashes when repeating the exact same command against the same &binvar. In those same versions, this also affects using the same &binvar as the data hashed by $hmac when it uses sha1 has the hash. It returns the correct hash of the input &binvar in spite of destroying it.

.. code:: text

    //bset &v 128 1 | noop $sha1(&v,1) | echo -a $bvar(&v,1-)

Users of those versions needing to use the contents of the &binvar after hashing would need to use a throw-away temporary &binvar whose contents are not needed after being hashed. 

Error Messages
--------------

Note that $sha1 differs from $crc in that it generates error for non-existent files instead of returning hash of $null string. Also, hex string returned by $sha1 is lowercase while $crc returns uppercase hex.

.. code:: text

    * Error accessing file: $sha1

Either file does not exist, or file permissions don't allow the file to be read. i.e. $sha1(non-existent-file,2) or $sha1(c:\hiberfil.sys,2)

.. code:: text

    * Invalid parameters: $sha1

Either using a zero-length/non-existent binary variable or specifying an N where $int(%N) isn't 0-2.

.. code:: text

    Both above errors halt execution of the script

.. note:: even though an SHA1 hash collision has been found between 2 different strings, it continues to be considered adequate in some situations, especially when used by $hmac as its hash function. The collision was possible in a scheme where they finding 2 strings having a matching hash regardless of that value, but it still remains out of reach of creating collisions against a specific sha1 hash. SHA1 continues to be widely used in Google Authenticator TOTP where sha1 is used inside HMAC. It continues to be used by github to detect changes in documents, where any collision would result in keeping the existing older file and discarding the new file having the matching sha1 hash.

Compatibility
-------------

.. compatibility:: 6.3

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$sha256 </identifiers/sha256>`
    * :doc:`$sha512 </identifiers/sha512>`
    * :doc:`$sha384 </identifiers/sha384>`
    * :doc:`$md5 </identifiers/md5>`
    * :doc:`$crc </identifiers/crc>`
    * :doc:`$hmac </identifiers/hmac>`
    * :doc:`$hotp </identifiers/hotp>`
    * :doc:`$totp </identifiers/totp>`

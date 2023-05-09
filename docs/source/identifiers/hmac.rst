$hmac
=====

$hmac returns an HMAC (keyed-Hash Message Authentication Code) based on the supplied key. See the Wikipedia page for algorithm details. $hmac is used to provide the security strength for the $hotp and $totp identifiers.

Synopsis
--------

.. code:: text

    $hmac(text|&binvar|filename, key, hash, N)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - text|&binvar|filename
      - the input
    * - key
      - the key
    * - N
      - the type of input, use N = 0 if input is plain text, N = 1 for &binvar, and 2 for filename
    * - hash
      - optional, hashing algorithm, can be md5, sha1 (default), sha256, sha384, or sha512.

Due to algorithm design:
* output is a hash digest that's the same length as the digest for the hash parameter (default sha1)
* If key length is longer than hash block length (128 bytes for sha512/384 64 bytes for md5/sha1/sha256), key shortened to be the binary hash digest of the key.
* HMAC is designed for non-binary keys. Shorter keys are padded with 0x00's to 'hash's block length', so keys differing by the number of trailing 0x00's are identical.
* Because HMAC uses 2 nested hashes using 2 modified copies of the key, usage as an authentication hash is not vulnerable to the length extension attack against auth_hash=$sha512(secret $+ message), and using hash=md5 isn't as vulnerable to the other weaknesses in md5.

Properties
----------

None

Example
-------

.. code:: text

    //echo -a $hmac(message 1,key,sha1,0)
    When given "message 1" and the $hmac output, it should require knowledge of 'key' to avoid brute-force testing for 'key' that would generate the correct hash output for $hmac(message 2,key,sha1,0) and preventing an outsider from counterfeiting a message.
    
    When receiving a file as an email attachment, and the email message contains the HMAC hash, the receiver can verify the file has not been tampered with by an outsider who does not know 'shared secret' and cannot create the correct HMAC using the shared secret against a forged message: $hmac(filename,shared secret,sha256,2)
    
    Generate HMAC hash of binary string:
    //bset -t &v 1 abc | echo -a $hmac(abc,key,sha1,0) same as $hmac(&v,key,sha1,1)
    
    Keyless hmac of each file in the $mircdir folder:
    //noop $findfile($mircdir,*,0,1,if ($file($1-).size isnum) echo -a $hmac($1-,,sha256,2) size $v1 $1-)

Warning
-------

From v7.54 back through at least v6.35, $hmac corrupts the &binvar if the length is 128+ and a multiple of 64 and contains at least 1 byte that isn't 0x00. This also affects using the $sha1 identifier against &binvar too. It returns the correct HMAC hash of the input &binvar in spite of destroying it.

.. code:: text

    //bset &v 128 1 | noop $hmac(&v,key,sha1,1) | echo -a $bvar(&v,1-)

Through v7.53, $hmac using hash method sha512 or sha384 and a key whose length is 65-128 returned an incorrect HMAC due to replacing the key with its own hash for lengths 65+ instead of only for 129+. This also affects $hotp and $totp using the same combination of key length and hashname.

.. code:: text

    //echo -a $hmac(message,$str(z,65),sha512) should be 9268b9d645082fc13c54f4590883961ab2adf80b169614d4eb90fe5a645f7d4aed13b9e3151623a7fb0ef2480182879ed7d530f1d169d352ad311054ef4d14f1

Compatibility
-------------

.. compatibility:: 7.42

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$hotp </identifiers/hotp>`
    * :doc:`$totp </identifiers/totp>`
    * :doc:`$sha1 </identifiers/sha1>`
    * :doc:`$sha256 </identifiers/sha256>`
    * :doc:`$sha512 </identifiers/sha512>`
    * :doc:`$sha384 </identifiers/sha384>`
    * :doc:`$md5 </identifiers/md5>`

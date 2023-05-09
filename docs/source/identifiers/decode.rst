$decode
=======

The $decode identifier allows you to decode literal text, or text in :doc:`%vars </beginner/variables>` or :ref:`binary_variables`. The $decode identifier uses either Uuencode or Base64|MIME or Base32 to decode.

Synopsis
--------

.. code:: text

    ; decoding
    $decode(text/%var/&binvar, amubt, N)
    
    ; encryption
    $decode(text/%var/&binvar, celirznp, key[, salt/iv])

* See * :doc:`$encode </identifiers/encode>` for more info, as this identifier's purpose is to reverse the encoding or encryption in strings created by $encode.

Parameters
----------

None

Decoding
^^^^^^^^

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Argument
      - Description
    * - %var/&binvar
      - The target to be decoded
    * - a
      - Target should be decoded using base32
    * - m
      - Target should be decoded using Mime
    * - u
      - Target should be decoded using Uuencode (this is default decode type)
    * - b
      - Target is a :ref:`binary_variables`, this output the result to the &binvar and $decode returns the total number of characters written to the binvar
    * - t
      - Target is text (this is default target type)
    * - N
      - Reference index for the Nth chunk in the output 60-character mem/UUencode encoded chunk (72 for base32)

Encryption
^^^^^^^^^^

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Argument
      - Description
    * - c
      - CBC encryption mode (either c or e)
    * - e
      - ECB encryption mode (either c or e)
    * - l
      - Literal key, a 56-byte key
    * - s
      - salt 
    * - i
      - initialization vector (IV)
    * - r
      - random IV
    * - z
      - 0x00 zero padding
    * - n
      - ones and zeros padding
    * - p
      - spaces padding

Example
-------

Echo to the active screen the following decoded text, using the Mime type:

.. code:: text

    //echo -a $decode(SGVsbG8gV2lraUNoaXAgdXNlciE=,m)

Decoding Quirks
---------------

Because base64/mime decodes from 4 text to 3 bytes, and base32 decodes from 8 text to 5 bytes, there can be strings where adding an additional digit to the encoding string does not result in longer output, due to each base64 digit representing 6 bits and base32 digits representing 5.

As with most decoders, even though encoders fill unused bit positions with '0' bits, $decode ignores if they are not 0's. For example, every encoded string created by $encode which uses '=' has at least 1 unused encoding bit that wasn't needed to encode the input byte string, which is why the mime encodings ending with '==' only ever have the final mime character being any of 'AQgw'.

So, if creating a string containing random base64 or base32 characters, if the length is such that $encode would have added '=' padding, there will be multiple characters in the final position who are treated as if the same when the string is decoded.

//echo -a $decode(YmJiYmE,m) $decode(YmJiYmF,m) $decode(YmJiYmG,m) $decode(YmJiYmH,m) $decode(YmJiYmI,m) -> bbbba bbbba bbbba bbbba bbbbb

Though decode does not currently require the presence of the '=' padding so it could correctly decode the string, some past versions might, and it won't harm anything to append a '=' to the encoded string to be certain.

Base32's decoder is designed to support Google Authenticator format, which means that it ignores spaces padding, but also ignores hyphens, and accepts the 018 digits as if they were mistakes intending to be the base32 symbols O L B:

.. code:: text

    //echo -a $decode(obqwg2ln,a) same as $decode(= - = 0=8=q=w=G=2=1=n = - =,a)
    result: pacim same as pacim

However, they treat invalid input differently, with base64 ignoring input past the 1st invalid character, while base32 quits with an error if there is any invalid input outside the above substitution and ignoring.

.. code:: text

    //echo -a $decode(abc@def,a)
    * Invalid parameters: $decode
    //echo -a $decode(YWJj@YWJj,m) same as $decode(YWJj,m) -> abc same as abc

Decode returns null output caused by decoding 0 or 1 encoding symbols, so one of the workarounds for scripts needing a zero length &binvar while supporting versions prior to the $regsubex 5th parm or /bset -z is to decode such a string held in a &binvar:

.. code:: text

    //bset -t &v 1 A | echo -a $decode(&v,bm) * $bvar(&v) * $bvar(&v,0)

Decryption Quirks
-----------------

Even though /help indicates the decryption syntax for $decode is the same as the encryption syntax for $encode, $decode is designed to intentionally ignore several switches, or to ignore their content.

For example, $encode always pads 1-8 bytes to make the message have a padded length that's a multiple of 8, and defaults to applying PKCS#7 padding to messages, unless using any of 3 padding switches to override (n = 0x80 and 0x00's, z = 0x00's p = spaces). However, $decode ignores your usage of padding switches, and instead attempts to match the end of the decrypted string against all 4 types of padding. This next example shows the result of using 'z' padding for certain message lengths where the final text character is a codepoint 128-or-greater that's a multiple of 64, whose UTF8 encoding ends with byte value 128. In these cases, $decode matches the final byte of the message as if it is part of 'n' padding, resulting in the final character of the text displayed as garbled.

.. code:: text

    message ending with trailing spaces has them stripped if changing 'men' to 'mep':
    //var -s %a $encode(123 $+ $str($chr(32),4),me,key) , %b $qt($decode(%a,mez,key))
    
    final byte of message is lost:
    //bset -t &v 8 0 | while ($bvar(&v,0) == 8) { bset -tc &v 1 $str(`,$rand(1,7)) $+ $chr($calc(64*$rand(2,40))) } | echo -a original: = $bvar(&v,1-) $bvar(&v,1-).text | noop $encode(&v,bmez,key) $decode(&v,bmez,key) | echo 4 -a decrypted = $bvar(&v,1-) $bvar(&v,1-).text

Solution: You should avoid using 'p' padding which can strip trailing spaces from the message, and same for using 'z' padding for binary strings which could end with 0x00, or with text strings which could end with byte value 128.

* Encrypting by default creates a random salt, then precedes the encrypted string with a 16-byte header as the "Salted__" label followed by the 8 bytes of the random salt being used. If using the 's' switch, that allows specifying a user-defined salt instead of letting one be randomly generated. When $decode sees the 1st 8 bytes of the ciphertext matching the 'Salted__' string, it ignores the 's' parameter you used, and instead uses the 8 bytes found in the ciphertext block following the 'Salted__'. However, $decode even does that when you used the 'l' switch to use a literal key instead of creating a hashed key based on the key parameter, and it ignores the 'i' switch instructing $decode to use a literal IV and to not generate a salted-key by combining the key parameter with what it 'thinks' is a salt. And that's the only reason the following can successfully decrypt the encrypted message:

.. code:: text

    //var -s %encrypt $encode(message,mcs,key,salt1234) , %decrypt $decode(%encrypt,mcli,key,foobar)

The same thing happens in reverse, where a message was created using the 'ir' switches which instructs $encode to create the message using a literal IV and using a different hash method than used by the default salt algorithm. But here the message is successfully decrypted because $decode ignores the syntax for decoding using a salt, because it recognizes the first 8 bytes of the ciphertext matching the 'RandomIV' label, and instead of rejecting as an error, it behaves as if the 'r' switch had been used:

.. code:: text

    //var -s %encrypt $encode(message,mcir,key,abcdefgh) , %decrypt $decode(%encrypt,mc,key)
    $decode also ignores the content of the salt parameter if it detects the 'Salted__' label, and instead uses the bytes it finds there.
    //var -s %encrypt $encode(message,mcs,key,abcdefgh) , %decrypt $decode(%encrypt,mcs,key,12345678)

While this is intended to help users who don't use the correct syntax, it does not permit ciphertext to be perfectly decrypted when correct syntax is used. Using the 'ci' switches without using 'r' results in encrypting using a user-defined literal IV but does not increase the filesize by 16 bytes in order to attach it as a header. In the rare cases where this results in encrypting a message so that the first 8 bytes of the actual ciphertext matches either of the 'Salted__' or 'RandomIV' labels, $decode again ignores the user switches and decides that the 1st block of the ciphertext must be a label instead, and then it uses the 2nd block of ciphertext as if it were either a salt or IV string, then begins decryption as of the 3rd 8-byte chunk of the message, resulting in either correct decryption for the message excluding the 1st 16 bytes, or having the output garbled due to using ciphertext as a salt in order to arrive at a completely wrong salted-key and salted-IV.

This next command encrypts the message using a literal key and a literal IV without storing the IV into the message header. Because the 1st 8 bytes of the ciphertext matches the 'RandomIV' label, the 1st 16 bytes of the decrypted string is missing:

.. code:: text

    //var -sp %switches mcli , %key key encrypts 1st block of ciphertext as 'RandomIV', %iv 122 228 210 234 175 127 205 30 , %iv $regsubex(%iv,/(\d+) ?/g,$chr(\t)) , %original This isn't shownButThisIs , %enc $encode(%original,%switches,%key,%iv) | bset -t &v 1 %enc | echo -a $decode(&v,bm) 1st 8 bytes of ciphertext: $bvar(&v,1-8).text | echo 3 -a original:msg: %original | echo 4 -a decrypted as: $decode(%enc,%switches,%key,%iv)
    result:
    1st 8 bytes of ciphertext: RandomIV
    original msg: This isn't shownButThisIs
    decrypted as: ButThisIs

In the next example, the same $encode switches for encrypting using a literal IV and literal key results in ciphertext whose 1st 8 bytes matches the 'Salted__' label. This makes $decode ignore the 'li' switches being used, and ignores the content of the IV parameter. Instead, it combines the key parameter with bytes 9-16 of the ciphertext as if that's a salt, causing $decode to generate the completely wrong salted key used for decryption, resulting in completely garbled output.

.. code:: text

    //var -sp %switches mcli , %key key encrypts 1st block of ciphertext as 'Salted__', %salt 128 173 196 14 99 213 69 247 , %salt $regsubex(%salt,/(\d+) ?/g,$chr(\t)) , %original Garbled Decryption Of 3rd Block and later , %enc $encode(%original,%switches,%key,%salt) | bset -t &v 1 %enc | echo -a $decode(&v,bm) 1st 8 bytes of ciphertext: $bvar(&v,1-8).text | echo 3 -a original::::: %original | echo 4 -a decrypted as: $decode(%enc,%switches,%key,salt)
    
    result:
    48 1st 8 bytes of ciphertext: Salted__
    original::::: Garbled Decryption Of 3rd Block and later
    decrypted as: ?¦h�Û_Z.4Kò?Ñ�H)O?R´?R?i®´¹:Ôw

Solution: If you use syntax which results in an encrypted file which doesn't have either of the 2 headers-with-labels, either the encryptor needs to reverse the mime layer to check if the ciphertext happens to begin with bytes which match either of the label strings then try encrypting again with a different IV, or else the decryptor must always remove the mime layer in order to insert a fake header if such a situation happens.

You can avoid doing that most of the time by checking to see if the base64 string begins with the first 10 base64 symbols that are the encoding of the 2 labels.

If using Blowfish encryption, it's best if you not use a version prior to v7.58 due to a series of important fixes in that and prior versions. This includes the fix of a GPF bug when $decode receives certain invalid inputs, and a fix in v7.56 where random salts containing the 0x00 byte are no longer truncated. If needing to communicate with someone using using v7.55 or earlier, both sides must create their random salt using the following alias to prevent the prior incorrect handling of salts resulting in 1/32 of messages being unable to be read in either direction.

alias randsalt returnex $regsubex($str(x,8),/x/g,$chr($rand(1,255))))

$encode does not reject invalid salt/iv strings longer than 8, and instead ignores the portion beyond length 8. This means that using the length 10 $ctime string as the salt or IV results in the identical key being used across a span of 100 seconds:

/.timerfoo 120 1 echo -a $encode(message,mcs,key,$ctime) * $ctime
Compatibility
-------------

.. compatibility:: 5.8

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$encode </identifiers/encode>`
    * :doc:`$base </identifiers/base>`

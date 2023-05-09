$address
========

$address return the address of the user associated with an event in the form user@host, or of the specified user.

If used without a parameter, this identifier is a local identifier existing only for the scope of an event and return the address of the user associated with an event in the form user@host.

Otherwise, it returns the address of the specified nickname in the given type.

Synopsis
--------

.. code:: text

    $address

.. code:: text

    $address(<nick>,<type>)

.. note:: $address returns $null string if the :doc:`$ial </identifiers/ial>` doesn't contain the address for this nick.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <nick>
      - The nickname you want the address of.
    * - N
      - The type of address, a positive integer between 1-19.

.. code:: text

    //.parseline -qit :nick!user@host JOIN $active Testing :testing 1 2 3
    //var %x 0 | while (%x < 10) { echo -ag * %x $+ : $address(nick,%x) | inc %x }

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Type
      - Description
    * - 0
      - ``*!user@host``
    * - 1
      - ``*!*user@host``
    * - 2
      - ``*!*@host``
    * - 3
      - ``*!*user@host``
    * - 4
      - ``*!*@host``
    * - 5
      - ``nick!user@host``
    * - 6 
      - ``nick!*user@host``
    * - 7
      - ``nick!*@host``
    * - 8
      - ``nick!*user@host``
    * - 9
      - ``nick!*@host``

Type 10-19 are same as types 0-9 except asterisks in host are expanded to the text they replaced, then all numbers are replaced by question marks.

Masks are case-insensitive and assigned by the internet provider, but IRC servers often provide user mode +x to help disguise them.

.. note:: Using the NICK portion of an address mask can cause a false negative when it keeps from matching someone if they're using one of their other nicks, and can cause a false positive if the server doesn't prevent people from using that nick without identifying to Nickserv.
    "user" is easily changeable by someone editing their mIRC settings then reconnecting to the server. Be careful about using Type-4 mask to defend against that, because the @*.host :ref:`matching_tools-wildcard` can match other users who also use the same internet provider. Disguised IP masks created by usermode +x are in the format of hexnumber#1.hexnumber#2.hexnumber#3.IP. For IPv4 addresses, the default method for creating the shadow mask is built on IP address style N1.N2.N3.N4, and hexnumber#3 is the same for all IP addresses N1.N2.*.*, hexnumber#2 is the same for all N1.N2.N3.* addresses, and generates the same disguised IP address each time the same IP address is scrambled.

Properties
----------

None

Example
-------

.. code:: text

    on *:text:!address:#:msg $chan address is $address
    
    ;or just in an editbox
    //echo -a $address(nick,2)

Bug: mIRC incorrectly creates :ref:`matching_tools-wildcard` mask *user as if disabling identd drops the 1st character of userid in order to add the ~ tilde and as if it doesn't drop the 10th letter of the UserID in order to fit the tilde into a 10-character UserID string. mIRC creates *user by replacing the 1st letter of USER with an asterisk, regardless whether or not it's a tilde - i.e. $+(*,$mid(UserID,2)). This causes a wildcard mask for an identd UserID of 10 characters that isn't matched both with/without identd enabled, and needlessly matches short UserID hosts which differ only in the first letter.

If your UserID string is ABCDEFGHIJ, your address appears like ABCDEFGHIJ@host when identd is enabled and appears as ~ABCDEFGHI@host when it's disabled. When identd is enabled, the Type-3 *user mask is *BCDEFGHIJ@*.host, and *ABCDEFGHI@*.host when identd is disabled. (The server drops the last letter of the UserID only when the tilde causes the length to exceed 10, so RAT@host losing identd becomes address ~RAT@host without dropping the ending letter.)

The identd-enabled and identd-disabled Type-3 address masks of 10-character UserID's don't match each other because of the masks disagree over whether the UserID always ends with the J or always ends with an I. Also, the unneccessary removal of a non-tilde at the beginning of *user causes it to see an identd-enabled RAT@host and create Type-3 *AT@*.host mask which matches CAT@host, SAT@host, FAT@host, etc.

This alias returns a slight alteration of $address(nick,3) which matches both identd/non-identd nicks, and limits false matches of other UserID's. It can be called like: //echo -a $address3alt(nick)

.. code:: text

    /address3alt {
      var %user $gettok($gettok($address($1,5),1,64),2,33)
      if (~* iswm %user) { var %user * $+ $mid(%user,2) $+ $iif($len(%user) isnum 10-,*) }
      else { var %user * $+ $left(%user,9) $+ $iif($len(%user) isnum 9-,*) }
      return * $+ $chr(33) $+ %user $+ @ $+ $gettok($address($1,3),2-,64)
    }

Compatibility
-------------

.. compatibility:: 2.1a

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$mask </identifiers/mask>`
    * :doc:`$ial </identifiers/ial>`
    * :doc:`$fulladdress </identifiers/fulladdress>`
    * :doc:`$site </identifiers/site>`
    * :doc:`$wildsite </identifiers/wildsite>`


$nopnick
========

.. attention:: This feature has essentially been replaced by :doc:`$nick </identifiers/nick>`

 $nopnick returns the Nth nickname that is not an operator on the channel.

.. note:: nicks returned by $nopnick are those who don't have the 'o' operator status, even if they have the non standard +qa mode/status, it means that if a nickname is only +q, $nopnick() can return that nickname. When used with 2 parameters, it is equivalent to $nick(#,N/nick,a,o)

Note2: the nickname doesn't have to be strictly an operator to be ignored, it means that someone which is an operator and is voiced won't be returned by $nopnick.

Synopsis
--------

.. code:: text

    $nopnick(#channel,N/nick)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - #channel
      - The channel you want to check for non-op nickname 
    * - N/nick
      - The Nth non-op nick on the channel, or if you pass a nickname, it returns the number N, where $nopnick(#,N) return the nickname.

.. note:: With a third and fourth parameter, i.e. $nopnick(#,N/nick,aohvr,aohvr), this identifier behaves exactly the same as :doc:`$nick </identifiers/nick>`

Properties
----------

None

Example
-------

.. code:: text

    //echo -a $nopnick($chan,1)

Compatibility
-------------

.. compatibility:: 2.1a

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$nick </identifiers/nick>`
    * :doc:`$opnick </identifiers/opnick>`
    * :doc:`$hnick </identifiers/hnick>`
    * :doc:`$nhnick </identifiers/nhnick>`
    * :doc:`$vnick </identifiers/vnick>`
    * :doc:`$nvnick </identifiers/nvnick>`

$nvnick
=======

.. attention:: This feature has essentially been replaced by :doc:`$nick </identifiers/nick>`

 $nvnick returns the Nth nickname that has no status on the channel.

.. note:: $nvnick(#,N) always returns a nickname which has a status below voice.

Synopsis
--------

.. code:: text

    $nvnick(#channel,N/nick)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - #channel
      - The channel you want to check for non-voice nickname 
    * - N/nick
      - The Nth 'regular' nick on the channel, or if you pass a nickname, it returns the number N, where $nvnick(#,N) return the nickname.

.. note:: When 2 parameters are used, it's the equivalent of $nick(#,N,r). With a third and fourth parameter, i.e. $nvnick(#,N/nick,aohvr,aohvr), this identifier behaves exactly the same as :doc:`$nick </identifiers/nick>`

Properties
----------

None

Example
-------

.. code:: text

    //echo -a $nvnick($chan,1)

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
    * :doc:`$nopnick </identifiers/nopnick>`

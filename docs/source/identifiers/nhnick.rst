$nhnick
=======

.. attention:: This feature has essentially been replaced by :doc:`$nick </identifiers/nick>`

 $nhnick returns the Nth nickname that is not an halfop/helper on the channel.

.. note:: $nhnick always returns nickname which have a status below halfop/helper, excluding the non standard +qa mode/status, it means that if a nickname is only +q, $nhnick() can return that nickname but a nickname being only +o can't be returned by $nhnick (it's not a status below halfop/helper)

Note2: the nickname doesn't have to be strictly an halfop/helper to be ignored, it means that someone which is an halfop/helper and is voiced won't be returned by $nhnick.

Synopsis
--------

.. code:: text

    $nhnick(#channel,N/nick)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - #channel
      - The channel you want to check for non-halfop/helper nickname 
    * - N/nick
      - The Nth non-halfop/helper nick on the channel, or if you pass a nickname, it returns the number N, where $nhnick(#,N) return the nickname.

.. note:: With a third and fourth parameter, i.e. $nhnick(#,N/nick,aohvr,aohvr), this identifier behaves exactly the same as :doc:`$nick </identifiers/nick>`

Properties
----------

None

Example
-------

.. code:: text

    //echo -a $nhnick($chan,1)

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
    * :doc:`$nopnick </identifiers/nopnick>`
    * :doc:`$vnick </identifiers/vnick>`
    * :doc:`$nvnick </identifiers/nvnick>`


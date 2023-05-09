$knick
======

The $knick identifier refers to the nickname of a user who has been kicked from a channel. This can also be the local mIRC client nickname if an On me - mIRC|ON ME kick event is being monitored.

Synopsis
--------

.. code:: text

    $knick

Parameters
----------

None

Example
-------

Send a notice to a kicked user with information about the kick:

.. code:: text

    ON *:KICK:#: {
      .notice $knick You were kicked from $chan by $nick for the following reason: $iif($1-,$1-,No reason given)
    }

The following is an example of the above code:

.. code:: text

    You were kicked from #BreakingBad by WalterWhite for the following reason: Stop mass-highlighting!

Compatibility
-------------

.. compatibility:: 2.1a

See also
--------

.. hlist::
    :columns: 4

* On ban - mIRC|ON BAN
* On join - mIRC|ON JOIN
* On part - mIRC|ON PART
* On unban - mIRC|ON UNBAN
    * :doc:`$chan </identifiers/chan>`
    * :doc:`$nick </identifiers/nick>`


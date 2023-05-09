$filename
=========

The $filename identifier is filled when an event's trigger deals with a file, such as On playend - mIRC|ON PLAYEND, On filercvd - mIRC|ON FILERCVD, On filesent - mIRC|ON FILESENT, etc.

Synopsis
--------

.. code:: text

    $filename

Properties
----------

None

Examples
--------

Echo the name of the filename, along with both the user's nickname and address if available, after a /dcc command - mIRC|DCC Get has successfully finished:

.. code:: text

    ON *:FILERCVD:*:echo -a Received filename: $filename $iif($nick,from $nick - ,from) Address: $address

Echo the name of the file that finished playing to the active window:

.. code:: text

    ON *:PLAYEND:echo -a * $filename has just finished playing.

Compatibility
-------------

.. compatibility:: 4.5

See also
--------

.. hlist::
    :columns: 4

* On filercvd - mIRC|ON FILERCVD
* On filesent - mIRC|ON FILESENT
* On playend - mIRC|ON PLAYEND
    * :doc:`/dcc </commands/dcc>`
    * :doc:`/play </commands/play>`


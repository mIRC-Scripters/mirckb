$msgstamp
=========

$msgstamp returns UTC timestamp for a irc server message that has an IRCv3 @time prefix tag, such as when CAP server-time or znc.in/server-time[-iso] are enabled on a server.

Synopsis
--------

.. code:: text

    $msgstamp

Parameters
----------

None

Example
-------

Reuse a ZNC playback buffer message timestamp with a self-defined format:

.. code:: text

    //echo -a $asctime($msgstamp, "[HH:nn:ss]") $text

Compatibility
-------------

.. compatibility:: 7.33


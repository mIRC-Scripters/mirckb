$nonstdmsg
==========

$nonstdmsg mIRC added support for handling PRIVMSG/NOTICE events that use source/target combinations that are not normally sent by an IRC server. These now trigger the on OPEN/TEXT/ACTION/NOTICE/SNOTICE/CTCP events but set $nonstdmsg to $true.

Synopsis
--------

.. code:: text

    $nonstdmsg

Parameters
----------

None

Compatibility
-------------

.. compatibility:: 7.69

See also
--------


On Udpwrite
===========

The ON UDPWRITE is an event which was added in mIRC with UDP, but never has been documented. The event was meant to be used as the :doc:`on sockwrite </events/on_sockwrite>` event for TCP, however the actual design ended up being that:
* on sockwrite triggers for UDP socket if no error happened
* on udpwrite will trigger if an error occurred.

.. note:: This behavior was changed for consistency and backward compatibility in mIRC 7.33:

* on udpwrite is no longer triggered.
* on sockwrite triggers for UDP socket regardless of the error state.

Writing more
------------

It is possible that the data hasn't sent successfuly, especially with UDP, you should be checking for error with :doc:`$sockerr </identifiers/sockerr>` before trying to do anything, here is a list of the possible value for $sockerr in the on UDPWRITE event:

* 0 - The data has been written sucessfuly.
* 3 - Error occurred while trying to send the data, $sock().wsmsg will contain a more specific error message.

Examples
--------

.. code:: text

    on *:udpwrite:name:{
      if ($sockerr) { echo -s An error occured while trying to read data: $sock($sockname).wsmsg | return }
    }

Compatibility
-------------

.. compatibility:: 5.5

Removed: mIRC v7.33

Removed On:27/05/2014

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/sockwrite </commands/sockwrite>`
    * :doc:`/sockclose </commands/sockclose>`
    * :doc:`/sockread </commands/sockread>`
    * :doc:`/sockaccept </commands/sockaccept>`
    * :doc:`/sockpause </commands/sockpause>`
    * :doc:`$sock </identifiers/sock>`
    * :doc:`$sockbr </identifiers/sockbr>`
    * :doc:`$sockerr </identifiers/sockerr>`

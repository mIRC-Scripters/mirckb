On Udpread
==========

The ON UDPREAD triggers when there is info waiting to be read on the specified UDP socket connection. You can read this info using the :doc:`$sockread </commands/sockread>` command.

To be able to use this event, you need to get the udp socket to stay opened (by default it is closed after each :doc:`$sockudp </commands/sockudp>` command) by using the -k switch of /sockudp.

.. note:: If this event triggers but no /sockread is performed to attempt to read the buffer, it is assumed that no script exists that is handling this buffer, so it is cleared and the info it contained is lost.

mIRC in general only understand $crlf terminated line. With socket, mIRC will stop at :doc:`$lf </identifiers/lf>` terminated line and any :doc:`$cr </identifiers/cr>` before a $lf is removed.

.. note:: A single /sockread may not be enough to read the entire buffer. You should keep reading until :doc:`$sockbr </identifiers/sockbr>` is set to zero. This is far faster than letting mIRC re-trigger the event. If your script does not read the whole buffer, the on udpread event is re-triggered if:

# you were reading into a &binvar.
# you were reading into a %var and there is still a terminated line in the buffer waiting to be read.


Synopsis
--------

.. code:: text

    ON <level>:UDPREAD:<matchtext>:<commands>

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <matchtext>
      - The name of the socket you want event to trigger on.
    * - <commands>
      - The commands to be performed when the event listener's criteria is met.

Connection State
----------------

You should be checking for error with $sockerr before reading data, here is a list of the possible value for $sockerr in the on UDPREAD event:

* 0 - Data received correctly.
* 3 - Error on connected socket occurred, $sock().wsmsg will contain a more specific error message.

Examples
--------

.. code:: text

    on *:udpread:name:{
      if ($sockerr) { echo -s An error occured while trying to read data: $sock($sockname).wsmsg | return }
      else {
        sockread %a
        echo -s rcvd: %a
      }
    }

Compatibility
-------------

.. compatibility:: 5.5

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

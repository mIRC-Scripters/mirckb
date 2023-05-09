On Sockwrite
============

The ON SOCKWRITE event triggers when data has been sent on a socket, even on a UDP socket. This event allows you to send more data without reaching the limit of the queue.

Synopsis
--------

.. code:: text

    ON <level>:SOCKWRITE:<matchtext>:<commands>

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

Writing more
------------

It is possible that the data hasn't been sent successfuly, especially with UDP, you should be checking for error with :doc:`$sockerr </identifiers/sockerr>` before trying to do anything, here is a list of the possible value for $sockerr in the on SOCKWRITE event:

* 0 - The data has been written successfuly.
* 3 - Error occurred while trying to send the data, $sock($sockname).wsmsg will contain a more specific error message.

Examples
--------

.. note:: Those example are not checking for :doc:`$sockerr </identifiers/sockerr>` to focus on their real purpose

What if you are making a server and you want to close the socket of a client, but you want to warn that client that you are going to close the socket?

You could easily be tempted to use the easy:

.. code:: text

    /sockwrite -n socket QUIT
    /sockclose socket

But this isn't going to work as expected, it might work, it might not work, here is a proper method:

.. code:: text

    sockwrite -n socket QUIT
    set %closesocket 1
    ...
    
    on *:sockwrite:socket:{
    ;check that all the data has been sent on the socket
      if ($sock(socket).sq == 0) {
        ;if we must close the socket
        if (%closesocket == 1) sockclose socket
      }
    }

Here is an example that will use on sockwrite to avoid getting an error because the sending buffer is full.

Let's assume you want to make a script which allows the user to input some text and create a pastebin link from that text using your favorite pastebin website.

The length of the data to be sent would be unknown, to make the script very well, you don't want to send the data line by line, that would be a waste, you want to send the maximum each time.

We are naturally not using a single line otherwise our limit would be of the line length limit of mIRC (4150 bytes).

The limit of the sending buffer being 16384, that's our maximum. A nice method is to write the content to be sent to a file and then to use {{mIRC|File handling}}. After :doc:`/fopening </commands/fopen>` the file, use :doc:`$fread </identifiers/fread>`(<name>,<N>,<&binvar>) which will fill <&binvar> with N bytes from the current pointer in the file, you can set N here to 16384 to get the fastest sending.

.. code:: text

    ;When you are about to send
    var %f content.txt
    .fopen handle $qt(%f)
    ;we check for the return value of $fread because if you get 0, the file is empty and there is nothing to send
    if ($fread(handle,16384,&tosend) > 0) sockwrite socket &tosend
    
    ;and then :
    
    on *:sockwrite:socket:{
      ;if we sent all of the previous content
      if ($sock(socket).sq == 0) {
        if ($fread(handle,16384,&tosend) > 0) sockwrite socket &tosend
        else ;we're done sending the content
      }
    }

Note that this is how you should theorically handle the sending of an unknown length of data. However, if the sending buffer is empty, you can send more than 16384 bytes (as long as you can set the binary variable holding more than that) using a binary variable. mIRC will correctly cut that in chunk of 16384 bytes or less. This then only becomes a problem if you are willing to queue more without waiting for it to be sent (which could take some times, you would end up with an error because the sending buffer is full, and you would need the above event)

Compatibility
-------------

.. compatibility:: 3.5

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on sockopen </events/on_sockopen>`
    * :doc:`on sockread </events/on_sockread>`
    * :doc:`on socklisten </events/on_socklisten>`
    * :doc:`on sockclose </events/on_sockclose>`
    * :doc:`/sockwrite </commands/sockwrite>`
    * :doc:`/sockclose </commands/sockclose>`
    * :doc:`/sockread </commands/sockread>`
    * :doc:`/sockaccept </commands/sockaccept>`
    * :doc:`/sockpause </commands/sockpause>`
    * :doc:`$sock </identifiers/sock>`
    * :doc:`$sockbr </identifiers/sockbr>`
    * :doc:`$sockerr </identifiers/sockerr>`
    * :doc:`$sockname </identifiers/sockname>`

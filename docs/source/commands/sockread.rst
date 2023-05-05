/sockread
=========

The **/sockread** command reads bytes from the receive buffer of a socket connection into a specified variable. This command must be and is to be used inside socket events.

mIRC in general only understand :doc:`$crlf </identifiers/crlf>` terminated line. With socket, mIRC only understands :doc:`$lf </identifiers/lf>` terminated line (any :doc:`$cr </identifiers/cr>` before a :doc:`$lf </identifiers/lf>` is removed).

The number of bytes waiting to be read can be retrieved using :doc:`$sock(name).rq </identifiers/sock>`

By default:

* /sockread %var reads a terminated line into the variable, if the received buffer does not contain a terminated line, no byte are read into the variable.
* /sockread &var try to read 4096 bytes into the variable.

The real number of bytes read by /sockread can be retrieved using :doc:`$sockbr </identifiers/sockbr>` .

Synopsis
--------

.. code:: text

        /sockread [-fn] <%var|&binvar>
        /sockread [numbytes] <%var|&binvar>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - f
      - When reading a terminated line (/sockread %var or /sockread -n &var), forces mIRC to fill the variable with whatever text is in the receive buffer, even if it does not end in a terminated line.
    * - n
      - Reads a terminated line into a :doc:`&binvars </intermediate/data_storage.html#binary-variables>` . If the incoming line does not contain a terminated line, no byte will be read into the :doc:`&binvars </intermediate/data_storage.html#binary-variables>` , unless you specify the **-f** switch.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - [numbytes]
      - The number of bytes to read from the receive buffer.
    * - [%var/&binvar]
      - The name of the variable to read the socket buffer into.

Reading
-------

A single /sockread may not be enough to read the entire buffer (if you are reading line by line for example). You might want to keep reading until :doc:`$sockbr </identifiers/sockbr>` (the number of bytes read) is set to zero. This is far faster than letting mIRC re-trigger the event. If your script does not read the whole buffer, the on sockread event is re-triggered if:

    a) you were reading into a &binvar.

    b) you were reading into a %var and there is still a terminated line in the buffer waiting to be read. 

This means you will miss the last line if it is not a terminated line and you are reading line by line only (and not in a binvar, although it's also easier to use on sockclose with binvar if you are reading line by line and facing this). You can read that line in the on sockclose event, :doc:`see below </commands/sockread#lAst_line_not_showing_up>` .

.. note:: (fixed since mIRC 7.36): Using SSL, on sockread might not be retriggered as it should, :doc:`on sockclose </events/on_events/on_sockclose>` will be triggered too early with $sockerr sets to 3, you must read the receive buffer from that event

.. note:: that the data received will vary in size. Practically speaking, we receive several kilobytes per second, it is easy to assume that the data you want is going to be sent and received the same way and above all, the way you want, but that's incorrect, you might receive very small packet at a very small speed.

A common situation when dealing with HTML is to check the source of the page you are working with, to identify something that is unlikley to change, and to use that as a reference. Doing this is not bad, but the way it is usually implemented by mIRC user is incorrect.

The common errors are to blindly try to match what you saw in the source as you read it with your socket but also to try to read from the received buffer assuming it will always have the data already, let's consider the following source of a page:

"this is my reference:

I want that line"

There are two mistakes:

* Trying to match the reference as you are reading. Consider the following code

.. code:: text

    on *:sockread:name:{

    var %a

    sockread -f %a

    if (%a == this is my reference:) {

    ...

    }

    }

If you do that, you cannot guarantee it will work 100% of the time.

If the received buffer is filled with a few bytes and ends up being "this is my ref" when on sockread triggers, the -f switch will force mirc to read that, and you won't be able to match your full line, for example here, the next time the event triggers, you might have a received buffer containing "erence:", but it might be "erence:\r\nI want that line" as well, screwing you anyway.

So you might think here "let's not use -f then":

.. code:: text

    on *:sockread:name:{

    var %a

    sockread %a

    if (%a == this is my reference:) {

    ...

    }

    }

.. note:: that you can read that last non terminated line inside the :doc:`on sockclose </events/on_sockclose>` event), should be fine. In fact, in this specific example and in general, it will work, because you are making sure %a is a full line or nothing. Well that's why it works in most situation, you are checking that %a is a specific text, which would fail if no byte were read into %a because a terminated line couldn't be found. However, if you are in a situation where you must check that %a is $null (usually because it read an empty $crlf line), you must check :doc:`$sockbr </identifiers/sockbr>` to know if you read bytes at all, a good example of this usage is shown below, which discard the headers of HTTP (check for an empty value after /Sockread %a reads an empty $crlf line):

.. code:: text

    alias testHTTP {

    sockclose testHTTP

    sockopen testHTTP mirc.com 80

    }

    on *:sockopen:testHTTP:{

    if (!$sockerr) {

    sockwrite -n $sockname GET / HTTP/1.1

    sockwrite -n $sockname Host: mirc.com

    sockwrite -n $sockname

    }

    }

    on *:sockread:testHTTP:{

    if (!$sockerr) {

    if ($sock($sockname).mark) {

    ; here you can start reading the real source the way you want

    }

    else {

    var %a

    sockread %a

    if ($sockbr) {

    if (%a == $null) sockmark $sockname 1

    }

    }

    }

    }

Getting problem because you are not checking properly for $sockbr is very unlikely to happen if you are reading line by line, because it is much much slower than reading the whole content of the received buffer and as such, the received buffer is filled by mIRC faster than your socket code reads it. But it is still possible.

Another solution consists in making a buffer by yourself and adding what you are reading to it, until you get the correct portion you want (a terminated line in these examples).

If you are reading the whole content of the received buffer with one /sockread using binary variable or just large portion of the received buffer in a binary variable, you are more likely to see the 

issue because you are basically reading the buffer as fast as mIRC fills it (or faster than line by line for large portion). The same solutions exists for binary variables, use /sockread -n to read a terminated line into the binvar, check $sockbr to make sure you read something etc. Using $bfind is the correct way to parse, unless you have very good evidence about the length of the lines you are going to receive and you want to go the easy way: if (text operator $bvar(&a,1,4096)) or similar.

* Reading from the receive buffer

This is the same as above but once you found the reference with the script, you want to grab the next line:

.. code:: text

    on *:sockread:name:{

    var %a

    sockread %a

    if ($sockbr == 0) return

    if (%a == this is my reference:) {

    sockread %a

    echo -a my line: %a

    }

    }

The same issue can happen, you cannot make sure there is a terminated line in the receive buffer. People mainly uses that because it avoids saving the state for the next time the event retriggers, indeed the correct way to read the next line once you found the reference is to try reading a terminated line using /sockread %var (or to use your own buffer and check when you have a new line, just like above) but you need to save the state if you can't find the next line currently:

.. code:: text

    on *:sockread:name:{

    var %a

    sockread %a

    if ($sockbr == 0) return

    if (%tryingnextline) { echo -a my line: %a | unset %tryingnextline | return }

    if (%a == this is my reference:) {

    set %tryingnextline 1

    sockread %a

    if ($sockbr) {

    echo -a my line: %a

    unset %tryingnextline

    }

    }

    }

.. note:: it can be a good idea and might be simpler for you to read everything to a file and then parse that file.

Last line not showing up
------------------------

Another common problem is reading the last line sent by an HTTP server, which isn't a terminated line (no $crlf or $lf).

Indeed, if you are using /sockread %var, you're will read properly line by line but that last line won't be read by this sockread command.

We also saw how this non terminated line in the received buffer wouldn't make mIRC retrigger the on sockread event.

One solution which doesn't involve more than that, is to read that line from the on sockclose event, indeed you are sure on sockread read the previous line, so inside on sockclose, you should get only that last non terminated line, this time we use the -f switch to force the read:

.. code:: text

    on *:sockclose:name:{

    if (!$sockerr) {

    var %a

    sockread -f %a

    if ($sockbr == 0) return

    echo -a > %a

    }

    }

If you are using HTTP 1.1 and you actually want the socket to remain open, you would need to grab the value of the content-length header, store that in a variable and increase another variable with the length of what you are reading, if the length of the received buffer + the value of that variable equal the value of the content length, you should first try to see if you have a line by reading with /sockread %a, and if no byte is read, then use /sockread -f %a.

Example
-------

Here is an example which will read and echo to the status window what is sent by a server line by line.

.. note:: leading/consecutives and trailing spaces and non-printable characters won't be shown correctly.

.. note:: 2**: too long line will produce an error.

.. note:: 3**: Using SSL, the on sockread event might not be triggered though it should, you must read the rest in the on sockclose event (has been fixed since mIRC 7.36).

.. code:: text

    ON *:SOCKREAD:mySocket:{
    var %a
    if ($sockerr > 0) { return }
    sockread %a
    if (!$sockbr) return
    while ($sockbr) {
    echo -a > %a
    sockread %a
    }
    }

.. note:: as we just saw, if the last line in the source does not end with a terminated line, it won't be read by that event.

If you ever worked with HTTP 1.1, you know that it can send data in chunk, here is a way to write the real content to a file:

.. code:: text

    on *:sockopen:socket:{
    ... your request...
    sockmark $sockname 0
    ;we write to source.txt
    .remove source.txt
    unset %bytestoread
    }
    on *:SOCKREAD:socket: {
    if (!$sockerr) {
    if ($sock($sockname).mark) {
    ;if we have a chunk to read
    if (%bytestoread > 0) {
    ;we try to read that much
    sockread %bytestoread &a
    bwrite source.txt -1 -1 &a
    ;but $sockbr tells us how much we read, we decrease by that number (in case we received something smaller than what we want, this part of the code will retrigger in this case, until %bytestoread is 0)
    dec %bytestoread $sockbr
    }
    ;if we don't have a chunk
    else {
    var %a
    sockread %a
    ;skip empty line
    while ($sockbr) && (%a == $null) { sockread %a }
    if (!$sockbr) || (%a == $null) return
    ;last chunk
    if (%a == 0) echo -a done
    ;convert the hexadecimal number to decimal
    else { set %bytestoread $base(%a,16,10) }
    }
    }
    else {
    ;$sock().mark is used to discard the headers
    var %a
    sockread %a
    if (%a == $null) sockmark $sockname 1
    }
    }
    }

Compatibility
-------------

Added: mIRC v5.3 (04 Jan 1998)

See Also
--------

.. hlist::
    :columns: 4

    * :doc:`$sock </identifiers/sock>`
    * :doc:`$sockname </identifiers/sockname>`
    * :doc:`$sockerr </identifiers/sockerr>`
    * :doc:`$sockbr </identifiers/sockbr>`
    * :doc:`/sockaccept </commands/sockaccept>`
    * :doc:`/sockclose </commands/sockclose>`
    * :doc:`/socklist </commands/socklist>`
    * :doc:`/socklisten </commands/socklisten>`
    * :doc:`/sockmark </commands/sockmark>`
    * :doc:`/sockopen </commands/sockopen>`
    * :doc:`/sockpause </commands/sockpause>`
    * :doc:`/sockrename </commands/sockrename>`
    * :doc:`/sockudp </commands/udp-socket>`
    * :doc:`/sockwrite </commands/sockwrite>`

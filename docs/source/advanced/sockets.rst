Sockets
=======

.. attention:: This article assumes that you have intermediate to advanced knowledge of the mIRC Scripting Language and familiarity with on events and custom aliases.

mIRC Sockets are a set of commands, identifiers, and events that allow scripts to create network sockets. mIRC supports both UDP and TCP sockets.

Socket
------

A socket is one endpoint of a two-way communication link between two processes running on a network. A socket is bound to a port number by which it can be identified. In mSL it is also bound to a specific name which we will call a handle. An endpoint is simply a combination of an IP address and a port number.

The following is an example of an endpoint:

.. code:: text

	74.125.91.104:80

The first part is the IP address (in this example we used www.google.com). The number that follows the colon (:) is the port number. In this case it's port number 80, which happens to be the default HTTP port.

IP Address
----------

An IP address is the numerical identification that is assigned to devices that utilize the Internet Protocol like your computer's network card. Think of it as your home address for the Internet. There are two versions of the IP protocol: IPv4 and IPv6. This tutorial will cover both.

A traditional IP address looks like this:

.. code:: text

	74.125.91.104

This is in fact IPv4. It is made up of four octets, each ranging between 0 and 255.

An IPv6 address looks something like this:

.. code:: text

	2002:1:0:1:0:0:4a7d:5b68

The details of how these addresses work are beyond the scope of this article.

Port
----

A port number is a 16-bit positive integer ranging from 0 to 65535. (2^16-1), giving you a total of 65,536 ports. Ports 1-1023 are called well known ports, ports 1024-49151 are registered ports, and ports in the range of 49152–65535 are dynamic and/or private, they cannot be registered.

Be careful not to be confused between the client and server ports. The server port is the port in which the client (you) will attempt to establish a connection; the server listens to incoming connection on this port. The client port is the port at the client's end, which are an incremental number and a much higher port number.

.. list-table:: Commonly Used Ports
	:widths: 50 50
	:header-rows: 1

	* - Application
	  - Port
	* - FTP	
	  - 20/21
	* - SSH
	  - 22
	* - HTTP
	  - 80
	* - POP3 (Email)
	  - 110
	* - HTTP over SSL (HTTPS)
	  - 443

mIRC Sockets
------------

There are two types of Internet sockets (there are actually more, but only these two types are available natively through mIRC):

Stream Sockets
Datagram Sockets

Stream Sockets
--------------

Stream sockets achieve a higher level transmission quality. Stream sockets are a connection-oriented protocol. The Transmission Control Protocol, TCP, does this by making sure that your data arrives in the correct order and error-free. Most applications like mIRC itself, a telnet client, and your web browser use that protocol.

Datagram Sockets
----------------

Datagram sockets on the other hand are called connectionless. You may have heard UDP or the User Datagram Protocol. The reason they are called connectionless is because they do not have to maintain an open connection as you do with stream sockets. As a consequence, data may arrive just fine, it may arrive out of order, or it might even get lost and never arrive.

So why on earth would anyone use that you may ask? Speed, speed, and ... more speed! UDP is much faster. Your data gets the address slapped on it and gets fired away. This protocol is best suited for streaming and games where speed is the top most priority.

Summary
-------

Below is a recap of the two socket types available:

.. list-table:: TCP vs UDP
	:widths: 50 50
	:header-rows: 1

	* - TCP
	  - UDP
	* - Goal: Used when reliable transport required and speed is secondary
	  - Goal: Used when speed is required and guaranteed delivery is secondary
	* - Connection-Oriented Protocol
	  - Connectionless Service
	* - - Reliable
	    - Order is guaranteed
	    - No data loss
	  - - Unreliable "best effort" delivery 
	    - Order is not guaranteed
	    - Possible data loss
	* - Decent Speed
	  - Fast

Where do we go from here?
-------------------------

So where do you go from here? Basic on the kind of socket you are looking to work with you will have to decide whether you want UDP or TCP.

TCP Sockets
===========

mIRC has built-in support for TCP Sockets. This tutorial is the TCP Sockets continuation of the sockets introduction. If you haven't read that, please do so first before moving on to this one.

Now that you have some familiarity with the different types of sockets we can go into the scripting aspect of things. The most common task scripters want to perform is retrieving a piece data from some website.

Throughout this tutorial we will create two complete scripts, one which will go to our very own example page and a second one that will go to YouTube and get the title of the page and the view count.

Creating a Connection
---------------------

Before we can do anything else we must first create a new connection to a specific address on a given port. This is done using the /sockopen command:

sockopen <handle> <address> <port>
A handle simply is a unique name by which we can refer to this exact socket.

Creating a secured Connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

I am sure you are very familiar with the padlock icon next to the URL in your browser. That icon indicated that website uses secure http (also known as HTTPS). The default port for HTTPS is 443. The /sockopen command can also be used to create secured SSL connections as well using the following syntax:

.. code:: text

	sockopen -e <handle> <address> <port>

IPv4 vs. IPv6 Sockets
~~~~~~~~~~~~~~~~~~~~~

The /sockopen command is directly influenced by the Ipv6 mode you have going on. Check this page for more information about IPv6.

Connection Example
~~~~~~~~~~~~~~~~~~

Example 1
^^^^^^^^^

Since we want to socket to our silly demo page, http://www.zigwap.com/mirc/sockets_demo, our sockopen command will look something like this:

.. code:: text

	alias example1 {
	  sockopen example1 www.zigwap.com 80
	}

The above alias will create a socket by the name "example1". We can use that name to manipulate our socket later on. As a precaution, in order to not attempt to open an already opened socket, we will close it. If the socket is not open, mIRC will simply do nothing. In the advanced part of this tutorial we will explain how to handle this situation more gracefully by creating dynamic names which will give us the ability to create as many sockets as we need.

.. code:: text

	alias example1 {
	  sockclose example1
	  sockopen example1 www.zigwap.com 80
	}

Example 2 (YouTube)
^^^^^^^^^^^^^^^^^^^

In this example I thought we would do something different. Providing a YouTube link like http://www.youtube.com/watch?v=FDw0NdhK6QU and the script will return information on the video.

.. code:: text

	alias YouTube {
	   if ($regex($1-, /\Qyoutube.com/watch?v=\E(\w+)$/)) {
	     sockclose YouTube
	     sockopen YouTube www.youtube.com 80
	     ; keep the video ID for later on
	     sockmark YouTube $regml(1)
	   }
	   else {
	     echo $color(info) -aef /YouTube: invalid youtube link
	     halt
	   }
	}

The Socket Mark
---------------

In the example above we introduced another command, the /sockmark command. The /sockmark command lets you store some text for that socket which can easily be retrieved using the $sock().mark identifier later on. This is a better alternative to using global variables (or any other kind of global storage method) because you don't need to clean it up later. The socket mark goes away automatically with the socket when it is closed.

.. code:: text

	sockmark <handle> <value>
	; The following will clear the mark:
	sockmark <handle>

The socket mark is restricted to the same line limit as the rest of mIRC (just under 4,150 bytes). A wildcard pattern can be used in the handle parameter to set the value of multiple sockets at once.

.. code:: text

	; Our socket mark value:
	$sock(<handle>).mark

Transmitting a Request After a Successful Connection
----------------------------------------------------

When a successful connection to the remote end-point has been established, the on sockopen event will trigger. Inside the on sockopen event we must send our initial request which would depend on what our script wants to do. A typical script that utilizes the HTTP protocol must send its headers in this event.

.. note:: If a connection failed, on sockopen will also trigger, the difference this time is that $sockerr is set, see the Error Handling section below for more informations.

The typical syntax for the on sockopen event is:

.. code:: text

	on *:sockopen:<handle>: {
	  ;Your requests goes here
	}

As we said before, from within the sockopen event we must send our request to the remote end-point. To send data to the remote end-point through the socket we use the /sockwrite command. The sockwrite command has the following syntax:

.. code:: text

	sockwrite [-tn] <name> <text|%var|&binvar>
	; You can limit the amount of data sent using the following syntax:
	sockwrite -b[tn] <name> <numbytes> <text|%var|&binvar>

By default, all space-delimited tokens that begin with the '&' symbol are treated as binary variables. The -t switch can be used to make the /sockwrite command treat it all as plain text instead.

The Sockwrite -n Switch and $crlf
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Because the sockwrite command can be used to send any type of data you must be very explicit about the data you are sending. If you want to send multiple lines, you must append a $crlf to the end of your data. Alternatively you can also use the -n switch which will append a $crlf automatically for you if the line doesn't already ends with a $crlf.

Consider the following piece of code:

.. code:: text

	sockwrite $sockname AAAAA
	sockwrite $sockname BBBBB
	sockwrite $sockname CCCCC

Even though we have used three distinct sockwrite calls to send the data, the exact data we sent is:

.. code:: text

	AAAAABBBBBCCCCC

On the other hand, the following code:

.. code:: text

	sockwrite -n $sockname AAAAA
	sockwrite -n $sockname BBBBB
	sockwrite -n $sockname CCCCC
	/* Or:
	  sockwrite $sockname AAAAA $+ $crlf
	  sockwrite $sockname BBBBB $+ $crlf
	  sockwrite $sockname CCCCC $+ $crlf
	*/

Sent the following data:

.. code:: text

	AAAAA
	BBBBB
	CCCCC

Understanding this concept is important to understanding how to send data correctly via protocols like HTTP.

/sockwrite's limit
~~~~~~~~~~~~~~~~~~

Just like anywhere in the mIRC Scripting language, there is a limit on the number of bytes you can send using /sockwrite. A socket in mIRC has two buffers, one for the receiving and one for the sending. The sending buffer is limited to 16384 bytes. /sockwrite will produce an error if you try to add more in the buffer. However, if the buffer is empty, it won't produce an error and will work.

In a typical script using HTTP and the GET method to grab something from a website, it's unlikely that you will reach this limit but note that when using POST, it's more likely to reach that limit, you can find an example on how to workaround this by using the on sockwrite event here.

Sending Data Example
~~~~~~~~~~~~~~~~~~~~

Example 1 (Continue)
^^^^^^^^^^^^^^^^^^^^

Remember that the page we want to socket to is http://www.zigwap.com/mirc/sockets_demo. Our sockopen event will look something like this: (In this example I will be using version 1.0 of HTTP)

.. code:: text

	on *:sockopen:example1: {
	  sockwrite -n example1 GET /mirc/sockets_demo HTTP/1.0
	  sockwrite -n example1 Host: www.zigwap.com
	  sockwrite -n example1
	}

.. note:: In HTTP, we must send a blank line at the end of our request to indicate that we are done with the header part, that's our 'sockwrite -n example1': remember -n appends a $crlf.

Example 2 (YouTube, Continue)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We will now add the sockopen part of our YouTube script. Recall that we stored the video ID in the socket mark? Well, we will now retrieve that ID using the $sock identifier and its mark property.

.. code:: text

	on *:sockopen:YouTube: {
	  sockwrite -n YouTube GET /watch?v= $+ $sock($sockname).mark HTTP/1.1
	  sockwrite -n YouTube Host: www.youtube.com
	  sockwrite -n YouTube
	}

URL Encoding
------------

Some characters have special meanings when used in the URL. You might be familiar with URLs that look like this:

.. code:: text

	http://www.example.com/foo.php?request&name=value

If we want to send something that includes characters like the '=', '?' and '&' we must escape them before they can be safely used. The exact rules are specified by the RFC 1738 (Top of page 3).

We will use the following aliases to encode and decode URLs:

.. code:: text

	; Encodes URLs
	alias urlEncode return $regsubex($1, /(\W)/g, $+(%, $base($asc(\t), 10, 16, 2)))
	; Decode encoded URLs
	alias urlDecode return $regsubex($replace($1, +, $chr(32)), /%([A-F\d]{2})/gi, $chr($base(\1, 16, 10)))

	; Since mIRC 7.x, mIRC is Unicode, since the percent encoding is byte based, you must decode the byte to utf8 with $utfdecode after decoding the percent encoding:

	alias urlDecode return $utfdecode($regsubex($replace($1, +, $chr(32)), /%([A-F\d]{2})/gi, $chr($base(\1, 16, 10))))

Consider the following example:

.. code:: text

	//echo -a $urlEncode(Hello & Goodbye?)
	//echo -a $urlDecode(Hello%20%26%20Goodbye%3F)

Will print:

.. code:: text

	Hello%20%26%20Goodbye%3F
	Hello & Goodbye?

Note the escaped characters. You should almost always encode all user input:

.. code:: text

	on *:SockOpen:example: {
	   sockwrite -n example GET /foo/bar.php?foo= $+ $urlEncode(%input) HTTP/1.1
	   sockwrite -n example Host: www.example.com
	   sockwrite -n example $crlf
	}

POST vs GET?
------------

By now you are probably asking yourself why did I use GET in our sockopen and how do you know what to use. In HTTP, there are two methods for sending data to the server: POST and GET. They only differ in the format we send that data. When requesting a normal page, you will most likely be using the GET method, when submitting a form; however, it might get a little tricky. When dealing with forms, by simply looking at the source code you can tell if it's a POST or a GET method:

.. code:: text

	<form id="FooBar" method="post" action="">
	   ...
	</form>

The most basic GET request will follow this basic syntax:

.. code:: text

	GET /folder/file.html HTTP/1.1
	Host: www.example.com
	<blank line>

Let's take a look at the header a little closer:

.. code:: text

	GET /folder/file.html HTTP/1.1

This line is made up of three parts: method, path and version. The "GET", which SHOULD be always in uppercase letters, is the method. For more information about the POST method see the advanced part of this tutorial. The next part is the path, relative to the root folder of the website. If our webpage is www.example.com/pub/foo/bar.html, our path would be /pub/foo/bar.html. Lastly, the final part of this line is the HTTP version, for all practical reasons, you will probably using version 1.0. Sometimes we might need to use version 1.1 if we want features that are only available in that version.

.. note:: For all practical purposes the HTTP RFC states that casing should not matter. Unfortunately, I came across multiple web servers that only accepted it in the exact casing we present in here. It's best to follow that rule as well.

Next is the Host header:

.. code:: text

	Host: www.example.com

The Host header is required in HTTP version 1.1. Once again, although it should not cause any issues it best to use "Host:", not "host:" or "HOST:". If you forget to include this line, the server will most likely send you an error 400 (Bad Request) status code.

Reading Incoming Data
---------------------

Once the server receives your request, it will send the response back to you. This will trigger the ON SOCKREAD event. The basic syntax of the on sockread event is:

.. code:: text

	on *:sockread:<handle>: {
	   ;Your code goes here
	}

The on sockread will most likely be the hardest and longest part of your code. When the on sockread event triggers, you have to read the data and decide what to do with it. If your script just needs some information from that page you will have to find and parse the appropriate line.

When it comes to HTTP, the data you will receive from the server will contain a header followed by a blank line which will be followed by the content of the page. The content of the page will look identical to that text you find when you right click on a web page and click on view source code.

Reading data that has been sent from the server is done with the /sockread command. That command is powerful because it allows you to read the data in a lot of ways, with HTTP, you'll likely want to get the data line by line.

To read a single line from the socket, we use the /sockread command that way:

.. code:: text

	sockread <%var>

That sockread command actually reads up to a $crlf. This is important to know because many web pages don't end with a $crlf which means the last line won't be read. The -f switch can be used to force the sockread command to read the line even if it does not end with a $crlf.

.. note:: If the variable does not exist, a global variable gets created. It is therefore advised to declare a local variable beforehand.

When working with binary data or if the line is too long to be read into an ordinary variable, you can read the data into a binary variable using the following syntax:

sockread [numbytes] <&binvar>
Reading into a binary variable will by default reads 4096 bytes unless you specify [numbytes] the number of byte to be read, there is a -n switch which can be used to read $crlf-terminated lines into the binary variable as well.

Debugging
~~~~~~~~~

Because the on sockread triggers when we get our data, it is the most interesting part of our script. Many people find it easier to script and debug when they can see the entire page source code. The script below can be used to see everything the server sent us in a custom window (@ $+ sockname):

.. code:: text

	;Print the entire server's reply to a custom window
	on *:sockread:Example1: {
	  window -deC @ $+ $sockname -1 -1 700 700
	  var %read
	  sockread -f %read
	  aline -p @ $+ $sockname : $+ %read
	}

Dealing with HTML code
~~~~~~~~~~~~~~~~~~~~~~

One of the first things you will have to deal with when writing HTTP scripts is HTML code and lots of it. The single most common task is to simply get rid of some unwanted HTML tags that enclose your code. Below is a very small, yet extremely handy alias that will strip most HTML tags away:

.. code:: text

	alias noHTML return $regsubex($1, /<[^>]+(?:>|$)|^[^<>]+>/g, $null)

Consider this simple example:

.. code:: text

	//echo -a $noHTML(<strong>Example</strong> - <p>This is an <em>example</em></p>)

Will print the following result:

.. code:: text

	Example - This is an example

Keep this alias safe. Trust me, this tiny alias will become one of your most precious possessions.

Error Handling
~~~~~~~~~~~~~~

Errors happen! It's a fact of life. It is your responsibility to check for them and gracefully handle them! The $sockerr identifier must be checked after every socket operations. If the value of $sockerr is greater than zero, an error has occurred and we MUST stop whatever it is we were going to do with the socket, cleanup, perhaps display an error message etc. Remember, inside the on sockopen event, $sockerr allows you to know if the connection was sucessful or not.

A basic example would look like this:

.. code:: text

	on *:sockread:example: {
	  if ($sockerr) { 
	    echo $color(info) -sef Socket Error: $sock($sockname).wsmsg
	    echo $color(info) -sef Socket Error Number: $sock($sockname).wserr Socket: $sockname
	  }
	  else {
	    ;my code goes here...
	  }
	}

Checking for an error gives you the opportunity to handle it in a sane way. Most scripts report that an error has occurred instead of simply stopping in their tracks.

Reading Data Example
~~~~~~~~~~~~~~~~~~~~

Example 1 (Continue)
^^^^^^^^^^^^^^^^^^^^

When I printed out the entire source the server sent us. The first part is the header, follows by a blank space, and follows by the actual page data. It should look something like this:

.. code:: text

	:HTTP/1.1 200 OK
	:Date: Sun, 11 Mar 2012 10:42:05 GMT
	:Server: Apache
	:X-Powered-By: PHP/5.2.17
	:Connection: close
	:Content-Type: text/html
	:
	:<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
	:   <html xmlns="http://www.w3.org/1999/xhtml">
	:       <head>
	:           <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
	:           <meta name="robots" content="noindex,follow" />
	:           <title>ZigWap - Demo Page</title>
	:       </head>
	:       <body>
	:           <div align="center">
	:               <p>This is an example page!</p>
	:               <p>This webpage is dedicated for the socket tutorial purpose. </p>
	:           </div>
	:       <p>Your random color is: Pink</p>        
	:       </body>
	:   </html>

The first part is the header, follows by a blank space, and follows by the actual page data. In this example we will be trying to retrieve the random color line. A simple if statement to check for *Your random colors is* should be sufficient enough.

.. code:: text

	on *:sockread:example1: {
	  var %read
	  sockread %read
	  ; check if this is the line we want
	  if (*Your random color is: * iswm %read) {
	    ; break down our line into words
	    tokenize 32 %read
	    ; get the color and remove the html tab
	    echo $color(info) -a Random Color: $noHTML($5)
	    ; close the socket, it's not needed
	    sockclose $sockname
	  }
	}

Example 2 (YouTube, Continue)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you tried to print the youtube page we did (http://www.youtube.com/watch?v=FDw0NdhK6QU) you will quickly realize how long the youtube webpage is. For this reason I will not show it here. The way we parse that page is very much like the one we did for the first example:

.. code:: text

	on *:sockread:YouTube: {
	  var %x
	  sockread %x
	  if ($regex(%x, <meta name="title" content="(.+)">)) {
	    ; parse the title
	    set %title. $+ $sockName $regml(1)
	  } 
	  else if (watch-view-count isin %x) {
	    ; read the next line
	    sockread %x
	    ; make sure it's a number
	    ; the (*UTF8) in the expression is required for the regex engine to interpret utf8 sequences, which is what mIRC use (here for a $chr(160))
	    if ($regex(%x,/(*UTF8)^ *([\d\xA0]+)/)) {
	      set %view. $+ $sockname $replace($regml(1),$chr(160),$chr(32))
	    }
	  }
	  ;if we find the username of the uploader, we are done
	  else if ($regex(%x,/<\/a><a ?href="\/user\/([^"]+)/)) {   
	    ; print out the info
	    echo -a Title: $($+(%, title., $sockname), 2) $&
	      Uploader: $regml(1) Views: $($+(%, view., $sockname), 2)
	    ; cleanup
	    unset %*. $+ $sockname
	    ; close the socket, no need to read anymore
	    sockclose $sockname
	  }
	}

Connection Terminated
---------------------

It is possible for the remote end-point to terminate a connection, the same way you can /sockclose a connection early. When this happens the on sockclose event will trigger. The syntax for that event is:

.. code:: text

	on *:sockclose:<handle>: {
	   ;Your code goes here
	}

.. note:: Only the remote end-port, not you, can trigger this event.

UDP Sockets
===========

This tutorial is the UDP Sockets continuation of the sockets introduction. If you haven't read that, please do so first before moving on to this one.

Recall that UDP is a connectionless protocol service. Because of this there are no on sockopen/sockread/sockclose events for the different stages like TCP. The basic idea is you send a message and quit, or you send a message and wait for response.

Sending A Packet
----------------

The /sockudp command allows you to send data to a specific address at a specific port destination. The syntax is:

.. code:: text

	; Sending some data
	/sockudp [-kb] <handle> <ipaddress> <port> [numbytes] [text|%var|&bvar]

By default, /sockudp sends the entire data specified. The -b switch can be used to limit the amount of bytes sent.

If you are expecting some data back, the -k switch can be used to force the UDP socket to remain open. This will allow you to listen to incoming data.

Listening for Incoming Data
---------------------------

If you are expecting data back (I.E. if you specified the -k switch) you can listen for incoming data via the on udpread event.

.. code:: text

	on *:udpread:<handle>:{
	   ; your code goes here
	}

Socket Failure and More Data Sending
------------------------------------

The on sockwrite event can be used to write additional data when the previous data is sent. Additionally, If the sockudp command fails, the on sockwrite event will trigger $sockerr set to a non-zero value.

.. code:: text

	on *:sockwrite:<handle>:{
	   ; your code goes here
	}

Examples
--------

Example 1 - Time Protocol
~~~~~~~~~~~~~~~~~~~~~~~~~

This example will use the Time Protocol to display the current time. The Time Protocol is a very simple network protocol that provides site-independent, machine readable date and time. The protocol is defined in RFC 868.

From RFC 868:

.. code:: text

	When used via UDP the time service works as follows:

	 S: Listen on port 37 (45 octal).
	 U: Send an empty datagram to port 37.
	 S: Receive the empty datagram.
	 S: Send a datagram containing the time as a 32 bit binary number.
	 U: Receive the time datagram.

	 The server listens for a datagram on port 37. When a datagram
	 arrives, the server returns a datagram containing the 32-bit time
	 value. If the server is unable to determine the time at its site, it
	 should discard the arriving datagram and make no reply.


From the instructions above you can see that the first thing we have to do is send an empty datagram to their server. On port 37. &null will hold our NULL byte.

.. code:: text

	alias getTime {
	  ; NULL byte
	  bset &null 1 0
	  ; Time.nist.gov = 132.163.96.4
	  sockudp -k getTime 132.163.96.4 37 &null
	}

Let's add a single line of code to print if an error occurred

.. code:: text

	on *:sockwrite:getTime:{
	  if ($sockerr) echo -a /getTime: Error: $sock($sockname).wserr - $sock($sockname).wsmsg
	}

Now, all we have to do is sit and wait for the datagram response. Remember that since UDP is connectionless protocol, its header is much smaller, thus much faster (Ideal for a time protocol).

.. code:: text

	on *:udpRead:getTime: {
	   ; read the reply
	   sockread -f &time

	   ; bvar to var
	   var %time $bvar(&time,1,$bvar(&time,0))

	   ; get convert to binary
	   var %bin $regsubex(%time,/(\d+)/g,$base(\1,10,2,8))

	   ; print it and close the socket
	   echo -a our 32-bit time value: %bin
	   sockclose $sockname
	}

Let's make sense of this 32bit time value, shall we?

Once again, from the RFC 868:

.. code:: text

	The Time

	 The time is the number of seconds since 00:00 (midnight) 1 January 1900
	 GMT, such that the time 1 is 12:00:01 am on 1 January 1900 GMT; this
	 base will serve until the year 2036.

	 For example:

	 the time 2,208,988,800 corresponds to 00:00 1 Jan 1970 GMT,
	 2,398,291,200 corresponds to 00:00 1 Jan 1976 GMT,
	 2,524,521,600 corresponds to 00:00 1 Jan 1980 GMT,
	 2,629,584,000 corresponds to 00:00 1 May 1983 GMT,
	 and -1,297,728,000 corresponds to 00:00 17 Nov 1858 GMT.

Since we know that 2,208,988,800 = 00:00 1 Jan 1970 GMT (Unix epoch). We can just do $calc(%time - 2208988800) to get the current Unix time. Now all we got to do is use $asctime to format it nicely.

.. code:: text

	on *:udpRead:getTime: {
	  ; read the reply
	  sockread -f &time
	  var %time $bvar(&time,1,$bvar(&time,0))

	  ; convert to binary, remove spaces
	  var %bin $regsubex(%time, /(\d+)\s?/g, $base(\1, 10, 2, 8))

	  ; get the current unix time in decimal system
	  var %time = $base(%bin, 2, 10)

	  ; print the time and close the socket
	  echo -a Currnt Time/Date: $asctime($calc(%time - 2208988800), yyyy-mm-dd hh:nn:ss TT)
	  sockclose $sockname
	}

Example 2 - QOTD Protocol
~~~~~~~~~~~~~~~~~~~~~~~~~

In this example we will use an interesting protocol, the Quote Of The Day, RFC 865. This is a very simple protocol; you send a blank datagram, and the server responds with a quote. The hardest part was actually finding a website that still supports this protocol. (The reason most servers don't have this service enabled is because it is vulnerable to a ping-pong attack, where an attacker spoofs a server's IP (that supports QOTD protocol) and sends a request to a second server that support it, causing both server to flood each other)

Send a request:

.. code:: text

	alias getQOTD {
	  ; NULL byte
	  bset &null 1 0
	  ; Dns resolved quotes4all.net to 85.25.143.214
	  sockudp -k getQOTD 85.25.143.214 17 &null
	}

Now wait for the quote:

.. code:: text

	on *:udpRead:QOTD: {
	   var %Quote
	   sockread -f %Quote
	   echo -ea %Quote
	   sockclose $sockname
	}

On Sockopen
===========

The ON SOCKOPEN event triggers when a TCP socket connection initiated with :doc:`$sockopen </commands/sockopen>` is either successfull or failed. This event also trigger after an SSL negociation (STARTTLS feature) is finished, you can check $sock().starttls which will be set to $true if the negociation was successful.

Synopsis
--------

.. code:: text

    ON <level>:SOCKOPEN:<matchtext>:<commands>

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <matchtext>
      - The name of the socket you want the event to trigger on.
    * - <commands>
      - The commands to be performed when the event listener's criteria is met.

Connection State
----------------

Because the sockopen event triggers for failed connections as well as successful connections, it's important to check the value of :doc:`$sockerr </identifiers/sockerr>` before continuing with any commands. Here is a list of the possible values returned by $sockerr in the on SOCKOPEN event:

* 0 - Success.
* 3 - Failure establishing socket connection: $sock($sockname).wsmsg will contain a more specific error message.
* 4 - Error resolving given hostname.

Examples
--------

.. code:: text

    on *:sockopen:example:{
    
      ;if an error occurred ($sockerr is not 0)
      if ($sockerr) {
        if ($sockerr == 3) {
          echo -s An error occurred while trying to connect: $sock($sockname).wsmsg
        }
        elseif ($sockerr == 4) {
          echo -s Error resolving hostname
        }
      }
    
      ;no error occurred ($sockerr was 0)
      else {
        ;perform commands after establishing a connection.
        ;usually this involves making a request for a webpage as shown below:
        sockwrite -n $sockname GET / HTTP/1.1
        sockwrite -n $sockname Host: www.example.com
        sockwrite -n $sockname Connection: close
        sockwrite    $sockname $crlf
      }
    }

Compatibility
-------------

.. compatibility:: 3.5

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on sockread </events/on_sockread>`
    * :doc:`on sockwrite </events/on_sockwrite>`
    * :doc:`on socklisten </events/on_socklisten>`
    * :doc:`on sockclose </events/on_sockclose>`
    * :doc:`/sockopen </commands/sockopen>`
    * :doc:`/sockwrite </commands/sockwrite>`
    * :doc:`/sockread </commands/sockread>`
    * :doc:`/sockclose </commands/sockclose>`
    * :doc:`/sockaccept </commands/sockaccept>`
    * :doc:`/sockpause </commands/sockpause>`
    * :doc:`$sockname </identifiers/sockname>`
    * :doc:`$sock </identifiers/sock>`
    * :doc:`$sockbr </identifiers/sockbr>`
    * :doc:`$sockerr </identifiers/sockerr>`

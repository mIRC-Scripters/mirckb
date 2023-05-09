On Sockread
===========

The ON SOCKREAD triggers when there is info waiting to be read on the specified TCP socket connection. You can read this info using the :doc:`$sockread </commands/sockread>` command.

.. note:: If this event triggers but no :doc:`$sockread </commands/sockread>` is performed to attempt to read the buffer, it is assumed that no script exists that is handling this buffer, so it is cleared and the info it contained is lost.

Synopsis
--------

.. code:: text

    ON <level>:SOCKREAD:<matchtext>:<commands>

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

It's important to check the value of :doc:`$sockerr </identifiers/sockerr>` to determine if any connection errors occurred and handle that case. Here is a list of possible values returned by $sockerr in the on SOCKREAD event:

* 0 - Data received correctly.
* 3 - Error occurred on connected socket: $sock($sockname).wsmsg will contain a more specific error message.

Examples
--------

You can find more information and examples in the :doc:`$sockread </commands/sockread>` command page.

Here is a basic outline:

.. code:: text

    on *:sockread:example:{
    
      ;if an error occurred ($sockerr is not 0)
      if ($sockerr) {
        echo -s An error occurred: $sock($sockname).wsmsg
      }
    
      ;no error occurred ($sockerr was 0)
      else {
    
        ;perform commands related to reading the data
    
        ;declare %r as a local variable for use in /sockread
        var %r
    
        ;read a line into %r from the buffer (this variable is subject to mIRC's Line Length Limit - see the /sockread page for more information)
        sockread %r
    
        ;do things with %r, such as checking its value or extracting parts to output later
    
      }
    }

Compatibility
-------------

.. compatibility:: 3.5

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on sockopen </events/on_sockopen>`
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

$notify
=======

$notify returns informations about nick in your notify list

Synopsis
--------

.. code:: text

    $notify(N/nick)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - nick
      - The nickname you want to get information about
    * - N
      - The Nth nick in the notify list you want to get information about, if N = 0, returns the total number of nicknames in the notify list

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - .ison
      - returns $true if the user is on IRC, $false otherwise
    * - .note
      - returns the note associated for that nickname in the notify list
    * - .sound
      - returns the online sound setting for that nickname
    * - .sound2
      - returns the offline sound setting for that nickname
    * - .whois
      - returns $true if the option 'whois' is set for this nickname
    * - .addr
      - returns the server adddress entry for this nickname if you used a server format
    * - .network
      - returns the network entry for this nickname (if you used something that isn't a server format, basically)

Without a property, $notify(nick) returns the Nth position and $notify(N) returns the nickname

Example
-------

.. code:: text

    //echo -a $notify(0)

Compatibility
-------------

.. compatibility:: 4.5

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/notify </commands/notify>`


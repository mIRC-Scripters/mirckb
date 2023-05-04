/uwho
=====

The **/uwho** command is used to grab a specified user's server information, which it then displays into the info section of the address book.

Synopsis
--------

.. code:: text

    /uwho [nick] [nick]

Switches
--------

None

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - [nick]
      - The user's nickname you want to lookup.
    * - [nick]
      - Some servers may require you to specify the user's name twice in order to lookup idle time or their away message, which may cause the results to delay a bit.

Examples
--------

'*Lookup information for user named *jeff***

.. code:: text

    /uwho jeff

**Lookup information for *jeff* and ensure we get idle time and away message*'

.. code:: text

    /uwho jeff jeff

Compatibility
-------------

Added: mIRC v3.1 (23 Apr 1995)

See also
--------

.. hlist::
    :columns: 4

    * :doc: `/abook </commands/abook>`
    * :doc: `/ial </commands/ial>`
    * :doc: `/whois </commands/whois>`

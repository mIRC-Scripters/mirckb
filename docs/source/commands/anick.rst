/anick
======

The **anick** command is used to set a new alternative nickname. The alternative nickname is the nickname that will be used if IRC indicates that your primary nickname is already in use. If the alternative nickname is taken as well, mIRC will place a '/nick ' text in the server's editbox and wait for the user's reply.

Synopsis
--------

.. code:: text

    /anick <nickname>

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
    * - <nickname>
      - The alternative nickname to change to.

Example
-------

.. code:: text

    /anick Foo

Output:

  * Your alternate nickname is now Foo

Compatibility
-------------

Added: mIRC v5.8 (14 Dec 2000)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$mnick </identifiers/mnick>`
    * :doc:`$anick </identifiers/anick>`
    * :doc:`$me </identifiers/me>`
    * :doc:`/identd </commands/identd>`

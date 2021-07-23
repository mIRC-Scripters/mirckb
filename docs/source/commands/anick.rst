/anick
======

The **anick** command is used to set a new alternative nickname. The alternative nickname is the nickname that will be used if IRC indicates that your primary nickname is already in use. If the alternative nickname is taken as well, mIRC will place a ``'/nick '`` text in the server's editbox and wait for the user's reply.

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

.. code:: text

    * Your alternate nickname is now Foo

Compatibility
-------------

Added: mIRC v5.8 (05 Sep 2000)

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$mnick </aliases/mnick>`
    * :doc:`$anick </aliases/anick>`
    * :doc:`$me </aliases/me>`
    * :doc:`/identd <identd>`

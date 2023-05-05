/ctcp
=====

The **/ctcp** command can be used to send a CTCP request to a user/channel

Synopsis
--------

.. code:: text

    /ctcp <nick/#channel> <ctcp>

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
    * - <nick>
      - Target nick/channel
    * - <ctcp>
      - CTCP

Example
-------

.. code:: text

    ;Version everyone in #mSL
    /ctcp #mSL VERSION

Compatibility
-------------

Added: mIRC v2.1a (28 Feb 1995)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$nick </identifiers/nick>`
    * :doc:`/ctcpreply </commands/tcp-socket>`
    * :doc:`/ctcps </commands/tcp-socket>`

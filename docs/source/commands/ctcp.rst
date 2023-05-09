/ctcp
=====

The /ctcp command can be used to send a CTCP request to a user/channel

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

.. compatibility:: 2.1a

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$nick </identifiers/nick>`
    * :doc:`/ctcpreply </commands/ctcpreply>`
    * :doc:`/ctcps </commands/ctcps>`


/pop
====

The **/pop** command performs a delayed op on a nickname. The purpose of this command is to prevent a channel window filling up with op mode changes whenever several users have the same nickname in their auto-op section.

Before performing the op it checks if the user is already opped.

Synopsis
--------

.. code:: text

    /pop <delay> [#channel] <nickname>

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
    * - <delay>
      - mIRC will pause around <delay> seconds before performing the op. If <delay> is zero, it does an immediate op.
    * - [#channel]
      - If specified, the channel you want to op the nickname on, otherwise the current channel is used
    * - <nickname>
      - The nickname you want to op.

Example
-------

None

Compatibility
-------------

Added: mIRC v3.42 (29 Jun 1995)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/pvoice </commands/pvoice>`

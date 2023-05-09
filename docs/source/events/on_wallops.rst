On Wallops
==========

The ON WALLOPS event triggers when an IRC operator issues a network-wide important notice.

This event fills the $1- and :doc:`$nick </identifiers/nick>` identifiers with the full text of the WALLOP, and the operator's name who issued it, respectively.

Synopsis
--------

.. code:: text

    ON <level>:WALLOPS:<matchtext>:<commands>

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <level>
      - The level for the event to trigger.
    * - <matchtext>
      - The text that to be matched. Can also be a :ref:`matching_tools-wildcard`.
    * - <commands>
      - The commands to be performed when the event listener's criteria is met.

Example
-------

Echo to the active window the current date/time, the IRC operator's name who sent the WALLOP, the WALLOP message, and prevent the default response:

.. code:: text

    ON ^*:WALLOPS:*: {
      echo -a  $asctime  ==> WALLOP From $nick :: Message:
      haltdef
    }

Compatibility
-------------

.. compatibility:: 4.6

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on snotice </events/on_snotice>`


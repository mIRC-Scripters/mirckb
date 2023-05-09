On Usermode
===========

The ON USERMODE event triggers when the local mIRC client's usermodes have been changed on a connection.

This event fills the :doc:`$1- </identifiers/dollar1dash>` identifier with the new usermodes for the client.

Synopsis
--------

.. code:: text

    ON <level>:USERMODE:<commands>

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <level>
      - The level for the event to trigger.
    * - <commands>
      - The commands to be performed when the event listener's criteria is met.

Example
-------

Halt the default mIRC response, and then echo the new details to the active window:

.. code:: text

    ON ^*:USERMODE: {
      echo -a * You have set new usermodes: $1-
      haltdef
    }

Compatibility
-------------

.. compatibility:: 5.0

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on snotice </events/on_snotice>`
    * :doc:`on wallops </events/on_wallops>`


On Snotice
==========

The ON SNOTICE event triggers when mIRC receives a server notice.

This event fills the :doc:`$1- </identifiers/dollar1dash>` identifier with the text from the server notice.

Synopsis
--------

.. code:: text

    ON <level>:SNOTICE:<matchtext>:<commands>

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
      - The text that to be matched. Can also be a :ref:`matching_tools-wildcard`.s
    * - <commands>
      - The commands to be performed when the event listener's criteria is met.

Example
-------

Halt the default server notice and echo it to the active window in plain text:

.. code:: text

    ON ^*:SNOTICE:*: {
      echo -a * Server notice: $1-
      haltdef
    }

Compatibility
-------------

.. compatibility:: 3.8

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on notice </events/on_notice>`
    * :doc:`on queryopen </events/on_queryopen>`
    * :doc:`on text </events/on_text>`


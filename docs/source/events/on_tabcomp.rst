On Tabcomp
==========

The ON TABCOMP event triggers when you press the tab key in an editbox

.. note:: This event is not triggered in an empty editbox if you have the 'Tab key changes editbox focus' option enabled in alt + o > other > keys.

Synopsis
--------

.. code:: text

    ON <level>:tabcomp:<*><=><!><@><?>#[,#]>:<commands>

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <level>
      - The corresponding :doc:`access levels </intermediate/events>` for the event to trigger.
    * - <matchtext>
      - The corresponding matchtext for the event to trigger.
    * - <*><?><#[,#]>
      - The place, or places where the event listens, you can specify specific name of window, seperate them by comma.
        * \* - Any query/channel window
        * ? - Any query windows
        * # - Any channel window
    * - <commands>
      - The commands to be performed when the event triggers

Examples
--------

None

Compatibility
-------------

.. compatibility:: 6.2

See also
--------

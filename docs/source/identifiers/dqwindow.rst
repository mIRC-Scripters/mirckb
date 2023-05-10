$dqwindow
=========

$dqwindow returns the state of the single message window. When used in on TEXT/ACTION events, it also returns opening/writing/written states.

The value can be checked using the & bit comparison operator:

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - $iif($dqwindow & 1,enabled,not enabled) 
      - the single message window is enabled/disabled
    * - $iif($dqwindow & 2,open,not open)
      - the single message window is open/not open
    * - $iif($dqwindow & 4,opening,not opening)
      - the single message window is going to be opened (or not going to be opened) because of the message received, apply to IRC events only
    * - $iif($dqwindow & 8,writing,not writing)
      - the single message window is going/not going to be written to because of the message received, apply to IRC events only
    * - $iif($dqwindow & 16,written,not written)
      - the message received was written/not written to the single message window, apply to IRC events only.

Synopsis
--------

.. code:: text

    $dqwindow

Parameters
----------

None

Properties
----------

None

Example
-------

None

Compatibility
-------------

.. compatibility:: 7.48

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/dqwindow </commands/dqwindow>`


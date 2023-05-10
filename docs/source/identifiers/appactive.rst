$appactive
==========

$appactive returns ``$true`` or ``$false`` depending on whether mIRC is the active window or not.

Synopsis
--------

.. code:: text

    $appactive

Switches
--------

None

Results
-------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Value
      - Description
    * - $true
      - mIRC is currently the active window.
    * - $false
      - mIRC is currently not the active window.

Example
-------

Let's say you have a listening event, just to make mIRC beep if someone uses your name in a channel. We call these notifications, as well as highlights. Well, if mIRC is the currently active window, these sounds can be either annoying or meaningless. Therefore, we would set up the listener to check the $appactive identifier to make sure mIRC is not active before sending out the audible notification.

.. code:: text

    ON *:TEXT:$($+(*,$me,*)):#: {
      ; Make sure mIRC is not the active application
      if (!$appactive) {
    
        ; Execute 5 beeps at 200 millisecond intervals
        beep 5 200
      }
    }

Compatibility
-------------

.. compatibility:: 5.3

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$appstate </identifiers/appstate>`


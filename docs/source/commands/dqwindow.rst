/dqwindow
=========

mIRC's DQ (*dedicated query*) window system is a feature that conveniently redirects all incoming queries to a single window. The **/dqwindow** command can be used to disable or enable as well as show and hide the DQ window.

You can determine if the DQ Window is on or off with this alias:

.. code:: text

    alias is_dqwindow {
    saveini
    return $iif($gettok($readini($mircini, n, options, n0), 22, 44), $true, $false)
    }

Synopsis
--------

.. code:: text

    /dqwindow [on|off|show|hide|min]

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
    * - on
      - Turns the DQWindow system on
    * - off
      - Turns off the DQ window system
    * - show
      - Displays the DQ window
    * - hide
      - Hides the DQ window
    * - min
      - Minimizes the DQ window
    * - close
      - Closes the DQ window

.. note:: Using this command without parameters displays a message indicating whether the DQ Window is 'on' or 'off'.

Example
-------

Turn on the dedicated query window:

.. code:: text

    /dqwindow on

Will print:

.. code:: text

    * Dedicated query window is on

Compatibility
-------------

Added: mIRC v5.1 (11 Sep 1997)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$me </identifiers/$me>`
    * :doc:`$nick </identifiers/$nick>`
    * :doc:`/close </commands/close>`
    * :doc:`/closemsg </commands/closemsg>`
    * :doc:`/window </commands/window>`

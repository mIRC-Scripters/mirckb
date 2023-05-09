$click
======

The $click identifier allows the tracking of clicks within a custom :ref:`picture_windows`.

Synopsis
--------

.. code:: text

    $click(@,N)[.property]

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Argument
      - Description
    * - @
      - The custom picture window name to target
    * - N
      - The Nth target in the click event list to track.

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Argument
      - Description
    * - x
      - Get the current x position of the mouse click
    * - y
      - Get the current y position of the mouse click

Attached Command
----------------

The $click click event history can be cleared from a custom picture window by using the following command:

.. code:: text

    /clear -c @pictureWindowName

Example
-------

The example below will create a custom alias, /clickWatch, that, when executed, will popup a custom window and display the live click results from the sclick event.

.. code:: text

    ; Create the custom alias to launch the example
    ;
    ; Synopsis: /clickWatch
    
    alias clickWatch {
    
      ; Custom picture window, which is centered
      window -dpC @clicker 0 0 250 125
    
      ; Custom 'update' alias keeps code from repeating
      ; During initial launch the values should be empty
      update 15 Total Clicks: empty
      update 35 Current Position: none yet
      update 55 Previous Position: none yet
    }
    ; Monitor the sclicks in our custom '@clicker' window
    menu @clicker {
      sclick: {
    
        ; Clear the window for the new value updates
        clear @clicker
    
        ; Set the %current and %prev variables to the current
        ; x/y click location, and to the previous x/y click
        ; locations, respectively
        var %current = $click(@clicker,0), %prev = $calc(%current - 1)
    
        ; Utilizing the custom 'update' alias, update the data
        update 15 Total Clicks: $click(@clicker,0)
        update 35 Current Position: $click(@clicker,%current)
        update 55 Previous Position: $iif(%prev,$click(@clicker,%prev),none yet)
      }
    }
    ; Custom update alias removes a lot of the /drawtext repetition
    ; from this example
    alias -l update {
      drawtext @clicker $color(normal) 7 $1 $2-
    }

Compatibility
-------------

.. compatibility:: 5.3

See also
--------

.. hlist::
    :columns: 4

* :ref:`picture_windows`


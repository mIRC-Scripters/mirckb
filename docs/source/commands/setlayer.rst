/setlayer
=========

The **/setlayer** command can be used to change the transparency of a given window. If no window is provided, the transparency setting will apply to the main MDI window. The setlayer works on all windows as long as the full name is provided, for example "Status Window" for the status window. 

Transparency
------------

Transparency can be between 0 and 255, where 0 = 100% transparency.

Synopsis
--------

.. code:: text

    /setlayer <0-255> [@window / #channel / query / windowName]

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
    * - <0-255>
      - alpha channel value
    * - [@window / #channel / query / windowName]
      - The window to apply the transparency to

Example
-------

.. code:: text

    Alias Example {
    ; create a new desktop window (with an editbox)
    window -de @Example
    ; set @example to 204/255 (%20) transparency
    setlayer 204 @Example
    ; a friendly message
    echo @Example 20% Transparency!
    }

You can change the transparency of other windows as well:

.. code:: text

    ; sets the dcc chat window with David to 75% Transparency. (The quotes are not required.)
    setlayer 191 "Chat David"

Compatibility
-------------

Added: mIRC v5.9 (15 Jun 2001)

See also
--------

.. hlist::
    :columns: 4

    * :doc: `/window </commands/window>`

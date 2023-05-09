/fupdate
========

The /fupdate command's setting is the maximum display update delay. So if you specify 100, it will update the display less frequently than 10. That said, with the latest algorithm, even if you specify 100, it may not reach that since it is adjusting automatically to the maximum value that makes a significant difference.

Higher numbers can reduce delay while a large number of text lines scroll down the window, but may also cause the screen display to update in unexpected ways. Users will need to benchmark different N values until they find one that works for them.

If used with no parameter, it displays the current setting.

Synopsis
--------

.. code:: text

    /fupdate [N]

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
    * - N
      - The algorithm setting, where 0 is disabled, or is on a scale from minimum 1 to maximum 100.

Example
-------

.. code:: text

    Display current setting: /fupdate
    Set to 10 within range 1-100: /fupdate 10
    Disable fupdate feature: /fupdate 0

.. note:: The /fupdate setting always reverts to default 0 each time mIRC restarts, so it must be reset each time using an ON START or perform-on-connect command

Compatibility
-------------

.. compatibility:: 7.52

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$fupdate </identifiers/fupdate>`

$leftwinwid
===========

$leftwinwid is an identifier that works for mouse events in custom picture windows. Whenever the mouse leaves a picture window, the $leftwinwid stores the window ID for that event.

Synopsis
--------

.. code:: text

    $leftwinwid

Parameters
----------

None

Properties
----------

None

Example
-------

Custom script that listens for the mouse leaving ``@tester``

.. code:: text

    alias testscript {
      $iif($window(@tester),clear @tester,window -p @tester)
    }
    menu @tester {
      leave:clear @tester | drawtext @tester 1 15 15 Mouse left window with ID $leftwinwid
    }

Once the above example has fired up, the mouse can now be hovered over the ``@tester`` window, and then moved outside of the window. In the top-left corner there will now be some text that says ``Mouse left window with ID <WindowID>``, where <WindowID> is replaced with the actual window's ID.

Compatibility
-------------

.. compatibility:: 6.2

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$activewid </identifiers/activewid>`
    * :doc:`$lactivewid </identifiers/lactivewid>`
    * :doc:`$leftwin </identifiers/leftwin>`
    * :doc:`$leftwincid </identifiers/leftwincid>`


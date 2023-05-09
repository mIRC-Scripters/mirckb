$leftwin
========

$leftwin is an identifier that works for mouse events in custom picture windows. Whenever the mouse leaves a picture window, $leftwin return the name of the window you just left, usually used in the leave menu event.

Synopsis
--------

.. code:: text

    $leftwin

Parameters
----------

None

Example
-------

Custom script that listens for the mouse leaving ''@tester''

.. code:: text

    alias testscript {
      $iif($window(@tester),clear @tester,window -p @tester)
    }
    menu @tester {
      leave:clear @tester | drawtext @tester 1 15 15 Mouse left window $leftwin
    }

Compatibility
-------------

.. compatibility:: 5.5

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$activewid </identifiers/activewid>`
    * :doc:`$leftwinwid </identifiers/leftwinwid>`
    * :doc:`$lactivewid </identifiers/lactivewid>`


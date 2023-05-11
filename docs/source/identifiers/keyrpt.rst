$keyrpt
=======

$keyrpt is filled during an :doc:`on keydown </events/on_keydown>`, or an :doc:`on keyup </events/on_keyup>` event inside of a :ref:`custom_windows`, it returns $true if the key is held down, $false otherwise..

Synopsis
--------

.. code:: text

    $keyrpt

Parameters
----------

None

Example
-------

Create an alias that launches a custom, :ref:`picture_windows` which listens for key presses and displays the key value pressed, the key character pressed, and if it is repeating:

.. code:: text

    alias keyDownTest {
      window -p $+ $iif($window(@myWindow),ra) @myWindow 550 300 250 105
    }
    ON *:KEYDOWN:@myWindow:*: {
      clear @myWindow
      drawtext @myWindow 1 3 3 Key value: $iif($keyval,$v1,NA)
      drawtext @myWindow 1 3 25 Key character: $iif($keychar,$v1,NA)
      drawtext @myWindow 1 3 47 @myWindow Repeating: $keyrpt
    }

The following command can now be typed into any mIRC command prompt:

.. code:: text

    /keyDownTest

Below is an image reflecting what this example will look like:

.. figure:: img/Keyup_event.png.webp

Note that this makes use of a :ref:`picture_windows`, as well as the /drawtext command - mIRC|drawtext command. These types of :ref:`picture_windows` and their tools can be very powerful in creating some amazing graphical layouts, as well as mIRC games.

Compatibility
-------------

.. compatibility:: 5.5

See also
--------

.. hlist::
    :columns: 4

    * :ref:`custom_windows`
    * :doc:`on keydown </events/on_keydown>`
    * :doc:`on keyup </events/on_keyup>`
    * :doc:`/drawtext </commands/drawtext>`
    * :doc:`$keychar </identifiers/keychar>`
    * :doc:`$keyval </identifiers/keyval>`


$keyval
=======

$keyval returns the key code of the key being pressed inside an :doc:`on keydown </events/on_keydown>` or :doc:`on keyup </events/on_keyup>` event.

/!\ This identifier is filled inside :doc:`on char </events/on_char>` but this is mostly for convenience and is incorrect, inside :doc:`on char </events/on_char>`, it only makes sense to check for :doc:`$keychar </identifiers/keychar>`

Synopsis
--------

.. code:: text

    $keyval

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
      drawtext @myWindow 1 3 3 Key value: $keyval
      drawtext @myWindow 1 3 47 @myWindow Repeating: $keyrpt
    }
    ON *:char:@myWindow:*: {
     drawtext @myWindow 1 3 25 Key character: $keychar
    }

The following command can now be typed into any mIRC command prompt:

.. code:: text

    /keyDownTest

Below is an image reflecting what this example will look like:

.. figure:: img/Keyup_event.png.webp

Note that this makes use of a :ref:`picture_windows`, as well as the :doc:`drawtext command </commands/drawtext>`. These types of :ref:`picture_windows` and their tools can be very powerful in creating some amazing graphical layouts, as well as mIRC games.

Compatibility
-------------

.. compatibility:: 5.5

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on keyup </events/on_keyup>`
    * :doc:`on keydown </events/on_keydown>`
    * :doc:`$keychar </identifiers/keychar>`
    * :doc:`$keyrpt </identifiers/keyrpt>`
    * :doc:`$keylparam </identifiers/keylparam>`


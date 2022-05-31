/fnord
======

The **/fnord** command echoes "Nothing to see here." in text of the same color as the background. This is an Easter Egg.

Synopsis
--------

.. code:: text

    /fnord

Switches
--------

None

Parameters
----------

None

Bugs
----

As of version 7.0, the text is the default color of the font due to the internal background/foreground color check that ensures the color of the text is not mistakenly set as the color of the background. The bug was fixed in mIRC 7.21.

Example
-------

.. code:: text

    /fnord

The above example is the equivalent of the following echo command:

.. code:: text

    //echo -aeq $+($chr(3),$color(background),$chr(44),$color(background),Nothing to see here.)

.. code:: text

    Nothing to see here.


Compatibility
-------------

Added: mIRC v6.3 (16/08/2007)

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
---------

.. hlist::
    :columns: 4

    * :doc:`/echo <echo>`
    * :doc:`/xyzzy <xyzzy>`

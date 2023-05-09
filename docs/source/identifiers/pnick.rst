$pnick
======

$pnick return the name of the channel or the nickname you are currently :doc:`/playing </commands/play>` to. This is useful with the -c and -a switches of :doc:`/play </commands/play>` 

Synopsis
--------

.. code:: text

    $pnick

Parameters
----------

None

Properties
----------

None

Example
-------

.. code:: text

    alias test.play {
      msg $pnick test : $1-
    }
And use //play -a test.play <nick|channel> file.txt

Compatibility
-------------

.. compatibility:: 3.72

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/play </commands/play>`


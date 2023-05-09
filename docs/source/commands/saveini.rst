/saveini
========

mIRC might cache settings before they get saved to disk. This command dumps all mIRC saved settings from memory to their respective INI files. The /saveini command should be called before attempting to access any settings from these files.

Synopsis
--------

.. code:: text

    /saveini

Switches
--------

None

Parameters
----------

None

Example
-------

mIRC settings should be flushed before attempting to access recent data:

.. code:: text

    ; returns the last text your searched using Ctrl+F
    alias lastFind {
      ; flush settings
      saveini
      ; return the last find text
      return $readini($mircini, n, find2, n0)
    }

Compatibility
-------------

.. compatibility:: 5.4

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$mircini </identifiers/mircini>`
    * :doc:`$readini </identifiers/readini>`
    * :doc:`$read </identifiers/read>`
    * :doc:`/load </commands/load>`
    * :doc:`/localinfo </commands/localinfo>`
    * :doc:`/reload </commands/reload>`
    * :doc:`/save </commands/save>`
    * :doc:`/savebuf </commands/savebuf>`
    * :doc:`/write </commands/write>`
    * :doc:`/writeini </commands/writeini>`


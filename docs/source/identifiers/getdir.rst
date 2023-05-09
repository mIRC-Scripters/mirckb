$getdir
=======

The $getdir identifier returns either the default DCC GET directory, or the DCC GET directory for the specified filespec.

Synopsis
--------

.. code:: text

    $getdir[( filespec )]

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - Filespec
      - If specified, returns mIRC-Options/DCC/Folders/DCC GET directory for that filespec

Example
-------

.. code:: text

    //if ($sound(*.mp3) != $getdir(*.mp3)) echo -a warning: MP3's do not download into the MP3 SOUND folder!

.. code:: text

    //echo -a The default DCC GET folder for filetypes not defined in mIRC-options/dcc/folders is $getdir

.. code:: text

    on *:FILESENT:*:{
      if ($getdir($filename) == $nofile($filename)) echo -a Note: $filename was sent from the DCC GET folder for that filename.
    }

Compatibility
-------------

.. compatibility:: 4.52

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$sound </identifiers/sound>`


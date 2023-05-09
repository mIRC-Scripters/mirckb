/wavplay
========

.. note:: /wavplay has essentially been replaced by the :doc:`/splay </commands/splay>` command.

The /wavplay command is used to play a .wav file of your choosing.

Synopsis
--------

.. code:: text

    /wavplay <sound.wav>

Switches
--------

None

Parameters
----------

None

Examples
--------

Play the file ''mywav.wav'' located in the ''Sounds'' directory of mIRC

.. code:: text

    /wavplay mywav.wav

Short alias script that will ask you which wav file you want to play

.. code:: text

    alias playwav {
    
      ; First, we create a variable, %file, to hold our
      ; user-selected wav file. Note that this is surrounded
      ; by the $qt() identifier which makes sure that the
      ; entire selection is surrounded by quotes. This is
      ; for older Windows' backward-compatibility.
      var %file = $qt($sfile(sounds\*.wav,Choose Wav,OK))
    
      ; Check to make sure the %file variable contains a
      ; real file.
      if ($isfile(%file)) {
    
        ; Now we simply play the wav file using /wavplay
        wavplay %file
      }
    }

Compatibility
-------------

.. compatibility:: 3.5

Removed: mIRC v5.51

Removed On: 19/02/1999

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/splay </commands/splay>`
    * :doc:`/vol </commands/vol>`
    * :doc:`$sound </identifiers/sound>`
    * :doc:`$vol </identifiers/vol>`


/load
=====

.. note:: that unlike the :doc: `/reload </commands/reload>` command, /load will trigger the ON LOAD and ON START events.

Synopsis
--------

.. code:: text

    /load -a[N] <filename>
    /load -p<scqnm> <filename>
    /load -r<uvs[N]> <filename>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -a
      - load aliases file
    * - -pm
      - load menubar popups file
    * - -pn
      - load nicklist popups file
    * - -pq
      - load query popups file
    * - -pc
      - load channel popups file
    * - -ps
      - load status window popups file
    * - -rsN
      - load remote script file
    * - -rvN
      - load variable file
    * - -ruN
      - load users file
    * - -N
      - if you specify the N value with -rs or -a, it loads the file into the Nth position in the script list or alias list. In the absence of N, the file is loaded into the last position.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <filename>
      - The script file to load

.. note:: In the absence of a path, assumes the file is located in $mircdir. Paths not beginning with drive letter or \ are relative to the location of $mircdir.<br />

.. note:: You can have samefilename.mrc and scripts\samefilename.mrc loaded at the same time. Do NOT load any script located in the downloads folder where someone can resume-send a script file on top of the file you have already loaded.

.. note:: default aliases file is aliases.ini and default popups file is popups.ini containing all 5 types of popups. Default setup has both filenames in scripts\ subfolder from $mircdir.

Example
-------

Load three remote script files.

.. code:: text

    alias load_remote {
    load -rs foo.mrc
    load -rs bar.mrc
    load -rs baz.mrc
    }

Loads script file into the 2nd position of the 'view' menu in Alt+R editor. If it's already loaded, moves the file to that position. If contains ON LOAD or ON START event handler, this triggers the Initialization Warning and/or performs the event handler.

.. code:: text

    load -rs2 foobar.mrc

Loads aliases file into the 1st position of the 'view' menu in Alt+D editor. If it's already loaded, moves the file to that position.

.. code:: text

    load -a1 C:\Foldername\aliases.mrc

Load a variables and a users file:

.. code:: text

    alias load_vars_and_users {
    load -ru users2.ini
    load -rv vars2.ini
    }

.. note:: If your aliases.ini was saved to a different file extension such as .mrc, it still needs to have the same scripting format used with the original filename. The only difference is that the disk file no longer is saved in the .ini format with lines beginning like n123=. Same applies with saving your users.ini and vars.ini files to other filetypes. However without the file extension being .ini, it's not possible to edit the 5 types of popups sharing the same filename, and -ru and -rv can't share the same filename either.

Compatibility
-------------

Added: mIRC v3.8 (25 Nov 1995)
See also
--------

.. hlist::
    :columns: 4

    * :doc: `$script </identifiers/$script>`
    * :doc: `$script </identifiers/$script>`
    * :doc: `$window </identifiers/$window>`
    * :doc: `/filter </commands/filter>`
    * :doc: `/loadbuf </commands/loadbuf>`
    * :doc: `/reload </commands/reload>`
    * :doc: `/save </commands/save>`
    * :doc: `/savebuf </commands/savebuf>`
    * :doc: `/unload </commands/unload>`
    * :doc: `/window </commands/window>`

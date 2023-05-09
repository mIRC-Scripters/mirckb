/save
=====

The /save command save the specified popups/users/variables to a file.

.. note:: You can only save one section at a time.

Synopsis
--------

.. code:: text

    /save -p<scqnm> <filename>
    /save -r<uv> <filename>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -pm
      - Saves the menubar popups.
    * - -pn
      - Saves the nicklist popups.
    * - -pq
      - Saves the query popups.
    * - -pc
      - Saves the channel popups.
    * - -ps
      - Saves the status window popups.
    * - -rv
      - Saves the variable file.
    * - -ru
      - Saves the users file.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <filename>
      - The script file to save to

Example
-------

None

Compatibility
-------------

.. compatibility:: 5.0

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/load </commands/load>`


/reload
=======

The /reload command reloads the specified alias/remote/popup file, you can only load one section of a popups file at a time. If reloading a remote script, the ON LOAD or ON START even within are not triggered.

.. note:: since mIRC v7.31, if you use the monitoring file options ( alt + r + r + o ) and a file warning dialog is opened for the file you are reloading, the dialog is automatically closed.

Synopsis
--------

.. code:: text

    /reload <-a|-pscqnm|-ruvsN> <filename>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -a
      - Specify an alias file.
    * - -pS
      - Specify a popup file, you must specify the S value which is 's' for a status window popup, 'c' for a channel popup, 'q' for query, 'n' for nicklist and 'm' for the menubar.
    * - -rTN
      - Specify a remote/user/variable file, you must specify the T value which is 'u' for an user file, 's' for a remote (script) file and 'v' for variable, the N value is optional: if specified, reload the file into the Nth position in the script list.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <filename>
      - The filename to be reloaded.

Example
-------

Loads scriptfile.mrc without triggering ON START or ON LOAD events. If it's already loaded, this moves it to position 1 in the remote script list.

.. code:: text

    /reload -rs1 scriptfile.mrc

Compatibility
-------------

.. compatibility:: 5.4

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/load </commands/load>`
    * :doc:`on load </events/on_load>`
    * :doc:`on start </events/on_start>`


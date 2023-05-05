/url
====

The **/url** command can be used to completely enable or disable the URL catcher. Additionally it can also be used to show and hide the URL list window as well as modify the items in the list. The URLs can be saved and loaded from an INI file. The URL command can also be used to open URLs in the browser. The URL command uses the default browser application in the system. If the mark is used, it must be a single character - multiple characters will be truncated.

Synopsis
--------

.. code:: text

    /url <on | off | show | hide | save | load | delete>
    /url -an <URLaddress>
    /url -r <N/mark>
    /url -i <N/Mark> <URLaddress>
    /url -ls <file.ini>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -a
      - Attempts to open the URL in the active browser window
    * - -n
      - Attempts to open the URL in a new window
    * - -r
      - Removes all items with a specific mark or the Nth item
    * - -i
      - Insert the URL with a specific mark or at the Nth position
    * - -l
      - Load all the URLs from a specific INI file
    * - -s
      - Save all the URLs to a specific INI file

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <on | off | show | hide | load | save | delete>
      - Show/Hide the URL list window or Enable/Disable the URL catcher, or load/save the url list window; you can pass a filename or a default urls.ini is used. **delete** should do the same as -r
    * - <URLaddress>
      - The URL address to use
    * - <N/mark>
      - A numeric value of a single character mark
    * - <file.ini>
      - The settings file to save/load the URLs from/into

Example
-------

.. code:: text

    ;remove all '?' marked URLs
    /url -r ?

    ;open the website in a new window
    /url -n www.google.com

    ;show the URL list window
    /url show

Compatibility
-------------

Added: mIRC vmIRC 3.7 ()

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$url </identifiers/url>`
    * :doc:`/help </commands/help>`
    * :doc:`/run </commands/run>`
    * :doc:`/winhelp </commands/winhelp>`

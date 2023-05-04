/run
====

The **/run** command executes the given file or object using the application associated with its file extension. It can also be used to open directories. The file parameter can be enclosed by a pair of double quotes to separate it from the argument list.

Synopsis
--------

.. code:: text

    /run -pnhau <file/dir/obj> [arguments]

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -h
      - hide the application in context
    * - -p
      - changes the working path to the path of the application in context
    * - -n
      - minimize the window upon opening
    * - -a
      - run as administrator, prompting you if mIRC is not running as admin, if mIRC is already running as admin, no prompt.
    * - -u
      - if mIRC is running as admin, runs the program without admin right

.. note::

* If mIRC is already running as admin and if you're not using -a nor -u, the program will still be running as admin as though you used -a, by default.

* In Win7-32 OS, using the -a switch fails if launching a 16-bit DOS executible, regardless of if mIRC is already running in elevated state or not. Workaround is to not use -a if mIRC is already running as admin, but to use -a if it is not.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <file/dir/obj>
      - the object/file to execute
    * - [arguments]
      - arguments list passed to the program

Example
-------

.. code:: text

    alias example {
    ; open our site
    run www.zigwap.com/mirc

    .. note:: pad, minimized

    .. note:: pad.exe

    }

Compatibility
-------------

Added: mIRC v2.1a (28 Feb 1995)
See also
--------

.. hlist::
    :columns: 4

    * :doc: `$isadmin </identifiers/$isadmin>`
    * :doc: `$url </identifiers/$url>`
    * :doc: `$file </identifiers/$file>`
    * :doc: `$findfilen </identifiers/$findfilen>`
    * :doc: `$finddir </identifiers/$finddir>`
    * :doc: `$finddirn </identifiers/$finddirn>`
    * :doc: `$isfile </identifiers/$isfile>`
    * :doc: `$isdir </identifiers/$isdir>`
    * :doc: `$exists </identifiers/$exists>`
    * :doc: `/url </commands/url>`

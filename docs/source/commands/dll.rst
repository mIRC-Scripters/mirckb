/dll
====

The **/dll** command can be used to call an exported function from a DLL with the specified parameters.

Synopsis
--------

.. code:: text

    /dll <libName.dll> <funcName> [data]
    /dll -m <callback> <libName.dll> <funcName> [data]
    /dll -u <libName.dll>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -u
      - Unload the given loaded library.
    * - -m
      - Call the procname in a new thread and call the alias <callback> when finished

.. note:: if you pass only a filename, (for example "test.dll", instead of /folder/test.dll or c:\fullpath\test.dll), /dll -u will begin with N=1 looking into the whole list of dlls for a match between $nopath($dll(Nth)) instead of looking into $mircdir only or looking in $mircdir first.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <libName.dll>
      - The name and path of the dynamic link library (DLL) file.
    * - <funcName>
      - The name of the exported function to call
    * - [data]
      - The data to pass to that function.

.. note:: If the path or filename contains a space, <libName.dll> MUST be enclosed in doublequotes.

Examples
--------

Look at the :doc:`dll </advanced/dll>` article to see how to use a dll as well as how to create them.

silently fails if $dll(1) contains a space:

.. code:: text

    //if ($dll(1)) dll -u $dll(1)

works whether or not $dll(1) contains a space:

.. code:: text

    //if ($dll(1)) dll -u $qt($dll(1))

if $dll(1) is $mircdir $+ subdir\foo.dll and $dll(2) is $mircdir $+ foo.dll
"/dll -u foo.dll" matches the 1st index matching $nopath(foo.dll), so it removes subdir\foo.dll unless that were loaded last. But "/dll -u $qt($dll(2))" removes the foo.dll not located in the subdir.

.. code:: text

    //dll foo.dll no_such_function | echo -a test

If foo.dll does not exist, the script halts with an error, and the echo does not display. If foo.dll does exist but the function does not exist, /dll displays an error to status window, but the script continues executing the echo. It also loads foo.dll even if the function doesn't exist, and remains loaded in memory if the .dll's initialization routine sets mKeep=$true. See the $dll article for keeping the .dll loaded after execution, and for keeping the .dll past 10 minutes of idle time.

While $dll(foo,function,) returns a 3rd parameter even if it's $null, "/dll foo.dll" does not require parm3.

Using

.. code:: text

    /dll file.dll function string

used for loading a dll is roughly equivalent to

.. code:: text

    noop $dll(file.dll,function,string)

Compatibility
-------------

Added: mIRC v5.6 (23 Sep 1999)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$dll </identifiers/dll>`
    * :doc:`$dllcall </identifiers/dllcall>`
    * :doc:`sendmessage </advanced/sendmessage>`

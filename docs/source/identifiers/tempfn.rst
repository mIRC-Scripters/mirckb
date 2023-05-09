$tempfn
=======

$tempfn returns a temporary filename in the :doc:`$mircdir </identifiers/mircdir>` using the same filename mask used by mIRC internally, such as for the :doc:`/write </commands/write>` command. Now accepts an optional pathname as an alternate folder location.

Synopsis
--------

.. code:: text

    $tempfn

.. code:: text

    $tempfn([path])

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - None or [path] 
      - Absolute or relative foldername for the temp file. If path not provided, default is $mircdir, and any path provided MUST exist. If Parenthesis is used is blank path, returns $null.

Properties
----------

None

Example
-------

.. code:: text

    //echo -a $tempfn

It does not create the disk filename, but offers the string as a "safe" filename that can be used without it already existing as a disk file or foldername.

The string returned is $mircdir $+ mirc $+ $rand(0,$calc(2^31-2)) $+ .tm_

.. note:: The filename mask is the same used internally by mIRC for disk write fuctions, such as in the /write command.

.. code:: text

    //echo -a $tempfn(temp)

Same except the string lists the filename's path as being in the temp subfolder beneath $mircdir. Halts with error if that foldername doesn't exist. Handles strings like ".." or "c:" or "\path" the same way as $findfile.

It is up to the user to use a folder where you have write permissions for actually creating the file. If D: is a DVD drive, $tempfn(D:\) returns a string containing D:\ as the path, even if the disk write would fail.

Compatibility
-------------

.. compatibility:: 7.46

.. compatibility:: 7.63

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$mircdir </identifiers/mircdir>`

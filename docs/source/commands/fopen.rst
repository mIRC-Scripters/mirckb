/fopen
======

The /fopen command opens <filename> and assigns it a handle. The file is opened for both writing and reading: see :ref:`file_handling`. If an error occurred, processing does not halt. You must check that :doc:`$fopen(\<handle\>).err </identifiers/fopen>` or :doc:`$ferr </identifiers/ferr>` is not true.

.. note:: mIRC keeps the handle even after a fail, you must always /fclose the handle you /fopen yourself.

If -x is not used, the file that is opened is also in shared read/write, meaning that an external application (a second mIRC) can also open the file at the same time, read and write to it, affecting the content of the file you're using.

Synopsis
--------

.. code:: text

    /fopen [-nox] <handle> <filename>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -n
      - Create a new file, fails if already exists
    * - -o
      - Creates a new file, overriding an old one if exists
    * - -x
      - Opens the file in exclusive mode (will fail to open if already in use)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <handle>
      - A handle associated with an open file.
    * - <filename>
      - The filename to open.

Example
-------

A simple example that prints one line to a new file:

.. code:: text

    ; simple fopen example
    alias fopen_example {
      .fopen -n h hello.txt
      ;error check
      if ($ferr) {
        echo -sce info * /fopen_example: example.txt already exists!
        halt
      }
      ;print text
      .fwrite h Hello There
      ;close the handle
      .fclose h
      ;open file in default editor
      run hello.txt
    }

A script that prints all the permutations of there-characters to a file.

.. code:: text

    ; print permutations [aaa]-[zzz]
    alias perm_example {
      .fopen -n h example.txt
      ;error check
      if ($ferr) {
        echo -sce info * /fopen_example: example.txt already exists!
        halt
      }
      ;print all the permutations to the file
      var %x = 97
      while (%x < 123) {
        var %y = 97
        while (%y < 123) {
          var %z = 97
          while (%z < 123) {
            .fwrite -n h $+($chr(%x), $chr(%y), $chr(%z))
            inc %z
          }
          inc %y
        }
        inc %x
      }
      ;close the handle
      .fclose h
    }

Broken Compatibility
--------------------

in mIRC ''7.22'' /fopen left the handle open even after it failed. The compatibility change stated above was changed back to the old behavior in mIRC 7.24.

Compatibility
-------------

Added: 29/08/2003

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$fopen </identifiers/fopen>`
    * :doc:`$fread </identifiers/fread>`
    * :doc:`$fgetc </identifiers/fgetc>`
    * :doc:`$feof </identifiers/feof>`
    * :doc:`$ferr </identifiers/ferr>`
    * :doc:`$file </identifiers/file>`
    * :doc:`/fclose </commands/fclose>`
    * :doc:`/flist </commands/flist>`
    * :doc:`/fseek </commands/fseek>`
    * :doc:`/fwrite </commands/fwrite>`


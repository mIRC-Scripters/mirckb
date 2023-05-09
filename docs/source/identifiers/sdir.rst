$sdir
=====

$sdir displays the select folder dialog and returns the selected folder

Synopsis
--------

.. code:: text

    $sdir(dir, title, button)
    
    $sdir="title" <dir>
    ;This is the old format still supported by mIRC
    ;The quotes are optional if title doesn't contain spaces

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - dir
      - The directory you want to open
    * - title
      - The optional title
    * - button
      - The optional text of the 'open' button on the dialog

.. note:: Prior version of mirc (before 7.x'ish) were using a different dialog selection which was allowing the usage of a :ref:`matching_tools-wildcard` to fill in the 'folder' field in the dialog, but mIRC is not longer using that dialog, and therefore it's now no longer possible to pass a :ref:`matching_tools-wildcard` as the 'dir' parameter here.

Properties
----------

None

Example
-------

.. code:: text

    //echo -a $sdir($mircdir,"choose a folder!,Ok!)

Compatibility
-------------

.. compatibility:: 5.81

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$sfile </identifiers/sfile>`


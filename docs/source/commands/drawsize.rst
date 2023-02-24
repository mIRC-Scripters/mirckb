/drawsize
=========

The **/drawsize** command extend the bitmap size of a picture window.

Synopsis
--------

.. code:: text

    /drawsize <@win> <w> <h>

Switches
--------

None

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <w>
      - new width
    * - <h>
      - new height

.. note:: A bitmap cannot be sized to less than the largest point that has been drawn on it (which can be reset with /clear). Once a size has been set, changing the window size will not resize it to less than the set size.

Practically speaking?

This command was added after a bug report was `made <http://forums.mirc.com/ubbthreads.php/ubb/showflat/Number/260318/>`_, revealing /drawrect is not drawing beyond the size of the window (it does not extend the bitmap to prevent too much memory usage with some failed parameter passed for coordinates).

/window can be used to set the size of the bitmap (-f) however /window also resize the window accordingly.

With /drawsize, you can extend the bitmap to make sure your draws are correctly made beyond the size of the window without having the size of the window (what's visible) to be the same (more or less, borders and visual effect put aside) as the size of the bitmap.

Example
-------

None

Compatibility
-------------

Added: mIRC v7.48 (15 Apr 2017)

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$window </identifiers/window>`
    * :doc:`$click </identifiers/click>`
    * :doc:`$mouse </identifiers/mouse>`
    * :doc:`$inellipse </identifiers/inellipse>`
    * :doc:`$inrect </identifiers/inrect>`
    * :doc:`$inroundrect </identifiers/inroundrect>`
    * :doc:`$inpoly </identifiers/inpoly>`
    * :doc:`$onpoly </identifiers/onpoly>`
    * :doc:`$rgb </identifiers/rgb>`
    * :doc:`$getdot </identifiers/getdot>`
    * :doc:`$height </identifiers/height>`
    * :doc:`/drawcopy <drawcopy>`
    * :doc:`/drawfill <drawfill>`
    * :doc:`/drawline <drawline>`
    * :doc:`/drawpic <drawpic>`
    * :doc:`/drawrect <drawrect>`
    * :doc:`/drawreplace <drawreplace>`
    * :doc:`/drawsave <drawsave>`
    * :doc:`/drawscroll <drawscroll>`
    * :doc:`/drawtext <drawtext>`
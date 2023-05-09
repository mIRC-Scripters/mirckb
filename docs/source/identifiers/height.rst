$height
=======

$height returns the height of text in pixel in the specified font.

Synopsis
--------

.. code:: text

    $height(text,font,size,bNiNpNtN)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - text
      - The text you want the width of
    * - font
      - The name of the font
    * - size
      - The size of the font, you can specify a negative value to match the size of fonts in the font dialog

Before, there was a 4th 5th and even a 6th true/false parameters (bold, italic, and control code processing), to set some custom measurements, it was changed to a single 4th parameter when tab processing were added:

bNiNpNtN - Optional, defines some options for the measurement, N can be 1 or 0 to enable or disable the option:

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - bN 
      - enables/disables bold
    * - iN 
      - enables/disables italic
    * - pN
      - enables/disables control code (-bi not needed there)
    * - tN 
      - enables/disables tab character

Properties
----------

None

Example
-------

.. code:: text

    //echo -a $height(test,verdana,15)

Compatibility
-------------

.. compatibility:: 5.4

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$width </identifiers/width>`
    * :doc:`$wrap </identifiers/wrap>`


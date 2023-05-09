$tip
====

$tip Allows you to create scripted tips that are independent of normal tip events. 

Synopsis
--------

.. code:: text

    $tip(<name>,<title>,<text>,delay,iconfn,iconpos,alias,wid) 
    create a tip, returns Nth position of tip if successfully created, 0 if not
    
    $tip(N/name) - returns information about a tip

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - name
      - The name of your tip.
    * - title
      - The title of your tip.
    * - text
      - The text appearing inside the tip, can contain colors
    * - delay
      - The duration of the tip, betwee, 3 and 60
    * - iconfn
      - the filename of the icon, if you want to use any
    * - iconpos
      - the position of the icon for a file containing multiple icons
    * - alias
      - the alias that will be called when the tip is double clicked
    * - wid
      - the id of the window to which the tip belongs
    * - cid
      - the id of the connection to which the tip belongs
    * - N
      - reference the Nth tip.

Properties
----------

When only one parameter is passed to $tip, you can use the following properties:

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - .name
      - returns the name of the tip (used with the N parameter typically)
    * - .title
      - return the title of the tip
    * - .text
      - return the text of the tip
    * - .delay
      - return the delay of the tip
    * - .iconfn
      - return the icon filename used if any
    * - .iconpos
      - return the position of the icon for a file containing multiple icons
    * - .alias
      - return the name of the alias called when double clicking the tip
    * - .wid
      - return the id the window to which the tip belongs

Example
-------

.. code:: text

    //echo -a $tip(test,test,test)

Compatibility
-------------

.. compatibility:: 6.3

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/tip </commands/tip>`
    * :doc:`/tips </commands/tips>`
    * :doc:`$tips </identifiers/tips>`


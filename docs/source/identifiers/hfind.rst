$hfind
======

$hfind Searches an hash table for the Nth item name which matches text. Returns item name.

.. note:: :doc:`/halt </commands/halt>` will stop the $hfind search if used from the command parameter (or inside the alias called, naturally) - note that versions prior to 7.59 this didn't work.

Synopsis
--------

.. code:: text

    $hfind(name/N, text, N, M, @window | command)[.data]

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - name/N
      - the Nth hash table or the name of it
    * - text
      - the expression to use to find a match
    * - N
      - The Nth match, use 0 to get the total number of match or to trigger the @window | command parameter for all matches
    * - M
      - optional, a letter indicating how to match, default to value normal text comparison (n) below:
        * n - normal text comparison
        * w - :ref:`matching_tools-wildcard` expression
        * W - hash table item/data is :ref:`matching_tools-wildcard` expression, see example below
        * r - regular expression
        * R - hash table item/data is regular expression, see example below
        * command | @win -- if you pass a @win name, the item name that matched is put in the window, otherwise mirc evaluate the command for each match, $1 can be used to access the item name

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - .data
      - instead of looking for matches against item, matches against data, but the item name is still returned.

Example
-------

.. code:: text

    //hadd -m test test test | echo -a $hfind(test,test,1) | hfree test

.. code:: text

    //hadd -m test test test | hadd -m test test test1 | echo -a $hfind(test,test*,0,w) | hfree test

.. code:: text

    //hadd -m test t*t | echo -a $hfind(test,this is a test,0,W) | hfree test

.. code:: text

    //hadd -m test t.+t | hadd -m test t(?=his) | echo -a $hfind(test,this is a test,0,R,echo -s $1) | hfree test

Compatibility
-------------

.. compatibility:: 5.81

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/hmake </commands/hmake>`
    * :doc:`/hadd </commands/hadd>`
    * :doc:`/hload </commands/hload>`
    * :doc:`/hfree </commands/hfree>`
    * :doc:`/hdec </commands/hdec>`
    * :doc:`/hinc </commands/hinc>`
    * :doc:`$hget </identifiers/hget>`


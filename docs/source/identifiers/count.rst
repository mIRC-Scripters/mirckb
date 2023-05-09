$count
======

The $count identifier allows mIRC to return the total count of a matching substring, or set of substrings to a target string.

Synopsis
--------

.. code:: text

    $count(string,substring,substring2,...)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Argument
      - Description
    * - string
      - The target string to match
    * - substring
      - The substring to match within the target
    * - substring2,...
      - The second substring to match, and beyond

Example
-------

The example string is going to be: My string to match

Echo the matching substring count for str:

.. code:: text

    //echo -a Result: $count(My string to match,str)

.. code:: text

    Result: 1

Echo the matching substring count for str and m:

.. code:: text

    //echo -a Result: $count(My string to match,str,m)

.. code:: text

    Result: 3

The above returns 3 because str is matched to string once, and m is matched to My and match; therefore, the total matches is 3.

Compatibility
-------------

.. compatibility:: 4.6

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$gettok </identifiers/gettok>`
    * :doc:`$matchtok </identifiers/matchtok>`


$remove
=======

$remove removes all occurrences of the given substring(s) from a string and returns the remainder. $removecs is the case sensitive version.

Synopsis
--------

.. code:: text

    $remove(string,substring,substringN)
    $removecs(string,substring,substringN)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - string
      - the original string you want to remove from
    * - substring
      - the substring you want to remove from the original string, you can
    * - substringN
      - you can pass multiple substring to be removed from the original string

Example
-------

Show the download folder as a relative location only if it's a subfolder of $mircdir

.. code:: text

    //echo -a $remove($getdir,$mircdir)

Remove the channel from a message

.. code:: text

    //echo -a $remove($active,$chan)

Show the download folder as a relative location only if it's a subfolder of $mircdir

.. code:: text

    //echo -a $remove($getdir,$mircdir)

.. code:: text

    Case-insensitive remove all 'a' from 'aAabcdaaA'
    //echo -a $remove(aAabcdaaA,a)
    returns: bcd
    Case-insensitive remove string 'ac' from 'AaCcX'
    //echo -a $remove(AaCcX,ac)
    returns: AcX
    The first match was at positions 2-3, and no matches were beyond.
    //echo -a $remove(AaCcX,ac,ac)
    ... uses string altered by 1st parameter when removing 2nd parameter string. Is equivalent to:
    //echo -a $remove( $remove(AaCcX,ac) , ac)

Compatibility
-------------

.. compatibility:: 4.52

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$replace </identifiers/replace>`
    * :doc:`$replacex </identifiers/replacex>`
    * :doc:`$deltok </identifiers/deltok>`
    * :doc:`$remtok </identifiers/remtok>`
    * :doc:`$reptok </identifiers/reptok>`

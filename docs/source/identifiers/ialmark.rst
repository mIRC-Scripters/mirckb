$ialmark
========

**$ialmark** returns information about marks created using :doc:`/ialmark </commands/ialmark>`

Synopsis
--------

.. code:: text

    $ialmark(nick,N/name) - returns $true or $false depending on whether the IAL is on or off.
    
.. code:: text
    
    $ial(nick/mask,N) - returns the Nth address matching a mask in the IAL

Marks are removed if the nick is removed from the IAL for any reason.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - **nick**
      - nickname
    * - **name**
      - name of a mark created by /ialmark
    * - **N**
      - optional, the Nth matching entry in the IAL, use N = 0 for the total number of matches

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - **.name** 
      - returns the name of the Nth named mark
    * - **.mark** 
      - returns the mark for that entry, set with :doc:`/ialmark </commands/ialmark>`

Example
-------

.. code:: text

    ;name of the 1st mark attached to your nick (not necessarily default)
    //echo -a $ialmark($me)
    ;the mark attached to the 1st named mark
    //echo -a $ialmark($me)
    ;total number marks
    //echo -a $ialmark($me,0)
    ;the name of the 2nd mark:
    //echo -a $ialmark($me,2)
    ;either 'foo' or $Null depending if that named mark is attached to that nick
    //echo -a $ialmark($me,foo)
    ;the mark attached to the named mark 'foo'
    //echo -a $ialmark($me,foo).mark
    ;the mark attached to the named mark '2' (not necessarily the 2nd named item)
    //echo -a $ialmark($me,2).mark
    ; list all itemnames and marks attached to your nick:
    //var %i 1 | while (%i <= $ialmark($me,0)) { echo -a $ord(%i) $ialmark($me,%i).name $ialmark($me,%i).mark | inc %i }

Compatibility
-------------

Added: mIRC v7.48 (15 Apr 2017)

See Also
--------

.. hlist::
    :columns: 4

    * :doc:`/ialmark </commands/ialmark>`

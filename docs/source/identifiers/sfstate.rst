$sfstate
========

$sfstate Returns either $null or 'cancel' or 'error' depending on the result of the last execution of either $sfile $sdir or $msfile(dir).

Synopsis
--------

 $sfstate Returns result of the last execution of either $sfile $sdir or $msfile(dir):

* Returns $null if the command successfully returns at least 1 filename (sfile or $msfile) or if $sdir returned a foldername.
* Returns 'cancel' if the selection window was closed by pressing ESCAPE or clicking 'cancel'
* returns 'error' if the selection window exited in an error condition.

.. note:: $sfstate is similar to $regml(N) where it returns a historical result until that value is replaced by a different result, even if the new result is $null.

Parameters
----------

None

Properties
----------

None

Example
-------

.. code:: text

    //echo -ag $msfile(c:\windows\) sfstate = $sfstate / $msfile(0) / $msfile(1)

* Select any filename, $sfstate returns $null
* Click the Cancel button and $sfstate returns 'cancel'
* Click on the C:\Windows\Fonts\ folder and press 'Open', and $sfstate returns 'error'.

Compatibility
-------------

.. compatibility:: 7.51Beta60

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$msfile </identifiers/msfile>`
    * :doc:`$sfile </identifiers/sfile>`
    * :doc:`$sdir </identifiers/sdir>`

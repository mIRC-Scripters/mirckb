/btrunc
=======

The **/btrunc** command can be used to truncate a file to a specific number of bytes. If The Number of bytes exceeds the size of the file, the file will be zero-pad to that size. If the file does not exist, a new file will be created.

Synopsis
--------
 
.. code:: text

	/btrunc <filename> <bytes>

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
	* - <filename>
	  - Filename of the file to be modified
	* - <bytes>
	  - Number of bytes to extend or trance the file by/to.

Example
-------

.. code:: text

	Alias Example {
	  var %temp = Hello! World
	  ;Write to a variable %temp's content
	  bwrite Example 0 $len(%temp) %temp
	  ;Truncate the file down to 6 bytes
	  btrunc Example 6
	  ;Read the file into a variable
	  bread Example 0 $file(Example).size &Example
	  ;Print out the variable's content
	  echo -a $bvar(&Example,1,$bvar(&Example,0)).text
	  ;Delete the file
	  remove Example
	}

Compatibility
-------------

Added: mIRC v5.8 (05 Sep 2000)

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.


See also
--------

.. hlist::
	:columns: 4

	* :doc:`$bvar </identifiers/bvar>`
	* :doc:`$bfind </identifiers/bfind>`
	* :doc:`/bcopy <bcopy>`
	* :doc:`/bread <bread>`
	* :doc:`/breplace <breplace>`
	* :doc:`/bset <bset>`
	* :doc:`/bwrite <bwrite>`
	* :doc:`/bunset <bunset>`
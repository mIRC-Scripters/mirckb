/bread
======

The **/bread** command can be used to read a certain amount of bytes from a file at a given position and store it in a binary variable.

.. note:: The beginning of the file is position 0.

Synopsis
--------

.. code:: text

   /bread -ta <filename> <bytepos> <numbytes> <&bvar>

Switches
--------


.. list-table::
	:widths: 15 85
	:header-rows: 1

	* - Switch
	  - Description
	* - -t
	  - Reads data preceding the first encountered line ending or EOF, interpreting as UTF8 text
	* - -a
	  - Modifier for -t switch, avoids translating codepoints 128-255 to UTF8 if the data doesn't contain codepoints 256+

Parameters
----------

.. list-table::
	:widths: 15 85
	:header-rows: 1

	* - Parameter
	  - Description
	* - <filename>
	  - The file name to read from. Double quotes needed if string contains space
	* - <bytepos>
	  - The starting byte position, '''remember, this starts at 0, not 1'''.
	* - <numbytes>
	  - The length (bytes) to be read.
	* - <&bvar>
	  - The binary variable to store the data in. If &binvar already exists, contents are replaced.

Example
-------

.. code:: text

	;noop $copyExample(FileA,FileB)
	alias copyExample {
	   ;Read the whole file into a binary variable
	   bread $qt($1) 0 $file($1).size &tempFile

	   ;Write the bytes form the binary variable to a file
	   bwrite $qt($2) 0 -1 &tempFile
	}

.. code:: text

	Using -t switch:
	Line ending is defined as data preceding

	//bset &v 1 233 | bwrite -c test.dat 0 &v | bread test.dat 0 9 &v2 | echo -a $bvar(&v2,1-)
	result: 233 because no switch used

	//bset &v 1 233 | bwrite -c test.dat 0 &v | bread -t test.dat 0 9 &v2 | echo -a $bvar(&v2,1-)
	result: 195 169 because -t used without -a interprets as UTF8 encoding of codepoint 233

	//bset &v 1 233 | bwrite -c test.dat 0 &v | bread -ta test.dat 0 9 &v2 | echo -a $bvar(&v2,1-)
	result: 233 because -ta used AND data read doesn't contain codepoint 256+

	//bset &v 1 226 156 148 233 | bwrite -c test.dat 0 &v | bread -ta test.dat 0 9 &v2 | echo -a $bvar(&v2,1-)
	result: 226 156 148 195 169 because data read contains codepoint 10004
	* If bread's offset changed from 0 to 3, result is 233 because the read portion of the line doesn't contain the codepoint above 255

.. code:: text

	//bread $qt($mircexe) 0 $file($mircexe).size &v | echo -a $md5(&v,1) is the same as $md5($mircexe,2) if enough memory available for binvar

Compatibility
-------------

Added: mIRC v5.3 (13 Dec 1997)

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
--------

.. hlist::
	:columns: 4

	* :doc:`$file </aliases/file>`
	* :doc:`/bcopy <bcopy>`
	* :doc:`/breplace <breplace>`
	* :doc:`/bset <bset>`
	* :doc:`/btrunc <btrunc>`
	* :doc:`/bunset <bunset>`
	* :doc:`/bwrite <bwrite>`
	* :doc:`$bvar </aliases/bvar>`
	* :doc:`$bfind </aliases/bfind>`

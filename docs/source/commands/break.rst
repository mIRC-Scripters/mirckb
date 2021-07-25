/break
======

The **/break** command terminates the execution of the nearest enclosing loop in which it appears.

Synopsis

.. code:: text

	/break

Switches
--------

None

Parameters
----------

None

Example
-------

.. code:: text

	/*
	Assume we have the following global variables:
	%foo = foobar
	%bar = example

	$isValue(testing) -> $false
	$isValue(foobar) -> %foo
	*/
	Alias isValue {
	  ;Declare a counter variable and a returning variable
	  var %count 1, %found $false

	  ;Loop through all the variables
	  while (%count <= $var(*)) {

		/*
		If we found one matching our argument, 
		get the value and break out of the loop
		*/
		if ($var(*,$v1).value == $1-) {
		  %found = $var(*,%count)
		  ;break
		  break
		}
		inc %count
	  }
	  ;return value
	  return %found
	}

Compatibility

Added: mIRC v5.7 (02 Feb 2000)

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
--------

.. hlist::
	:columns: 4

	* :doc:`/continue <continue>`
	* :doc:`/goto <goto>`
	* :doc:`/halt <halt>`
	* :doc:`/if <if>`
	* :doc:`/return <return>`
	* :doc:`/while <while>`
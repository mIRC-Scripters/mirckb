/bunset
=======

The **/bunset** command unsets a binary variable. You can unset multiple variables using the space delimiter.

Synopsis
--------

.. code:: text

	/bunset &binvar [&binvar [&binvar ...]]

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
	* - &binvar
	  - The name of the binary variable to unset

Example
-------

.. code:: text

	Alias Example {
	  ;Create a binary variable
	  bset -t &Example 1 cool text

	  ;Print out its content
	  echo -a $qt($bvar(&Example,1,$bvar(&Example,0)).text)

	  ;Unset the variable
	  bunset &Example

	  ;Print out its content ($null)
	  echo -a $qt($bvar(&Example,1,$bvar(&Example,0)).text)
	}

Compatibility
-------------

Added: mIRC v5.7 (02 Feb 2000)

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
--------

.. hlist::
	:columns: 4

	* :doc:`$bvar </aliases/bvar>`
	* :doc:`$bfind </aliases/bfind>`
	* :doc:`/bread <bread>`
	* :doc:`/breplace <breplace>`
	* :doc:`/bwrite <bwrite>`
	* :doc:`/bset <bset>`
	* :doc:`/bcopy <bcopy>`
	* :doc:`/btrunc <btrunc>`
/avoice
=======

Auto-Voice is a feature that can be used to manage access for a channel. Whenever a user who's address matches an address in the auto-voice list joins the channel, mIRC will voice them.

The **/avoice** command can be used to disable or enable this feature as well as add and remove users from and to the list.

Synopsis
--------

.. code:: text 

	/avoice -rwal <nick/address> [#channel1,#channel2,...] [type] [network]
 
	/avoice <on|off>

Switches
--------

.. list-table::
	:widths: 15 85
	:header-rows: 1

	* - Switch
	  - Description
	* - -r
	  - Indicates address/nick to should be removed, you can pass a channel name to remove that channel only from the list of channel for that entry
	* - -w
	  - Auto-Voice apply to any network
	* - -a
	  - Add the entry (default)
	* - -l
	  - Lists all of the auto-voice entries

Parameters
----------

.. list-table::
	:widths: 15 85
	:header-rows: 1

	* - Parameter
	  - Description
	* - <on/off>
	  - Turns the auto-voice feature on/off.
	* - <nick/address>
	  - The nickname or address of the person to be added to the auto-voice list. Both nickname and addresses are acceptable. Addresses can be wildcard addresses.
	* - [#channel1,#channel2,...]
	  - Channels to apply the auto-voice to.
	* - [type]
	  - Address type to be used.
	* - [network]
	  - Optional network name to apply the auto-voice to.

Example
-------

.. code:: text

	;Turn on auto voice
	/avoice on

	;Add Madgoat to the auto-voice list. Address type 2, network Undernet
	/avoice MadGoat 2 Undernet

	;Remove Madgoat from the auto-voice list
	/avoice -r MadGoat 2 Undernet

	;Turn off auto voice3
	/avoice off

The above example will output:

.. code:: text

	* Auto-Voice is on
	-
	* Added *!*@Example.com to auto-voice list
	-
	* Removed *!*@Example.com from auto-voice list
	-
	* Auto-Voice is off

Compatibility
-------------

Added: mIRC v5.9 (26 Apr 2001)

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
--------

.. hlist::
	:columns: 4

	* :doc:`$aop </identifiers/aop>`
	* :doc:`$avoice </identifiers/avoice>`
	* :doc:`$auto </identifiers/auto>`
	* :doc:`/aop <aop>`
	* :doc:`/auto <auto>`
	* :doc:`/ignore <ignore>`
	* :doc:`/pop <pop>`
	* :doc:`/pvoice <pvoice>`

.. mIRC Knowledge Base documentation master file, created by
   sphinx-quickstart on Sun Dec 27 20:06:05 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to mIRC Knowledge Base!
===============================================

The mIRC Scripting Language, abbreviated as mSL, is an event-driven, procedural scripting language embedded inside the mIRC client. mSL’s main feature is its seamless ability to interact with other IRC clients on IRC in order to perform a variety of tasks.

Although widely used to make bots to automatically manage a channel, mIRC can also be modified, via the scripting language mSL, to include a host of new features, such as: basic games, small functions and macros, the ability to play music, and even operate small applications. Scripts are stored in plain text files (.mrc) or as INI files. With the aid of COM scripts and DLLs, mSL can be further extended to automate just about everything in the Windows environment.

Overview
--------

mSL code can be executed right from the edit box or in the case of more complex scripts as aliases or as events. Aliases are mSL’s version of functions while events are triggered events that automatically activate when the appropriate event occurs.

Language Constructs
-------------------

mSL inherits most of its syntax from the C Programming Language with respect to both the curly syntax as well as its general behavior. For example, like in C, constructs such as if statements evaluate to $true for anything other than 0 and $false. For example ``if (1) { .. }``.

A big departure from most other languages is the fact that mSL makes no distinction between code and plain text. Code is often embedded among plain text and is evaluated as such. For example ``One $calc(1+1) Three`` will correctly treat the ``One`` as plain text, mIRC evaluates the ``$calc`` identifier into ``2`` and finally treat ``Three`` as plain text. The result will be: ``One 2 Three``. On the surface this may seem like it could result in many ambiguities, however in practice it works fairly fluidly with just a handful of problematic cases - many of which can be easily escaped.

Variables and Text Utilities
----------------------------

mSL offers a plethora of facilities that provide an extensive set of ways to work with text and manipulate it.

Variables can be global, in which case they persist for ever until manually removed, or local - which are automatically removed after returning from an on event or an alias call. Variables are defined using the /var and /set commands and have no fixed data type. In fact everything is more or less treated as plain text with the exception of a handful of identifiers that operate on numbers. There is a large number of identifiers that can operate on strings - anything from determining the size, to obtaining a portion of the string from the beginning or end, to case transformation, and pattern matching. For example, the simple $left identifier can be used to obtain a portion from the left side of the string - e.g., ``$left(Hello!!, 4)`` will yield ``Hell``.

Data Storage
------------

Being an event-driven scripting language, mSL only (normally) executes scripts in response to either an IRC event (i.e. a message from the IRC server), an input event by the user, or a timer event. If you want to store information between these event-driven script executions, then you need to use one of the several data storage methods available in mIRC.

Your choice of method depends on three things:

1. Persistence of data after mIRC is closed
2. Volume of data - the performance impact and volume limitations of mIRC
3. The functionality you need to access and process the data The most functional and highest performance storage method is hash tables, which are suitable for large volumes of data and for frequent read and write access. However whilst you can save and restore hash tables from files, you can only save the entire table which has a significant overhead and any changes made since the last save will be lost when mIRC terminates.

The simplest and easiest to use is variables, particularly suitable for simple low-volume data such as script settings.

Variables, INI Files and Text Files all write data to flat files, and are suitable for moderate volumes of data and write activity. For hard coded storage of values you can shorten your plain text to a custom identifier.

For large volume persistent data, needing both high performance and file storage, you may need to store the data in both hash tables for read access then save and load hash tables to and from INI Files.

If you need advice before coding, why not ask for advice in one of the :doc:`misc/mirc_help_channels`.

History
-------

Khaled Mardam-Bey first began development on mIRC in 1994. The original goal for mIRC’s creation was to solve the main issues that haunted some of the earlier IRC clients, which were plagued with steep learning curves, limited feature sets, and other notable issues [1]_. The first public version of mIRC was released on the 28th of February, 1995. The mIRC scripting language grew as commands were added on an ad-hoc basis. Only commands that were directly related to IRC were originally added; however, this slowly changed as the need for more customization grew.

Throughout the 3.0 - 4.0 versions, mSL gained most of the syntax we are familiar with today. Because of the ambiguous nature of the language, such as no real tokens, the use of sigils was introduced in order to distinguish meaningful tokens from plain text tokens. The **$** sigil was introduced to indicate that the token is an identifier. The language began gaining traction when variables were added in version 4.0 [2]_. Variables are preceded by the **%** sigil. Later on, in version 4.1, the concatenation operator was added, which looks like **$+**.

One of the largest updates to the mIRC scripting language took place in version 4.5, which brought evaluation brackets, aliases in remotes, goto statements, string manipulation, identifiers, if statements and operators, as well as variable assignment arithmetic.

mIRC 4.6 to 5.0 brought a stream of new identifiers and commands to perform more complex operations. Version 5.0 also introduced new custom windows, which gave scripters the ability to create customized mIRC windows.

mIRC 5.3 saw the introduction of sockets and picture windows, which were introduced in order to allow scripts the ability to have graphical user interfaces. In version 5.5, dialogs were added which allowed native-looking components to be added onto a window, such as buttons, check boxes and list boxes.

mIRC 7.0 brought about unicode support into the language.

References
----------

.. [1]
   `Personal FAQ <https://www.mirc.com/pfaq.html>`__

.. [2]
   `Versions.txt <https://www.mirc.com/versions.txt>`__

Index
=====

.. toctree::
   :maxdepth: 2
   :caption: Beginner

   beginner/bootcamp
   beginner/variables
   beginner/string_and_token_manipulation
   beginner/aliases

.. toctree::
   :maxdepth: 2
   :caption: Intermediate

   intermediate/control_flow_statements
   intermediate/data_storage
   intermediate/events
   intermediate/matching_tools
   intermediate/gui_scripting

.. toctree::
   :maxdepth: 2
   :caption: Advanced

   advanced/sockets
   advanced/eval_brackets

.. toctree::
   :maxdepth: 2
   :caption: Miscellaneous

   misc/mirc_help_channels

.. toctree::
   :maxdepth: 1
   :caption: About

   about/license
   about/credits

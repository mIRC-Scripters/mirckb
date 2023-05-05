/dcc
====

DCC is an IRC sub-protocol used to establish a direct connection with another IRC client.

Communication does not go through the IRC server like normal PRIVMSGs. DCC lets you chat as well as send and get files. DCC is usually initiated using the IRC server. DCC requires the use of your IP address to initiate a connection with another client.

**DCC Chat:**

.. note:: that the DCC Chat messages are still sent as plaintext.

**DCC Get:**
This command lets you separate download folders according to their file extinctions. Files not matching any of the extinctions you specified are placed in the default DCC get directory.

**DCC Reject:** lets you rejects a dcc send.

.. note:: The DCC get/reject command must be called from a CTCP event or the on DCCServer send event.

**DCC Ignore:**
This command is used to add/remove files from the ignore/accept list. mIRC will automatically accept/decline the file when someone sends you if it's in the list.

**DCC nick:**
This command lets you change the name associated with a dcc chat, send, get, or fserver.

**DCC Passive:**
This command lets you turn passive DCC on or off.

.. note:: mIRC uses a passive protocol to establish connection with a client which is behind a firewall.

**DCC Send:**
The DCC send command lets you initiate a DCC send connection with another user. If more than one file is specified, a session for each file will get initiated.

**DCC Trust**
This command allows you to maintain a trust list of users or address whom mIRC can automatically accept a DCC send.

**DCC Maxcps**
This command lets you change the Max Cps value on the fly

Synopsis
--------

.. code:: text

    /dcc chat <nickname>
    /dcc fserve
    /dcc get <folder>
    /dcc ignore -uM [on | off | accept | ignore]
    /dcc maxcps <N>
    /dcc nick -sgcf <oldnick> <newnick>
    /dcc passive [on | off]
    /dcc reject
    /dcc send [-clmn] <nick> <file1> [file2] ... [fileN]
    /dcc trust [-r] <on | off | nick | address | level>

Switches
--------

DCC Nick

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -s
      - Send
    * - -g
      - Get
    * - -c
      - Chat
    * - -f
      - FServer

DCC Send

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -c
      - Close the DCC send window once transfer is complete
    * - -l
      - Limits the transfer rate to the max cps limit (see /dcc maxcps)
    * - -m
      - Minimize the DCC send window
    * - -n
      - Allows the transfer rate to exceed the max cps limit (see /dcc maxcps)

DCC Trust

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -r
      - removes the user/address from the trusted list

DCC Ignore

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -uM
      - sets the 'turn ignore back on' option on for M minutes

Parameters
----------

DCC Chat

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <nickname>
      - The name of the user to initiate a DCC chats with

DCC Get

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <folder>
      - A specific folder to redirect a file into

DCC Ignore

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - [on | off]
      - Turns DCC Ignore on or off
    * - [accept | ignore]
      -

DCC maxcps

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <N>
      - new max cps

DCC Nick

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <oldnick>
      - Original dcc window name
    * - <newnick>
      - New dcc window name

DCC Passive

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - [on | off]
      - Turns DCC Passive mode on or off

DCC Send

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <nick>
      - The name of the user to initiate a DCC send with
    * - <file1>
      - The file name to be sent
    * - [file2] ... [fileN]
      - Any additional files will have a session of their own

DCC Trust

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <on | off>
      - Turns DCC Trust list on or off
    * - <nick | address | level>
      - NickName/Address/Level of the user to be added to the list

Example
-------

N/A

Compatibility
-------------

* chat/send/get: 

Added: mIRC v2.1a (28 Feb 1995)
* server: 

Added: mIRC v5.1 (11 Sep 1997)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$dccignore </identifiers/dccignore>`
    * :doc:`$dccport </identifiers/dccport>`
    * :doc:`/dccserver </commands/dccserver>`

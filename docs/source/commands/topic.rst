/topic
======

The /topic command enables changing, displaying, or removing the #channel topic, subject to having permissions allowed by the network.

Synopsis
--------

.. code:: text

    /topic [-r] <#channelname> '[topic_string]
    /topic  -r  <#channelname>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -r
      - remove the topic instead

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - topic string
      - new content for #channel topic

Example
-------

.. code:: text

    ; set topic
    //topic $active new topic
    ; remove topic
    //topic -r $active
    ; show current topic
    //topic $active

Notes:
* Network permissions can deny this command, such as needing to be @op when channel mode +t is set, or not being in channel
* $chan(#channelname).topic continues to report the old string until server sends the RAW event indicating the new topic
* Prior to v7.68 topic could only be deleted like: //topic $active $chr(58)

Compatibility
-------------

.. compatibility:: 3.9

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$chan </identifiers/chan>`
    * :doc:`on topic </events/on_topic>`

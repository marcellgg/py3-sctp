An overview of the Python SCTP module
=====================================

Description
-----------

This module is a wrapper for libraries implementing the SCTP protocol
and available on *Linux* and *FreeBSD*. This module strictly
implements the API described in `RFC 6458 <rfc6458_>`__. It consists
of a pure Python module :py:mod:`sctp` and three C-modules
:py:mod:`_sctp.sctp`, :py:mod:`_sctp.sctp_info` and
:py:mod:`_sctp.sctp_event`.

.. note:: The SCTP module does not implement everything marked as
          **deprecated** in `RFC 6458 <rfc6458_>`__ (e.g.,
          :Py:`SCTP_USE_EXT_RCVINFO` socket option,
          :Py:`sctp_sendmsg()` function,...).

The core class is the :py:class:`~sctp.sctp_socket` class. It inherits
all attributes and methods from the :py:class:`socket.socket` class in
the Python :py:mod:`socket` module (except for the method
:py:meth:`~socket.socket.accept` - see note below). To create such a
class:

.. code-block:: Python

   >>> from socket import *
   >>> from sctp import *
   >>> sock = sctp_socket(AF_INET, SOCK_STREAM)
   >>> sock.connect(('localhost', 20000)) # method inherited
   >>> data, addr, info, infotype, flags = sock.sctp_recvv(1024) # new method
   ...
   >>> sock.close()  # method inherited

.. note:: Method :Py:`accept()` of class
          :py:class:`~sctp.sctp_socket` behaves in the same way
          as the standard method :py:meth:`~socket.socket.accept`,
          i.e., it takes no arguments and returns a pair :Py:`(conn,
          address)`. The only difference is that :Py:`conn` is a
          :py:class:`~sctp.sctp_socket` object and not a
          :py:class:`socket.socket` object.

`RFC 6458 <rfc6458_>`__ defines a number of socket options and, where
applicable, the corresponding C structures, the latter being available
as classes, with the same name, inheriting from :py:class:`dict`.
The same applies to SCTP events and notifications, which are also
implemented as classes inheriting from :py:class:`dict`.

.. warning:: Unlike the standard Python module :py:mod:`socket` module, IPv6
	     addresses are **necessarily** 4-tuples of the form
	     :Py:`(host, port, flowinfo, scope_id)`, see
	     :ref:`ip-addresses` for details.

Class diagrams
--------------

Module :py:mod:`sctp`
^^^^^^^^^^^^^^^^^^^^^

.. graphviz::

   digraph {
     rankdir=LR
     edge [arrowhead="vee", color="#5a6062"]
     node [shape="box", style=filled, fillcolor="#ffe7d4", color="#5a6062"]
     a [label="sctp.sctp_socket"]
     b [
          style=none
          shape = none
          label = <<table border="0" cellspacing="0" bgcolor="#e9f6f1"
	  align="left">
          <tr><td port="m0" border="1" bgcolor="#aee3f3">Methods</td></tr>
          <tr><td border="1" align="left">getsockopt()</td></tr>
          <tr><td border="1" align="left">setsockopt()</td></tr>
          <tr><td border="1" align="left">sctp_opt_info()</td></tr>
          </table>>
    ]
     a -> b:m0
     c [label="_sctp.sctp.sctp_socket"]
     d [
          style=none
          shape = none
          label = <<table border="0" cellspacing="0" bgcolor="#e9f6f1"
	  align="left">
	  <tr><td port="m0" border="1" bgcolor="#aee3f3">Properties</td></tr>
	  <tr><td border="1" align="left">sctp_type</td></tr>
	  <tr><td border="1" align="left">sock</td></tr>
          <tr><td border="1" bgcolor="#aee3f3">Methods</td></tr>
          <tr><td border="1" align="left">sctp_bindx()</td></tr>
          <tr><td border="1" align="left">sctp_connectx()</td></tr>
          <tr><td border="1" align="left">sctp_getladdrs()</td></tr>
	  <tr><td border="1" align="left">sctp_getpaddrs()</td></tr>
	  <tr><td border="1" align="left">sctp_recvv()</td></tr>
	  <tr><td border="1" align="left">sctp_sendv()</td></tr>
	  <tr><td border="1" align="left">sctp_peeloff()</td></tr>
          </table>>
     ]
     c -> d:m0
     o [label="object"]
     {
       edge [constraint=false]
       a -> c -> o
     }
   }

.. graphviz::
   
   digraph {
     rankdir=LR
     edge [arrowhead="vee", arrowtail="vee", color="#5a6062"]
     node [shape="box", style=filled, fillcolor="#ffe7d4", color="#5a6062"]
     g [label="sctp.sctp_*"]
     h [
          style=none
          shape = none
          label = <<table border="0" cellspacing="0" bgcolor="#ffe7d4"
	  align="left">
          <tr><td border="1" align="left">sctp_initmsg</td></tr>
	  <tr><td bgcolor="white" height="5px"></td></tr>
	  <tr><td border="1" align="left">sctp_paddrparams</td></tr>
	  <tr><td bgcolor="white" height="5px"></td></tr>
	  <tr><td border="1" align="left">sctp_paddrinfo</td></tr>
	  <tr><td bgcolor="white" height="5px"></td></tr>
	  <tr><td border="1" align="left">sctp_rtoinfo</td></tr>
	  <tr><td bgcolor="white" height="5px"></td></tr>
	  <tr><td border="1" align="left">sctp_assocparams</td></tr>
	  <tr><td bgcolor="white" height="5px"></td></tr>
	  <tr><td border="1" align="left">sctp_setprim</td></tr>
	  <tr><td bgcolor="white" height="5px"></td></tr>
	  <tr><td border="1" align="left">sctp_setadaptation</td></tr>
	  <tr><td bgcolor="white" height="5px"></td></tr>
	  <tr><td border="1" align="left">sctp_assoc_value</td></tr>
	  <tr><td bgcolor="white" height="5px"></td></tr>
	  <tr><td border="1" align="left">sctp_authkeyid</td></tr>
	  <tr><td bgcolor="white" height="5px"></td></tr>
	  <tr><td border="1" align="left">sctp_sack_info</td></tr>
	  <tr><td bgcolor="white" height="5px"></td></tr>
	  <tr><td border="1" align="left">sctp_default_sndinfo</td></tr>
	  <tr><td bgcolor="white" height="5px"></td></tr>
	  <tr><td border="1" align="left">sctp_default_prinfo</td></tr>
	  <tr><td bgcolor="white" height="5px"></td></tr>
	  <tr><td border="1" align="left">sctp_status</td></tr>
	  <tr><td bgcolor="white" height="5px"></td></tr>
	  <tr><td border="1" align="left">sctp_setpeerprim</td></tr>
	  <tr><td bgcolor="white" height="5px"></td></tr>
	  <tr><td border="1" align="left">sctp_authchunk</td></tr>
	  <tr><td bgcolor="white" height="5px"></td></tr>
	  <tr><td border="1" align="left">sctp_authkey</td></tr>
	  <tr><td bgcolor="white" height="5px"></td></tr>
	  <tr><td border="1" align="left">sctp_event</td></tr>
          </table>>
     ]
     g -> h [dir=both]
     a [label="sctp.sctp_generic"]
     b [
          style=none
          shape = none
          label = <<table border="0" cellspacing="0" bgcolor="#e9f6f1"
	  align="left">
          <tr><td port="m0" border="1" bgcolor="#aee3f3">Properties</td></tr>
          <tr><td border="1" align="left">fmt</td></tr>
          <tr><td border="1" align="left">size</td></tr>
	  <tr><td border="1" align="left">to_bytes</td></tr>
	  <tr><td border="1" bgcolor="#aee3f3">Methods</td></tr>
	  <tr><td border="1" align="left">set_value()</td></tr>
          </table>>
     ]
     a -> b:m0
     {
       edge [constraint=false]
       c [label="dict"]
       g -> a -> c
     }
   }

Module :py:mod:`~_sctp.sctp_info`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. graphviz::
   
   digraph {
     rankdir=LR
     edge [arrowhead="vee", arrowtail="vee", color="#5a6062"]
     node [shape="box", style=filled, fillcolor="#ffe7d4", color="#5a6062"]
     g [label="_sctp.sctp_info.sctp_*"]
     h [
          style=none
          shape = none
          label = <<table border="0" cellspacing="0" bgcolor="#ffe7d4"
	  align="left">
          <tr><td border="1" align="left">sctp_sndinfo</td></tr>
	  <tr><td bgcolor="white" height="5px"></td></tr>
	  <tr><td border="1" align="left">sctp_prinfo</td></tr>
	  <tr><td bgcolor="white" height="5px"></td></tr>
	  <tr><td border="1" align="left">sctp_authinfo</td></tr>
	  <tr><td bgcolor="white" height="5px"></td></tr>
	  <tr><td border="1" align="left">sctp_sendv_spa</td></tr>
	  <tr><td bgcolor="white" height="5px"></td></tr>
	  <tr><td border="1" align="left">sctp_rcvinfo</td></tr>
	  <tr><td bgcolor="white" height="5px"></td></tr>
	  <tr><td border="1" align="left">sctp_nxtinfo</td></tr>
	  <tr><td bgcolor="white" height="5px"></td></tr>
	  <tr><td border="1" align="left">sctp_recvv_rn</td></tr>
          </table>>
     ]
     g -> h [dir=both]
     {
       edge [constraint=false]
       a [label="dict"]
       g -> a
     }
   }

Module :py:mod:`~_sctp.sctp_event`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. graphviz::

   digraph {
     rankdir=LR
     edge [arrowhead="vee", color="#5a6062"]
     node [shape="box", style=filled, fillcolor="#ffe7d4", color="#5a6062"]
     a [label="_sctp.sctp_event"]
     b [
          style=none
          shape = none
          label = <<table border="0" cellspacing="0" bgcolor="#e9f6f1"
	  align="left">
          <tr><td port="m0" border="1" bgcolor="#aee3f3">Methods</td></tr>
          <tr><td border="1" align="left">parse_notification()</td></tr>
          </table>>
     ]
     a -> b:m0
   }

.. _examples:

Some examples
-------------

A simple *echo* client/server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is the *echo* client/server revisited. Here, both the client and
the server use different streams for sending and receiving data.

.. literalinclude:: code/echo_client.py
   :language: Python
   :caption: echo_client.py

The client sends data on stream :Py:`Streams.OUT` (:Py:`1`) and
receives it on stream :Py:`Streams.IN` (:Py:`0`).

.. literalinclude:: code/echo_server.py
   :language: Python
   :caption: echo_server.py

The server sends data on stream :Py:`Streams.OUT` (:Py:`0`) and
receives it on stream :Py:`Streams.IN` (:Py:`1`).

The Python version of the example shown in `Appendix A <rfc6458appA_>`__ of RFC 6458
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: code/one-to-one.py
   :language: Python
   :caption: one-to-one.py

To test this script with *discard* server on *Linux*, you must first
start this server. This requires two steps (as root):

#. Edit file :Bash:`/etc/xinetd.d/discard` and set :Bash:`disable=no`
   for TCP protocol.

#. Start *discard* server with command :Bash:`withsctp`:

   .. code-block:: console

      # withsctp xinetd

And finally, run the script as a non-privileged user:

.. code-block:: console

   $ python3 one_to_one.py

The Python version of the example shown in `Appendix B <rfc6458appB_>`__ of RFC 6458
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: code/one-to-many.py
   :language: Python
   :caption: one-to-many.py

To test this script, first run it as root (port=9 is a priviliged
one):

.. code-block:: console
   :caption: root window

   # python3 one-to-many.py

In another window, run :Bash:`one_to_one.py` as a non-privileged user:

.. code-block:: console
   :caption: user window

   $ python3 one_to_one.py

In root window, you will see something like that:

.. code-block:: console
   :caption: root window

   # python3 one-to-many.py
   Communication up (streams (in/out)=(2048/10)).
   ^^^ Adaptation indication 01020304 received.
   Message received from ::ffff:127.0.0.1:52378: len=1000, sid=0
   , unordered, tsn=3093043390, ppid=1234.
   Message received from ::ffff:127.0.0.1:52378: len=1000, sid=1
   , unordered, tsn=3093043391, ppid=1234.
   Message received from ::ffff:127.0.0.1:52378: len=1000, sid=2
   , unordered, tsn=3093043392, ppid=1234.
   Message received from ::ffff:127.0.0.1:52378: len=1000, sid=3
   , unordered, tsn=3093043393, ppid=1234.
   Message received from ::ffff:127.0.0.1:52378: len=1000, sid=4
   , unordered, tsn=3093043394, ppid=1234.
   Message received from ::ffff:127.0.0.1:52378: len=1000, sid=5
   , unordered, tsn=3093043395, ppid=1234.
   Message received from ::ffff:127.0.0.1:52378: len=1000, sid=6
   , unordered, tsn=3093043396, ppid=1234.
   Message received from ::ffff:127.0.0.1:52378: len=1000, sid=7
   , unordered, tsn=3093043397, ppid=1234.
   Message received from ::ffff:127.0.0.1:52378: len=1000, sid=8
   , unordered, tsn=3093043398, ppid=1234.
   Message received from ::ffff:127.0.0.1:52378: len=1000, sid=9
   , unordered, tsn=3093043399, ppid=1234.
   ^^^ Shutdown received.
   Communication completed.

.. _rfc6458: https://datatracker.ietf.org/doc/html/rfc6458
.. _rfc6458appA: https://datatracker.ietf.org/doc/html/rfc6458#appendix-A
.. _rfc6458appB: https://datatracker.ietf.org/doc/html/rfc6458#appendix-B

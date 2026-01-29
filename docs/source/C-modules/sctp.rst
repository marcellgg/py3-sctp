Module _sctp.sctp
=================

.. module:: _sctp.sctp

.. _ip-addresses:

IP addresses
------------

The format of IPv4 addresses is identical to that of the standard
Python :py:mod:`socket` module. Thus, such an address is a 2-tuple
:Py:`(host, port)`.

Unlike the standard Python :py:mod:`socket` module (where IPv6
addresses can be 2-tuples), IPv6 addresses here are **necessarily**
4-tuples of the form :Py:`(host, port, flowinfo, scope_id)`. For
example, the address :Py:`('::1', 2000)` will be interpreted as an
IPv4 address, which will trigger an error.

For instance, we must be able to distinguish between
:Py:`('localhost', 2000)` and :Py:`('localhost', 2000, 0, 0)`, as
shown in the following example:

    .. code-block:: Python

       >>> sock = sctp_socket(AF_INET6, SOCK_STREAM)
       >>> sock.sctp_bindx((('localhost', 2000), ('localhost', 2000, 0, 0)),\
		    SCTP_BINDX_ADD_ADDR)
       
Functions
---------
	    
Creating SCTP sockets
^^^^^^^^^^^^^^^^^^^^^
.. py:class:: sctp_socket(family, type, proto=IPPROTO_SCTP)

   Create a new SCTP socket object using the given address family,
   socket type and protocol number. Address family must be
   :py:data:`~socket.AF_INET` or :py:data:`~socket.AF_INET6`. Socket
   type must be :py:data:`~socket.SOCK_STREAM` or
   :py:data:`~socket.SOCK_SEQPACKET` and protocol number must be
   :py:data:`IPPROTO_SCTP`.

   Raises :py:exc:`SCTPError` when one of the arguments is invalid.

   .. note::
      Newly created SCTP sockets inherit all methods and
      attributes from sockets in the standard Python :py:mod:`socket` module.

Other functions
^^^^^^^^^^^^^^^
Two utility functions (not defined in `RFC 6458 <rfc6458_>`__):

.. py:function:: ipaddr_to_sockaddr_storage(ip_addr)

   :param ip_addr: an IPv4 address (host, port) or an IPv6 address
                   (host, port, flowinfo, scope_id)
   :returns: a :C:`struct sockaddr_storage` (See `RFC 3493 -- section-3.10
             <rfc3493_>`__) as a :py:class:`bytes` object
   :raise: :py:exc:`TypeError` if **ip_addr** is not a valid IPv4/v6
	   address.

.. py:function:: sockaddr_storage_to_ipaddr(bytes)

   :param bytes: a :C:`struct sockaddr_storage` (see `RFC 3493 --
             section-3.10 <rfc3493_>`__) as a :py:class:`bytes` object
   :returns: an IPv4 address (host, port) or an IPv6 address (host,
                   port, flowinfo, scope_id)

   If **bytes** cannnot be interpreted as :C:`struct
   sockaddr_storage`, function **sockaddr_storage_to_ipaddr()**
   returns :Py:`('???', 0)` or :Py:`('???', 0, 0, 0)` (no exception
   raised).
 
SCTP Socket Objects
-------------------
Attributes
^^^^^^^^^^
.. py:attribute:: sctp_socket.sctp_type

   Is either :Py:`'one-to-one'` or :Py:`'one-to-many'` depending on
   whether the socket type is :py:data:`~socket.SOCK_STREAM` or
   :py:data:`~socket.SOCK_SEQPACKET`.

.. py:attribute:: sctp_socket.sock

   The underlying :py:class:`socket.socket`.

   .. note::
      This read-only attribute is for internal use only.

Methods
^^^^^^^
.. note::
   In all methods that take an iterable of IPv4/IPv6 addresses as an
   argument, the :py:exc:`TypeError` exception is thrown if the socket
   is an IPv4 socket and there are one or more IPv6 addresses among
   the addresses.

.. py:method:: sctp_socket.sctp_bindx(addrs, flags)

   :param addrs: an iterable of IPv4/IPv6 addresses
   :param flags: must be :Py:`SCTP_BINDX_ADD_ADDR` or
                 :Py:`SCTP_BINDX_REM_ADDR`
   :returns: :Py:`None`
   :raise: :py:exc:`TypeError`, :py:exc:`ValueError` or :py:exc:`OSError`

   This method is a wrapper for function :C:`sctp_bindx()` described
   in `RFC 6458 -- section-9.1 <rfc6458bindx_>`__.

.. py:method:: sctp_socket.sctp_connectx(addrs, *, assoc_id=False)

   :param addrs: an iterable of IPv4/IPv6 addresses
   :param assoc_id: boolean
   :returns: :Py:`None` if **assoc_id** is :Py:`False` or "*association
             identifier*" otherwise
   :raise: :py:exc:`TypeError`, :py:exc:`ValueError` or :py:exc:`OSError`

   This method is a wrapper for function :C:`sctp_connectx()` described
   in `RFC 6458 -- section-9.9 <rfc6458connectx_>`__.

.. py:method:: sctp_socket.sctp_getladdrs([assoc_id])

   :param assoc_id: identifier of the association to query (:C:`int32_t`)
   :returns: a tuple of IPv4/IPv6 addresses or :Py:`None`

   This method is a wrapper for function :C:`sctp_getladdrs()` described
   in `RFC 6458 -- section-9.5 <rfc6458getladdrs_>`__.

.. py:method:: sctp_socket.sctp_getpaddrs([assoc_id])

   :param assoc_id: identifier of the association to query (:C:`int32_t`)
   :returns: a tuple of IPv4/IPv6 addresses or :Py:`None`

   This method is a wrapper for function :C:`sctp_getpaddrs()` described
   in `RFC 6458 -- section-9.3 <rfc6458getpaddrs_>`__.

.. py:method:: sctp_socket.sctp_recvv(bufsize)
   
   :param bufsize: size of the :py:class:`bytes` object receiving the data
   :returns: a 5-tuple :Py:`(data, addr, info, infotype, flags)` where:
	     
	     * :Py:`data` is a :py:class:`bytes` object holding the
               data received (up to **bufsize**)
	     * :Py:`addr`: sender address
	     * :Py:`info` is either a
               :py:class:`~_sctp.sctp_info.sctp_rcvinfo` or a
	       :py:class:`~_sctp.sctp_info.sctp_nxtinfo` or a
	       :py:class:`~_sctp.sctp_info.sctp_recvv_rn` object
	     * :Py:`infotype` is either the constant
               :py:data:`SCTP_RECVV_NOINFO` or :py:data:`SCTP_RECVV_RCVINFO`
	       or :py:data:`SCTP_RECVV_NXTINFO` or :py:data:`SCTP_RECVV_RN`
	     * :Py:`flags`: received message flags (e.g.,
               :py:data:`MSG_NOTIFICATION`)
   :raise: :py:exc:`TypeError`, :py:exc:`ValueError` or :py:exc:`OSError`

   This method is a wrapper for function :C:`sctp_recvv()` described
   in `RFC 6458 -- section-9.13 <rfc6458recvv_>`__.

   In order to receive attribures
   :py:class:`~_sctp.sctp_info.sctp_rcvinfo` and
   :py:class:`~_sctp.sctp_info.sctp_nxtinfo`, you must first activate
   socket options :py:data:`SCTP_RECVRCVINFO` and
   :py:data:`SCTP_RECVNXTINFO` respectively as shown below:

   .. code-block:: Python

      >>> sock = sctp_socket(AF_INET SOCK_STREAM)
      >>> sock.setsockopt(IPPROTO_SCTP, SCTP_RECVRCVINFO, 1)
      ... # waiting for data
      >>> sock.sctp_recvv(1024)
      >>> _, _, info, infotype, _ = s.sctp_recvv(1024)
      >>> print(infotype == SCTP_RECVV_RCVINFO)
      True
      >>> print(info)
      {'rcv_sid': 0, 'rcv_ssn': 0, 'rcv_flags': 0, 'rcv_ppid': 0, 'rcv_tsn': 188475,
       'rcv_cumtsn': 0, 'rcv_context': 0, 'rcv_assoc_id': 955}

   An other example with both options:

   .. code-block:: Python

      >>> sock = sctp_socket(AF_INET SOCK_STREAM)
      >>> sock.setsockopt(IPPROTO_SCTP, SCTP_RECVRCVINFO, 1)
      >>> sock.setsockopt(IPPROTO_SCTP, SCTP_RECVNXTINFO, 1)
      ... # waiting for data
      >>> sock.sctp_recvv(1024)
      >>> _, _, info, infotype, _ = s.sctp_recvv(1024)
      >>> print(infotype == SCTP_RECVV_RN)
      True
      >>> print(info.nxtinfo)
      {'nxt_sid': 1, 'nxt_flags': 0, 'nxt_ppid': 0, 'nxt_length': 68,
       'nxt_assoc_id': 23}

   .. note:: An option may have been requested but not received.

.. py:method:: sctp_socket.sctp_sendv(data, [addrs, [info, [flags]]])

   :param data: data to send: an iterable of :py:class:`bytes` object
   :param addrs: destination addresses: an iterable of IPv4/v6
                 addresses or :Py:`None`
   :param info: attributes that can be used to describe a message to
		be sent or :Py:`None`. The **info** parameter can be either
		a :py:class:`~_sctp.sctp_info.sctp_sndinfo` or
		a :py:class:`~_sctp.sctp_info.sctp_prinfo` or
		a :py:class:`~_sctp.sctp_info.sctp_authinfo` or
		a :py:class:`~_sctp.sctp_info.sctp_sendv_spa` object
		
   :param flags: the same flags as used by the
		 :py:meth:`~socket.socket.sendmsg()` call flags (e.g.,
		 :Py:`MSG_DONTROUTE`). Default value is :Py:`0`
   :returns: number of bytes sent
   :raise: :py:exc:`TypeError`, :py:exc:`ValueError` or :py:exc:`OSError`

   This method is a wrapper for function :C:`sctp_sendv()` described
   in `RFC 6458 -- section-9.12 <rfc6458sendv_>`__.

   Two examples showing how to use the **info** parameter:
   
   * sending data on stream number 5,
     
     .. code-block:: Python

	>>> sock = sctp_socket(AF_INET6 SOCK_STREAM)
	...
	>>> info = sctp_sndinfo(snd_sid=5)
	>>> noc = sock.sctp_sendv((b'some data',), None, info)
	>>> print(noc)
	9

   * sending data on stream number 5 and setting lifetime to 1 second,

     .. code-block:: Python

	>>> sock = sctp_socket(AF_INET6 SOCK_STREAM)
	...
	>>> sndinfo = sctp_sndinfo(snd_sid=5)
	>>> prinfo = sctp_prinfo(pr_policy=SCTP_PR_SCTP_TTL, pr_value=1000)
	>>> spa = sctp_sendv_spa((sndinfo, prinfo))
	>>> noc = sock.sctp_sendv((b'some data',), None, spa)

.. py:method:: sctp_socket._getsockopt(level, optname, optval)

   :param int level: option level
   :param int optname: option name
   :param bytes optval: option value

   For example, when the level is :Py:`IPPROTO_SCTP` and the option is
   :py:data:`~_sctp.sctp.SCTP_PEER_ADDR_PARAMS`, you need to pass a
   partially pre-filled bytes object as the option value. However, the
   method :py:meth:`~socket.socket.getsockopt` provided by the
   standard Python :py:mod:`socket` module takes an integer (optional)
   as its last argument. Hence the need to introduce this auxiliary
   method.

   .. note:: This method is intended for internal use only.
   
Constants
---------
This module export the following constants:

.. py:data:: IPPROTO_SCTP

sctp_sendv() -- sctp_recvv() attributes:

* .. py:data:: SCTP_RECVRCVINFO
* .. py:data:: SCTP_RECVNXTINFO
* .. py:data:: SCTP_SENDV_NOINFO
* .. py:data:: SCTP_SENDV_SNDINFO
* .. py:data:: SCTP_SENDV_PRINFO
* .. py:data:: SCTP_SENDV_AUTHINFO
* .. py:data:: SCTP_SENDV_SPA
* .. py:data:: SCTP_SEND_SNDINFO_VALID
* .. py:data:: SCTP_SEND_PRINFO_VALID
* .. py:data:: SCTP_SEND_AUTHINFO_VALID
* .. py:data:: SCTP_RECVV_NOINFO
* .. py:data:: SCTP_RECVV_RCVINFO
* .. py:data:: SCTP_RECVV_NXTINFO
* .. py:data:: SCTP_RECVV_RN

SCTP Socket Options
^^^^^^^^^^^^^^^^^^^

Initialization Parameters (see `RFC 6458 -- section-8.1.3
<rfc6458init_>`__):

* .. py:data:: SCTP_INIT
* .. py:data:: SCTP_INITMSG

sctp_bindx() flags (see `RFC 6458 -- section-9.1
<rfc6458bindx_>`__):

* .. py:data:: SCTP_BINDX_ADD_ADDR
* .. py:data:: SCTP_BINDX_REM_ADDR

Retransmission Timeout Parameters (see `RFC 6458 -- section-8.1.1
<rfc6458rto_>`__):

* .. py:data:: SCTP_RTOINFO

Association Parameters (see `RFC 6458 -- section-8.1.2
<rfc6458sasoc_>`__):

* .. py:data:: SCTP_ASSOCINFO

Peer address parameters (see `RFC 6458 -- section-8.1.12
<rfc6458pap_>`__):

* .. py:data:: SCTP_PEER_ADDR_PARAMS
* .. py:data:: SPP_*

  field :C:`spp_flags` of :C:`struct sctp_paddrparams`

Peer address information (see `RFC 6458 -- section-8.2.2
<rfc6458pai_>`__):

* .. py:data:: SCTP_GET_PEER_ADDR_INFO
* .. py:data:: SCTP_UNCONFIRMED
* .. py:data:: SCTP_ACTIVE
* .. py:data:: SCTP_INACTIVE

Set Primary Address (see `RFC 6458 -- section-8.1.9
<rfc6458ssp_>`__):

* .. py:data:: SCTP_PRIMARY_ADDR

Set Adaptation Layer Indicator (see `RFC 6458 -- section-8.1.10
<rfc6458ssb_>`__):

* .. py:data:: SCTP_ADAPTATION_LAYER

Get or Set the Maximum Fragmentation Size (see `RFC 6458 -- section-8.1.16
<rfc6458assoc_>`__):

* .. py:data:: SCTP_MAXSEG

Get or Set the List of Supported HMAC Identifiers (see `RFC 6458 --
section-8.1.17 <rfc6458hmi_>`__):

* .. py:data:: SCTP_HMAC_IDENT

Get or Set the Active Shared Key (see `RFC 6458 -- section-8.1.18
<rfc6458ask_>`__):

* .. py:data:: SCTP_AUTH_ACTIVE_KEY

Get or Set Delayed SACK Timer (see `RFC 6458 -- section-8.1.19
<rfc6458sack_>`__):

* .. py:data:: SCTP_DELAYED_SACK

Get or Set Fragmented Interleave (see `RFC 6458 -- section-8.1.20
<rfc6458frin_>`__):

* .. py:data:: SCTP_FRAGMENT_INTERLEAVE

Set or Get the Maximum Burst (see `RFC 6458 -- section-8.1.24
<rfc6458mabu_>`__):

* .. py:data:: SCTP_MAX_BURST

Set or Get the Default Context (see `RFC 6458 -- section-8.1.25
<rfc6458deco_>`__):

* .. py:data:: SCTP_CONTEXT

Set Default Send Parameters (see `RFC 6458 -- section-8.1.31
<rfc6458dsp_>`__):

* .. py:data:: SCTP_DEFAULT_SNDINFO

Set Default PR-SCTP Parameters (see `RFC 6458 -- section-8.1.32
<rfc6458dpp_>`__):

* .. py:data:: SCTP_DEFAULT_PRINFO

Association Status (see `RFC 6458 -- section-8.2.1
<rfc6458ast_>`__):

* .. py:data:: SCTP_STATUS

  field *sstat_state*:

  * .. py:data:: SCTP_CLOSED
  * .. py:data:: SCTP_COOKIE_WAIT
  * .. py:data:: SCTP_COOKIE_ECHOED
  * .. py:data:: SCTP_ESTABLISHED
  * .. py:data:: SCTP_SHUTDOWN_PENDING
  * .. py:data:: SCTP_SHUTDOWN_SENT
  * .. py:data:: SCTP_SHUTDOWN_RECEIVED
  * .. py:data:: SCTP_SHUTDOWN_ACK_SENT

Get the List of Chunks the Peer Requires to Be Authenticated (see
`RFC 6458 -- section-8.2.3 <rfc6458pac_>`__):

* .. py:data:: SCTP_PEER_AUTH_CHUNKS

Get the List of Chunks the Local Endpoint Requires to Be Authenticated (see
`RFC 6458 -- section-8.2.4 <rfc6458lac_>`__):

* .. py:data:: SCTP_LOCAL_AUTH_CHUNKS

Get the Current Number/List of Associations (see `RFC 6458 -- section-8.2.5/6
<rfc6458cna_>`__):

* .. py:data:: SCTP_GET_ASSOC_NUMBER
* .. py:data:: SCTP_GET_ASSOC_ID_LIST

Set Peer Primary Address (see `RFC 6458 -- section-8.3.1
<rfc6458ppa_>`__):

* .. py:data:: SCTP_SET_PEER_PRIMARY_ADDR

Add a Chunk That Must Be Authenticated (see `RFC 6458 -- section-8.3.2
<rfc6458aca_>`__):

* .. py:data:: SCTP_AUTH_CHUNK

Set a Shared Key (see `RFC 6458 -- section-8.3.3 <rfc6458ssk_>`__):

* .. py:data:: SCTP_AUTH_KEY

Deactivate/Delete a Shared Key (see `RFC 6458 -- section-8.3.4/5
<rfc6458ddk_>`__):

* .. py:data:: SCTP_AUTH_DEACTIVATE_KEY
* .. py:data:: SCTP_AUTH_DELETE_KEY
  
Sizes (:C:`sizeof()`) of various structures (:C:`struct sctp_*`)

* .. py:data:: SCTP_INITMSG_CSIZE
* .. py:data:: SCTP_PADDRPARAMS_CSIZE
* .. py:data:: SCTP_PADDRINFO_CSIZE
* .. py:data:: SCTP_RTOINFO_CSIZE
* .. py:data:: SCTP_ASSOCPARAMS_CSIZE
* .. py:data:: SCTP_SETPRIM_CSIZE
* .. py:data:: SCTP_SETADAPTATION_CSIZE
* .. py:data:: SCTP_MAXSEG_CSIZE
* .. py:data:: SCTP_DELAYED_SACK_CSIZE
* .. py:data:: SCTP_SNDINFO_CSIZE
* .. py:data:: SCTP_DEFAULT_PRINFO_CSIZE
* .. py:data:: SCTP_STATUS_CSIZE
* .. py:data:: SCTP_SET_PEER_PRIMARY_ADDR_CSIZE
* .. py:data:: SOCKADDR_STORAGE_CSIZE

  .. _align:
  .. note:: The C structures defined in :C:`<netinet/sctp.h>` are
     aligned differently depending on the implementation. For example,
     on FreeBSD they have attribute :C:`__attribute__((packed))`,
     while on Linux they have attribute :C:`__attribute__((packed,
     aligned(4)))`.  Knowing these sizes allows module :py:mod:`sctp`
     to calculate the possible padding required when using module
     :py:mod:`struct` (see :py:attr:`~sctp.sctp_generic.fmt`
     property).  These constants are intended for internal use only.

Miscellaneous:

* .. py:data:: SCTP_NODELAY
* .. py:data:: SCTP_AUTOCLOSE
* .. py:data:: SCTP_DISABLE_FRAGMENTS
* .. py:data:: SCTP_I_WANT_MAPPED_V4_ADDR
* .. py:data:: SCTP_PARTIAL_DELIVERY_POINT
* .. py:data:: SCTP_AUTO_ASCONF
* .. py:data:: SCTP_REUSE_PORT
* .. py:data:: SCTP_AUTH_HMAC_ID_SHA1
* .. py:data:: SCTP_AUTH_HMAC_ID_SHA256

Exceptions
----------
.. py:exception:: SCTPError

.. _rfc3493: https://datatracker.ietf.org/doc/html/rfc3493#section-3.10
.. _rfc6458bindx: https://datatracker.ietf.org/doc/html/rfc6458#section-9.1
.. _rfc6458connectx: https://datatracker.ietf.org/doc/html/rfc6458#section-9.9
.. _rfc6458getladdrs: https://datatracker.ietf.org/doc/html/rfc6458#section-9.5
.. _rfc6458getpaddrs: https://datatracker.ietf.org/doc/html/rfc6458#section-9.3
.. _rfc6458recvv: https://datatracker.ietf.org/doc/html/rfc6458#section-9.13
.. _rfc6458sendv: https://datatracker.ietf.org/doc/html/rfc6458#section-9.12
.. _rfc6458rto: https://datatracker.ietf.org/doc/html/rfc6458#section-8.1.1
.. _rfc6458sasoc: https://datatracker.ietf.org/doc/html/rfc6458#section-8.1.2
.. _rfc6458init: https://datatracker.ietf.org/doc/html/rfc6458#section-8.1.3
.. _rfc6458ssp: https://datatracker.ietf.org/doc/html/rfc6458#section-8.1.9
.. _rfc6458ssb: https://datatracker.ietf.org/doc/html/rfc6458#section-8.1.10
.. _rfc6458pap: https://datatracker.ietf.org/doc/html/rfc6458#section-8.1.12
.. _rfc6458assoc: https://datatracker.ietf.org/doc/html/rfc6458#section-8.1.16
.. _rfc6458hmi: https://datatracker.ietf.org/doc/html/rfc6458#section-8.1.17
.. _rfc6458ask: https://datatracker.ietf.org/doc/html/rfc6458#section-8.1.18
.. _rfc6458sack: https://datatracker.ietf.org/doc/html/rfc6458#section-8.1.19
.. _rfc6458frin: https://datatracker.ietf.org/doc/html/rfc6458#section-8.1.20
.. _rfc6458mabu: https://datatracker.ietf.org/doc/html/rfc6458#section-8.1.24
.. _rfc6458deco: https://datatracker.ietf.org/doc/html/rfc6458#section-8.1.25
.. _rfc6458dsp: https://datatracker.ietf.org/doc/html/rfc6458#section-8.1.31
.. _rfc6458dpp: https://datatracker.ietf.org/doc/html/rfc6458#section-8.1.32
.. _rfc6458ast: https://datatracker.ietf.org/doc/html/rfc6458#section-8.2.1
.. _rfc6458pai: https://datatracker.ietf.org/doc/html/rfc6458#section-8.2.2
.. _rfc6458pac: https://datatracker.ietf.org/doc/html/rfc6458#section-8.2.3
.. _rfc6458lac: https://datatracker.ietf.org/doc/html/rfc6458#section-8.2.4
.. _rfc6458cna: https://datatracker.ietf.org/doc/html/rfc6458#section-8.2.5
.. _rfc6458ppa: https://datatracker.ietf.org/doc/html/rfc6458#section-8.3.1
.. _rfc6458aca: https://datatracker.ietf.org/doc/html/rfc6458#section-8.3.2
.. _rfc6458ssk: https://datatracker.ietf.org/doc/html/rfc6458#section-8.3.3
.. _rfc6458ddk: https://datatracker.ietf.org/doc/html/rfc6458#section-8.3.4
.. _rfc6458: https://datatracker.ietf.org/doc/html/rfc6458

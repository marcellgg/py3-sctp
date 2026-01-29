Module sctp
===========

.. module:: sctp

Objects
-------

.. py:class:: sctp_generic(**kwds)

   :bases: :py:class:`dict`

   .. py:attribute:: __fields__

      :type: dict
      :value: {}

      Valid dictionary keys with value formats and default values.
      
   .. py:attribute:: __c_size__

      :type: int
      :value: 0

      The size in bytes of the corresponding C-structure
      (:C:`sizeof()`).  See :ref:`note <align>` in
      :py:mod:`_sctp.sctp` about alignment of C-structures.

   .. py:attribute:: __optname__

      :type: int
      :value: 0

      Socket option name (e.g., :py:data:`~_sctp.sctp.SCTP_RTOINFO`)

   .. py:property:: fmt

      :classmethod:
      :type: str

      The format used by :py:func:`struct.pack` in property
      :py:data:`~sctp.sctp_generic.to_bytes`. It takes into account
      any possible padding (see :ref:`note <align>` in
      :py:mod:`_sctp.sctp` about padding).
      
   .. py:property:: size

      :classmethod:
      :type: int

      A shortcut for
      :Py:`struct.calcsize(`:py:data:`~sctp.sctp_generic.fmt`:Py:`)`.

   .. py:property:: to_bytes

      :type: str

      Converts the dictionary into a bytes object (using
      :py:func:`struct.pack` with format
      :py:data:`~sctp.sctp_generic.fmt`).

   .. py:method:: set_value(field, value)

      :param str field:
      :param value:
      :type value: int or bytes
      :returns: **value**, if check succeeded
      :raises TypeError: if check failed

   .. warning:: This class cannot be instanciated.

.. py:class:: sctp_initmsg(*, sinit_num_ostreams=0, sinit_max_instreams=0, \
	      sinit_max_attempts=0, sinit_max_init_timeo=0)

   :bases: :py:class:`~sctp.sctp_generic`

   See :py:data:`~_sctp.sctp.SCTP_INITMSG` socket option.

.. py:class:: sctp_paddrparams(*, spp_assoc_id=0, \
	      spp_address=bytes(SOCKADDR_STORAGE_CSIZE), \
	      spp_hbinterval=0, spp_pathmaxrxt=0, spp_pathmtu=0, \
	      spp_flags=0, spp_ipv6_flowlabel=0, spp_dscp=0)

   :bases: :py:class:`~sctp.sctp_generic`

   See :py:data:`~_sctp.sctp.SCTP_PEER_ADDR_PARAMS` socket option.

.. py:class:: sctp_paddrinfo(*, spinfo_assoc_id=0, \
	      spinfo_address=bytes(SOCKADDR_STORAGE_CSIZE), \
	      spinfo_state=0, spinfo_cwnd=0, spinfo_srtt=0, \
              spinfo_rto=0, spinfo_mtu=0)

   :bases: :py:class:`~sctp.sctp_generic`

   See :py:data:`~_sctp.sctp.SCTP_GET_PEER_ADDR_INFO` socket option.

.. py:class:: sctp_rtoinfo(*, srto_assoc_id=0, srto_initial=0, \
	      srto_max=0, srto_min=0)

   :bases: :py:class:`~sctp.sctp_generic`

   See :py:data:`~_sctp.sctp.SCTP_RTOINFO` socket option.

.. py:class:: sctp_assocparams(*, sasoc_assoc_id=0, sasoc_asocmaxrxt=0, \
              sasoc_number_peer_destinations=0, sasoc_peer_rwnd=0, \
              sasoc_local_rwnd=0, sasoc_cookie_life=0)

   :bases: :py:class:`~sctp.sctp_generic`

   See :py:data:`~_sctp.sctp.SCTP_ASSOCINFO` socket option.

.. py:class:: sctp_setprim(*, ssp_assoc_id=0, \
	      ssp_addr=bytes(SOCKADDR_STORAGE_CSIZE))

   :bases: :py:class:`~sctp.sctp_generic`

   See :py:data:`~_sctp.sctp.SCTP_PRIMARY_ADDR` socket option.

.. py:class:: sctp_setadaptation(*, ssb_adaptation_ind=0)

   :bases: :py:class:`~sctp.sctp_generic`

   See :py:data:`~_sctp.sctp.SCTP_ADAPTATION_LAYER` socket option.

.. py:class:: sctp_assoc_value(*, assoc_id=0, assoc_value=0)

   :bases: :py:class:`~sctp.sctp_generic`

   See :py:data:`~_sctp.sctp.SCTP_MAXSEG`,
   :py:data:`~_sctp.sctp.SCTP_MAX_BURST`,
   :py:data:`~_sctp.sctp.SCTP_CONTEXT` socket options.

.. py:class:: sctp_sack_info(*, sack_assoc_id=0, sack_delay=0, \
              sack_freq=0)

   :bases: :py:class:`~sctp.sctp_generic`

   See :py:data:`~_sctp.sctp.SCTP_DELAYED_SACK` socket option.

.. py:class:: sctp_authkeyid(*, scact_assoc_id=0, scact_keynumber)

   :bases: :py:class:`~sctp.sctp_generic`

   See :py:data: :py:data:`~_sctp.sctp.SCTP_AUTH_ACTIVE_KEY` socket option.

.. py:class:: sctp_default_prinfo(*, pr_policy=SCTP_PR_SCTP_NONE, \
              pr_value=0, pr_assoc_id=0)

   :bases: :py:class:`~sctp.sctp_generic`

   See :py:data:`~_sctp.sctp.SCTP_DEFAULT_PRINFO` socket option.

.. py:class:: sctp_status(*, sstat_assoc_id=0, sstat_state=0, sstat_rwnd=0, \
              sstat_unackdata=0, sstat_penddata=0, sstat_instrms=0, \
              sstat_outstrms=0, sstat_fragmentation_point=0, \
              sstat_primary=bytes(sctp_paddrinfo.size))

   :bases: :py:class:`~sctp.sctp_generic`

   See :py:data:`~_sctp.sctp.SCTP_STATUS` socket option.

.. py:class:: sctp_setpeerprim(*, sspp_assoc_id=0, \
	      sspp_addr=bytes(SOCKADDR_STORAGE_CSIZE))

   :bases: :py:class:`~sctp.sctp_generic`

   See :py:data:`~_sctp.sctp.SCTP_SET_PEER_PRIMARY_ADDR` socket option.

.. py:class:: sctp_authchunk(*, sauth_chunk=ChunkTypes.DATA.value)

   :bases: :py:class:`~sctp.sctp_generic`

   See :py:data:`~_sctp.sctp.SCTP_AUTH_CHUNK` socket option.

.. py:class:: sctp_authkey(*, sca_assoc_id=0, sca_keynumber=0, \
	      sca_key=None)

   :bases: :py:class:`dict`

   See :py:data:`~_sctp.sctp.SCTP_AUTH_KEY` socket option.

.. py:class:: sctp_event(*, se_assoc_id=0, se_type=0, se_on=0)

   :bases: :py:class:`~sctp.sctp_generic`

   See :py:data:`~_sctp.sctp_event.SCTP_EVENT` socket option.

.. py:class:: sctp_socket(family, type, proto=IPPROTO_SCTP)

   :bases: :py:class:`_sctp.sctp.sctp_socket`

   .. py:method:: getsockopt(level, optname, optval=None)

      :param int level: option level (e.g.,
                        :py:data:`~_sctp.sctp.IPPROTO_SCTP`)
      :param int optname: option name (e.g.,
			  :py:data:`~_sctp.sctp.SCTP_GET_PEER_ADDR_INFO`)
      :param optval:
      :type optval: :Py:`None`, :py:class:`int` or object inherited from
                    :py:class:`~sctp.sctp_generic`
      :returns: a :py:class:`int` object, a :py:class:`bytes` object, a
		:py:class:`tuple` object or an object inherited from
		:py:class:`~sctp.sctp_generic`
      :raises TypeError, OSError:

      .. note:: When **optname** is not :Py:`IPPROTO_SCTP`,
                :Py:`getsockopt()` behaves exactly like method
                :py:meth:`~socket.socket.getsockopt()` of the standard Python
                object :py:class:`~socket.socket`.

      Some examples when **level** is :Py:`IPPROTO_SCTP`:

      .. code-block:: Python

	 >>> sock = sctp_socket(AF_INET, SOCK_SEQPACKET)
	 >>> sock.connect(('localhost', 2000))
	 >>> spinfo = sctp_paddrinfo(spinfo_address=(('localhost', 20000)))
	 >>> print(s.getsockopt(IPPROTO_SCTP, SCTP_GET_PEER_ADDR_INFO, spinfo))
	 {'spinfo_assoc_id': 29, 'spinfo_address': ('127.0.0.1', 20000),
	  'spinfo_state': 2, 'spinfo_cwnd': 131064, 'spinfo_srtt': 0,
	  'spinfo_rto': 3000, 'spinfo_mtu': 65532}

      .. code-block:: Python

	 >>> sock = sctp_socket(AF_INET, SOCK_STREAM)
	 >>> print(sock.getsockopt(IPPROTO_SCTP, SCTP_INITMSG))
	 {'sinit_num_ostreams': 10, 'sinit_max_instreams': 65535,
	  'sinit_max_attempts': 8, 'sinit_max_init_timeo': 60000}

      .. code-block:: Python

	  >>> sock = sctp_socket(AF_INET, SOCK_STREAM)
	  >>> id = sock.sctp_connectx((('localhost', 20000),), assoc_id=True)
	  >>> print(sock.getsockopt(IPPROTO_SCTP, SCTP_PEER_AUTH_CHUNKS, id))
	  {'gauth_assoc_id': 3, 'gauth_chunks': (128, 193)}

   .. py:method:: setsockopt(level, optname, *values)

      :param int level: option level (e.g.,
                        :py:data:`~_sctp.sctp.IPPROTO_SCTP`)
      :param int optname: option name (e.g.,
			  :py:data:`~_sctp.sctp.SCTP_PEER_ADDR_PARAMS`)
      :param values: the same values as those required by method
		     :py:meth:`~socket.socket.setsockopt()` of the
		     standard Python object :py:class:`~socket.socket`
		     or an object inherited from
                     :py:class:`~sctp.sctp_generic`
      :returns: :Py:`None`
      :raises TypeError, OSError:

      .. note:: When **optname** is not :Py:`IPPROTO_SCTP`,
                :Py:`setsockopt()` behaves exactly like method
                :py:meth:`~socket.socket.setsockopt()` of the standard Python
                object :py:class:`~socket.socket`.
      
      An example showing how to change the number of output streams
      during initialization:

      .. code-block:: Python

	 >>> sock = sctp_socket(AF_INET, SOCK_STREAM)
	 >>> sinit = sock.getsockopt(IPPROTO_SCTP, SCTP_INITMSG)
	 >>> print(sinit['sinit_num_ostreams'])
	 10
	 >>> sinit['sinit_num_ostreams'] = 100
	 >>> sock.setsockopt(IPPROTO_SCTP, SCTP_INITMSG, sinit)

   Some specific socket options
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   * :py:data:`~_sctp.sctp.SCTP_FRAGMENT_INTERLEAVE`

     Last argument of :Py:`setsockopt()` must be :Py:`0`, :Py:`1` or
     :Py:`2`.

   * :py:data:`~_sctp.sctp.SCTP_HMAC_IDENT`

     To set this option: :Py:`setsockopt(IPPROTO_SCTP,
     SCTP_HMAC_IDENT, ids)` where :Py:`ids` is a tuple of HMAC
     identifiers. For example:

     .. code-block:: Python

	>>> setsockopt(IPPROTO_SCTP, SCTP_HMAC_IDENT,
	               (SCTP_AUTH_HMAC_ID_SHA256, SCTP_AUTH_HMAC_ID_SHA1))

     .. warning:: Algorithm
                  :py:data:`~_sctp.sctp.SCTP_AUTH_HMAC_ID_SHA1` is
                  mandatory, otherwise :py:exc:`ValueError` is raised.

     To get the list of supported HMAC identifiers:

     .. code-block:: Python

	>>> print(getsockopt(IPPROTO_SCTP, SCTP_HMAC_IDENT))
	(3, 1)

   * :py:data:`~_sctp.sctp.SCTP_PEER_AUTH_CHUNKS`,
     :py:data:`~_sctp.sctp.SCTP_LOCAL_AUTH_CHUNKS`

     Both options can take an *association identifier* as an optional
     parameter:

     .. code-block:: Python

	>>> sock = sctp_socket(AF_INET, SOCK_STREAM, IPPROTO_SCTP)
	>>> id = sock.sctp_connectx((('localhost', 20000),), assoc_id=True)
	>>> print(sock.getsockopt(IPPROTO_SCTP, SCTP_PEER_AUTH_CHUNKS, id))
	{'gauth_assoc_id': 3, 'gauth_chunks': (128, 193)}

   * :py:data:`~_sctp.sctp.SCTP_AUTH_CHUNK`

     This (write-only) option takes a member of :py:class:`ChunkTypes`
     as argument:

     .. code-block:: Python

	>>> sauth = sctp_authchunk(sauth_chunk=ChunkTypes.COOKIE_ACK)
	>>> sock.setsockopt(IPPROTO_SCTP, SCTP_AUTH_CHUNK, sauth)

     .. warning:: Chunk types :py:data:`INIT`, :py:data:`INIT_ACK`,
                  :py:data:`SHUTDOWN_COMPLETE` and :py:data:`AUTH`,
                  are not allowed, otherwise :py:exc:`ValueError` is
                  raised.

   * :py:data:`~_sctp.sctp.SCTP_AUTH_KEY`

     This option will set a shared secret key as follows:

     .. code-block:: Python

	>>> sca = sctp_authkey(sca_keynumber=13, sca_key=b'some secret')
	>>> sock.setsockopt(IPPROTO_SCTP, SCTP_AUTH_KEY, sca)

     To disable and then remove this shared secret key:

     .. code-block:: Python

	>>> scact = sctp_authkeyid(scact_keynumber=13)
	>>> sock.setsockopt(IPPROTO_SCTP, SCTP_AUTH_DEACTIVATE_KEY, scact)
	>>> sock.setsockopt(IPPROTO_SCTP, SCTP_AUTH_DELETE_KEY, scact)

   .. py:method:: sctp_opt_info([id], optname, optval)

      :param int id: association identifier, default is 0 (ignored if
                     socket is a *one-to-one* socket)
      :param int optname: option name (e.g.,
			  :py:data:`~_sctp.sctp.SCTP_ASSOCINFO`)
      :param optval: an object inherited from
		     :py:class:`~sctp.sctp_generic` (e.g.,
		     :py:class:`~sctp.sctp_assocparams`)
      :returns: a :py:class:`int` object, a :py:class:`bytes` object,
		a :py:class:`tuple` object or an object inherited from
		:py:class:`~sctp.sctp_generic`
      :raises TypeError, ValueError, OSError:

      The **optval** parameter must have a field whose name ends with
      :Py:`'assoc_id'`, such as :Py:`'srto_assoc_id'`, otherwise
      :py:exc:`ValueError` is raised. The value of **id** is then
      assigned to this field before calling
      :Py:`getsockopt(IPPROTO_SCTP, optname, optval)`.

      An example with *one-to-one* socket:

      .. code-block:: Python

	 >>> sock = sctp_socket(AF_INET, SOCK_STREAM)
	 >>> sock.sctp_connectx((('localhost', 20000),))
	 >>> optval = sctp_assoc_value()
	 >>> opt = sctp_opt_info(SCTP_MAXSEG, optval)
	 >>> print(opt)
	 {'assoc_id': 0, 'assoc_value': 65484}

      Another one with *one-to-many* socket:

      .. code-block:: Python

	 >>> sock = sctp_socket(AF_INET, SOCK_SEQPACKET)
	 >>> sock.sctp_connectx((('localhost', 20000),))
	 >>> optval = sctp_status()
	 >>> opt = sctp_opt_info(SCTP_STATUS, optval)
	 ...
	 OSError: sctp_socket._getsockopt(): [22, Invalid argument]
	 # parameter `id' is required for one-to-many sockets

	 >>> id = sock.sctp_connectx((('localhost', 20000),), assoc_id=True)
	 >>> optval = sctp_status()
	 >>> opt = sctp_opt_info(id, SCTP_STATUS, optval)
	     #                   ^^
	     #	        required parameter id
	 >>> print(opt)
	 {'sstat_assoc_id': 321, 'sstat_state': 4, 'sstat_rwnd': 106496,
	  'sstat_unackdata': 0, 'sstat_penddata': 0, 'sstat_instrms': 2,
	  'sstat_outstrms': 10, 'sstat_fragmentation_point': 65484,
	  'sstat_primary': {'spinfo_assoc_id': 321, 'spinfo_address':
	                    ('127.0.0.1', 20000), 'spinfo_state': 2,
			    'spinfo_cwnd': 131064, 'spinfo_srtt': 0,
			    'spinfo_rto': 3000, 'spinfo_mtu': 65532}}

      .. note:: In fact, if the :Py:`'assoc_id'` field of **optval**
		is named :Py:`'field_assoc_id'` for example,
		:Py:`sctp_opt_info(id, optname, optval)` is equivalent
		to: :Py:`optval['field_assoc_id'] = id;`
		:Py:`getsockopt(IPPROTO_SCTP, optname, optval)`.


Some useful objects
^^^^^^^^^^^^^^^^^^^

.. py:class:: ChunkTypes
   
   :bases: :py:class:`enum.IntEnum`

   .. py:data:: DATA, INIT, INIT_ACK, SACK, HEARTBEAT, HEARTBEAT_ACK,
    ABORT, SHUTDOWN, SHUTDOWN_ACK, ERROR, COOKIE_ECHO, COOKIE_ACK,
    SHUTDOWN_COMPLETE, AUTH

   .. py:method:: name(type)
      
      :classmethod:
      :param int type: chunk type as an integer in range [0-255] (see
		       `RFC 4960 -- section-3.2 <rfc4960chty_>`__)
      :Returns: the plain name of the chunk type (e.g.,
                :Py:`ChunkTypes.name(11)` returns :Py:`'COOKIE_ACK'`)
      :raises TypeError: if **type** is not an integer in range [0-255]

.. _rfc4960chty: https://datatracker.ietf.org/doc/html/rfc4960#section-3.2

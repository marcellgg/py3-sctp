Module _sctp.sctp_info
======================

.. module:: _sctp.sctp_info

Excepted for classes :py:class:`sctp_sendv_spa` and
:py:class:`sctp_recvv_rn`, all objects defined in this module inherit
from the Python :py:class:`dict` object.

Objects
-------

.. py:class:: sctp_sndinfo(*, snd_sid=0, snd_flags=0, snd_ppid=0, \
	      snd_context=0, snd_assoc_id=0)

   :param snd_sid: :C:`uint16_t`
   :param snd_flags: :C:`uint16_t`
   :param snd_ppid: :C:`uint32_t`
   :param snd_context: :C:`uint32_t`
   :param snd_assoc_id: :C:`int32_t`

   Python wrapper for :C:`struct sctp_sndinfo` defined in `RFC 6458 --
   section-5.3.4 <rfc6458sndinfo_>`__.

.. py:class:: sctp_prinfo(*, pr_policy=SCTP_PR_SCTP_NONE, pr_value=0)

   :param pr_policy: must be :Py:`SCTP_PR_SCTP_NONE` or
		     :Py:`SCTP_PR_SCTP_TTL`
   :param pr_value: :C:`uint32_t`

   Python wrapper for :C:`struct sctp_prinfo` defined in `RFC 6458 --
   section-5.3.7 <rfc6458prinfo_>`__.

   .. note:: Parameter :Py:`pr_value` is ignored when :Py:`pr_policy`
      is :Py:`SCTP_PR_SCTP_NONE`.

.. py:class:: sctp_authinfo(*, auth_keynumber=0)

   :param auth_keynumber: :C:`uint16_t`

   Python wrapper for :C:`struct sctp_authinfo` defined in `RFC 6458 --
   section-5.3.8 <rfc6458authinfo_>`__.

.. py:class:: sctp_sendv_spa(infos)

   :param infos: an iterable of :Py:`sctp_[snd|pr|auth]info`
                 objects. Only one type of object is permitted at a
                 time. Therefore, no more than three objects are
                 accepted.

   Python wrapper for :C:`struct sctp_sendv_spa` defined in `RFC 6458 --
   section-9.12 <rfc6458sendvspa_>`__.

   :py:class:`sctp_sendv_spa` object has 3 readable/writable attributes:
   
   * .. py:attribute:: sndinfo

        a :py:class:`sctp_sndinfo` object or :Py:`None`

   * .. py:attribute:: prinfo

        a :py:class:`sctp_prinfo` object or :Py:`None`
	
   * .. py:attribute:: authinfo

        a :py:class:`sctp_authinfo` object or :Py:`None`
   
.. code-block:: python
   :caption: **Some examples of how these objects can be used**
   
   >>> si = sctp_sndinfo(snd_sid=1)
   >>> sp = sctp_prinfo()
   >>> spa = sctp_sendv_spa((si, sp))
   >>> print(spa)
   {'sndinfo': {'snd_sid': 1, 'snd_flags': 0, 'snd_ppid': 0, 'snd_context': 0,
    'snd_assoc_id': 0}, 'prinfo': {'pr_policy': 0, 'pr_value': 0}, 'authinfo': None}
   >>> spa.sndinfo = None
   >>> spa.authinfo = sctp_authinfo(auth_keynumber=1234)
   >>> print(spa)
   {'sndinfo': None, 'prinfo': {'pr_policy': 0, 'pr_value': 0}, 'authinfo':
    {'auth_keynumber': 1234}}

.. py:class:: sctp_rcvinfo(*, rcv_sid=0, rcv_ssn=0, rcv_flags=0, rcv_ppid=0,\
	      rcv_tsn=0, rcv_cumtsn=0, rcv_context=0, rcv_assoc_id=0)

   :param rcv_sid: :C:`uint16_t`
   :param rcv_ssn: :C:`uint16_t`
   :param rcv_flags: :C:`uint16_t`
   :param rcv_ppid: :C:`uint32_t`
   :param rcv_tsn: :C:`uint32_t`
   :param rcv_cumtsn: :C:`uint32_t`
   :param rcv_context: :C:`uint32_t`
   :param rcv_assoc_id: :C:`int32_t`

   Python wrapper for :C:`struct sctp_rcvinfo` defined in `RFC 6458 --
   section-5.3.5 <rfc6458rcvinfo_>`__.

.. py:class:: sctp_nxtinfo(*, nxt_sid=0, nxt_flags=0, nxt_ppid=0,\
	      nxt_length=0, nxt_assoc_id=0)

   :param nxt_sid: :C:`uint16_t`
   :param nxt_flags: :C:`uint16_t`
   :param nxt_ppid: :C:`uint32_t`
   :param nxt_length: :C:`uint32_t`
   :param nxt_assoc_id: :C:`int32_t`

   Python wrapper for :C:`struct sctp_nxtinfo` defined in `RFC 6458 --
   section-5.3.6 <rfc6458nxtinfo_>`__.

.. py:class:: sctp_recvv_rn(infos)

   :param infos: an iterable of :Py:`sctp_[rcv|nxt]info`
                 objects. Only one type of object is permitted at a
                 time. Therefore, no more than two objects are
                 accepted.

   Python wrapper for :C:`struct sctp_recvv_rn` defined in `RFC 6458 --
   section-9.13 <rfc6458recvvrn_>`__.

   :py:class:`sctp_recvv_rn` object has 2 readable/writable attributes:
   
   * .. py:attribute:: rcvinfo
     
        a :py:class:`sctp_rcvinfo` object or :Py:`None`

   * .. py:attribute:: nxtinfo

        a :py:class:`sctp_nxtinfo` object or :Py:`None`

Constants
---------
This module export the following constants:

.. py:data:: SCTP_UNORDERED
.. py:data:: SCTP_ADDR_OVER
.. py:data:: SCTP_ABORT
.. py:data:: SCTP_EOF
.. py:data:: SCTP_SENDALL
.. py:data:: SCTP_SEND_SNDINFO_VALID
.. py:data:: SCTP_SEND_PRINFO_VALID
.. py:data:: SCTP_SEND_AUTHINFO_VALID
.. py:data:: SCTP_PR_SCTP_NONE
.. py:data:: SCTP_PR_SCTP_TTL
.. py:data:: SCTP_NOTIFICATION
   
.. _rfc6458sndinfo: https://datatracker.ietf.org/doc/html/rfc6458#section-5.3.4
.. _rfc6458prinfo: https://datatracker.ietf.org/doc/html/rfc6458#section-5.3.7
.. _rfc6458authinfo: https://datatracker.ietf.org/doc/html/rfc6458#section-5.3.8
.. _rfc6458sendvspa: https://datatracker.ietf.org/doc/html/rfc6458#section-9.12
.. _rfc6458rcvinfo: https://datatracker.ietf.org/doc/html/rfc6458#section-5.3.5
.. _rfc6458nxtinfo: https://datatracker.ietf.org/doc/html/rfc6458#section-5.3.6
.. _rfc6458recvvrn: https://datatracker.ietf.org/doc/html/rfc6458#section-9.13

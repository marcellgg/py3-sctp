Module _sctp.sctp_event
=======================

.. module:: _sctp.sctp_event

Functions
---------

.. py:function:: parse_notification(notif)

   :param bytes notif:
   :returns: **notif** as a dictionary
   :raises OSError TypeError:

   Let's look at an example of how to use this function. First, you
   must subscribe to the desired notification, let's say
   :py:data:`SCTP_SENDER_DRY_EVENT`:

   .. code-block:: Python

      >>> sock = sctp_socket(AF_INET6, SOCK_SEQPACKET)
      ...
      >>> event = sctp_event(se_assoc_id=3, se_type=SCTP_SENDER_DRY_EVENT, se_on=1)
      >>> sock.setsockopt(IPPROTO_SCTP, SCTP_EVENT, event)

   Then, when receiving data:

   .. code-block:: Python

      >>> data, addr, info, infotype, flags = sock.sctp_recvv(1024)
      >>> if flags & MSG_NOTIFICATION: print(parse_notification(data))
      {'sn_type': 32777, 'sender_dry_flags': 0, 'sender_dry_assoc_id': 3}

   .. note:: If you have subscribed to multiple notifications,
      discrimination will be based on the :Py:`'sn_type'` field,
      common to all notifications. In the example above, the field
      indicating the type is named :Py:`'sn_type'` and not
      :Py:`'sender_dry_type'`. The same applies to all other
      notifications:

      .. code-block:: Python

	 >>> notif = parse_notification(data)
	 >>> if notif['sn_type'] == SCTP_SENDER_DRY_EVENT:
	 ........ # do something
         >>> elif notif['sn_type'] == SCTP_ASSOC_CHANGE:
	 ........ # do something else

Constants
---------
This module export the following constants:

.. py:data:: MSG_NOTIFICATION

SCTP Socket Options
^^^^^^^^^^^^^^^^^^^

SCTP_EVENT Option (see `RFC 6458 -- section-6.6.2 <rfc6458evo_>`__):

.. py:data:: SCTP_EVENT

Notifications
^^^^^^^^^^^^^

SCTP_ASSOC_CHANGE (see `RFC 6458 -- section-6.1.1 <rfc6458ach_>`__):

* .. py:data:: SCTP_ASSOC_CHANGE

  The keys in the dictionary returned by the function
  :py:func:`parse_notification` are: :Py:`'sn_type'`,
  :Py:`'sac_flags'`, :Py:`'sac_state'`, :Py:`'sac_error'`,
  :Py:`'sac_outbound_streams'`, :Py:`'sac_inbound_streams'`,
  :Py:`'sac_assoc_id'`.

  :Py:`'sac_state'`:
      
  * .. py:data:: SCTP_COMM_UP
  * .. py:data:: SCTP_COMM_LOST
  * .. py:data:: SCTP_RESTART
  * .. py:data:: SCTP_SHUTDOWN_COMP
  * .. py:data:: SCTP_CANT_STR_ASSOC

  The :Py:`'sac_info'` key may be present in the following two cases:

  #. If :Py:`'sac_state'` is :py:data:`SCTP_COMM_LOST` and an ABORT
     chunk was received for this association, :Py:`'sac_info'`
     contains the complete ABORT chunk as a :py:class:`bytes` object.

  #. If :Py:`'sac_state'` is :py:data:`SCTP_COMM_UP` or
     :py:data:`SCTP_RESTART`, :Py:`'sac_info'` is a :py:class:`tuple` of
     integers in range [0-255] (:C:`uint8_t`). These integers can have the
     following values:

     * .. py:data:: SCTP_ASSOC_SUPPORTS_PR
     * .. py:data:: SCTP_ASSOC_SUPPORTS_AUTH
     * .. py:data:: SCTP_ASSOC_SUPPORTS_ASCONF
     * .. py:data:: SCTP_ASSOC_SUPPORTS_MULTIBUF

     .. warning:: Previous constants are only defined in *FreeBSD* not
                  in *Linux*.

SCTP_PEER_ADDR_CHANGE (see `RFC 6458 -- section-6.1.2 <rfc6458pach_>`__):

* .. py:data:: SCTP_PEER_ADDR_CHANGE

  The keys in the dictionary returned by the function
  :py:func:`parse_notification` are: :Py:`'sn_type'`,
  :Py:`'spc_flags'`, :Py:`'spc_aaddr'`, :Py:`'spc_state'`,
  :Py:`'spc_error'` and :Py:`'spc_assoc_id'`.

  :Py:`'spc_state'`:

  * .. py:data:: SCTP_ADDR_AVAILABLE
  * .. py:data:: SCTP_ADDR_UNREACHABLE
  * .. py:data:: SCTP_ADDR_REMOVED
  * .. py:data:: SCTP_ADDR_ADDED
  * .. py:data:: SCTP_ADDR_MADE_PRIM

SCTP_REMOTE_ERROR (see `RFC 6458 -- section-6.1.3 <rfc6458rerr_>`__):

* .. py:data:: SCTP_REMOTE_ERROR

  The keys in the dictionary returned by the function
  :py:func:`parse_notification` are: :Py:`'sn_type'`,
  :Py:`'sre_flags'`, :Py:`'sre_error'` and :Py:`'sre_assoc_id'`.

  .. note:: :Py:`'sre_error'` is in host byte order.

SCTP_SHUTDOWN_EVENT (see `RFC 6458 -- section-6.1.5 <rfc6458shev_>`__):

* .. py:data:: SCTP_SHUTDOWN_EVENT

  The keys in the dictionary returned by the function
  :py:func:`parse_notification` are: :Py:`'sn_type'`,
  :Py:`'sse_flags'` and :Py:`'sse_assoc_id'`.

SCTP_ADAPTATION_INDICATION (see `RFC 6458 -- section-6.1.6 <rfc6458sai_>`__):

* .. py:data:: SCTP_ADAPTATION_INDICATION

  The keys in the dictionary returned by the function
  :py:func:`parse_notification` are: :Py:`'sn_type'`,
  :Py:`'sai_flags'`, :Py:`'sai_adaptation_ind'` and
  :Py:`'sre_assoc_id'`.

SCTP_PARTIAL_DELIVERY_EVENT (see `RFC 6458 -- section-6.1.7 <rfc6458pdapi_>`__):

* .. py:data:: SCTP_PARTIAL_DELIVERY_EVENT

  The keys in the dictionary returned by the function
  :py:func:`parse_notification` are: :Py:`'sn_type'`,
  :Py:`'pdapi_flags'`, :Py:`'pdapi_indication'`, :Py:`'pdapi_stream'`,
  :Py:`'pdapi_seq'` and :Py:`'pdapi_assoc_id'`.

  :Py:`'pdapi_indication'`:

      * .. py:data:: SCTP_PARTIAL_DELIVERY_ABORTED

SCTP_AUTHENTICATION_EVENT (see `RFC 6458 -- section-6.1.8 <rfc6458authe_>`__):

* .. py:data:: SCTP_AUTHENTICATION_EVENT

  The keys in the dictionary returned by the function
  :py:func:`parse_notification` are: :Py:`'sn_type'`,
  :Py:`'auth_flags'`, :Py:`'auth_keynumber'`, :Py:`'auth_indication'`
  and :Py:`'auth_assoc_id'`.

  :Py:`'auth_indication'`:

      * .. py:data:: SCTP_AUTH_NEW_KEY
      * .. py:data:: SCTP_AUTH_NO_AUTH
      * .. py:data:: SCTP_AUTH_FREE_KEY

SCTP_SENDER_DRY_EVENT (see `RFC 6458 -- section-6.1.9 <rfc6458ede_>`__):

* .. py:data:: SCTP_SENDER_DRY_EVENT

  The keys in the dictionary returned by the function
  :py:func:`parse_notification` are: :Py:`'sn_type'`,
  :Py:`'sender_dry_flags'` and :Py:`'sender_dry_assoc_id'`.

SCTP_NOTIFICATIONS_STOPPED_EVENT (see `RFC 6458 --
section-6.1.10 <rfc6458nse_>`__):

* .. py:data:: SCTP_NOTIFICATIONS_STOPPED_EVENT

  The keys in the dictionary returned by the function
  :py:func:`parse_notification` are: :Py:`'sn_type'` and
  :Py:`'sn_flags'`.

  .. warning:: Unlike FreeBSD, Linux does not support this
               notification (e.g.,
               :py:data:`SCTP_NOTIFICATIONS_STOPPED_EVENT` is not
               defined).
  
SCTP_SEND_FAILED_EVENT (see `RFC 6458 -- section-6.1.11 <rfc6458sfe_>`__):

* .. py:data:: SCTP_SEND_FAILED_EVENT

  The keys in the dictionary returned by the function
  :py:func:`parse_notification` are: :Py:`'sn_type'` and
  :Py:`'ssfe_flags'`, :Py:`'ssfe_error'`, :Py:`'ssfe_info'`,
  :Py:`'ssfe_assoc_id'` and :Py:`'ssfe_data'`.

  :Py:`'ssfe_flags'`:

      * .. py:data:: SCTP_DATA_UNSENT
      * .. py:data:: SCTP_DATA_SENT

  :Py:`'ssfe_info'` is a :py:class:`~_sctp.sctp_info.sctp_sndinfo`
  object and :Py:`'ssfe_data'` is a :py:class:`bytes` object.

.. _rfc6458ach: https://datatracker.ietf.org/doc/html/rfc6458#section-6.1.1
.. _rfc6458pach: https://datatracker.ietf.org/doc/html/rfc6458#section-6.1.2
.. _rfc6458rerr: https://datatracker.ietf.org/doc/html/rfc6458#section-6.1.3
.. _rfc6458shev: https://datatracker.ietf.org/doc/html/rfc6458#section-6.1.5
.. _rfc6458sai: https://datatracker.ietf.org/doc/html/rfc6458#section-6.1.6
.. _rfc6458pdapi: https://datatracker.ietf.org/doc/html/rfc6458#section-6.1.7
.. _rfc6458authe: https://datatracker.ietf.org/doc/html/rfc6458#section-6.1.8
.. _rfc6458ede: https://datatracker.ietf.org/doc/html/rfc6458#section-6.1.9
.. _rfc6458nse: https://datatracker.ietf.org/doc/html/rfc6458#section-6.1.10
.. _rfc6458sfe: https://datatracker.ietf.org/doc/html/rfc6458#section-6.1.11
.. _rfc6458evo: https://datatracker.ietf.org/doc/html/rfc6458#section-6.2.2


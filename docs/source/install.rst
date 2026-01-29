Installation
============

This Python module is an encapsulation of the SCTP library provided by
*Linux* and *FreeBSD* operating systems (no other systems are
currently supported). Therefore, these libraries must be installed
beforehand.

SCTP library
------------

Linux
^^^^^

On Debian-based Linux systems, you need to install the following
packages:

.. code:: console

   # apt-get install libsctp1 libusrsctp2 libsctp-dev libusrsctp-dev
   # apt-get install lksctp-tools # optional package 

If you want to use the authentication part of the SCTP protocol, you
must configure it:

.. code:: console

   # sysctl -w net.sctp.auth_enable=1 # 0 by default

FreeBSD
^^^^^^^

On FreeBSD system, you need to install the following packages:

.. code:: console

   # pkg install sctplib libusrsctp
   # pkg install tsctp # optional package

On FreeBSD, SCTP authentication is enabled by default:

.. code:: console

   # sysctl net.inet.auth_enable
   net.inet.auth_enable: 1

Module py3-sctp
---------------

The recommended approach is to first create a Python virtual environment:

.. code:: console

   $ python3 -m venv py3-sctp
   $ cd py3-sctp
   $ source bin/activate
   (py3-sctp) $ python3 -m pip install --upgrade pip setuptools wheel

Next, retrieve the py3-sctp module and build it:

.. code:: console

   (py3-sctp) $ python3 -m pip install py3-sctp

To get an insight into how this module works, see :ref:`examples`.

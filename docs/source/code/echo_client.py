from socket import *
from sctp import *
from enum import IntEnum

ADDR = '127.0.0.1'
PORT = 20000
DATA = b'Some data to be echoed'

class Streams(IntEnum):
    IN =  0
    OUT = 1

sock = sctp_socket(AF_INET, SOCK_STREAM)
sock.setsockopt(IPPROTO_SCTP, SCTP_RECVRCVINFO, 1)

info = sctp_sndinfo(snd_sid=Streams.OUT)
sock.sctp_sendv((DATA,), ((ADDR, PORT),), info)

data, addr, info, infotype, flags = sock.sctp_recvv(1024)
if infotype == SCTP_RECVV_RCVINFO and info['rcv_sid'] == Streams.IN:
    print(f'Received from {addr}:\n  {data}')

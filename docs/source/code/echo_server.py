from socket import *
from sctp import *
from enum import IntEnum

ADDR = '0.0.0.0'
PORT = 20000

class Streams(IntEnum):
    IN =  1
    OUT = 0

sock = sctp_socket(AF_INET, SOCK_STREAM)
sock.bind((ADDR, PORT))
sock.listen(1)

while True:
    s, addr = sock.accept()
    s.setsockopt(IPPROTO_SCTP, SCTP_RECVRCVINFO, 1)
    
    data, addr, info, infotype, _ = s.sctp_recvv(1024)
    if infotype == SCTP_RECVV_RCVINFO and info['rcv_sid'] == Streams.IN:
        sndinfo = sctp_sndinfo(snd_sid=Streams.OUT)
        s.sctp_sendv((data,), (addr,), sndinfo)
    s.close()
sock.close()

from socket import *
from sctp import *

PORT = 9
ADDR = '127.0.0.1'
SIZE_OF_MESSAGE = 1000
NUMBER_OF_MESSAGES = 10
PPID = 1234

# Create a one-to-one style SCTP socket.
sd = sctp_socket(AF_INET, SOCK_STREAM)

# Prepare for requesting 2048 outgoing streams.
init = sctp_initmsg(sinit_num_ostreams=2048)
sd.setsockopt(IPPROTO_SCTP, SCTP_INITMSG, init)

ind = sctp_setadaptation(ssb_adaptation_ind=0x01020304)
sd.setsockopt(IPPROTO_SCTP, SCTP_ADAPTATION_LAYER, ind)

# Connect to the discard server.
sd.connect((ADDR, PORT))

# Get the actual number of outgoing streams.
status = sd.getsockopt(IPPROTO_SCTP, SCTP_STATUS, sctp_status())

info = sctp_sndinfo(snd_ppid=htonl(PPID), snd_flags=SCTP_UNORDERED)
buffer = b'A' + bytes(SIZE_OF_MESSAGE - 1)
for i in range(NUMBER_OF_MESSAGES):
    info['snd_sid'] = i % status['sstat_outstrms']
    sd.sctp_sendv((buffer,), None, info)
sd.close()


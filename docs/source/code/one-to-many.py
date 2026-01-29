from socket import *
from sctp import *

BUFFER_SIZE = (1 << 16)
PORT = 9
ADDR = '::'
TIMEOUT = 5
   
def print_notification(buf):
    data = parse_notification(buf)
    if data['sn_type'] == SCTP_ASSOC_CHANGE:
        if data['sac_state'] == SCTP_COMM_UP:
            print(
                "Communication up (streams (in/out)="
                f"({data['sac_inbound_streams']}/"
                f"{data['sac_outbound_streams']}))."
            )
        elif data['sac_state'] == SCTP_COMM_LOST:
            print(f"Communication lost (error={data['sac_error']}).")
        elif data['sac_state'] == SCTP_RESTART:
            print(
                "Communication restarted (streams (in/out)="
                f"({data['sac_inbound_streams']}/"
                f"{data['sac_outbound_streams']}))."
            )
        elif data['sac_state'] == SCTP_SHUTDOWN_COMP:
            print("Communication completed.")
        elif data['sac_state'] == SCTP_CANT_STR_ASSOC:
            print("Communication couldn't be started.")
    elif data['sn_type'] == SCTP_PEER_ADDR_CHANGE:
        print(f"^^^ Peer Address change: {data['spc_aaddr']} ", end='')
        if data['spc_state'] == SCTP_ADDR_AVAILABLE:
            print("is available.")
        elif data['spc_state'] == SCTP_ADDR_UNREACHABLE:
            print(f"is not available (error={data['spc_error']}).")
        elif data['spc_state'] == SCTP_ADDR_REMOVED:
            print("was removed.")
        elif data['spc_state'] == SCTP_ADDR_ADDED:
            print("was added.")
        elif data['spc_state'] == SCTP_ADDR_MADE_PRIM:
            print("is primary.")
    elif data['sn_type'] == SCTP_SHUTDOWN_EVENT:
        print("^^^ Shutdown received.")
    elif data['sn_type'] == SCTP_ADAPTATION_INDICATION:
        print(
            f"^^^ Adaptation indication {data['sai_adaptation_ind']:08x}"
              " received."
        )

def main():
    event_types = (
        SCTP_ASSOC_CHANGE,
        SCTP_PEER_ADDR_CHANGE,
        SCTP_SHUTDOWN_EVENT,
        SCTP_ADAPTATION_INDICATION
        )
    sd = sctp_socket(AF_INET6, SOCK_SEQPACKET)
    event = sctp_event(se_assoc_id=SCTP_FUTURE_ASSOC, se_on=1)
    for e in event_types:
        event['se_type'] = e
        sd.setsockopt(IPPROTO_SCTP, SCTP_EVENT, event)
    sd.setsockopt(IPPROTO_SCTP, SCTP_AUTOCLOSE, TIMEOUT)
    sd.setsockopt(IPPROTO_SCTP, SCTP_RECVRCVINFO, 1)
    sd.bind((ADDR, PORT))
    sd.listen(1)
    while True:
        data, addr, info, infotype, flags = sd.sctp_recvv(BUFFER_SIZE)
        if flags & MSG_NOTIFICATION:
            print_notification(data)
        else:
            print(
                f"Message received from {addr[0]}:{addr[1]}: "
                f"len={len(data)}", end=''
            )
            if infotype == SCTP_RECVV_RCVINFO:
                print(f", sid={info['rcv_sid']}")
                if (info['rcv_flags'] & SCTP_UNORDERED):
                    print(", unordered", end='')
                else: 
                    print(f", ssn={info['rcv_ssn']}", end='')
                print(f", tsn={info['rcv_tsn']}", end='')
                print(f", ppid={ntohl(info['rcv_ppid'])}.")
            elif infotype in (
                    SCTP_RECVV_NOINFO, SCTP_RECVV_NXTINFO, SCTP_RECVV_RN):
                print(".")
    sd.close()
    
if __name__ == '__main__':
    main()
    

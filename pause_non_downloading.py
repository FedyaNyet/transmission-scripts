#!/Users/fwolf/Code/transmission/venv/bin/python

import transmissionrpc
from transmissionrpc.error import TransmissionError


def main():
    try:
        tc = transmissionrpc.Client('localhost', port=9091)
        for torrent in tc.get_torrents():
            if torrent.status != "downloading":
                torrent.stop()
    except TransmissionError:
        pass

if __name__ == "__main__":
    main()

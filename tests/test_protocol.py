import pytest
import io
import sys
sys.path.insert(1, './dvic_chat')
from protocol import DataStream, Packet1Auth, Packet2Message

class Focket:
    def __init__(self) -> None:
        self.buffer = io.BytesIO()
        
    def send(self, data: bytes):
        self.buffer.write(data)
        
    def recv(self, size: int):
        self.buffer.seek(0)
        return self.buffer.read(size)

def test_datastream_receive_int():
    fs = Focket()
    fs.send(b'\x00\x00\x00\x01')
    d = DataStream(fs)
    assert d.receive_int() == 1

def test_datastream_send_int():
    fs = Focket()
    d = DataStream(fs)
    d.send_int(1)
    assert fs.recv(4) == b'\x00\x00\x00\x01'
    
if __name__ == '__main__':
    pytest.main()
    
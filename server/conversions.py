import struct

# These conversions from https://stackoverflow.com/questions/21017698/converting-int-to-bytes-in-python-3
def int_to_bytes(x: int) -> bytes:
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')
    
def int_from_bytes(xbytes: bytes) -> int:
    return int.from_bytes(xbytes, 'big')

# def float_to_bytes(f: float) -> bytes:
#     return struct.unpack('f', )

# https://stackoverflow.com/questions/5415/convert-bytes-to-floating-point-numbers
def float_to_bytes(f: float) -> bytes:
    return struct.pack('f', f)

def float_from_bytes(fbytes: bytes) -> float:
    return struct.unpack('f', fbytes)
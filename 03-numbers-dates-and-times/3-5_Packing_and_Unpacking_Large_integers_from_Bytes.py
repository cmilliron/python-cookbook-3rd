'''
3.5. Packing and Unpacking Large Integers from Bytes
Problem
You have a byte string and you need to unpack it into an integer value. Alternatively, you need to convert a large integer back into a byte string.

Solution
Suppose your program needs to work with a 16-element byte string that holds a 128-bit integer value.
'''

data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'

print(len(data))

print(int.from_bytes(data, 'little'))

print(int.from_bytes(data, 'big'))

x = 94522842520747284487117727783387188

print(x.to_bytes(16, 'big'))
print(x.to_bytes(16, 'little'))

import struct

hi, lo = struct.unpack('>QQ', data)
print((hi << 64) + lo)
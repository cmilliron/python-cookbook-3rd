# 

"""
2.20 performing Text Operations on Byte Strings

Problem: You want to preform common text ooperations (e.g., stripping, 
searching, and replacement) on byte strings

Solution:

Byte strings already support most of the same built-in operations as text strings.
"""

data = b"Hello World"

print(data[0:5])

print(data.startswith(b"Hello"))

print(data.split())

print(data.replace(b'Hello', b"hello Cruel"))


# Such operations also work with byte arrays
print("Byte Array section")
data_bytearray = bytearray(b"Hello World")


print(data_bytearray[0:5])

print(data_bytearray.startswith(b"Hello"))

print(data_bytearray.split())

print(data_bytearray.replace(b'Hello', b"hello Cruel"))


"""
You can apply regular expressions patterns matching to byte strings, 
but the patterns themselves need to be speciified as bytes.
"""

data_for_re = b'FOO:BAR,SPAM'
import re

# re.split('[:,]', data_for_re) doesn't work

print(re.split(b"[:,]", data_for_re))
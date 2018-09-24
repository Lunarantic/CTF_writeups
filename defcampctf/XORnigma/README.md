# XORnigma
### (Junior - 1pts)
  
> Obtain the file from given [file](xornigma.py)
------
We are provided a python source code which has generated a encrypted output using a key over a flag

In this challenge we need to reverse the python code and the encryption to receive the flag

First thing first we can see that output is an hexcode; with first 4 bytes as 0

Encryption is simple one XORing each character in flag with key repeating key in cycle till whole flag is encrypted

Having first 4 bytes as 0 means that flag and key has first 4 characters similar

We know that flag has pattern as follows:
```
DCTF{*******...}
```
So our key will have DCTF in start and D will XOR with some character again if length is shorter; even we know 5th and last char in flag the output; all be need to do is check 5th char used against flag to find pattern for key

Hence, lets XOR fifth char with encrypted string's fifth char
```python
>>> chr(ord('3f'.decode('hex'))^ord('{'))
'D'
```
It seems our key's fifth might be repeating let's take *DCTF* as our key; which makes sense
```python
>>> import itertools
>>> def xor_two_str(s, key):
...     key = key * (len(s) / len(key) + 1)
...     return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in itertools.izip(s, key))
...
>>> flag_key = 'DCTF'
>>> x = '000000003f2537257777312725266c24207062777027307574706672217a67747374642577263077777a3725762067747173377326716371272165722122677522746327743e'
>>> xor_two_str(x.decode('hex'), flag_key)
'DCTF{fcc34eaae8bd3614dd30324e932770c3ed139cc2c3250c5b277cb14ea33f77a0}'
```
Ohh, we got the flag there it is

------
Flag: DCTF{fcc34eaae8bd3614dd30324e932770c3ed139cc2c3250c5b277cb14ea33f77a0}

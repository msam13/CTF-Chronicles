from pwn import *

r = remote("mercury.picoctf.net",20266)
r.recvuntil("This is the encrypted flag!\n")
flag = r.recvline()
print(flag)

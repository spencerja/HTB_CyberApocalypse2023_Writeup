#!/usr/bin/env python3

from pwn import *

p = remote('178.62.64.13', 31174)
win = 'rock,paper,scissors'

#Start game 1 and chain
p.sendline('1')

#Looping sendline is too fast, so I wait for interactive marker >>
for i in range(100):
    p.sendlineafter('>>',win)

response = p.recvallS()
print(response)
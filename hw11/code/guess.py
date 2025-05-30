from pwn import *

server = remote('140.112.91.4', 1234)

server.sendlineafter(b'Your choice: ', b'1')
server.sendlineafter(b'Guess a number: ', b'1')
k1 = int(server.recvuntil(b'.').decode().split(' ')[8].rstrip(','))
# print(k1)

server.sendlineafter(b'Your choice: ', b'1')
server.sendlineafter(b'Guess a number: ', b'1')
k2 = int(server.recvuntil(b'.').decode().split(' ')[8].rstrip(','))
# print(k2)

server.sendlineafter(b'Your choice: ', b'1')
server.sendlineafter(b'Guess a number: ', b'1')
k3 = int(server.recvuntil(b'.').decode().split(' ')[8].rstrip(','))
# print(k3)

m = 0xa34d80e56c2cd0d35209cb13e5665fc58176fac6b1fee26af23388deebee59da1a884cbba6111ea819f7a2059f0accd8b1e7e23dbe4d90896b2cd482c0b934d97e3bbdbfd26b968e9bfeb2f8df037cab44557d2cf6eb57385a191c3db536c62f781e598405bdd818ae98dfd7df48c4da55d9d5b49d75aa46c91a27a186b9bf77

a = pow(k1-k2, -1, m) * (k2-k3)
c = (k2-a*k1)%m

cur = k3

for i in range(100):
    server.sendlineafter(b'Your choice: ', b'1')
    cur = (a*cur+c)%m
    server.sendlineafter(b'Guess a number: ', str(cur))

server.sendlineafter(b'Your choice: ', b'2')
flag = server.recvuntil(b'}')
print(flag)
from pwn import *
import hashlib

mp = dict()
for i in range(2**24):
    mp[hashlib.md5(str(i).encode()).hexdigest()[0:8]] = i

server = remote('140.112.91.4', 1234)
server.sendlineafter(b'Your choice: ', b'4')

for i in range(10):
    prefix = server.recvuntil(b': ').decode().split(' ')[7].strip('"').rstrip('"')
    ans = str(mp[prefix])
    server.sendline(ans)

ans1 = server.recvline()
ans2 = server.recvline()
print(ans1.decode(), ans2.decode())
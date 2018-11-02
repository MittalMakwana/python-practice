import sys
import os

bufsize = 8192

lines = 400
fname = "test.ping"
fsize = os.stat(fname).st_size
print(f'this is a file size: {fsize}')
iter = 0
with open(fname) as f:
    if bufsize > fsize:
        bufsize = fsize-1
    print(bufsize)
    data = []
    while True:
        iter +=1
        print(f"seek {fsize-bufsize*iter} , iter: {iter}, f.tell: {f.tell()}, len data: {len(data)}")
        f.seek(fsize-bufsize*iter)
        data.extend(f.readlines())
        print(data)

        if len(data) >= lines or f.tell() == 0:
            print(''.join(data[-lines:]))
            break

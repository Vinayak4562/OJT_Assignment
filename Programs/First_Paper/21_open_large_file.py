with open('password.txt', 'rb') as f:
    out_put = f.read()
    print(out_put)
    chunk_size = 1024 # read 1KB at a time
    while True:
        chunk = f.read(chunk_size)
        if not chunk:
            break
with open('large_file.txt', 'rb') as f:
    chunk_size = 1024 # read 1KB at a time
    while True:
        chunk = f.read(chunk_size)
        if not chunk:
            break
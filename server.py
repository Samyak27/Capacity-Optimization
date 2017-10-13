import pickle
import socket


class foo(object):
    pass

TCP_IP = '0.0.0.0'
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()

print "conn info: ", conn
while True:
    objrcv = pickle.loads ( conn.recv ( 1024 ) )
    print "conn recv: ", objrcv
    print "conn from: ", addr
    if objrcv.Y == 0:
        print 'down count'
        print objrcv.X
        #yahaan se down jaaega
    elif objrcv.Y == -1:
        print "upcount"
        print  objrcv.X
        #yahaan se up jaaega

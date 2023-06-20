import socket,threading
import json

f1=open('D:\\project\\network programming\\homework2\\venv\\quiz .json','r')
d1=json.load(f1)
f1.close()

ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
ss.bind(('127.0.0.1',7777))
ss.listen(5)

def handel_request(i,csocket,cadd):
    print('Accepted new client:',i,cadd)
    print()
    while True:
        d2 = {}
        correctAnswers={}
        score = 0
        for key, val in d1.items():
            csocket.send(key.encode())
            cmsg = csocket.recv(1024).decode()
            x=int(cmsg)
            d2[key] = [x]
            if x == d1[key]:
                score += 1
                correctAnswers[key]=[x]
        if val==400:
            d2["the score is: "] = score
            print(d2)
            print('the correct Answer of client',i,' is: ',correctAnswers)
            s=''
            for key,val in d2.items():
                s+=key
                s+=' '
                s+=str(val)
                s+=' '
            c = ''
            for key, val in correctAnswers.items():
                c += key
                c += ' '
                c += str(val)
                c += ' '
            csocket.send(s.encode())
            csocket.send('the correct Answer'.encode())
            csocket.send(c.encode())
            csocket.close()

i=1
while True:
    print('[+]TCP MultiThreads server waiting for new clients...')
    cs,cadd=ss.accept()
    client=threading.Thread(target=handel_request,args=(i,cs,cadd))
    client.start()
    i+=1

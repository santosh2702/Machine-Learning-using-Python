
# coding: utf-8
# ## CGI programming
# ##  Server

# In[ ]:


import socket
s=socket.socket()
host=socket.gethostname()
port=8000
s.bind((host,port))
print("waiting for connection...........")
s.listen(5)
while True:
    conn,addr=s.accept()
    print('GOT Connection from',addr)
    #conn.send("Server saying hi")
    conn.close()


# ## client

# In[ ]:


import socket
s=socket.socket()
host=socket.gethostname()
port=8000
s.connect((host,port))
print(s.recv(1024).decode())
s.close()


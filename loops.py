for i in range(1,10):
    print(f"Checking Server {i}...")
    
#While Loop
server_up=False
while not server_up:
    print("Waiting for the server to start....")
    server_up = True
print("Serve is Running and Up!")
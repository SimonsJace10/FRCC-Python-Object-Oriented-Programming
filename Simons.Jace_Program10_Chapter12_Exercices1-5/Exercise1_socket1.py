import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

link = input("input a link to scrape data from\n")


try:
    split = link.split('/')
    socket_connect = split[2]

    mysock.connect((socket_connect, 80))

    cmd = ('GET ' + link + ' HTTP/1.0\r\n\r\n').encode()
    mysock.send(cmd)

    print(mysock)

    # while True:
    #     data = mysock.recv(512)
    #     if len(data) < 1:
    #         break
    #     print(data.decode(), end='')
except:
    print("URL entered is either improperly formatted or does not exist.")


mysock.close()

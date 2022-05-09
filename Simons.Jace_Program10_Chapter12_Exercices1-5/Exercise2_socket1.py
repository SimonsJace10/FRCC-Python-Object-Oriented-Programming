import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

link = input("input a link to scrape data from\n")

char_count = 0

try:
    split = link.split('/')
    socket_connect = split[2]

    mysock.connect((socket_connect, 80))

    cmd = ('GET ' + link + ' HTTP/1.0\r\n\r\n').encode()
    mysock.send(cmd)

    while True:
        if char_count >= 3000:
            break
        data = mysock.recv(1)
        if len(data) < 1:
            break
        print(data.decode(), end='')
        char_count += 1

    print(char_count)
except:
    print("URL entered is either improperly formatted or does not exist.")


mysock.close()

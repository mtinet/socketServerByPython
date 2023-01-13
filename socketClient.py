# echo_client.py
#-*- coding:utf-8 -*-

import socket

# 접속 정보 설정
SERVER_IP = '127.0.0.1'
SERVER_PORT = 5050
SIZE = 1024
SERVER_ADDR = (SERVER_IP, SERVER_PORT)

cmd = input("아무거나 입력하셈 : ")

# 클라이언트 소켓 설정
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect(SERVER_ADDR)  # 서버에 접속
    client_socket.send(cmd.encode())  # 서버에 메시지 전송
    msg = client_socket.recv(SIZE)  # 서버로부터 응답받은 메시지 반환
    print("resp from server : {}".format(msg))  # 서버로부터 응답받은 메시지 출력

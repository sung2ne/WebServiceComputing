#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

host = os.getenv('IP', '0.0.0.0')
port = os.getenv('PORT', 80)

# 사용자 목록
user_list = {}

# index
@app.route('/')
def index():
    return render_template('index.html')
    
    
# socketio 연결
@socketio.on('connect', namespace='/')
def on_connect():
    print 'new client connected, socketid:', request.sid
    emit('server, socketid', {'socketid': request.sid})
    
    
# 채팅방 퇴장
@socketio.on('client, disconnect', namespace='/')
def on_disconnect(data):
    name = user_list[data['socketid']]
    del user_list[data['socketid']]
    emit('server, join chat', {'user_list': user_list}, broadcast=True)  
    emit('server, disconnect', {'name': name}, broadcast=True)  
    
    
# 채팅방 입장
@socketio.on('client, join chat', namespace='/')
def join_chat(data):
    user_list[request.sid] = data['name']
    emit('server, join chat', {'user_list': user_list}, broadcast=True)    
    emit('server, new client', {'name': data['name']}, broadcast=True) 
    
    
# 대화 입력
@socketio.on('client, input message', namespace='/')
def join_chat(data):
    print '[' + data['name'] + ', ' + request.sid + '] ' + data['message']
    emit('server, input message', {'name': data['name'], 'message': data['message']}, broadcast=True)
    
    
# main
if __name__ == '__main__':
    socketio.run(app, host, port)

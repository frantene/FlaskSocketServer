from flask import Flask, render_template, session, redirect, request, url_for
from flask_socketio import SocketIO, join_room, leave_room
from utilities.function import generate_code
from datetime import datetime
import uuid


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

rooms: dict = {}
members_names: dict = {}


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/create', methods=['GET', 'POST'])
def form_room_create():
    if request.method == 'POST':
        while True:
            code: str = generate_code(8)
            if code not in rooms:
                directory: str = f'/room/{code}'
                break

        rooms[code] = {
            'RoomName': request.form['room_name'],
            'MembersList': [],
            'MessageHistory': []
        }
        session['Username'] = request.form['username']
        session['UUID'] = str(uuid.uuid4())
        session['Room'] = code
        members_names[session['UUID']] = session['Username']
        print(f'Create: {rooms=}')
        return redirect(directory)

    session['Main'] = []
    return redirect(url_for('main'))


@app.route('/join', methods=['GET', 'POST'])
def form_room_join():
    print("1")
    if request.method == 'POST':
        print(f'Join: {rooms=}')
        print('2')
        code = request.form['room_code']
        if code in rooms.keys():
            print('if')
            session['Username'] = request.form['username']
            session['UUID'] = str(uuid.uuid4())
            session['Room'] = code
            members_names[session['UUID']] = session['Username']
            return redirect(f'/room/{code}')
        else:
            print('else')
            return redirect(url_for('main'))

    return redirect(url_for('main'))


@app.route('/data')
def data():
    return [rooms, members_names]


@app.route('/room/<code>')
def room(code):
    print(f'room code: {rooms=}')
    if session.get('UUID') is None or session.get('Username') is None:
        return redirect(url_for('main'))

    if code in rooms.keys() and session.get('UUID') not in rooms[code].get('MembersList'):
        return render_template("room.html")
    else:
        return redirect(url_for('main'))


@socketio.on('my event')
def handle_message(message):
    user = {
        'Name': message['Name'],
        'UUID': session['UUID'],
        'serverMessage': message['data'],
        'Time': datetime.now().strftime("%b %d, %Y %H:%M:%S"),
    }
    session['Main'].append(user)
    socketio.emit('new_data', user)


@socketio.on('room join')
def room_join(_):
    if rooms.get(session['Room']) is not None:
        rooms[session['Room']]['MembersList'].append(session['UUID'])
        join_room(session['Room'])
        temp_data = {
            'MemberList': [],
            'MessageHistory': []
        }
        for x in rooms[session['Room']]['MembersList']:
            temp_data['MemberList'].append(members_names[x])

        socketio.emit("room name", rooms[session['Room']]['RoomName'], to=session['Room'])


@socketio.on('connect')
def connect():
    print(session['UUID'], "connected")


@socketio.on('disconnect')
def room_leave():
    if session.get('Room') in rooms.keys():
        rooms[session['Room']]['MembersList'].remove(session['UUID'])
        if len(rooms[session['Room']]['MembersList']) == 0:
            del rooms[session['Room']]
        leave_room(session['Room'])


if __name__ == '__main__':
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True, host='0.0.0.0')

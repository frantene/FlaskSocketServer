document.addEventListener("DOMContentLoaded", function() {
    document.getElementById('RoomCode').innerHTML = window.location.pathname.split('/room/')[1];
});

var socket = io();

socket.emit('room join', '');

socket.on('room name', function(data) {
    document.getElementById('RoomName').innerHTML = data;
    console.log(data);
    socket.disconnect();
});


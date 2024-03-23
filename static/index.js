var socket = io();

socket.on('new_data', function(message) {
    document.getElementById('UUID').innerHTML = message['UUID'];
    document.getElementById('serverMessage').innerHTML = message['serverMessage'];
    document.getElementById('Time').innerHTML = message['Time'];
    document.getElementById('Name').innerHTML = message['Name'];

    var table = document.getElementById('history').getElementsByTagName('tbody')[0];
    var newRow = table.insertRow();
    newRow.insertCell(0).innerHTML = message['Name'];
    newRow.insertCell(1).innerHTML = message['serverMessage'];
    newRow.insertCell(2).innerHTML = message['Time'];
});

function sendMessage(){
    if (document.getElementById("Message").value != '' && document.getElementById("firstname").value != '') {
        var message = document.getElementById("Message").value;
        var name = document.getElementById('firstname').value;
        socket.emit('my event', {data: message, 'Name': name});
    }
}

function handleKeyPress(event, choice) {
    if (event.keyCode === 13) {
        switch(choice) {
            case 1:
                sendMessage();
        }
    }
}
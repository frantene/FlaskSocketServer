var socket = io();

socket.emit('room join');

socket.on('member_list', function(members) {
    var member_list = document.getElementById('MemberList');
    member_list.innerHTML = ''
    for (let x in members) {
        member_list.innerHTML += `<li>${members[x]}</li>`;
    }
});

socket.on('message_history', function(messages) {
    var message_history = document.getElementById('Messages');
    console.log(messages);
    for (let x in messages) {
        console.log(messages[x]);
        message_history.innerHTML += `
           <div class="Message-Container">
                <div class="Message-Header">
                    <p class="Message-User">${messages[x]['PlayerName']}</p>
                    <p class="Message-Time">${messages[x]['Time']}</p>
                </div>
                <p class="Message-Message">${messages[x]['Message']}</p>
            </div>
        `;
    }
});

function sendMessage(){
    if (document.getElementById("Message-Input").value != '') {
        var user_message = document.getElementById("Message-Input").value;
        socket.emit('room messages', user_message);
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
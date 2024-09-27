
const code = document.getElementById("code").innerText
const boardElement = document.getElementById('board');
const statusElement = document.getElementById('status');
const winnerElement = document.getElementById('winner')
const socket = new WebSocket(`ws://${window.location.host}/ws/game/${code}/`);


let gameActive = true;
socket.onopen = function() {
console.log("Connected to the game room.");
statusElement.textContent = "Connected to the game!";
statusElement.classList.add('status')
};


socket.onmessage = function(event) {
const data = JSON.parse(event.data);
updateBoard(data.board);
if (data.winner) {
    winnerElement.textContent = `Winner: ${data.winner}`;
    winnerElement.classList.add('winner')
    gameActive = false; 
    statusElement.textContent = "Reseting game in 2 sec"
    statusElement.classList.add('status')
    setTimeout(()=>{
        statusElement.textContent = ''
        socket.send(JSON.stringify({
            action:'reset'
        }))
    },2000)
}else if(data.reset) {
    gameActive = true;
    statusElement.textContent = "Game reset. Start playing!";
}else{
    let counter = 0;
    statusElement.textContent=''
    winnerElement.textContent = ''
    for(let i = 0; i < data.board.length;i++)
    {
        if (data.board[i]!=''){
            counter++
        }

    }
    if(counter == data.board.length)
    {
        winnerElement.textContent = `Draw`;
        winnerElement.classList.add('winner')
        gameActive = false; 
        statusElement.textContent = "Reseting game in 2 sec"
        statusElement.classList.add('status')
        setTimeout(()=>{
            statusElement.textContent = ''
            socket.send(JSON.stringify({
                action:'reset'
            }))
        },2000)
    }
}

};

socket.onclose = function(event) {
console.log("Disconnected from the game room.");
statusElement.textContent = "Disconnected from the game.";
};

socket.onerror = function(error) {
console.error("WebSocket Error: ", error);
statusElement.textContent = "Error occurred in the connection.";
};

function updateBoard(board) {
    boardElement.innerHTML = '';
    board.forEach((cell, index) => {
        const cellElement = document.createElement('div');
        cellElement.className = 'cell';
        cellElement.textContent = cell;
        cellElement.onclick = () => makeMove(index);
        boardElement.appendChild(cellElement);
    });
}

function makeMove(index) {
    if (!gameActive) return; 
    socket.send(JSON.stringify({
        action: 'make_move',
        position: index
    }));
}
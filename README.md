# CodeAlpha_Multiplayer-Online-Game-Server
## Overview
CodeAlpha_Multiplayer-Online-Game-Server is a real-time multiplayer Tic-Tac-Toe web application. Players can join or create game rooms using unique room codes and compete in classic Tic-Tac-Toe matches, with real-time updates, game resets, and winner announcements.

## Features
-- **Real-Time Multiplayer**: Players can join or create a game room and play live with opponents.  
-- **Dynamic Game Board**: A fully interactive and responsive Tic-Tac-Toe board that updates in real-time.  
-- **Game Reset Functionality**: Automatically resets after a winner is declared, allowing new matches to start seamlessly.  
-- **Responsive Design**: User-friendly interface accessible on various devices, including mobile and desktop.  

## Setup
1. **Clone the repository**:
   ```sh
   git clone https://github.com/nathnael1/CodeAlpha_Multiplayer-Online-Game-Server.git
2. Navigate to the project directory  
    ```sh
    cd CodeAlpha_Multiplayer-Online-Game-Server/tictactoe
3. Install dependent projects
    ```sh
    pip install -r requirements.txt
5. Apply the migrations  
    ```sh
    python manage.py migrate
5. Run the development server using daphne
    ```sh
    daphne -p 8000 tictactoe.asgi:application

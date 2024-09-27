import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .game_logic import TicTacToe
from collections import defaultdict
games = defaultdict(lambda: TicTacToe(room_code=""))  

class GameConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_code = self.scope['url_route']['kwargs']['room_code']
        self.room_group_name = f'game_{self.room_code}'
        
        if self.room_code not in games:
            games[self.room_code] = TicTacToe(self.room_code)
        
        self.game = games[self.room_code]

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        await self.send(text_data=json.dumps({
            'board': self.game.board,
            'winner': None  ,
            'reset': False
        }))
        
    async def reset(self):
        self.game.reset_game()
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'game_update',
                'winner':None,
                'board':self.game.board,
                'reset':True
            }
        )
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        action = text_data_json['action']
        if action == "make_move":
            position = text_data_json['position']
            winner = self.game.make_move(position)
        elif action == "reset":
            await self.reset()
            return
        
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'game_update',
                'winner':winner,
                'board':self.game.board,
                'reset':False
            }
            
        )
    async def game_update(self,event):
        board = event['board']
        winner = event['winner']
        reset = event['reset']
        await self.send(
            text_data = json.dumps({
                'board':board,
                'winner':winner,
                'reset':reset
            })
        )
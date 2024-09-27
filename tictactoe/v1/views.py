from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def game_view(request, room_code):
    return render(request, 'game.html', {'room_code': room_code})

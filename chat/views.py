from django.shortcuts import render


# Create your views here.
def index_view(request):
    return render(request, 'chat_temp/index.html', {})


def room_view(request, room_name):
    context = {
        'room_name': room_name
    }
    return render(request, 'chat_temp/room.html', context)

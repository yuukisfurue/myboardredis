from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Friend
from .forms import FriendForm

def index(request):
    data = Friend.objects.all()
    params = {
        'title': 'Board',
        'data': data,
    }
    return render(request, 'board/index.html', params)

# create model
def create(request):
    if (request.method == 'POST'):
        obj = Friend()
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/board')
    params = {
        'title': 'Board',
        'form': FriendForm(),
    }
    return render(request, 'board/create.html', params)

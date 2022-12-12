from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Friend
from .forms import FriendForm
from django.views.generic import ListView
from django.views.generic import DetailView
from .forms import FindForm 
from django.core.paginator import Paginator
from django.db.models import Q    # 追記
from django.db.models import Count,Sum,Avg,Min,Max
from .forms import CheckForm    #☆
from django.core.paginator import Paginator

class FriendList(ListView):
    model = Friend

class FriendDetail(DetailView):
    model = Friend

def index(request, num=1):
    data = Friend.objects.all()
    page = Paginator(data, 5)
    params = {
        'title': 'Board',
        'message':'',
        'data': page.get_page(num),
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

def edit(request, num):
    obj = Friend.objects.get(id=num)
    if (request.method == 'POST'):
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/board')
    params = {
        'title': 'Board',
        'id':num,
        'form': FriendForm(instance=obj),
    }
    return render(request, 'board/edit.html', params)

def delete(request, num):
    friend = Friend.objects.get(id=num)
    if (request.method == 'POST'):
        friend.delete()
        return redirect(to='/board')
    params = {
        'title': 'Board',
        'id':num,
        'obj': friend,
    }
    return render(request, 'board/delete.html', params)

def find(request):
    if (request.method == 'POST'):
        msg = request.POST['find']
        form = FindForm(request.POST)
        sql = 'select * from board_friend'
        if (msg != ''):
            sql += ' where ' + msg
        data = Friend.objects.raw(sql)
        msg = sql
    else:
        msg = 'search words...'
        form = FindForm()
        data =Friend.objects.all()
    params = {
        'title': 'Board',
        'message': msg,
        'form':form,
        'data':data,
    }
    return render(request, 'board/find.html', params)

def check(request):
    params = {
        'title': 'Board',
        'message':'check validation.',
        'form': FriendForm(),
    }
    if (request.method == 'POST'):
        obj = Friend()
        form = FriendForm(request.POST, instance=obj)
        params['form'] = form
        if (form.is_valid()):
            params['message'] = 'OK!'
        else:
            params['message'] = 'no good.'
    return render(request, 'board/check.html', params)
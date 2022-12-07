from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    params = {
        'title':'Board/Index',
        'msg':'これは、サンプルで作ったページです。',
        'goto':'next',
    }
    return render(request, 'board/index.html', params)

def next(request):
    params = {
        'title':'Board/Next',
        'msg':'これは、もう１つのページです。',
        'goto':'index',
    }
    return render(request, 'board/index.html', params)
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import BoardForm

class BoardView(TemplateView):
    
    def __init__(self):
        self.params = {
            'title': 'Board',
            'message': 'your data:',
            'form': BoardForm()
        }
    
    def get(self, request):
        return render(request, 'board/index.html', self.params)

    def post(self, request):
        msg = 'あなたは、<b>' + request.POST['name'] + \
            '（' + request.POST['age'] + \
            '）</b>さんです。<br>住所は <b>' + request.POST['address'] + \
            '</b> ですね。'
        self.params['message'] = msg
        self.params['form'] = BoardForm(request.POST)
        return render(request, 'board/index.html', self.params)
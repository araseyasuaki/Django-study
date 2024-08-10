from django.shortcuts import render

# Create your views here.

def index(request):
  return render(request, 'index.html')

def baidu(request):
  return render(request, 'baidu.html')

def info(request):
  username = '承太郎'
  book = {'manga': '鬼滅の刃', 'syousetu': '人間失格'}
  books = [
    {'name': 'コイキング', 'type': '水'},
    {'name': 'ギャラドス', 'type': '水・飛行'},
  ]
  class Person:
    def __init__(self, realname):
      self.realname = realname
  context = {
    'username': username,
    'book': book,
    'books': books,
    'person': Person("智スーパーサイヤ人")
  }
  return render(request, 'info.html', context=context)

def if_view(request):
  age = 17
  return render(request, 'if.html', context={'age': age})
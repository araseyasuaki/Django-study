from django.shortcuts import render, HttpResponse

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
  age = 19
  return render(request, 'if.html', context={'age': age})

def for_view(request):
  books = [
    # {'name': 'コイキング', 'type': '水'},
    # {'name': 'ギャラドス', 'type': '水・飛行'},
  ]
  person = {
    'realname': '荒瀬康明',
    'age': '19',
    'height': '179',
  }
  context = {
    'books': books,
    'person': person,
  }
  return render(request, 'for.html', context)

def with_vier(request):
  context = {
    'books': [
      {'name': 'コイキング', 'type': '水'},
      {'name': 'ギャラドス', 'type': '水・飛行'},
    ]
  }
  return render(request, 'with.html', context)

def url_view(request):
  return render(request, 'url.html')

def book_detail(request, book_id):
  return HttpResponse(f'ポケモンNo.は：{book_id}')


def filter_view(request):
  greet = "Hello World, Hello Django"
  context = {
    "greet": greet,
  }
  return render(request, 'filter.html', context)
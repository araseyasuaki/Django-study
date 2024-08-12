from django.shortcuts import render

def fromtpage(request):
  return render(request, 'blog/frontpage.html')

from django.shortcuts import render

# Create your views here.
def robotstxt(request):
    return render(request, 'robots.txt')
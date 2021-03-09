from django.shortcuts import render

def image(request):
    return render(request, 'articles/image.html')

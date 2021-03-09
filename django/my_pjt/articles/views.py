from django.shortcuts import render

def image(request):
    return render(request, 'articles/image.html')

def search(request):
    return render(request, 'articles/search.html')

def result(request, param1, param2):
    print(param1 * param2)
    context = {
        'result': param1 * param2,
    }
    return render(request, 'articles/result.html', context)
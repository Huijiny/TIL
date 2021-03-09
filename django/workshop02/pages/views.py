from django.shortcuts import render

def dinner(request, dinner, people):
    context = {
        'dinner': dinner,
        'people': people,
    }
    return render(request, 'dinner.html', context)

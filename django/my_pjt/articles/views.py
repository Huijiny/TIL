from django.shortcuts import render

def image(request):
    return render(request, 'articles/image.html')

def search(request):
    return render(request, 'articles/search.html')

def result(request, param1, param2):
    context = {
        'result': param1 * param2,
    }
    return render(request, 'articles/result.html', context)

def dtl_practice(request):
    foods = ['족발', '초밥', '김치', '빵',]
    fruits = ['apple', 'banana', 'coconut', 'durian',]
    empty_list = []
    my_sentence = 'you need python'
    context = {
        'foods': foods,
        'empty_list': empty_list,
        'fruits': fruits,
        'my_sentence': my_sentence,
    }

    return render(request, 'articles/dtl_practice.html', context)
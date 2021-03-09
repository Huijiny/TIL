from django.shortcuts import render
import random
def lotto(request):
    lotto_number = random.sample(range(1, 45), 6)
    context = {
        'lotto_number': lotto_number
    }
    return render(request, 'lotto.html', context)
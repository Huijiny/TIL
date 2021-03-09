from django.shortcuts import render
import random
import requests


def check_winner(random_people, lotto_number, bonus):
    winner = [0] * 6
    for person in random_people:
        count = 0
        for num in lotto_number:
            if num in person:
                count += 1
        if count == 6:
            winner[0] += 1
        elif count == 5:
            if bonus in person:
                winner[1] += 1
            else:
                winner[2] += 1
        elif count == 4:
            winner[3] += 1
        elif count == 3:
            winner[4] += 1
        else:
            winner[5] += 1
    return winner


def lotto(request):
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=953'
    response = requests.get(url).json()

    lotto_number = [ response.get('drwtNo'+str(i)) for i in range(1, 7)]
    bonus = response.get('bnusNo')
    
    random_people = [random.sample(range(1, 45), 7) for _ in range(1000)]
    
    winner = check_winner(random_people, lotto_number, bonus)
                
    context = {
        'lotto_number': lotto_number,
        'bonus': bonus,
        'winner': winner,
    }
    return render(request, 'pages/lotto.html', context)

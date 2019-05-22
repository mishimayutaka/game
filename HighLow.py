import random
marks = ['spade', 'heart', 'diamond', 'club']
numbers = range(1,14)
cards = []
for i in marks:
    for j in numbers:
        cards.append((i, j))
card_count = 0
win_count = 0.0
judge_count = 0
cards.append(('joker',14))
cards.append(('joker',15))
random.shuffle(cards)

print('START High and Low')
while card_count < len(cards) - 1:
    open_card = cards[card_count][1]
    open_mark = cards[card_count][0]
    while open_card == 14 or open_card ==15:
        print('jokerがでたのでデッキから1枚引きます')
        card_count += 1
        open_card = cards[card_count][1]
        open_mark = cards[card_count][0]
        judge_count += 1
    if open_card == 1 or open_card == 13:
        while True:
            print('現在のカードは' + open_mark + 'の' + str(open_card) + 'です')
            answer = input('黒:1 , 赤:2 のいずれかを入力してください：')
            if answer == '1' or answer == '2':
                break
            else:
                print('1か2で入力してください')
        card_count += 1
        answer_card = cards[card_count][1]
        answer_mark = cards[card_count][0]
        if answer_card == 14 or answer_card == 15:
            print('jokerです。両隣は1盛り！')
            judge_count += 1
        else:
            print('次のカードは' + answer_mark + 'の' +str(answer_card) + 'でした')
            if answer_mark == 'club' or answer_mark == 'spade':
                if answer == '1':
                    print('SAFE')
                    win_count += 1
                else:
                    print('OUT')
                judge_count += 1
            else:
                if answer == '2':
                    print('SAFE')
                    win_count += 1
                else:
                    print('OUT')
                judge_count += 1
    else:
        while True:
            print('現在のカードは' + open_mark + 'の' + str(open_card) + 'です')
            answer = input('High:1 , Low:2 のいずれかを入力してください：')
            if answer == '1' or answer == '2':
                break
            else:
                print('1か2で入力してください')
        card_count += 1
        answer_card = cards[card_count][1]
        answer_mark = cards[card_count][0]
        if answer_card == 14 or answer_card == 15:
            print('jokerです。両隣は1盛り！')
            judge_count += 1
        else:
            print('次のカードは' + answer_mark + 'の' + str(answer_card) + 'でした')
            if open_card < answer_card:
                print('Highでした')
                if answer == '1':
                    print('SAFE')
                    win_count += 1
                else:
                    print('OUT 1盛り！')
                judge_count += 1
            elif open_card == answer_card:
                print('同じ数です。倍プッシュや！')
                judge_count += 1
            else:
                print('Lowでした')
                if answer == '2':
                    print('SAFE')
                    win_count += 1      
                else:
                    print('OUT 1盛り！')
                judge_count += 1       
print('デッキ切れです')
win_p = win_count * 100 / judge_count
print('勝率は' + str(win_p) + '%でした')
fin = input('ボタンを押してください。終了します。：')
print('finish')
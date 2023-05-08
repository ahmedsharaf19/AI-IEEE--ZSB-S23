number_cards = int(input().strip())
cards = list(map(int,input().split()))
sum_sereja , sum_dima = 0 , 0
flag_player = True    # Sereja Playing
for i in range(number_cards) :
    if cards[0] > cards[-1] :
        max_card = cards[0]
        cards.pop(0)
    else :
        max_card = cards[-1]
        cards.pop(-1)
    
    if flag_player :
        sum_sereja += max_card
        flag_player = False
    else :
        sum_dima += max_card
        flag_player = True

print(sum_sereja,sum_dima)

        






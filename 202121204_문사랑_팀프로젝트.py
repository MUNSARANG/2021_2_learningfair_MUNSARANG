import time

print("Python 블랙잭 게임에 오신것을 환영합니다.\n")
time.sleep(2)
print("Python 블랙잭은 Python으로 구동되는 블랙잭 게임 입니다. \n")
time.sleep(2)


Blackjack_rule=('블랙잭이란?', '기본 규칙', '세부 규칙', '게임 내 규칙')

Explanation=input("블랙잭 룰에 대한 설명을 들으시겠습니까? (Y/N)\n")

if Explanation == 'Y':
    print()
    print(Blackjack_rule)
    time.sleep(2)

    while 1:
        print()
        rule = int(input('원하시는 설명의 번호를 적어주세요. (블랙잭이란? = 1, 기본 규칙 = 2, 세부 규칙 = 3, 게임 내 규칙 = 4, 설명 종료 = 5 )'))

        if rule == 1:
            print()
            print('블랙잭이란 딜러와 플레이어가 카드를 한장씩 받아 21에 가까운 수를 만드는 사람이 이기며 21을 초과하면 지는 게임입니다.\n')
            time.sleep(2)
            continue

        if rule == 2:
            print()
            print('기본 규칙\n')
            time.sleep(2)
            print('먼저 플레이어는 베팅 금액을 정합니다. 게임에서 이기면 베팅액의 2배를 돌려받습니다.\n')
            time.sleep(2)
            print('블랙잭은 조커를 제외한 52장의 플레잉(또는 트럼프라 불리는)카드를 사용합니다.\n')
            time.sleep(2)
            print('게임이 시작되기 전 플레이어는 베팅을 진행하며 베팅 이후 딜러와 플레이어가 카드를 각각 2장씩 받습니다.\n')
            time.sleep(2)
            print('딜러의 카드 2장 중 1장은 공개되지 않으며 플레이어의 카드 2장은 전부 공개 됩니다.\n')
            time.sleep(2)
            print('플레이어는 공개된 딜러의 카드와 공개되지 않은 딜러의 카드를 보고 판단하여 Hit, Stay등의 행동을 할 수 있습니다.\n')
            time.sleep(2)
            print('Hit, Stay에 관한 내용은 4번 게임 내 규칙을 읽어주시기 바랍니다.\n')
            time.sleep(1)
            continue


        if rule == 3:
            print()
            print('세부 규칙\n')
            time.sleep(2)
            print('숫자카드인 2~10은 그 숫자대로 점수를 세고, K,Q,J은 10점으로 계산합니다.\n')
            time.sleep(2)
            print('에이스(A)카드는 게임을 하는 곳에 따라 1 또는 11로 계산합니다. 우리 게임에서는 11로 계산하도록 하겠습니다.\n')
            time.sleep(2)
            print('플레이어는 자신의 카드의 합이 21이 넘지 않는 한 계속해서 카드를 받을 수 있고, 원할 때 카드를 그만 받을 수 있습니다.\n')
            time.sleep(2)
            print('반대로 딜러는 딜러 본인의 카드의 합이 17이 넘으면 카드를 더이상 받지 못합니다.\n')
            time.sleep(2)
            print('딜러의 카드합이 17이 넘으면 카드를 더 이상 받지 못한다는 것을 잘 이용하십시오.\n')

            continue

        if rule == 4:
            print()
            print('게임 내 규칙\n')
            time.sleep(2)
            print(' 1. Hit(힛) : 카드를 한 장 더 받을 수 있습니다.\n')
            time.sleep(2)
            print(' 2. Stay(스테이) : 카드를 더 받지 않습니다. 플레이어가 Stay를 선언하면 딜러의 카드가 공개됩니다.\n')
            time.sleep(2)
            print(' 3, Bust(버스트) : 카드의 총합이 21이 넘는 경우입니다. 즉시 패배합니다.\n')
            time.sleep(2)
            print(' 4. Blackjack(블랙잭) : 카드의 총합이 정확히 21이 되는 경우 입니다. 게임에서 즉시 승리합니다.\n')
            time.sleep(2)
            print(' 실제 카지노의 블랙잭은 더 많은 룰이 존재하지만 게임이 복잡해지므로 우리 게임에서는 위 4가지 규칙만을 이용하겠습니다.\n')

            continue

        if rule == 5:
            while 1:
                Game_start2=input('게임을 시작하겠습니까? (Y/N)\n')
                if Game_start2 == 'N':
                    really1 = input('게임을 종료하시겠습니까? (Y/N)\n')

                    if really1 == 'Y':
                        print('게임을 종료합니다')
                        time.sleep(1)
                        raise SystemExit
                    if really1 == 'N':
                        continue
                if Game_start2 == 'Y':
                    break
                    
            break
        
    print()
if Explanation == 'N':
    while 1:
        Game_start1=input('게임을 시작하겠습니까? (Y/N)\n')
        if Game_start1 == 'N':
            Game_over1=input('게임을 종료하시겠습니까? (Y/N)\n')

            if Game_over1=='Y':
                print()
                print('게임을 종료합니다')
                time.sleep(1)
                raise SystemExit

            if Game_over1=='N':
                continue

        if Game_start1 == 'Y':

            print('게임을 시작합니다. 잠시만 기다려 주십시오.\n')
            time.sleep(2)
            break

while 1:
    username=input('이름을 입력해 주십시오: \n')
    usernameYN=input(username + '이/가 당신의 이름이 맞습니까? (Y/N)')

    if usernameYN == 'Y':
        print()
        print('게임을 시작합니다.\n')
        break
    else:
        continue

while 1:
    print()
    print('카드 만드는 중......')
    playing_cards1 = ['A','2','3','4','5','6','7','8','9','10','K','Q','J']
    playing_cards2 = ['A','2','3','4','5','6','7','8','9','10','K','Q','J']
    playing_cards3 = ['A','2','3','4','5','6','7','8','9','10','K','Q','J']
    playing_cards4 = ['A','2','3','4','5','6','7','8','9','10','K','Q','J']

    playing_cards1.extend(playing_cards2)
    playing_cards1.extend(playing_cards3)
    playing_cards1.extend(playing_cards4)

    time.sleep(2)
    print()
    print('카드가 생성되었습니다.\n')
    print('딜러 모셔오는 중......\n')
    time.sleep(2)
    print('딜러를 초빙했습니다.\n')
    time.sleep(1)
    print()
    print('3초 후 게임이 시작됩니다\n')
    time.sleep(1)
    print('3\n')
    time.sleep(1)
    print('2\n')
    time.sleep(1)
    print('1\n')
    print()


    import random
    dealer_deck = random.sample(playing_cards1,1)
    print(dealer_deck)
    dealer_deck1 = random.sample(playing_cards1,1)
    print()
    time.sleep(1)
    print('딜러의 카드 한 장이 공개되었습니다.\n')
    time.sleep(1)
    player_deck = random.sample(playing_cards1, 2)
    print('당신의 패 입니다.')
    print(player_deck)
    time.sleep(2)

    player_deck1=[]

    while 1:
        print('무엇을 하시겠습니까? (번호입력)\n')
        player_choice=input(' 1: Hit(한장 뽑기), 2: Stay(카드 추가 안함) \n')
        if player_choice == '1':
            print('한 장을 추가합니다.\n')
            time.sleep(1)
            player_deck1 = random.sample(playing_cards1, 1)
            player_deck.extend(player_deck1)
            print(player_deck)
            print()
            time.sleep(2)
            continue
        elif player_choice == '2':
            print('카드를 추가하지 않습니다.\n')
            break

    print()
    time.sleep(1)

    search = 'A'
    for word in player_deck:
        if search in word:
            player_deck.remove(word)
            player_deck.append('11')
    search = 'K'
    for word in player_deck:
        if search in word:
            player_deck.remove(word)
            player_deck.append('10')
    search = 'Q'
    for word in player_deck:
        if search in word:
            player_deck.remove(word)
            player_deck.append('10')
    search = 'J'
    for word in player_deck:
        if search in word:
            player_deck.remove(word)
            player_deck.append('10')


    search = 'A'
    for word in player_deck:
        if search in word:
            player_deck.remove(word)
            player_deck.append('11')
    search = 'K'
    for word in player_deck:
        if search in word:
            player_deck.remove(word)
            player_deck.append('10')
    search = 'Q'
    for word in player_deck:
        if search in word:
            player_deck.remove(word)
            player_deck.append('10')
    search = 'J'
    for word in player_deck:
        if search in word:
            player_deck.remove(word)
            player_deck.append('10')

    player_deck2 = list(map(int, player_deck))
    time.sleep(1)
    print(player_deck2)
    print()
    time.sleep(1)

    player_deck3 = sum(player_deck2)
    print(player_deck3)
    print()
    hap = player_deck3

    if player_deck3 > 21:
        print(username + ' 님의 패의 숫자 합이 21을 넘었습니다.\n')
        time.sleep(1)
        print(username + ' 님의 버스트(Bust) 입니다. 이번 게임에서 패배하셨습니다.\n')

    if player_deck3 == 21:
        print(username + ' 님의 패의 숫자 합은 21 입니다\n')
        time.sleep(1)
        print('블랙잭! 이번 게임에서 승리하셨습니다.\n')

    if player_deck3 < 21:
        print(username + ' 님의 패의 숫자 합은 ' + str(hap) + ' 입니다\n')
        time.sleep(1)
        print('딜러의 패 합을 확인하겠습니다\n')
        time.sleep(1)
        print('딜러의 공개 카드와 비공개 카드를 오픈하겠습니다. \n')
        time.sleep(1)

        dealer_deck.extend(dealer_deck1)
        print(dealer_deck)
        time.sleep(1)

        search = 'A'
        for word in dealer_deck:
            if search in word:
                dealer_deck.remove(word)
                dealer_deck.append('11')
        search = 'K'
        for word in dealer_deck:
            if search in word:
                dealer_deck.remove(word)
                dealer_deck.append('10')
        search = 'Q'
        for word in dealer_deck:
            if search in word:
                dealer_deck.remove(word)
                dealer_deck.append('10')
        search = 'J'
        for word in dealer_deck:
            if search in word:
                dealer_deck.remove(word)
                dealer_deck.append('10')

        search = 'A'
        for word in dealer_deck:
            if search in word:
                dealer_deck.remove(word)
                dealer_deck.append('11')
        search = 'K'
        for word in dealer_deck:
            if search in word:
                dealer_deck.remove(word)
                dealer_deck.append('10')
        search = 'Q'
        for word in dealer_deck:
            if search in word:
                dealer_deck.remove(word)
                dealer_deck.append('10')
        search = 'J'
        for word in dealer_deck:
            if search in word:
                dealer_deck.remove(word)
                dealer_deck.append('10')
                
        dealer_deck2 = list(map(int, dealer_deck))
        print()
        print(dealer_deck2)
        print()
        time.sleep(1)

        dealer_deck3 = sum(dealer_deck2)
        dealer_deck3_1 = []
        print(dealer_deck3)
        print()

        dealer_deck4 = []
        while 1:
            if dealer_deck3 >= 17:
                print('딜러의 카드 합이 17을 넘겼습니다.\n')
                time.sleep(1)
                print('더 이상 카드를 드로우 하지 않습니다.\n')
                break

            if dealer_deck3 < 17:
                print()
                print('딜러의 카드 합이 17 이하 이므로 딜러가 카드를 뽑습니다.\n')
                dealer_deck4 = random.sample(playing_cards1, 1)
                dealer_deck3_1.extend(dealer_deck4)
                time.sleep(1)
                print('딜러가 다음 카드를 뽑았습니다\n')
                print(dealer_deck3_1)
                print()
                time.sleep(1)

                search = 'A'
                for word in dealer_deck3_1:
                    if search in word:
                        dealer_deck3_1.remove(word)
                        dealer_deck3_1.append('11')
                search = 'K'
                for word in dealer_deck3_1:
                    if search in word:
                        dealer_deck3_1.remove(word)
                        dealer_deck3_1.append('10')
                search = 'Q'
                for word in dealer_deck3_1:
                    if search in word:
                        dealer_deck3_1.remove(word)
                        dealer_deck3_1.append('10')
                search = 'J'
                for word in dealer_deck3_1:
                    if search in word:
                        dealer_deck3_1.remove(word)
                        dealer_deck3_1.append('10')

                search = 'A'
                for word in dealer_deck3_1:
                    if search in word:
                        dealer_deck3_1.remove(word)
                        dealer_deck3_1.append('11')
                search = 'K'
                for word in dealer_deck3_1:
                    if search in word:
                        dealer_deck3_1.remove(word)
                        dealer_deck3_1.append('10')
                search = 'Q'
                for word in dealer_deck3_1:
                    if search in word:
                        dealer_deck3_1.remove(word)
                        dealer_deck3_1.append('10')
                search = 'J'
                for word in dealer_deck3_1:
                    if search in word:
                        dealer_deck3_1.remove(word)
                        dealer_deck3_1.append('10')

                dealer_deck3_2 = list(map(int, dealer_deck3_1))
                dealer_deck3_3 = sum(dealer_deck3_2)
                dealer_deck3 = dealer_deck3 + dealer_deck3_3
                print('카드 추가 후 딜러의 패 합입니다.\n')
                print(dealer_deck3)
                time.sleep(0.5)
                print()

        hap1 = dealer_deck3

        time.sleep(1)
        print('딜러의 카드 드로우가 끝났습니다\n')
        time.sleep(1)
        print('딜러의 카드 합은 ' + str(hap1) + ' 입니다\n')
        time.sleep(1)

        if hap1 > 21: 
            print('딜러의 패의 숫자 합이 21을 넘었습니다.\n')
            time.sleep(1)
            print('딜러의 버스트(Bust)입니다. 딜러가 패배하였습니다.\n')

        if hap1 == hap:
            print(username + ' 님과 딜러의 패 합이 같습니다.\n')
            time.sleep(1)
            print('이번 경기는 무승부입니다.\n')

        if hap1 < 21:
            print('딜러와 플레이어의 카드 합을 비교하고 승패를 결정하겠습니다.\n')
            time.sleep(2)
            print(str(hap1) + ' : 딜러의 카드 합 입니다.\n')
            time.sleep(1)
            print(str(hap) + ' : ' + username + ' 님의 카드 합 입니다.\n')
            time.sleep(1)

            if hap1 > hap:
                print('딜러의 카드 합이 ' + username + ' 님의 카드 합 보다 큽니다\n')
                time.sleep(1)
                print(username + ' 님이 패배하셨습니다\n')

            if hap1 < hap:
                print(username + ' 님의 카드 합이 딜러의 카드 합보다 큽니다.\n')
                time.sleep(1)
                print(username + ' 님이 승리하셨습니다!\n')

    while 1:
        request = input('게임을 계속하시겠습니까? (Y/N)\n')
        if request == 'N':
            really = input('게임을 종료하시겠습니까? (Y/N)\n')
            if really == 'Y':
                print('게임을 종료합니다')
                time.sleep(1)
                raise SystemExit
            if really == 'N':
                continue
        if request == 'Y':
            print('게임을 계속합니다\n')
            time.sleep(1)
            break
    continue
                
            
            
    
    
    



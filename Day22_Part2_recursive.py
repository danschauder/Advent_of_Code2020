import re, sys
sys.setrecursionlimit(5000)
# input="""Player 1:
# 9
# 2
# 6
# 3
# 1

# Player 2:
# 5
# 8
# 4
# 7
# 10"""

input="""Player 1:
21
48
44
31
29
5
23
11
12
27
49
22
18
7
15
20
2
45
14
17
40
35
6
24
41

Player 2:
47
1
10
16
28
37
8
26
46
25
3
9
34
50
32
36
43
4
42
33
19
13
38
39
30"""

reg1=re.compile(r"""
                \n\n
                """,re.VERBOSE)

decks = [a for a in re.split(reg1,input) if len(a)>0]
player1=[int(v) for k,v in enumerate(decks[0].splitlines()) if k>0]
player2=[int(v) for k,v in enumerate(decks[1].splitlines()) if k>0]

def card_battle(deck1,deck2,deck1_history,deck2_history):
    # print(recursion_depth)
    # print(deck1_history)
    d1=deck1.copy()
    d2=deck2.copy()
    d1_h = deck1_history.copy()
    d2_h = deck2_history.copy()
    if len(deck1)==0:
        return (d2,'d2')
    elif len(deck2)==0:
        return (d1,'d1')
    elif ','.join([str(b) for b in d2]) in d2_h or ','.join([str(a) for a in d1]) in d1_h:
        print('rip cord')
        return (d1,'d1')
    else:
        d1_h.add(','.join([str(a) for a in d1]))
        d2_h.add(','.join([str(b) for b in d2]))
        battle_card1=d1.pop(0)
        battle_card2=d2.pop(0)
        if battle_card1<=len(d1) and battle_card2<=len(d2):
            sub_battle_winner = card_battle(d1,d2,set(),set())
            if sub_battle_winner[1]=='d1':
                d1.append(battle_card1)
                d1.append(battle_card2)
            else:
                d2.append(battle_card2)
                d2.append(battle_card1)
        elif battle_card1>battle_card2:
            d1.append(battle_card1)
            d1.append(battle_card2)
        else:
            d2.append(battle_card2)
            d2.append(battle_card1)
        return card_battle(d1,d2,d1_h,d2_h)

def score_winner(deck):
    p = len(deck)
    i = 0
    score=0
    while p>0:
        score+= deck[i]*p
        i+=1
        p-=1
    return score

winner = card_battle(player1,player2,set(),set())
print(winner)
print(score_winner(winner[0]))

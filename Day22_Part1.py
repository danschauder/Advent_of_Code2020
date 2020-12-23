import re
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

def card_battle(deck1,deck2):
    d1=deck1.copy()
    d2=deck2.copy()
    battle_card1=d1.pop(0)
    battle_card2=d2.pop(0)
    if battle_card1>battle_card2:
        d1.append(battle_card1)
        d1.append(battle_card2)
    else:
        d2.append(battle_card2)
        d2.append(battle_card1)
    return (d1, d2)

def score_winner(deck):
    p = len(deck)
    i = 0
    score=0
    while p>0:
        score+= deck[i]*p
        i+=1
        p-=1
    return score

rounds=2000
i=0
game_over=False
while i<rounds and not game_over:
    results=card_battle(player1,player2)
    player1=results[0]
    player2=results[1]
    if len(player1)==0 or len(player2)==0:
        game_over=True
    else:
        i+=1

winner = player1 if len(player1)>len(player2) else player2

print(score_winner(winner))
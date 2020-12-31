import re
# txt="""Player 1:
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

# txt="""Player 1:
# 43
# 19

# Player 2:
# 2
# 29
# 14"""

txt="""Player 1:
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

decks = [a for a in re.split(reg1,txt) if len(a)>0]
player1=[int(v) for k,v in enumerate(decks[0].splitlines()) if k>0]
player2=[int(v) for k,v in enumerate(decks[1].splitlines()) if k>0]

def battle_cards(deck1,deck2):
    d1=deck1.copy()
    d2=deck2.copy()
    battle_log=set()
    def make_move(winner=None):
        nonlocal d1,d2,battle_log
        key = (tuple(d1),tuple(d2))
        if key in battle_log:
            return(d1,'d1')
        elif len(d1)==0:
            return (d2,'d2')
        elif len(d2)==0:
            return (d1,'d1')
        if winner is None:
            battle_log.add(key)
            battle_card1=d1.pop(0)
            battle_card2=d2.pop(0)
            if battle_card1>battle_card2:
                d1.append(battle_card1)
                d1.append(battle_card2)
            else:
                d2.append(battle_card2)
                d2.append(battle_card1)
            return (d1, d2)
        else:
            battle_log.add(key)
            battle_card1 = d1.pop(0)
            battle_card2 = d2.pop(0)
            if winner=='d1':
                d1.append(battle_card1)
                d1.append(battle_card2)
            else:
                d2.append(battle_card2)
                d2.append(battle_card1)
            return (d1, d2)

            
    return make_move

def score_winner(deck):
    p = len(deck)
    i = 0
    score=0
    while p>0:
        score+= deck[i]*p
        i+=1
        p-=1
    return score

def spawn_game(deck1,deck2):
    game_over=False
    top_game = battle_cards(deck1,deck2)
    subgame_winner=''
    while not game_over:
        if len(subgame_winner)>0:
            next_move = top_game(subgame_winner)
            subgame_winner=''
        else:
            next_move = top_game()
        if type(next_move[1]) is str:
            return next_move
            game_over=True
        elif len(next_move[0])>0 and len(next_move[1])>0:
            if (next_move[0][0]<=len(next_move[0])-1) and (next_move[1][0]<=len(next_move[1])-1):
                sub_game = spawn_game(next_move[0][1:next_move[0][0]+1],next_move[1][1:next_move[1][0]+1])
                subgame_winner=sub_game[1]
                    

game_winner = spawn_game(player1,player2)

print(f'The winner is {game_winner}')

print(f'The winning score is {score_winner(game_winner[0])}')
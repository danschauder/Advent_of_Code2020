# txt="""389125467"""
txt="""135468729"""

sequence = [int(i) for i in txt]

def cup_game(s):
    seq = s
    current_cup_index=0
    current_cup_value=0
    len_s = len(seq)
    def move_cups():
        nonlocal seq, current_cup_index

        current_cup_value=seq[current_cup_index]

        ##Find the indexes of the 3 components that need to move
        ##Store them in cups_to_move list
        cups_to_move = []
        for i in range(1,4):
            if current_cup_index+i<len_s:
                cups_to_move.append(current_cup_index+i)
            else:
                cups_to_move.append(i-(len_s-current_cup_index))

        ##Find the target value and index
        if seq[current_cup_index]-1 in seq:
            target_value = seq[current_cup_index]-1
        else:
            target_value = len_s
        found_target=False
        while not found_target:
            if target_value not in [seq[j] for j in cups_to_move]:
                found_target=True
            else:
                if target_value-1 in seq:
                    target_value-=1
                else:
                    target_value=len_s

        items_to_move = []
        for el in cups_to_move:
            items_to_move.append(seq[el])
        
        new_seq = [el for el in seq if el not in items_to_move]
        seq=new_seq

        target_index = 0
        for k,v in enumerate(seq):
            if v==target_value:
                target_index=k

        for k,v in enumerate(items_to_move):
            seq.insert(target_index+k+1,v)

        for k,v in enumerate(seq):
            if v==current_cup_value:
                current_cup_index=k

        if current_cup_index<len_s-1:
            current_cup_index+=1
        else:
            current_cup_index=0

        return (seq,current_cup_index,items_to_move,target_value,target_index)
    return move_cups


def find_answer(s):
    st = ''.join([str(i) for i in s])
    st_i = st.find('1')
    part1 = st[st_i+1:]
    part2 = st[0:st_i]
    return part1 + part2

game = cup_game(sequence)
k=0
while k<99:
    print(game())
    k+=1

ans1=game()
print(ans1)
print(f'answer is {find_answer(ans1[0])}')
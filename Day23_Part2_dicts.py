"""This implementation completes much more quickly than
my custom linked list implementation"""

# txt="""389125467"""
txt="""135468729"""

sequence = [int(i) for i in txt]

sequence_part2 = [int(i) for i in range(len(sequence)+1,1000001)]

sequence = sequence + sequence_part2

lookup = {}

for k,v in enumerate(sequence):
    if k<len(sequence)-1:
        lookup[v] = sequence[k+1]
    else:
        lookup[v] = sequence[0]

max_val = len(sequence)

current_cup = sequence[0]

move_counter=0
print('making moves')
while move_counter<10000000:
    first_pick = lookup[current_cup]
    second_pick = lookup[first_pick]
    third_pick = lookup[second_pick]
    fourth_pick = lookup[third_pick]
    if current_cup>1:
        target_val = current_cup-1
    else:
        target_val=max_val
    while target_val in [first_pick, second_pick, third_pick]:
        if target_val-1>0:
            target_val-=1
        else:
            target_val=max_val
    node_after_target = lookup[target_val]
    lookup[current_cup] = fourth_pick
    lookup[target_val] = first_pick
    lookup[third_pick] = node_after_target
    current_cup = fourth_pick
    move_counter+=1


a = lookup[1]
b = lookup[a]
print(a)
print(b)
print(a * b)

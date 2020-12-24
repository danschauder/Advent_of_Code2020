txt="""389125467"""
# txt="""135468729"""

sequence = [int(i) for i in txt]

sequence_part2 = [int(i) for i in range(len(sequence)+1,101)]

sequence = sequence + sequence_part2


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head=node
            while len(nodes)>0:
                node.next = Node(data=nodes.pop(0))
                node = node.next
            node.next = self.head

    def __repr__(self):
        node = self.head
        nodes = []
        while node.next is not self.head:
            nodes.append(node.data)
            node = node.next
        nodes.append(node.data)
        nodes.append("None")
        return " -> ".join([str(n) for n in nodes])


max_val = len(sequence)

print(max_val)

llist = LinkedList(sequence)

current_cup = llist.head

move_counter=0

while move_counter<10:
    print(llist)
    first_pick = current_cup.next
    second_pick = first_pick.next
    third_pick = second_pick.next
    fourth_pick = third_pick.next
    current_cup_val = current_cup.data
    if current_cup_val>1:
        target_val = current_cup_val-1
    else:
        target_val=max_val
    while target_val in [first_pick.data, second_pick.data, third_pick.data]:
        if target_val-1>0:
            target_val-=1
        else:
            target_val=max_val
    target_node = third_pick.next
    while target_node.data != target_val:
        target_node = target_node.next
    # print(f'{first_pick.data} -- {second_pick.data} -- {third_pick.data} -- target is {target_node.data}')
    node_after_target = target_node.next
    current_cup.next = fourth_pick
    target_node.next = first_pick
    third_pick.next = node_after_target
    current_cup = current_cup.next
    move_counter+=1

print(llist)
# check_node = llist.head
# while check_node.data!=1:
#     check_node=check_node.next

# print(check_node.data)
# next_node = check_node.next
# print(next_node.data)
# next_node2 = next_node.next
# print(next_node2.data)

# current_cup_index=0
# current_cup_value=indexes_to_nums[current_cup_index]
# len_s=len(sequence)
# print(current_cup_value)
# def cup_game():
#     global nums_to_indexes, indexes_to_nums, current_cup_index, current_cup_value, len_s
#     cups_to_move=[]
#     for i in range(1,4):
#         if current_cup_index+i<len_s:
#             cups_to_move.append(current_cup_index+i)
#         else:
#             cups_to_move.append(i-(len_s-current_cup_index))
#     return cups_to_move

# k=0
# while k<9999999:
#     cup_game()
#     k+=1

# def cup_game(s):
#     seq = s
#     current_cup_index=0
#     current_cup_value=0
#     len_s = len(seq)
#     def move_cups():
#         nonlocal seq, current_cup_index

#         current_cup_value=seq[current_cup_index]

#         ##Find the indexes of the 3 components that need to move
#         ##Store them in cups_to_move list
#         cups_to_move = []
#         for i in range(1,4):
#             if current_cup_index+i<len_s:
#                 cups_to_move.append(current_cup_index+i)
#             else:
#                 cups_to_move.append(i-(len_s-current_cup_index))

#         ##Find the target value and index
#         if seq[current_cup_index]-1 in seq:
#             target_value = seq[current_cup_index]-1
#         else:
#             target_value = len_s
#         found_target=False
#         while not found_target:
#             if target_value not in [seq[j] for j in cups_to_move]:
#                 found_target=True
#             else:
#                 if target_value-1 in seq:
#                     target_value-=1
#                 else:
#                     target_value=len_s

#         items_to_move = []
#         for el in cups_to_move:
#             items_to_move.append(seq[el])
        
#         new_seq = [el for el in seq if el not in items_to_move]
#         seq=new_seq

#         target_index = 0
#         for k,v in enumerate(seq):
#             if v==target_value:
#                 target_index=k

#         for k,v in enumerate(items_to_move):
#             seq.insert(target_index+k+1,v)

#         for k,v in enumerate(seq):
#             if v==current_cup_value:
#                 current_cup_index=k

#         if current_cup_index<len_s-1:
#             current_cup_index+=1
#         else:
#             current_cup_index=0

#         return (seq,current_cup_index,items_to_move,target_value,target_index)
#     return move_cups


# def find_answer(s):
#     st = ''.join([str(i) for i in s])
#     st_i = st.find('1')
#     part1 = st[st_i+1:]
#     part2 = st[0:st_i]
#     return part1 + part2

# game = cup_game(sequence)
# k=0
# while k<9999999:
#     game()
#     print(k)
#     k+=1

# ans1=game()

# found_1=False
# i=0
# while not found_1:
#     if ans1[0][i]==1:
#         found_1=True
#     else:
#         i+=1

# l=0
# if i+1==len(ans1[0]):
#     pass
# else:
#     l=i+1

# m=0
# if l+1==len(ans1[0]):
#     pass
# else:
#     m=l+1

# print(ans1[0][i])
# print(ans1[0][l])
# print(ans1[0][m])
# # print(f'answer is {find_answer(ans1[0])}')

"""In this implementation, I created my own LinkedList class. This solution does complete
eventually, but is fairly slow. I wrote another solution (Day23_Part2_dicts.py) which uses
built-in dict classes and completes much more quickly than this one"""

# txt="""389125467"""
txt="""135468729"""

sequence = [int(i) for i in txt]

sequence_part2 = [int(i) for i in range(len(sequence)+1,1000001)]

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
        self.lookup = {}
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head=node
            self.lookup[node.data] = node
            while len(nodes)>0:
                node.next = Node(data=nodes.pop(0))
                self.lookup[node.next.data] = node.next
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

    def find_node(self, data):
        return self.lookup[data]


max_val = len(sequence)

print('building linked list')
llist = LinkedList(sequence)

current_cup = llist.head

move_counter=0
print('making moves')
while move_counter<10000000:
    # print(llist)
    # print(move_counter)
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
    target_node = llist.find_node(target_val)
    # print(f'{first_pick.data} -- {second_pick.data} -- {third_pick.data} -- target is {target_node.data}')
    node_after_target = target_node.next
    current_cup.next = fourth_pick
    target_node.next = first_pick
    third_pick.next = node_after_target
    current_cup = current_cup.next
    move_counter+=1


a = llist.find_node(1).next.data
b = llist.find_node(1).next.next.data
print(a)
print(b)
print(a * b)

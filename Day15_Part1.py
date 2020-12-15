from collections import defaultdict
input=[0,20,7,16,1,18,15]
num_log=defaultdict()
turn_counter=1
last_said=0
for el in input:
    num_log[el]={'last':turn_counter,'time_before_last':turn_counter}
    last_said=el
    turn_counter+=1

rounds=2020
while turn_counter<=rounds:
    if last_said in num_log.keys():
        next_num=num_log[last_said]['last']-num_log[last_said]['time_before_last']
        last_said=next_num
        if next_num in num_log.keys():
            num_log[next_num]['time_before_last']=num_log[next_num]['last']
            num_log[next_num]['last']=turn_counter
        else:
            num_log[next_num]={'last':turn_counter,'time_before_last':turn_counter}
    else:
        next_num=0
        if next_num in num_log.keys():
            num_log[next_num]['time_before_last']=num_log[next_num]['last']
            num_log[next_num]['last']=turn_counter
        else:
            num_log[next_num]={'last':turn_counter,'time_before_last':turn_counter}

    turn_counter+=1
print(last_said)
# input="""939
# 7,13,x,x,59,x,31,19"""
input="""1000053
19,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,523,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,13,x,x,x,x,23,x,x,x,x,x,29,x,547,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,17"""

input_parsed=input.splitlines()

target=int(input_parsed[0])
buses=input_parsed[1].split(',')
buses_cleaned=[int(i) for i in buses if i!='x']


min_wait=10000
ans=0
for bus in buses_cleaned:
    remainder = target % bus
    wait = bus - remainder
    if wait<min_wait:
        min_wait=wait
        ans=bus
print(min_wait * ans)
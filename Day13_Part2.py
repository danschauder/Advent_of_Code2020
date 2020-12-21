import numpy as np
# input="""939
# 7,13,x,x,59,x,31,19"""
# input="""1000053
# 19,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,523,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,13,x,x,x,x,23,x,x,x,x,x,29,x,547,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,17"""
input="""123123
19,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,523,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,13,x,x,x,x,23,x,x,x,x,x,29,x,547,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,17"""

input_parsed=input.splitlines()

buses=input_parsed[1].split(',')

b_i=[]
mods=[]
N=1
for k,v in enumerate(buses):
    if v!='x':
        # print(k,v)
        if k==0:
            b_i.append(0)
        else:
            if int(v)<k:
                offset = k // int(v)
                b_i.append(int(v) - (k-offset*int(v)))
            else:
                b_i.append(int(v)-k)
        mods.append(int(v))
        N=N*int(v)
b_i=np.array(b_i)
mods=np.array(mods)
n_i = np.array([N/mod for mod in mods])


def invert_mod(coef,mod):
    simplified_coef = coef % mod
    ans=1
    found_ans=False
    while not found_ans:
        if (simplified_coef*ans)%mod==1:
            found_ans=True
        else:
            ans +=1
    return ans

x_i = np.array([invert_mod(n_i[i],mods[i]) for i in range(len(mods))])
raw_answer=int(0)
for i in range(len(mods)):
    raw_answer+=int(b_i[i])*int(n_i[i])*int(x_i[i])

answer = raw_answer % N
print(N)
print(answer)
# answer = 1068781
# print(answer%7)
# print(answer%13)
# print(answer%59)
# print(answer%31)
# print(answer%19)
for k, mod in enumerate(mods):
    print(f"remainder is {answer % mod}, remainder should be {b_i[k]}")


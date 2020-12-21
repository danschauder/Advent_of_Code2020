import collections
from itertools import combinations
# input = """28
# 33
# 18
# 42
# 31
# 14
# 46
# 20
# 48
# 47
# 24
# 23
# 49
# 45
# 19
# 38
# 39
# 11
# 1
# 32
# 25
# 35
# 8
# 17
# 7
# 9
# 4
# 2
# 34
# 10
# 3"""

input = """99
104
120
108
67
136
80
44
129
113
158
157
89
60
138
63
35
57
61
153
116
54
7
22
133
130
5
72
2
28
131
123
55
145
151
42
98
34
140
146
100
79
117
154
9
83
132
45
43
107
91
163
86
115
39
76
36
82
162
6
27
101
150
30
110
139
109
1
64
56
161
92
62
69
144
21
147
12
114
18
137
75
164
33
152
23
68
51
8
95
90
48
29
26
165
81
13
126
14
143
15"""

##Parse the input string into a list of ints. I assume the input is a consistent list of integers evenly separated by newlines.
parsed_input = [int(a) for a in input.splitlines()]

##Sort the list in place
parsed_input.sort()

##Explicitly append the last jump to the device as a +3
parsed_input.append(parsed_input[-1]+3)

##Explicitly insert the starting point of 0 at the beginning of the list
parsed_input.insert(0,0)

##Set up a dictionary to memoize the dynamic program. Once the program has calculated
##the number of ways from a given node to the end, it doesn't need to keep recalculating
##it every time. This information is stored in the visited dict.
visited={}

##Define the dynamic program. The program uses recursion with memoization.
def dp(i):
    #print(i)
    if i==len(parsed_input)-1:
        return 1
    elif i in visited.keys():
        return visited[i]
    else:
        ans=0
        for el in range(i+1,len(parsed_input)):
            if (parsed_input[el]-parsed_input[i])<=3:
                ans+= dp(el)
        visited[i]=ans
        return ans

##Print the answer
print(dp(0))
import collections
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

##Define a diffs list to store the inter-adapter jolt differences. Initialize the array with the difference between 0 and the first adapter.
diffs = [parsed_input[0]]

#Update diffs to store the inter-adapter jolt differences
diffs = diffs + [(parsed_input[i+1]-parsed_input[i]) for i in range(len(parsed_input)-1)]

#Append 3 to the end of the diffs list since the last jolt difference will always be 3
diffs.append(3)

#Define frequencies of the diffs
freqs = collections.Counter(diffs)

#Print the product of the frequency of 1's and the frequency of 3's
print(freqs[1] * freqs[3])
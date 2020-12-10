input = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""

##Parse the input string into a list of ints. I assume the input is a consistent list of integers evenly separated by newlines.
parsed_input = [int(a) for a in input.splitlines()]

##Sort the list in place
parsed_input.sort()
print(parsed_input)
import math
input = ['.#..............##....#.#.####.',
'##..........#.....##...........',
'.......#....##...........#.#...',
'.........#.#...#..........#....',
'.........#..#................##',
'..#...#..#..#...........#......',
'...................#...##..##..',
'........#.....##...#.#.#...#...',
'#..#.##......#.#..#..........#.',
'......#.#...#.#...#........##.#',
'.....#.####........#...........',
'...###..#............#.........',
'.....#.......##......#...#.....',
'#......##......................',
'......#..............#.........',
'..##...#....###.##.............',
'#...#..........#.#.........#...',
'...........#........#...#......',
'.....##.........#......#..#....',
'#..............#....#.....#....',
'.#......#....#...#............#',
'.####..........##..#.#.........',
'....#...#......................',
'....................#....#.#...',
'..........###.#...............#',
'.#...........#...##............',
'.#.#..#.....#...#....#.......#.',
'.##........#..#....#...........',
'.........#.....#......###......',
'..............#..#.......#.....',
'........#..#.#...........#..#..',
'#.........#......#.....##.#.#..',
'........#.#.#....#.............',
'........#........#.#.##........',
'#......#.#..........#..#.......',
'..#....#...##......###..#..#...',
'............#..#.#.........#...',
'....#.#...........#..........##',
'.......#.#.#..#......#...#.....',
'..#.........##.#.........#...#.',
'......#....#.#....#........#.#.',
'.#....###....#..............#..',
'.#....#.......#....#..#.....#..',
'.....#.....#...................',
'..#.....#......#......#........',
'......##.##...#...#...#...#.##.',
'##...#....#...#..#...#...#.....',
'..#.....#...#...##.##...#......',
'.....#.............##...#......',
'.....................#.##..#...',
'#...#....#....#........#.....#.',
'..#...#.........#...#..#.....#.',
'#.#......#...................#.',
'..#...........##...............',
'..#....#........#..#...........',
'...........#...................',
'.............###......#....#...',
'...........#...#....#..#....#..',
'.....##............#.#.......#.',
'.....#..#....#...#....#........',
'...............##........#.#...',
'.........#...#.#....#.......#..',
'#..#.......#.......#...#.......',
'..#...........................#',
'......#.......#..#......#......',
'.#.......#..................##.',
'..#.........#..#.##.#....#...##',
'...#..#....#...#....#.#........',
'.#...#........##..#..#.......#.',
'.....#........#....#....#..#...',
'............#...........#......',
'..###.......#..#....#......#...',
'.....#...#.......#..#..........',
'..#........##.#....##..........',
'#....#.............#..##......#',
'....#.................##.......',
'...#.......#........#....##.#.#',
'##..##..#.....#.....#..........',
'...#...............#....#..#...',
'.#...##....#....#.....#....##..',
'...#.....#......#......#.......',
'#.....#.......##.....#..#....##',
'.....#.#...##.#......##....#.#.',
'..........#....#.#...#.........',
'.#..##...#.....................',
'...........##..#...#....#......',
'...#......#........#.......#...',
'.#......#..#........#.....#..#.',
'.......#........##..#.##....#..',
'.##..........#..#...#.....#....',
'.....##...............#.#......',
'..##.....#..#......#..##.#.#...',
'....#......#.##...........#....',
'#.#..#.......#......#.#........',
'...#.#..#....#............#..#.',
'...#..........###....#....#...#',
'........##...#.......#..#....#.',
'..#...#.....#..#........##.....',
'...#..#.##.#.#.##..............',
'.......#...#.........#.....#..#',
'..#.....#.#..........#..#......',
'......#..........#......#.....#',
'.#...........#........#......##',
'..##............#......#...#..#',
'#..................#...........',
'#....#..#.........#........#..#',
'..#.#....###..#...#...##...##..',
'...#....#..#.....#.............',
'.#........##.##...#....#...#...',
'.........#.......##.#.....##...',
'#.#.....##...#........#...#...#',
'.....#.#.##...#.....#.##..#....',
'........#...##...#...#.#..#..#.',
'.##....#.##...#.......#........',
'...#..#................#..#....',
'....#.......#......#...#.##....',
'#......###..#...#......#.......',
'..#...#...##...........##......',
'.......#...#..##....##......#..',
'....#.#.............#.#...##..#',
'..........#........#...#......#',
'............#.#.#....###.......',
'#..#...#.#.####...#..#...#.....',
'.##.......#.##...#.............',
'#..#...........#.#.##.......#..',
'...#..#.#...#...###..#.#..#.#..',
'..#...#.....#..#....#....#.....',
'.........##.......#............',
'.........##.##......###........',
'.............#.#....#..#.....#.',
'...#....#.#.......#......##....',
'............#..................',
'....##...#..........#...#..#...',
'#..#....#.....#.......#.##.#..#',
'.....#.........##.............#',
'#.....#.#...#............##..##',
'..............#....#.....#.....',
'.#....###..#.#.....###.#..#....',
'.....#....##...#....#......#...',
'..........#...#....#...........',
'............#....#..#.........#',
'..##.....#.#...#.......#...#...',
'...#...#..#......##...#.....##.',
'......#.##............##.#....#',
'....#......#...##.....#.....###',
'.#.###...............#...#.#...',
'..#....................##...#..',
'.......#.....##...........#....',
'#.........#....#....#....#....#',
'..#.#..##.#.#..................',
'.....#.......#................#',
'...........#.......#........#..',
'#...#.........#.#.....#.....#..',
'..........#..#...........#.....',
'#..#.##..##..#.#.##.........#..',
'#..#..#....##..#.........#.....',
'#.#.......................#.#..',
'.##......#.#...#......#....#...',
'..#.#................#..##.....',
'.......#..................#...#',
'.....#.........##.#....#.......',
'#..........#..#.#..........#..#',
'..#..#.....#.........#...#.....',
'..............#.....#..#...#.##',
'...............................',
'...#............##......#.....#',
'.......#..#.............#.#....',
'...........#..........#........',
'...#.####..#......#...#....#...',
'##......#.##.....#.............',
'....#.........#...#...........#',
'...#........#.......#.#..#.#.#.',
'..#.......#.........#....#.....',
'................#.#.#.##...#..#',
'#.##...#...#..#.....#.....#..#.',
'...............#...........#...',
'.....##.#...............##...#.',
'.#..##.##......................',
'.......#.........#..#..#.......',
'...#......#..................#.',
'...#.#..#....#....#............',
'...........#...#..#....##......',
'.....#...#..#.#....#....#....#.',
'.......#...#...#.#.#...........',
'....#......#......#...##..#....',
'##...#.#.....#..#.##...........',
'#.#..#.....#..#................',
'...#..#.#......#.#...........##',
'##....#...#.....###..#...#....#',
'...#.....#.#.#......##...#...#.',
'............#.......#..........',
'....#..........###.......#.....',
'.................##..##....#...',
'...........#........##..#......',
'...#.#...#.....#........#...#..',
'#...#.#......#.#...........#...',
'..#..........#....#..........#.',
'..#................#...........',
'#...#.#....#.#.......#.........',
'.#...........##..#....#....#..#',
'.##........#.....#...#..#....#.',
'......#......#...#.............',
'.......#..#...#.##....#..#.#...',
'.......#......#....#....#.#.#..',
'..........##.....#....##.#.....',
'.........##..#...#.....#..#....',
'...#....#..........#..#...#..#.',
'.......#.....##.#..#.....#...#.',
'#...#......#......#...#........',
'#..#....#.#......#......#......',
'.......#.##....................',
'...##...#.....#......##......#.',
'.#...................###.......',
'....#........###...#........#..',
'...#............#.....#..#.....',
'..................#......#....#',
'..##......#..##..##......#.#...',
'........##....##.......#...#...',
'.#.#....#.....#.....#....#....#',
'...##.#.............#....##....',
'.........#.....#...#......#....',
'..#.....#............#....##...',
'..##.....#.....##.##...........',
'#....#.#.......#..#......#.....',
'##.......#.....#.....####....#.',
'##...#.......#...#.....#.......',
'#.....#..##.##...##..#.....#..#',
'..........#......#..#.#........',
'..##.#......#..............#...',
'.#...#..........#.......#....#.',
'..#....##...#...........#....#.',
'..#.........#..#......#......#.',
'.##....#......#.#.........#..##',
'.......#...#....##............#',
'.##.................#.#........',
'...#.#...#..#..#.....#.#.......',
'.#.#.......#...................',
'..#..#.....#......#.....##..##.',
'.#........#.##......#..........',
'....##...#............#.#....#.',
'.......#.#..#....##.#....#....#',
'......####...#..#.....#........',
'..........#..#.........#.#..#.#',
'..........##.........#.##......',
'.##..#.#.....#.....#....#......',
'............#..#...............',
'.....##.........#...#...##...##',
'........#.##.#...#.....#....#.#',
'#......##.#.##..........##.....',
'#..#..#........#.........#..#..',
'...............#.#..##.........',
'.#.......##.#..#....#...#....##',
'.#..##.....##......#....#...#.#',
'........#...#.........#.....#.#',
'...........#............#...#..',
'................#...........#..',
'..............##........#....#.',
'..........#.....##.....#..#....',
'#......#....###..#..#..........',
'.....#.#.....##....#.#.......#.',
'...#...#...............#.#.....',
'.............#.......#.........',
'.....#.....#..#......#.....#...',
'.........#.................#.##',
'.#.....#.##..#.................',
'..#......#.......#.....#...#..#',
'..#..#.#.#...#.......#.##......',
'..........#..#.........#.......',
'.#..........#...#....#..#...##.',
'.#.#.#.###.....#...#.#.#.......',
'....##............#............',
'.#.#.............#..#......#.#.',
'.#.#..........##..#.....#..#.#.',
'...........#.##..#...#.#.....#.',
'...........#..#....#...........',
'..#................#.#...#....#',
'...............##........##....',
'....#.............#........#...',
'...#......#.#.#........#.......',
'#..............#..##.#..##.....',
'.#.#.###................##.....',
'.............#..#.........#....',
'.......##..#............#...#..',
'...#...#...........#.....#.....',
'........#......#.#.#......#..#.',
'#.##.......#......#..#..#.#....',
'...#........#...........#...#..',
'..#...........#.........#......',
'.............#....#....#.......',
'....#.........#........#......#',
'..#............##..#.........#.',
'.#...#...#..#...#........#..#..',
'...#....##..............#......',
'...........#...#....#.#.##..###',
'..#....#......#.........#..#...',
'.......#...#...................',
'.#...#.#...................#...',
'.#.....##.#.......#.#.#...##..#',
'.....#..#.#.........#...#..##..',
'.#..#.##.#......#......#.#...#.',
'......#..#....##..#....##....##',
'#...#......##........##........',
'.#.........###................#',
'.................#..###..#.#...',
'..#.#........#..#........#...#.',
'#.#....#....#..#...#.#......#..',
'.#.#.............###.........#.',
'.....#...............##...#...#',
'..............#...#........#..#',
'...................#..#.......#',
'#......................#.....#.',
'...#.........#..##...#...#.##..',
'.....#..........#.........#....',
'.....#...#............#..#.....',
'.............#............#....',
'...#.........#.................',
'#...........#.#...............#',
'.....#...#.....#..#.##.......##',
'...#....#.#...........#........',
'.........................#.#...',
'.#..#...........#.#........#...',
'.............#.#.....#..#....#.',
'.....#...#.###...#..#........#.',
]
x_slopes=[1,3,5,7,1]
y_slopes=[1,1,1,1,2]
trees=[]
height=len(input)
width = len(input[0])

for i in range(len(x_slopes)):
    chars_needed = math.ceil(height/y_slopes[i])*x_slopes[i]
    reps_needed = math.ceil(chars_needed/width)
    expanded_map = [a*reps_needed for a in input]
    trees_count=0
    for j in range((height//y_slopes[i])-1):
        if expanded_map[(j+1)*y_slopes[i]][(j+1)*x_slopes[i]]=='#':
            trees_count+=1
        j+=1
    trees.append(trees_count)
    i+=1
print(trees)
print(math.prod(trees))